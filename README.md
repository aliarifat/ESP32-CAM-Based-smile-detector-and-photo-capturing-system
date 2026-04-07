# 📸 ESP32-CAM Smile Detector & Auto Photo Capture System

An intelligent computer vision project using **ESP32-CAM** and **Python (OpenCV)** that automatically captures a photo when a smile is detected.

---

## 🚀 Overview

This project demonstrates a real-time **smile detection system** using image processing. The ESP32-CAM captures images and serves them over Wi-Fi, while a Python script processes those images to detect faces and smiles.

📷 When a smile is detected → the system **automatically captures and saves a photo**.

---

## 🧠 How It Works

### 1. ESP32-CAM (Image Server)
- Captures images at **800x600 resolution**
- Hosts images via HTTP
- Endpoint example:
  http://<ESP32-IP>/cam-hi.jpg
  - Acts like a continuously refreshed snapshot camera

### 2. Python Application (Processing Unit)
The Python script performs:

#### a. Image Fetching
- Downloads image from ESP32-CAM
- Converts raw data into an OpenCV image

#### b. Image Analysis
- Detects faces using Haar Cascades
- Detects smiles within detected faces

#### c. Action Trigger
- If smile detected:
- Saves clean image (no bounding boxes)
- Displays captured image

### 3. Display System
- Live feed window: `ESP32-CAM Video`
- Captured image preview window
- Exit anytime using **`q` key**

---

## 🔁 Workflow Loop
Capture → Fetch → Process → Detect → Save → Repeat

Runs continuously until stopped.

---

## 📁 Project Structure

```text
project_folder/
├── esp32_cam_basic.ino
├── smile_pic_esp32cam.py
├── haarcascade_frontalface_default.xml
└── haarcascade_profileface.xml
```

---

## 🧰 Components Required

| Component                                   | Quantity |
|--------------------------------------------|----------|
| ESP32-CAM WiFi + Bluetooth Module          | 1        |
| FTDI USB to Serial Converter (3.3V/5V)     | 1        |
| Male-to-Female Jumper Wires                | 4        |
| Female-to-Female Jumper Wire               | 1        |
| Micro USB Data Cable                       | 1        |

---

## 🔌 Circuit Connections

| ESP32-CAM | FTDI Converter |
|----------|----------------|
| 5V       | VCC            |
| GND      | GND            |
| U0T      | RX             |
| U0R      | TX             |
| IO0      | GND (for upload mode) |

⚠️ Set FTDI to **5V mode**

---

## ⚙️ Setup Instructions

### 1. ESP32-CAM Setup
- Install ESP32 board support in Arduino IDE
- Install required drivers (CP210x / FTDI)
- Upload: `esp32_cam_basic.ino`
- Disconnect IO0 from GND after upload
- Press **RST**

📌 Note the IP address shown in Serial Monitor

---

### 2. Python Environment Setup

#### Create Virtual Environment
```bash
python -m venv venv


```


## 🧰 Components Required

| Component                                   | Quantity |
|--------------------------------------------|----------|
| ESP32-CAM WiFi + Bluetooth Module          | 1        |
| FTDI USB to Serial Converter (3.3V/5V)     | 1        |
| Male-to-Female Jumper Wires                | 4        |
| Female-to-Female Jumper Wire               | 1        |
| Micro USB Data Cable                       | 1        |

---

## 🔌 Circuit Connections

| ESP32-CAM | FTDI Converter |
|----------|----------------|
| 5V       | VCC            |
| GND      | GND            |
| U0T      | RX             |
| U0R      | TX             |
| IO0      | GND (for upload mode) |

⚠️ Set FTDI to **5V mode**

---

## ⚙️ Setup Instructions

### 1. ESP32-CAM Setup
- Install ESP32 board support in Arduino IDE
- Install required drivers (CP210x / FTDI)
- Upload: `esp32_cam_basic.ino`
- Disconnect IO0 from GND after upload
- Press **RST**

📌 Note the IP address shown in Serial Monitor

---

### 2. Python Environment Setup

#### Create Virtual Environment
```bash
python -m venv venv
Activate Environment
# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
Install Dependencies
pip install opencv-python numpy


```
### 3. Haar Cascade Files

Download:

haarcascade_frontalface_default.xml
haarcascade_profileface.xml

From:
https://github.com/opencv/opencv/tree/master/data/haarcascades

Place them in the project directory.


---
### 4. Configure Python Script
```bash
Edit smile_pic_esp32cam.py:
```
### ▶️ Running the Project
Power the ESP32-CAM
Run:
```bash
python smile_pic_esp32cam.py
```
Stand in front of camera and smile 😊
📸 Image will be saved as:
Run:
```bash
smile_detected.jpg
```
### ✅ Features
* Real-time image streaming
* Face detection
* Smile detection
* Automatic image capture
* Clean image saving (no overlays)
* Live preview window
 ---
### 🧪 Testing
* Ensure ESP32 is connected to Wi-Fi
* Verify image URL works in browser
* Run Python script
* Smile in front of camera
---

<img width="494" height="602" alt="Screenshot 2025-04-09 020528" src="https://github.com/user-attachments/assets/7b4495b5-ff4f-405f-825e-af0f832cd053" />

### Troubleshooting

| Issue                         | Solution                   |
| ----------------------------- | -------------------------- |
| No image                      | Check IP address           |
| Upload fails                  | Press RST during upload    |
| Guru Meditation Error         | Ensure stable power        |
| Continuous dots during upload | Reset board                |
| Detection not working         | Verify Haar files location |

---

### 💡 Applications
* 📸 Smart selfie booths
* 😊 Emotion detection systems
* 🏪 Customer engagement tracking
* 🎉 Event photo capture systems  

---
### 🔧 Future Improvements
* Add timestamp to images
* Cloud upload (Google Drive / AWS)
* Email notifications
* Smile counter analytics
* Voice feedback system
* Raspberry Pi standalone setup
