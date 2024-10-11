# ScreenTimeCalculator

**ScreenTimeCalculator** is a tool for calculating character screen time in videos using face detection and recognition techniques. It employs RetinaFace for accurate face detection and FaceNet for embedding extraction, enabling users to analyze video content efficiently. Ideal for filmmakers and researchers seeking to quantify character presence.

## Key Features
- Detects faces in videos using RetinaFace.
- Clusters faces to identify different characters.
- Calculates screen time for each character.
- User-friendly command-line interface for easy interaction.

## Technologies Used
- Python
- OpenCV
- Keras with TensorFlow
- NumPy
- Matplotlib

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SAHFEERULWASIHF/ScreenTimeCalculator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ScreenTimeCalculator
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions
1. Place your video file in the `input` directory (create this directory if it doesn’t exist).
2. Run the main script:
   ```bash
   python main.py
   ```
3. Follow the prompts to analyze the video. The program will process the video, detect faces, and calculate screen time for each identified character.

## Example Output
The program will output the detected characters along with their respective screen time. Below is an example of the expected output format:

```
Processing complete!

Please label this face (Cluster -1): peter
Labeled as: peter
Cluster peter has a screen time of: 0.05 seconds with a screen presence of: 0.21%.
Please label this face (Cluster 0): dr octo
Labeled as: dr octo
Cluster dr octo has a screen time of: 7.08 seconds with a screen presence of: 29.64%.
Please label this face (Cluster 1): peter
Labeled as: peter
Cluster peter has a screen time of: 8.88 seconds with a screen presence of: 37.17%.
Please label this face (Cluster 2): peter
Labeled as: peter
Cluster peter has a screen time of: 4.55 seconds with a screen presence of: 19.04%.
All specified faces have been labeled.




Total screen time for peter: 13.48 seconds based on 809 frames
Total screen time for dr octo: 7.08 seconds based on 425 frames
```

Additionally, a visual representation (e.g., a plot or chart) may be displayed to illustrate the screen time distribution among characters.

![Sample Output]<!-- Replace with an actual image link -->


https://github.com/user-attachments/assets/90027074-fdb4-4937-b824-310035fa6f71


