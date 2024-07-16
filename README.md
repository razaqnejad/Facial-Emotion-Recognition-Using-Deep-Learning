# Facial Emotion Recognition Using Deep Learning CNN

This project focuses on developing a real-time facial emotion detection system using various machine learning algorithms, with a primary focus on Convolutional Neural Networks (CNN). The performance of CNN is compared against other algorithms like Random Forest (RF), Support Vector Machine (SVM), K-Nearest Neighbors (KNN), and VggNet.

## Authors
- Fatemeh Reazaqnejad
- razaqnejad@gmail.com
## Course
Algorithmic Graph Theory by Dr. Farnaz Shikhi, Computer Engineering - Fall

## Introduction
This project aims to develop a real-time emotion detection system. After evaluating multiple algorithms, we determined that CNN provided the best overall performance for real-time emotion detection, despite Random Forest initially showing better results on test files.

## Dataset
Download Dataset: [Facial Emotion Recognition Dataset](https://drive.google.com/file/d/1tedoFTFFBbM2iUvdg37WQFSq07ghYrll/view?usp=drive_link)

## Steps to Follow
1. **Adding Libraries**: Import necessary libraries for data processing, model training, and evaluation.
2. **Loading Dataset**: Load and preprocess the dataset for model training.
3. **Apply PCA**: Use PCA for dimensionality reduction and save the PCA-transformed data.
4. **Train with Algorithms**: Train models using SVM, RF, CNN, VggNet, and KNN algorithms, and save the model data.
5. **Load Model**: Load the trained model for evaluation.
6. **Get Reports**: Generate and analyze reports to evaluate model performance.
7. **Save Test Predictions**: Save the predictions made on test data.
8. **Reload Model and Map Emotions**: Load the model and map predicted emotions.
9. **Real-Time Face Recognition**: Implement real-time face recognition.
10. **Real-Time Recognition with Emojis**: Enhance real-time recognition by overlaying emojis on detected faces.

## Data Loading
Load and preprocess the dataset by splitting into training and testing sets and applying PCA for dimensionality reduction.

## Model Training and Evaluation
Train various models and evaluate their performance to select the best model for real-time emotion detection. CNN was chosen for its robustness, accuracy, efficiency, and generalization capabilities.

## CNN Model Training
The CNN model includes multiple convolutional layers, max pooling layers, and dense layers to classify emotions accurately.

## Model Saving and Loading
Save the trained CNN model and preprocessing tools (scaler and PCA) to files for consistent application during future predictions. Load the model for real-time use.

## Real-Time Emotion Detection
Implement real-time face detection and emotion recognition, with the option to overlay emojis on detected faces based on the predicted emotion.

## Running the Code
To run the project, follow these steps:
1. Ensure all necessary libraries are installed.
2. Download and preprocess the dataset.
3. Train the models and save the best-performing one.
4. Load the trained model for real-time emotion detection.
5. Run the real-time face detection with emoji overlay.

## Example Output
<div style="display: flex; align-items: flex-start;">
    <div style="margin-right: 20px;">
        <div>
            <strong>Angry</strong>
            <br>
            <img src="../media/Real_Time/angry.png" width="350" style="margin-top: 10px;">
        </div>
        <div style="margin-top: 10px;">
            <strong>Happy</strong>
            <br>
            <img src="../media/Real_Time/happy.png" width="350" style="margin-top: 10px;">
        </div>
    </div>
    <div style="margin-right: 20px;">
        <div>
            <strong>Surprise</strong>
            <br>
            <img src="../media/Real_Time/surprise.png" width="350" style="margin-top: 10px;">
        </div>
        <div style="margin-top: 10px;">
            <strong>Sad</strong>
            <br>
            <img src="../media/Real_Time/sad.png" width="350" style="margin-top: 10px;">
        </div>
    </div>
    <div style="margin-right: 20px;">
        <div>
            <strong>Fear</strong>
            <br>
            <img src="../media/Real_Time/fear.png" width="350" style="margin-top: 10px;">
        </div>
        <div style="margin-top: 10px;">
            <strong>Neutral</strong>
            <br>
            <img src="../media/Real_Time/neutral.png" width="350" style="margin-top: 10px;">
        </div>
</div>

## Contact
For any questions or issues, please contact the authors by razaqnejad@gmail.com
