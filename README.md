# YOLOv8 Person Detection Web App

![UI Screenshot](screenshot.png)

A simple and modern web application for person detection using YOLOv8. Detect people in images or via your webcam, all from a beautiful web interface built with Flask and Bootstrap.

## Features
- Upload an image or use your live webcam for detection
- See detection results instantly in the browser
- Clean, responsive, and modern UI
- Loading spinner for better user experience
- Results saved for later review

## Demo
![UI Screenshot](screenshot.png)

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/Person_Detection_YOLOv8.git
cd Person_Detection_YOLOv8
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download YOLOv8 weights
Place your YOLOv8 weights file (e.g., `yolo11n.pt`) in the project root. You can use your own or download from [Ultralytics](https://github.com/ultralytics/ultralytics).

### 4. Run the app
```bash
python app.py
```

### 5. Open in your browser
Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage
- **Live Webcam:** Select "Live Webcam" and click "Start Detection". The app will use your default camera.
- **Upload Image:** Select "Upload Image", choose a file, and click "Start Detection". The result will be shown below the form.

## Project Structure
```
├── app.py                # Flask backend
├── predict.py            # YOLOv8 prediction script
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Main UI template
├── uploads/              # Uploaded images
├── runs/detect/          # YOLOv8 output folders
├── yolo11n.pt            # YOLOv8 weights (not included)
├── README.md             # This file
└── screenshot.png        # UI screenshot (add this for GitHub display)
```

## Screenshot
![UI Screenshot](screenshot.png)

## License
This project is for educational and research purposes. See LICENSE for details. 