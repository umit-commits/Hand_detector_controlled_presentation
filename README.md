# my_projects1
 
Welcome to the Hand Detector Controlled Presentation project! This project allows you to control a presentation using hand gestures detected by a webcam. The presentation consists of slides stored in the "slides" folder, and you can navigate through them by performing specific hand gestures.

Prerequisites
* Python
* OpenCV
* cvzone library

Installation
1 - Clone the repository: 
git clone https://github.com/your-username/your-repository.git
cd your-repository

2 - Install the required dependencies:
pip install opencv-python
pip install numpy
pip install cvzone

Usage 
1 -Ensure your webcam is connected.
2 - Run the hand_detector_presentation.py script:
python hand_detector_presentation.py

Use the following hand gestures to control the presentation:
Thumb up: Move to the previous slide.
Little finger (pinky) extended: Move to the next slide.
Three extended fingers (index, middle, ring): Draw on the current slide.
Four extended fingers (excluding thumb): Undo the last drawing.
Press 'q' to exit the presentation.


Configuration 
*You can customize the presentation by adjusting the following parameters in the script:

my_path: Path to the folder containing slides.
width and height: Webcam resolution.
gestur_line: The height at which hand gestures are accepted.
button_delay: Number of frames to wait between button presses.

Feel free to modify the code to suit your specific requirements or integrate additional features. If you encounter any issues or have suggestions, please create an issue on the GitHub repository. Happy presenting!
