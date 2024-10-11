# face_recognition.py
from .extractor import extract_faces
from .clustering import cluster_faces
from .visualization import visualize_and_label_clusters

class FaceRecognition:
    def __init__(self, video_path):
        self.video_path = video_path

    def run(self):
        face_embeddings, face_images, fps, total_frames = extract_faces(self.video_path)
        if face_embeddings.size == 0:
            print("Exiting the program due to no faces detected.")
            return
        
        cluster_labels = cluster_faces(face_embeddings)
        screen_time_per_label = visualize_and_label_clusters(cluster_labels, face_images, fps, total_frames)
        
        print("\n\n\n") 
        for label, data in screen_time_per_label.items():
            total_screen_time = data['screen_time']
            print(f"Total screen time for {label}: {total_screen_time:.2f} seconds based on {data['frame_count']} frames")
