# Face and Eye Detection with OpenCV

This project demonstrates how to use OpenCV to perform real-time face and eye detection using your webcam. The program captures video, detects faces and eyes within each frame, and highlights them with rectangles.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project uses OpenCV's Haar Cascade Classifiers, which are pre-trained models for object detection. It processes live video from your webcam, detects faces and eyes, and draws rectangles around them for visualization. It's a great starting point for anyone interested in learning about computer vision and image processing with Python.

## Features

- **Real-time Face Detection:** Detects faces in real-time using your webcam.
- **Real-time Eye Detection:** Detects eyes within detected faces.
- **Customizable Scaling:** Resize video frames for faster processing.
- **Easy-to-Understand Code:** Well-commented Python code suitable for beginners.

## Installation

### Prerequisites

- Python 3.x
- OpenCV

### Install OpenCV

You can install OpenCV via pip:

```bash
pip install opencv-python
```

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/face-eye-detection.git
cd face-eye-detection
```

### Download Haar Cascade Files

Make sure you have the following Haar Cascade XML files in your project directory:
- `haar_frontal.xml` (for face detection)
- `haar_frontaleye.xml` (for eye detection)

You can download these files from OpenCV's GitHub repository or find them in the `data` folder of OpenCV.

## Usage

Run the following command to start the face and eye detection:

```bash
python detect_faces_eyes.py
```

Press `q` to quit the application.

## Dependencies

- **OpenCV**: Used for image and video processing.
- **NumPy**: Although not directly used, it is a dependency of OpenCV.

## Project Structure

```plaintext
face-eye-detection/
├── haar_frontal.xml
├── haar_frontaleye.xml
├── detect_faces_eyes.py
└── README.md
```

- `haar_frontal.xml`: Haar Cascade for face detection.
- `haar_frontaleye.xml`: Haar Cascade for eye detection.
- `detect_faces_eyes.py`: The main Python script for face and eye detection.
- `README.md`: Project documentation.

## Contributing

Contributions are welcome! If you find any bugs or want to add new features, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Key Points:
- **Introduction**: Provides an overview of the project.
- **Features**: Highlights the main features of the project.
- **Installation**: Guides the user on how to set up the project.
- **Usage**: Instructions on how to run the program.
- **Dependencies**: Lists required libraries.
- **Project Structure**: Gives an overview of the project files.
- **Contributing**: Encourages community contributions.
- **License**: Specifies the licensing information.
