import cv2
import numpy as np
from insightface.app import FaceAnalysis

# Initialize the face embedding model only once
face_app = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
face_app.prepare(ctx_id=0)

def get_embedding(face_app, face_img):
    faces = face_app.get(face_img)
    if len(faces) == 0:
        return None
    return faces[0].embedding

