import numpy as np
import matplotlib.pyplot as plt

def visualize_and_label_clusters(cluster_labels, face_images, fps, total_frames):
    unique_labels = np.unique(cluster_labels)
    screen_time_per_label = {}

    for label in unique_labels:
        indices = np.where(cluster_labels == label)[0]
        if len(indices) == 0:
            continue

        frame_count = len(indices)
        
        screen_presence_percentage = (frame_count / total_frames) * 100

        screen_time = frame_count / fps  

        first_index = indices[0]
        face_image = face_images[first_index]

        plt.imshow(face_image)
        plt.axis('off')
        
        plt.title(f"Cluster {label} - Screen Presence: {screen_presence_percentage:.2f}%")
        
        plt.show(block=False)
        plt.pause(0.5)
        
        label_input = input(f"Please label this face (Cluster {label}): ")
        print(f"Labeled as: {label_input}")

        plt.close()

        if label_input in screen_time_per_label:
            screen_time_per_label[label_input]['frame_count'] += frame_count
            screen_time_per_label[label_input]['screen_time'] += screen_time  
            screen_time_per_label[label_input]['screen_presence_percentage'] += screen_presence_percentage  
        else:
            screen_time_per_label[label_input] = {
                'frame_count': frame_count,
                'screen_time': screen_time,
                'screen_presence_percentage': screen_presence_percentage  
            }

        print(f"Cluster {label_input} has a screen time of: {screen_time:.2f} seconds with a screen presence of: {screen_presence_percentage:.2f}%.")

    print("All specified faces have been labeled.")
    return screen_time_per_label
