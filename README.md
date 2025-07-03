# 👁️‍🗨️ Face and Motion Detection using Python

A real-time face and motion detection system using OpenCV. This project captures video from a webcam, detects faces using Haar cascades, and tracks motion by comparing frame differences.

---

## 📌 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Setup & Installation](#-setup--installation)

## ℹ️ About

This project uses Python and OpenCV to perform:
- **Face detection** using Haar Cascade Classifiers.
- **Motion detection** by comparing pixel differences between frames.
It can be used for security cameras, intruder detection, or AI experimentation.

---

## ✨ Features

- 🔍 Real-time face detection from webcam
- 🧠 Uses OpenCV’s pre-trained Haar Cascade model
- 🎥 Motion detection via frame differencing
- 💾 Option to save detected frames or video
- 🖥️ Simple and lightweight UI via OpenCV windows

---

## 🛠️ Tech Stack

- **Language**: Python 3.x  
- **Libraries**:  
  - OpenCV (`cv2`)  
  - NumPy  
  - imutils *(optional)*

---

## 🚧 Setup & Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/SharadBaghel/Project.git
   cd Project
   
**2. Install Dependencies**

    pip install -r requirements.txt

    If requirements.txt not available, manually install:

    pip install opencv-python numpy imutils
