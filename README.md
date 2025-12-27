<img width="1784" height="981" alt="Screenshot 2025-12-27 150305" src="https://github.com/user-attachments/assets/bab98b1c-225b-4137-ae0e-b8e8e3d5ed03" /># 🚗 Driver Drowsiness Detection System 😴

A real-time **Driver Drowsiness Detection System** developed using **Python, OpenCV, MediaPipe, NumPy, and Pygame**.  
The system monitors a driver’s eye movement through a webcam and triggers an alarm when drowsiness is detected.

---

## 📌 Objective
Driver fatigue is one of the major causes of road accidents.  
This project aims to **detect early signs of drowsiness** and alert the driver to improve road safety.

---

## 🛠️ Technologies Used
- Python  
- OpenCV  
- MediaPipe  
- NumPy  
- Pygame  

---

## ✨ Key Features
- Real-time face and eye detection  
- Eye Aspect Ratio (EAR) based drowsiness detection  
- Audio alarm alert system  
- Webcam-based live monitoring  
- Simple and efficient implementation  

---

## 📁 Project Structure
DriverDrowsinessDetection/
│
├── main.py
├── alarm.wav
└── README.md

---

## 🧠 How It Works
1. Captures live video using a webcam  
2. Detects facial landmarks using MediaPipe Face Mesh  
3. Calculates Eye Aspect Ratio (EAR)  
4. If eyes remain closed for a specific duration, the system detects drowsiness  
5. An alarm sound is played to alert the driver  

<img width="799" height="624" alt="Screenshot 2025-12-27 150420" src="https://github.com/user-attachments/assets/19ef645e-b1bb-4e69-8dda-90b5fe749240" />

---

## 📦 Requirements
- opencv-python  
- mediapipe  
- numpy  
- pygame  

---

## ▶️ How to Run
1. Ensure Python is installed  
2. Install required libraries  
3. Run `main.py`  
4. Press **Q** to exit the program  

---

## 🔊 Alarm
- The `alarm.wav` file is used to alert the driver  
- Ensure the file is present in the project directory  

---

## 🚀 Future Improvements
- GUI-based application  
- Real-time eye openness graph  
- Alert logging and report generation  
- SMS / WhatsApp alerts  
- Multilingual voice alert system  

---

## 👨‍💻 Author
**Abhishek**  
AI & Computer Vision Enthusiast  

---

⭐ If you find this project useful, consider giving it a star!


