# dict_learning_for_image_reconstruction
A dictionary learning algorithm to reconstruct images from event data
========================================================================

A partial implementation of the paper [Direct face detection and video reconstruction from event cameras](https://ieeexplore.ieee.org/document/7477561) by Souptik Barua, Yoshitaka Miyatani, and Ashok Veeraraghavan.

________________________________________________________________________

The algorithm implemented in the Jupyter notebook reconstructs images from event data, via learning a sparse dictionary with atoms consisting of image gradients and corresponding events on simulated data. At inference time, the algorithm takes only the events as input, and gains the corresponding image gradients from the dictionary.

Installation
=========================================================
If Jupyter is already installed, open the Notebook. If not, install Jupyter notebook (for Linux: pip3 install jupyter), and then open the notebook.

Learn a dictionary
=========================================================
To run the code, download the datasets from [dataset](/dataset), and you are good to go.
