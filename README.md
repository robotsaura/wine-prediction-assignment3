# Wine Quality Predictor

## App Wine Quality Predictor
https://wine-q-predictor-89263edf257e.herokuapp.com/

## Author
Saura Naderi

## Class
NU ANA 680

## Problem Statement
Wine quality prediction is an important task for wine producers and consumers alike. Accurate predictions can help in quality control and in making informed choices about wine production and consumption. In this project, we aim to create a predictor for wine quality using machine learning techniques.

## Description
This project utilizes the Wine Quality Dataset from the UCI Machine Learning Repository. The dataset contains features that describe the chemical properties of red and white wine. Our goal is to develop predictive models that can classify the quality of the wine based on these features.

## Methodology
### Data Cleaning
- Removed rows that did not contain integer values.
- Split the dataset into a training set (80%) and a test set (20%).

### Model
- We selected the Random Forest Regressor due to its superior accuracy compared to other models evaluated.
- The trained models for red and white wine were exported as pickle files.

### App Development
- Developed a web application using Flask to create a user-friendly interface for inputting data and viewing predictions.
- Deployed the application on Heroku for easy access and scalability.

## Support
I utilized ChatGPT to assist with writing and debugging the code, ensuring the application runs smoothly and meets the project requirements.

## Interesting to Note

## References
UCI Machine Learning Repository [https://archive.ics.uci.edu/ml/datasets/wine+quality]. Irvine, CA: University of California, School of Information and Computer Science.
