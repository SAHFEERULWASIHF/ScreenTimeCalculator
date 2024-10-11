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
        
        # Calculate screen presence percentage
        screen_presence_percentage = (frame_count / total_frames) * 100

        # Calculate screen time in seconds
        screen_time = frame_count / fps  

        # Display the first face in the cluster
        first_index = indices[0]
        face_image = face_images[first_index]

        plt.imshow(face_image)
        plt.axis('off')
        
        # Add title with screen presence percentage to the plot
        plt.title(f"Cluster {label} - Screen Presence: {screen_presence_percentage:.2f}%")
        
        plt.show(block=False)  # Non-blocking show
        plt.pause(0.5)  # Pause for half a second to show the image
        
        # Get the label for this face
        label_input = input(f"Please label this face (Cluster {label}): ")
        print(f"Labeled as: {label_input}")

        # Close the plot after input
        plt.close()

        # Add the calculated screen time to the dictionary
        if label_input in screen_time_per_label:
            screen_time_per_label[label_input]['frame_count'] += frame_count
            screen_time_per_label[label_input]['screen_time'] += screen_time  
            screen_time_per_label[label_input]['screen_presence_percentage'] += screen_presence_percentage  # Store screen presence for cumulative calculation
        else:
            screen_time_per_label[label_input] = {
                'frame_count': frame_count,
                'screen_time': screen_time,
                'screen_presence_percentage': screen_presence_percentage  # Store screen presence for the first occurrence
            }

        print(f"Cluster {label_input} has a screen time of: {screen_time:.2f} seconds with a screen presence of: {screen_presence_percentage:.2f}%.")

    print("All specified faces have been labeled.")
    return screen_time_per_label


# def visualize_and_label_clusters(cluster_labels, face_embeddings, face_images, fps, total_frames):
#     unique_labels = np.unique(cluster_labels)
#     screen_time_per_label = {}

#     for label in unique_labels:
#         indices = np.where(cluster_labels == label)[0]
        
#         if len(indices) == 0:
#             continue
        
#         # Count the frames for this cluster
#         frame_count = len(indices)
#         screen_time = (frame_count / total_frames) * (1 / fps) * 60  # Convert to minutes

#         # Prompt the user for a label for the first face in the cluster
#         first_index = indices[0]
#         face_image = face_images[first_index]
#         plt.imshow(face_image)
#         plt.axis('off')
#         plt.show()

#         # User labeling
#         label_input = input(f"Please label this face (Cluster {label}) or type 'spamface' to exclude: ")
        
#         if label_input.strip().lower() == 'spamface':
#             print(f"Cluster {label} labeled as spamface and will be excluded.")
#             continue  # Skip this cluster
        
#         print(f"Labeled as: {label_input}")
        
#         # Add screen time to the corresponding label
#         if label_input in screen_time_per_label:
#             screen_time_per_label[label_input]['frame_count'] += frame_count
#             screen_time_per_label[label_input]['screen_time'] += screen_time
#         else:
#             screen_time_per_label[label_input] = {
#                 'frame_count': frame_count,
#                 'screen_time': screen_time
#             }
        
#         print(f"Cluster {label_input} has a screen time of: {screen_time:.2f} minutes.")

#     print("All specified faces have been labeled.")
#     return screen_time_per_label
