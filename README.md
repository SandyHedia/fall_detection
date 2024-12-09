# Fall Detection Project

## Overview

The Fall Detection Project is designed to identify and alert users when a fall is detected in a monitored area. Using a YOLO-based object detection model, the system analyzes video feeds in real-time to detect falls. Upon detection, it sends an alert message and the corresponding image to a specified Telegram chat for immediate response.

## Features

- **Real-time Fall Detection**: Utilizes a YOLO model to process video frames and detect falls with high accuracy.
- **Alert Notifications**: Sends Telegram alerts with a custom message and an image of the detected fall.
- **Customizable Thresholds**: Configurable confidence threshold for fall detection and cooldown time for repeated alerts.
- **Video Feed Visualization**: Displays the annotated video feed with detected falls.

## Requirements

- Python 3.8 or later
- Required Python libraries:
  - `ultralytics` for YOLO model
  - `cv2` (OpenCV) for video processing
  - `requests` for Telegram API integration

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd fall-detection-project
   ```

2. Install the required dependencies:
   ```bash
   pip install ultralytics opencv-python requests
   ```

3. Download the YOLO model weights (`best.pt`) and place them in the `asset` directory.

4. Update the Telegram bot credentials in the `main.py` file:
   ```python
   BOT_TOKEN = '<your_bot_token>'
   CHAT_ID = '<your_chat_id>'
   ```

## Usage

1. Place the video to be analyzed in the `test` directory (e.g., `fall.mp4`).

2. Run the fall detection script:
   ```bash
   python main.py
   ```

3. The system will display the video feed with annotated detections and send alerts via Telegram when a fall is detected.

## Configuration

- **Confidence Threshold**: Adjust the detection confidence level in the code to tune sensitivity.
- **Cooldown Time**: Change the `cooldown_time` parameter to modify the interval between consecutive alerts.

## File Structure

```plaintext
fall-detection-project/
│
├── asset/
│   └── best.pt                # YOLO model weights
│
├── test/
│   └── fall.mp4               # Sample video file
│
├── main.py                    # Main fall detection script
│
└── README.md                  # Project documentation
```

## Future Improvements

- Add support for additional notification methods, such as email or SMS.
- Enable live video feed monitoring through IP cameras.
- Enhance model accuracy with additional training data.
