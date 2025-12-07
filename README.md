# RetinaCardio

### Cardiovascular Disease Prediction using Retina Image Analysis

A Flask-based web application that uses deep learning models to predict cardiovascular disease from retina images. This project leverages transfer learning with pre-trained CNN architectures including ResNet, MobileNet, and VGG16.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Screenshots](#screenshots)
- [Author](#author)

## Overview

Cardiovascular diseases are among the leading causes of death globally. Research has shown that changes in retinal blood vessels can indicate early signs of cardiovascular conditions. This application uses trained deep learning models to analyze retina images and predict the likelihood of cardiovascular disease.

The system processes uploaded retina scan images through multiple CNN architectures and provides predictions based on learned patterns from medical imaging data.

## Features

- **Multiple AI Models**: Choose from three different deep learning architectures
  - ResNet (Residual Network)
  - MobileNet (Lightweight CNN)
  - VGG16 (Visual Geometry Group)
- **Modern Web Interface**: Clean, responsive UI with glassmorphism design
- **Drag and Drop Upload**: Easy image upload functionality
- **Instant Predictions**: Real-time analysis results
- **Color-Coded Results**: Visual indication of healthy vs disease predictions
- **Secure Authentication**: Login system for access control

## Technology Stack

| Component | Technology |
|-----------|------------|
| Backend | Python 3.11, Flask |
| ML Framework | TensorFlow 2.x, Keras |
| Frontend | HTML5, CSS3, JavaScript |
| Fonts | Google Fonts (Inter) |
| Models | ResNet, MobileNet, VGG16 (pre-trained) |

## Project Structure

```
RetinaCardio/
├── app.py                    # Flask application entry point
├── requirements.txt          # Python dependencies
├── MobileNetmodel.keras      # MobileNet trained model
├── ResNetmodel.keras         # ResNet trained model
├── VGG16.keras               # VGG16 trained model
├── uploads/                  # Uploaded images directory
└── templates/
    ├── login.html            # Login page
    ├── home.html             # Home/information page
    └── index.html            # Main prediction interface
```

## Installation

### Prerequisites

- Python 3.11 or 3.12 (TensorFlow is not compatible with Python 3.13+)
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/abhi3114-glitch/RetinaCardio.git
   cd RetinaCardio
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify TensorFlow installation**
   ```bash
   python -c "import tensorflow as tf; print(tf.__version__)"
   ```

## Usage

### Starting the Application

```bash
# Windows (if multiple Python versions installed)
py -3.11 app.py

# Standard
python app.py
```

The application will start on `http://127.0.0.1:5000`

### Login Credentials

| Username | Password |
|----------|----------|
| abhishek | abhishek |
| admin | admin |

### Making Predictions

1. Navigate to `http://127.0.0.1:5000` in your browser
2. Log in with the credentials above
3. Click on "Test" in the navigation bar
4. Upload a retina scan image (PNG, JPG, or JPEG format)
5. Select one or more AI models for analysis
6. Click "Analyze Image"
7. View the prediction results

## Models

### Model Architecture Details

| Model | Parameters | Input Size | Strengths |
|-------|------------|-----------|-----------|
| ResNet | ~25M | 224x224 | Deep residual learning, prevents vanishing gradients |
| MobileNet | ~3.4M | 224x224 | Lightweight, efficient for mobile/edge deployment |
| VGG16 | ~138M | 224x224 | Simple architecture, proven performance |

### Prediction Thresholds

- **ResNet**: Threshold 0.8473 (above = healthy)
- **MobileNet**: Threshold 0.5886 (below = healthy)
- **VGG16**: Threshold 0.4498 (below = healthy)

### Model Files

The trained model files are in Keras format:
- `ResNetmodel.keras` (~284 MB)
- `MobileNetmodel.keras` (~40 MB)
- `VGG16.keras` (~177 MB)

## Screenshots

### Login Page
Modern glassmorphism login interface with gradient background.

### Home Page
Information about AI/ML in medical science with feature cards highlighting the application capabilities.

### Prediction Interface
Clean upload area with model selection cards and color-coded result display.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET, POST | Login page |
| `/home` | GET | Home/information page |
| `/index` | GET, POST | Prediction interface |

## Troubleshooting

### TensorFlow Not Found
Ensure you are using Python 3.11 or 3.12. TensorFlow is not compatible with Python 3.13 or 3.14.

```bash
# Check Python version
python --version

# Use specific version on Windows
py -3.11 app.py
```

### Model Loading Errors
Verify that all `.keras` model files are present in the root directory alongside `app.py`.

### Image Upload Issues
- Ensure the image is in PNG, JPG, or JPEG format
- Maximum recommended image size: 10MB
- The `uploads/` directory must exist and be writable

## Future Improvements

- Add user registration system
- Implement result history tracking
- Add model accuracy metrics display
- Support for batch image processing
- Export prediction reports as PDF
- Add API endpoints for external integration

## License

MIT License - Feel free to use and modify for your own projects.

## Author

**Abhishek**

---

Built with Python, TensorFlow, and Flask
