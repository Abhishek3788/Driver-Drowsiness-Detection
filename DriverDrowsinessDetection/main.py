import cv2
import mediapipe as mp
import pygame
import time

# Initialize Pygame for alarm sound
pygame.mixer.init()
pygame.mixer.music.load("alarm.wav")  # Ensure alarm.wav is in the same folder

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)
mp_drawing = mp.solutions.drawing_utils

# Eye landmark indices
LEFT_EYE = [159, 145]
RIGHT_EYE = [386, 374]

# Eye openness calculation
def get_eye_openness(landmarks, eye_indices):
    top = landmarks[eye_indices[0]]
    bottom = landmarks[eye_indices[1]]
    return abs(top.y - bottom.y)

# Open webcam
cap = cv2.VideoCapture(0)

drowsy_start = None
alarm_playing = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror for real-time feel
    h, w = frame.shape[:2]

    # Overlay for dark techy background effect
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (w, h), (10, 10, 30), -1)
    frame = cv2.addWeighted(overlay, 0.3, frame, 0.7, 0)

    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for landmarks in results.multi_face_landmarks:
            # Neon-techy style drawing
            mp_drawing.draw_landmarks(
                frame, landmarks, mp_face_mesh.FACEMESH_TESSELATION,
                mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=1, circle_radius=0),   # cyan lines
                mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=1)                     # glowing yellow for refinement
            )

            lm = landmarks.landmark
            left_eye = get_eye_openness(lm, LEFT_EYE)
            right_eye = get_eye_openness(lm, RIGHT_EYE)
            avg_openness = (left_eye + right_eye) / 2

            if avg_openness < 0.01:
                if drowsy_start is None:
                    drowsy_start = time.time()
                elif time.time() - drowsy_start > 2:
                    cv2.putText(frame, "DROWSINESS ALERT!", (30, 60),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 255), 4)  # RED TEXT
                    if not alarm_playing:
                        pygame.mixer.music.play(-1)
                        alarm_playing = True
            else:
                drowsy_start = None
                if alarm_playing:
                    pygame.mixer.music.stop()
                    alarm_playing = False

    # Techy border lines (optional)
    cv2.line(frame, (0, 0), (w, 0), (255, 255, 255), 1)
    cv2.line(frame, (0, h), (w, h), (255, 255, 255), 1)
    cv2.line(frame, (0, 0), (0, h), (255, 255, 255), 1)
    cv2.line(frame, (w-1, 0), (w-1, h), (255, 255, 255), 1)

    cv2.imshow("👁️ Neon Drowsiness Detector", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop()
pygame.mixer.quit()
