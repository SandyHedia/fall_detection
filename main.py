import requests
from ultralytics import YOLO
import cv2
import time

# Telegram notification setup
BOT_TOKEN = ''
CHAT_ID = ''

def send_telegram_message_with_image(message, image_path):
    # Send the text message
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message, 'parse_mode': 'HTML'}
    requests.post(url, data=data)

    # Send the image
    url_photo = f'https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto'
    with open(image_path, 'rb') as photo:
        files = {'photo': photo}
        data = {'chat_id': CHAT_ID, 'caption': message}
        response = requests.post(url_photo, files=files, data=data)

    if response.status_code == 200:
        print("Image sent successfully!")
    else:
        print("Failed to send image:", response.text)


# Load YOLO model
model = YOLO('asset/best.pt')
cap = cv2.VideoCapture('test/fall.mp4')

alert_sent = False
cooldown_time = 10
last_alert_time = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    fall_detected = any(
        box.cls == 0 and box.conf >= 0.8 for result in results for box in result.boxes)

    current_time = time.time()
    if fall_detected and (not alert_sent or current_time - last_alert_time > cooldown_time):
        # Save the detected frame as an image
        image_path = "fall_detection.jpg"
        cv2.imwrite(image_path, frame)

        # Send message and image through Telegram
        send_telegram_message_with_image("Alert: Fall detected at Grandma's house!", image_path)

        alert_sent = True
        last_alert_time = current_time

    if current_time - last_alert_time > cooldown_time:
        alert_sent = False

    annotated_frame = results[0].plot()
    cv2.imshow('Fall Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
