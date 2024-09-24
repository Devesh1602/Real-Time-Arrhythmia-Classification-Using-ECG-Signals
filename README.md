# Real Time Arrhythmia Classification Using ECG Signals

## Overview
This project tackles the challenge of detecting cardiac arrhythmias from ECG signals by automating the process using deep learning. Cardiovascular diseases affect millions globally, and detecting arrhythmias early can be crucial. Our solution converts ECG-derived QRS complexes into 2D images and uses an 8-layer CNN to classify 17 types of arrhythmias.

## Features
1) QRS Complex Extraction: Based on annotated files, the R-peak is centered and scaled to create uniform input for the model.
2) Data Augmentation: Horizontal/vertical flips, shifts, and cropping were applied to improve model generalization.
3) Proportionate Sampling: To address class imbalance across the 17 arrhythmia types, proportionate sampling was applied.
4) Model: A custom 8-layer deep CNN was designed and trained.
5)Performance: Achieved 92.39% accuracy on test data using 10-fold cross-validation.

## Tech Stack
Frameworks: TensorFlow, Keras
Data Augmentation: OpenCV, NumPy
Languages: Python
Model: Custom CNN

## Usage
Input ECG data and the system will automatically extract QRS complexes and classify arrhythmias.
Outputs include predictions and visualizations of the detected arrhythmia type.

## Results
Accuracy: 92.39% on test data.
10-fold Cross-Validation: Ensured robustness in performance.
Confusion Matrix: Included for detailed performance evaluation.
