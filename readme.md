# Sequence Classifier
This project implements a machine learning model to classify DNA, RNA, and protein sequences. It includes a graphical user interface (GUI) for easy interaction.

## Overview
The sequence classifier follows these main steps:

1. Read sequence data from FASTA files
2. Extract features from sequences using one-hot encoding 
3. Train a Support Vector Machine (SVM) model on the sequence features
4. Build a GUI with Tkinter to allow user sequence input and classification

## Usage
To use the sequence classifier:

1. Clone this GitHub repository
2. Install dependencies: `pip install -r requirements.txt` 
3. Run `python sequence_classifier.py`
4. Input sequences via the GUI and hit "Classify" 

The output will display the predicted class (positive/negative), predicted probability, and detected sequence type (DNA, RNA, or protein).
Some sample sequences are provided to test the classifier.

## Implementation Details
- `read_fasta.py` - Module to parse FASTA files and extract sequences
- `feature_extraction.py` - One-hot encoding of sequences 
- `model_training.py` - Functions to train SVM model
- `gui.py` - Tkinter GUI implementation
- `sequence_classifier.py` - Main driver script

The trained SVM model and sample training data are provided in the `models/` and `data/` directories respectively.

## Contributing
Contributions to improve the sequence classifier are welcome! Potential areas of improvement:

- Additional feature engineering from sequences 
- Trying other machine learning algorithms
- Enhancing the GUI
- Expanding the sequence database

Please open an issue or submit a pull request if you would like to contribute.
