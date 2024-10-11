import cv2
import numpy as np
from retinaface import RetinaFace
from keras_facenet import FaceNet

facenet = FaceNet()

def extract_faces(video_path):
    cap = cv2.VideoCapture(video_path)
    face_embeddings = []
    face_images = []

    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Frame rate of the video: {fps}")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total frames in the video: {total_frames}")

    processed_frames = 0  

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        processed_frames += 1  
        
        current_time = processed_frames / fps

        print(f"Processing frame {processed_frames}/{total_frames} - Time: {current_time:.2f}s  completed: {100 * processed_frames / total_frames:.2f}%", end='\r')

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = RetinaFace.detect_faces(rgb_frame)

        if isinstance(results, dict):
            for key in results:
                box = results[key]['facial_area']
                x1, y1, x2, y2 = box[0], box[1], box[2], box[3]
                face = rgb_frame[y1:y2, x1:x2]
                if face.size == 0:
                    continue 

                face_resized = cv2.resize(face, (160, 160))
                face_expanded = np.expand_dims(face_resized, axis=0)
                embedding = facenet.embeddings(face_expanded)
                face_embeddings.append(embedding)
                face_images.append(face_resized)

    cap.release()
    
    if not face_embeddings:
        print("No faces detected in the video.")
        return np.array([]), [], fps, total_frames

    face_embeddings = np.array(face_embeddings).reshape(len(face_embeddings), -1)
    print("\nProcessing complete.")
    return face_embeddings, face_images, fps, total_frames
