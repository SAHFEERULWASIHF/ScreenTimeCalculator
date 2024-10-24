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
Total screen time for women: 35.34 seconds based on 848 frames
Total screen time for kamal: 9.17 seconds based on 220 frames
```

Additionally, a visual representation (e.g., a plot or chart) may be displayed to illustrate the screen time distribution among characters.

[Sample Input]<!-- Replace with an actual image link -->


https://github.com/user-attachments/assets/22680f19-d24d-4f5c-abb5-7db4a3455c5c

[Respective Sample Output]<!-- Replace with an actual image link -->


https://github.com/user-attachments/assets/ca224afc-fa96-4464-b47c-7906ce027ca2

