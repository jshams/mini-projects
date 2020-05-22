# Pulsar Star Prediction
This project was created to identify if a star is a pulsar star based on various factors.
It uses machine learning to classify a star into two groups: Pulsar or not.
The dataset was taken from [Kaggle - Predicting a Pulsar Star](https://www.kaggle.com/pavanraj159/predicting-a-pulsar-star).

## The Models
The models can be viewed in this neat [Jupyter Notebook](pulsar_stars_ML.ipynb)
that walks throught the steps for creating the two models.  
The first model uses **Support Vector Machines** and the second uses **Logistic Regression**.

## Support Vector Machine (SVM) Model:
An SVM or SVC (support vector classifier) model works by drawing a line between a set
of points to separate two classes.  
<img src="https://www.researchgate.net/profile/Hamid_Baghaee/publication/330557084/figure/fig5/AS:770135056977924@1560625914689/General-classification-hyperplane-representation-of-SVM-algorithm.png" height="300px"/>  
SVM aims to draw the best line (hyperplane) that separates two classes while maximizing the margin.
Maximizing the margin reduces the risk of error.

## Logistic Regression Model:
Logistic regression models work like SVMs except instead of drawing a line, LogReg aims to separate
its data with a sigmoid function that looks like an S-curve.  
<img src="https://storage.ning.com/topology/rest/1.0/file/get/2808358994?profile=original" height="300px"/>  
The S-curve allows LogReg to create a more tailored fit to your data.

## Which model was better?
The SVM model worked slightly better than the LogReg model.
I believe this is because the variance is low among the feature's datas.
Logistic Regression tends to work better wben features have vastly different ranges,
but because the features all have small ranges I believe the SVM model worked better.

## Technologies Used:
- Python
- Pandas
- Sklearn
- Jupyter Notebook
- Seaborn
- Matplotlib
- Numpy

## Methodologies:
- Machine Learning Classification
- Logistic Regression
- Support Vector Machines
- Data Preprocessing

## Original Project:
[Original Pulsar Star Prediction](https://github.com/jshams/DS-2.1-machine-learning/blob/master/assignments/Final-Project/)