# NDVI from One Camera

Predict plant health and NDVI maps from a single camera via spectral imaging and a deep neural network.

--------------------------------------------------------------------------------------------------

CONTRIBUTORS:

	Student Authors:	
        Alexander Hulet    u1299427@utah.edu
        
  	Mentor:	
        Al Ingold          a.ingold@utah.edu

	Instructor:	
        Rajesh Menon       rmenon@eng.utah.edu

--------------------------------------------------------------------------------------------------

IMPLEMENTATION:

    Hardware List:
    - Raspberry Pi 5
    - Raspberry Pi Camera Module 2 (8MP)
        - Recommend swapping this out for camera matching the NOIR cameras specs
    - ArduCam NoIR Camera Module (16MP)
        - There is a version of this camera that has an IR cut filter. Using the matching camera
        would likely improve results due to less distortion from preprocessing and resizing.
    - 33 mm IR Pass filter
    - 5V/3A Batter pack
        - The pi 5 requires the power input to be able to supply at least 5V at 3A, though getting as close to 5V at 5A as possible is ideal.
    - Button and LED
        - Used with the Pi's GPIO pins to take pictures and indicate that the camera is ready for
        use.

    NOTE: We used Raspberry Pi Connect to interface with the device remotely. It requires the device
        to be on the same network as the pi, but removes the need for any other periferals. If you want to go that way, you'll need to set up your pi account on the Pi 5 by either reinstalling the OS or by creating a new user account with permisions.

    Capture.py: The script that runs the image capturing. It takes a burst of image pairs and records timestamps that are used to remove unpaired images.
    - The LED will illuminate when the camera is ready to take pictures.
    - Press the button, the camera will take a burst of images, and wait for the LED to re-illuminate.
    - The image pairs are saved to the folders on the desktop, transfer the images to a USB to
    move the dataset to a desktop to train the model.
    - The script is run on startup from it's location on the desktop. If you need to adjust or troubleshoot you can do so by altering the file on the desktop.

--------------------------------------------------------------------------------------------------

FILE STRUCTURE:

    - model
        - dataset
            - train
                - inputs
                    - NDVI: Contains the ground truth NDVI maps
                    - RGB: Contains the real inputs
        discriminator_model.keras: Most recently saved version of the discriminator model.
            The training notebook is set up to automatically update this file every 10000 
            steps.
        generator_model.keras: Most recently saved version of the generator model.
            The training notebook is set up to automatically update this file every 10000 
            steps.
        README.md: You are here *
        training_notebook.ipynb: Notebook environment used to train the Pix2Pix model. Has
            several methods to help with analysis and dataset management.

--------------------------------------------------------------------------------------------------

USAGE:

	Ensure the dataset has been properly prepared and placed. At the bottom of the file you can
    update the location of the dataset and load the models you are using.
 
--------------------------------------------------------------------------------------------------
