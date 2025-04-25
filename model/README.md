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

    The notebook make use of TensorFlow and Keras as the main machine learning framework.

    The GAN model is broken into two submodels:
        Discriminator: Provides feedback to the generator on how 'real' the images seem.
            - Architecture: Makes use of SpectralNormalized Convolutional2D layers to extract spacial
            patterns and prevent gradient issues. The output shape from the model is not one dimensional to allow for flexibility.
            - Loss: A modified BinaryCrossentropy is used because the Discriminator is picking one of
            two classes: real or fake. The discriminator is trained on two real and fake image pairs 
            at the same time, so the loss is the agrigate of the two values.
        Generator: Generates the predicted NDVI map based on the RGB input.
            - Architecture: Modified UNET model that makes use of 5 encoders and 5 decoders with skip connections between the encoders and decoders of matching sizes. Between the set of encoders and set of decoders is the bottle neck.
            - Loss: The loss is calculated using the performance of generated images against the discriminator and the L1 loss. The total loss is calculated as gen_loss + LAMBDA * l1_loss where LAMBDA is a value that weights L1 loss higher to encourage the model to match the image instead of just beat the discriminator.

    The training loop runs one batch at a time, meaning images are pulled and generated as sets.

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
