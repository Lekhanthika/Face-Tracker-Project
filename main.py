import cv2
import json
import os
import numpy as np
from datetime import datetime
from ultralytics import YOLO
from insightface.app import FaceAnalysis

# Load config
with open("config.json") as f:
    config = json.load(f)

frame_skip = config["frame_skip"]
video_path = config["video_path"]
yolo_model_path = config["model"]["yolo_model"]
save_dir = config.get("save_dir", "cropped_faces")

os.makedirs(save_dir, exist_ok=True)

# Initialize YOLO
model = YOLO(yolo_model_path)

# Initialize InsightFace
face_app = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
face_app.prepare(ctx_id=0, det_size=(640, 640))

# Helper for cosine similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

known_embeddings = []
visitor_id = 0
frame_id = 0

# Open video
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_id % frame_skip == 0:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_app.get(rgb_frame)

        if not faces:
            print(f"⚠️ Frame {frame_id}: No faces detected.")
        else:
            for i, face in enumerate(faces):
                embedding = face.embedding
                if embedding is None:
                    print(f"⚠️ Frame {frame_id}, Face {i}: No embedding found.")
                    continue

                # Compare with known embeddings
                is_known = False
                for known in known_embeddings:
                    if cosine_similarity(embedding, known) > 0.6:
                        is_known = True
                        print(f"🔁 Frame {frame_id}, Face {i}: Known visitor")
                        break

                if not is_known:
                    known_embeddings.append(embedding)
                    visitor_id += 1
                    print(f"🆕 Frame {frame_id}, Face {i}: New visitor registered (Total: {visitor_id})")

                    # Save cropped face
                    box = face.bbox.astype(int)
                    x1, y1, x2, y2 = box
                    crop = frame[y1:y2, x1:x2]
                    if crop.size > 0:
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        filename = f"{save_dir}/visitor_{visitor_id}_frame{frame_id}_{timestamp}.jpg"
                        cv2.imwrite(filename, crop)

    frame_id += 1

cap.release()
cv2.destroyAllWindows()
