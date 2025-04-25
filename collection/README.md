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

    The notebook makes use of several image processing packages to set up and augment the dataset.

--------------------------------------------------------------------------------------------------

FILE STRUCTURE:

    - processing
        - dataset
            - _raw: Contains the images that come directly from the camera
                - noir
                - rgb
            - nir_mono: Resized NIR images
            - red_mono: Resized RED images
            - rgb: Resized RGB images
            - split_dataset: Contains the dataset after it has been split into the tiles
                - NDVI_MONO
                - NIR_MONO
                - RED_MONO
                - RGB
        README.md: You are here *
        dataset_processing.ipynb: Notebook environment used to process and prepare the dataset. Has
            several methods tthat can be skipped or changed to better fit needs.

--------------------------------------------------------------------------------------------------

