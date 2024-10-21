# Project: SVD and Its Application

## Introduction

This project implements Singular Value Decomposition (SVD) and applies it to two areas: image compression and collaborative filtering.

**Keep it simple:** Mathematics is often the art of assigning different names to the same concept. SVD is essentially just decomposing vectors onto orthogonal axes—it just happens to have a fancier name.

## Requirements

To run the notebooks, you will need:

- Python 3.6+
- Numpy
- Matplotlib
- Scipy
- OpenCV (`cv2`)

Alternatively, you can use [Google Colab](https://colab.research.google.com) to run the code without installation.

### Installation

To install the necessary packages, run the following commands:

```bash
pip install numpy
pip install matplotlib
pip install scipy
pip install opencv-python

```
## Prerequisite Knowledge

To fully understand the project, you should have basic knowledge of:

- **Linear Algebra**: vectors, matrices, inverse matrices, eigenvalues, eigenvectors, unit length, properties of matrices (especially square matrices).
  - If you need a refresher, refer to [Linear Algebra](#) or [Eigenvalues and Eigenvectors](#).
  
- **Python**: You should also have some experience with Python, basic image processing, and machine learning concepts.

## Decomposing a Vector into Two Orthogonal Axes

In this section, we will decompose a 2D vector into two orthogonal axes. This process can be applied to any 2D vector, and the axes are orthogonal to each other. For more information, see [Decomposing a Vector into Two Orthogonal Axes](#).

## Applying SVD to Matrices

After understanding vector decomposition, we will extend this concept to matrices. We'll express the operation of vector decomposition using matrices through SVD.

## Notebooks for Image Processing using SVD

### 1. `Denoising_Image_SVD.ipynb`

This notebook demonstrates how SVD can be applied to reduce noise in images. It walks through loading a noisy image, applying SVD, and visualizing the results.

**Usage**:
- Load a image
- LOad a file noise.npy
- Apply different levels of approximation by using fewer singular values.
- Observe noise reduction as image quality improves.

### 2. `Image_Compression.ipynb`

In this notebook, SVD is applied to compress images. By retaining fewer singular values, you can compress the image while maintaining an acceptable level of quality.

**Usage**:
- Load an image.
- Apply SVD to achieve compression by reducing the number of singular values.
- Observe the balance between compression level and image quality.
