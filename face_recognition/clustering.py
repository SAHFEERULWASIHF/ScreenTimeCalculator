from sklearn.cluster import DBSCAN

def cluster_faces(face_embeddings):
    if face_embeddings.ndim != 2 or face_embeddings.shape[0] == 0:
        raise ValueError("Input to DBSCAN must be a non-empty 2D array.")
    
    dbscan = DBSCAN(eps=0.5, min_samples=5, metric='euclidean')
    cluster_labels = dbscan.fit_predict(face_embeddings)
    
    return cluster_labels
