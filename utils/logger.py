import os
from datetime import datetime
import cv2

def save_event(face_id, face_img, event_type):
    date_str = datetime.now().strftime("%Y-%m-%d")
    path = f"logs/{event_type}s/{date_str}"
    os.makedirs(path, exist_ok=True)

    filename = f"{path}/{face_id}_{event_type}.jpg"
    cv2.imwrite(filename, face_img)

    with open("logs/events.log", "a") as f:
        f.write(f"{datetime.now()}, {event_type}, {face_id}, {filename}\n")

    return filename
