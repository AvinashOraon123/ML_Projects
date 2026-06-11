# Rail-Wheel Contact Analysis Neural Network

This project implements a deep learning regression model designed to predict rail-wheel contact parameters based on an augmented dataset. It utilizes a feed-forward neural network architecture built with TensorFlow/Keras to analyze complex relationships between input features and target contact variables.

## Project Overview

The objective of this model is to perform accurate regression analysis to facilitate understanding of contact mechanics in railway engineering. The workflow encompasses data preprocessing, feature scaling, model architecture design, hyperparameter training, and comprehensive performance evaluation.

## Workflow

* **Data Loading & Preprocessing**: The pipeline loads data from Excel, splits it into training, validation, and test sets, and applies `StandardScaler` to ensure normalized input for the neural network.
* **Neural Network Architecture**: The model is defined as a `Sequential` network consisting of:
* Input layer handling 14 features.
* Hidden layers: 64 units (`relu`), 36 units (`relu`), and 24 units (`tanh`).
* Output layer: Single unit for continuous regression output.


* **Training**: Optimized using the Adam optimizer with Mean Absolute Error (MAE) as the loss function over 500 epochs with a batch size of 30.
* **Evaluation**: Model performance is validated using R² score, Root Mean Squared Error (RMSE), and Mean Absolute Error (MAE).
* **Output**: Predictions are inverse-transformed to their original scale and exported to an Excel file with a timestamped filename for further analysis.

## Key Metrics

The model evaluates performance using the following metrics:

* **R² Score**: To determine the proportion of variance explained by the model.
* **RMSE**: To quantify the magnitude of prediction errors.
* **MAE**: To measure the average absolute error between predicted and actual values.

## File Contents

* `avinash_neural_network_rail_wheel_contant_analysis_for_workshop.py`: The core Python notebook/script containing the full data pipeline and model logic.
* `Augmented_Data.xlsx`: (Required Input) The dataset containing the 14 feature columns and the target variable.
* `model1_WN_.keras`: The saved trained model file generated upon successful execution.

## Requirements

To run this project, you will need the following Python libraries:

* `tensorflow`
* `pandas`
* `numpy`
* `matplotlib`
* `scikit-learn`
* `openpyxl` (for Excel file handling)

## Usage

1. Ensure your `Augmented_Data.xlsx` file is correctly formatted with features in columns 0–13 and the target variable in column 15.
2. Update the data loading path if running in a local environment instead of Google Colab.
3. Execute the script to train the model and generate performance plots.
4. The final predictions will be automatically downloaded as an Excel report.
