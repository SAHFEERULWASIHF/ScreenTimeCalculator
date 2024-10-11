from face_recognition.face_recognition import FaceRecognition

if __name__ == "__main__":
    video_path = 'input/spiderman.mp4'
    face_recognition = FaceRecognition(video_path)
    face_recognition.run()
