# Detect Sample Dataset

The dataset used for sample and finger detection was collected by **Al-Waleed Al-Isaii**, a software engineer at **Sohar University, Oman**.

## Dataset Description

The primary focus of the dataset that has been collected is to train the AI model to detect the required Regions of Interest (ROIs), regardless of whether the sample was placed correctly on the container or not, as long as the sample is in its place under the fingers.
The required ROIs are the following:
•	The fingers and sample (R1)
•	The sample (R2)
•	The fingers (R3)

The methodology for collecting the dataset was to have the camera placed in four different predetermined positions, by sliding it to the left or to the right. In each camera position, the light level was changed five times and in each light level the exposure of the camera was adjusted accordingly. The exposure values are reflected in the name of each image. Moreover, in light level 5, the focus of the camera needed to be adjusted, otherwise the image would look blurry.

The light levels represent the following light conditions:
Level 1: The room lights were on.
Level 2: The room lights were off, the door was shut, and a portable LED light was on and facing directly at the container.
Level 3: The room lights were off, the door was shut, and a portable LED light was on but facing away from the container at an approximately 90-degree angle to the left of the container.
Level 4: The room lights were off, the door was shut, and a portable LED light was on but facing away from the container at an approximately 180-degree angle.
Level 5: The room lights were off, the door was shut, and the portable LED light was turned off. The only light source was coming through the door's window.

Furthermore, in each camera position and light level, the samples were shuffled around on the container, with each different sample placed at least once under the fingers.
