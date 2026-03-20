# SportVision AI: YOLO-Based Sports Player Detection and Tracking

SportVision AI is a computer vision project built using **YOLOv8, OpenCV, and Python** for sports video analysis.  
It detects and tracks players in video frames, making it useful for player movement analysis, sports analytics, and real-time computer vision learning.

---

## Features

- Player detection using **YOLOv8**
- Object tracking across video frames
- Bounding box visualization on players
- Video frame processing with **OpenCV**
- Reusable tracking pipeline with saved stub support
- Can be extended for ball tracking, team classification, and tactical analysis

---

## Tech Stack

- **Python**
- **YOLOv8 (Ultralytics)**
- **OpenCV**
- **NumPy**
- **Pickle**
- **Computer Vision**
- **Deep Learning**

---

## Project Overview

This project analyzes sports videos by detecting players in each frame and tracking them throughout the video.  
The system is designed to help in:

- Player tracking
- Sports performance analysis
- Movement understanding
- Learning real-world computer vision workflows

---

## Project Structure

```bash
SportVision/
│
├── .vscode/
├── input_video/
├── stubs/
├── trackers/
├── training/
├── utils/
├── .gitignore
├── main.py
├── yolo_inference.py
└── README.md
