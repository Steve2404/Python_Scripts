# -*- coding: utf-8 -*-

# lineare_regression
#
# Routinen zur Berechnung der multivariaten linearen Regression mit Modell-
# funktion
#
#   h_theta(x) = theta_0 + theta_1 * x_1 + ... + theta_n * x_n
#
# und Kostenfunktion
# 
#   J(theta) = 1/(2m) sum_i=1^m ( h_theta(x^(i)) - y^(i) )^2
#
# Der Vektor theta wird als
#
#   (theta_0, theta_1, ... , theta_n)
#
# gespeichert. Die Feature-Matrix mit m Daten und n Features als
#
#         [ - x^(1) -  ]
#   X = [    .            ]    (m Zeilen und n Spalten)
#         [ - x^(m) - ]
#

import numpy as np


#%% train_test_split (wird bereit gestellt)

# Teilt den Datensatz in Training (Anteil frac) und Test (Rest)
#
# [Xtrain, Xtest, ytrain, ytest] = train_test_split(X,y,frac)
#
# Eingabe:
#   X      Matrix m x n (numpy.ndarray)
#   y      Vektor der Länge m der Zielwerte (numpy.ndarray)
#   frac   Anteil im Trainingsset 0 <= frac <= 1 
#
# Ausgabe
#   Xtrain Featurematrix Trainingsset 
#          mtrain x n mit mtrain = frac * m (numpy.ndarray)
#   Xtest  Featurematrix Testset 
#          mtest = m - mtrain (numpy.ndarray)
#   ytrain Vektor Zielwerte Trainingsset Länge mtrain (numpy.ndarray)
#   ytest  Vektor Zielwerte Testset Länge mtest (numpy.ndarray)
#
def train_test_split(X, y, frac, seed):
    m = X.shape[0]
    np.random.seed(seed)
    index = np.arange(m)
    np.random.shuffle(index)
    cut = int(m*frac)
    return X[index[:cut],:], X[index[cut:],:], y[index[:cut]], y[index[cut:]]


#%% mean_squared_error

# Berechnung des mittleren Fehlerquadrats
#
# mse = mean_squared_error(y_true, y_pred)
#
# Eingabe:
#   y_true  Vektor der Länge m der wahren Zielwerte (numpy.ndarray)
#   y_pred  Vektor der Länge m der vorhergesagten Zielwerte (numpy.ndarray)
#
# Ausgabe
#   mse    Mittleres Fehlerquadrat mse = 1/m sum_(i=1)^m (y_true_i-y_pred_i)^2
#
def mean_squared_error(y_true, y_pred):
    # TODO: berechne mse
    return mse


#%% Routinen der Belegarbeit
#%% extend_matrix

# Erweitert eine Matrix um eine erste Spalte mit Einsen
#
# X_ext = extend_matrix(X)
#
# Eingabe:
#   X      Matrix m x n (numpy.ndarray)
#
# Ausgabe
#   X_ext  Matrix m x (n+1) der Form [1 X] (numpy.ndarray)
#
def extend_matrix(X):
    # TODO: setze X_ext
    return X_ext


    
#%% LR_fit

# Berechnung der optimalen Parameter der multivariaten linearen Regression 
# mithilfe der Normalengleichung.
#
# X_ext = LR_fit(X, y)
#
# Eingabe:
#   X      Matrix m x n mit m Datenpunkten und n Features (numpy.ndarray)
#   y      Vektor der Länge m der Zielwerte (numpy.ndarray)
#
# Ausgabe
#   theta  Vektor der  Länge n+1 der optimalen Parameter (numpy.ndarray)
#
# Hinweis: Benutzen Sie extend_matrix und np.linalg.solve zur Lösung des 
#   linearen Gleichungssystems
#
def LR_fit(X, y):
    # TODO: berechne theta
    return theta

    
#%% LR_predict

# Berechnung der Vorhersage der der multivariaten linearen Regression.
#
# y = LR_predict(X,theta)
#
# Eingabe:
#   X      Matrix m x n mit m Datenpunkten und n Features (numpy.ndarray)
#   theta  Vektor der  Länge n+1 der Parameter (numpy.ndarray)
#
# Ausgabe
#   y      Vektor der Länge m der Vorhersagewerte (numpy.ndarray)
#
# Hinweis: Benutzen Sie extend_matrix.
#
def LR_predict(X, theta):
    # TODO: berechne y
    return y
    

#%% r2_score

# Berechnung des Bestimmtheitsmaßes R2
#
# y = r2_score(X, y, theta)
#
# Eingabe:
#   X      Matrix m x n mit m Datenpunkten und n Features (numpy.ndarray)
#   y      Vektor der Länge m der Zielwerte (numpy.ndarray)
#   theta  Vektor der  Länge n+1 der Parameter (numpy.ndarray)
#
# Ausgabe
#   r2     Bestimmtheitsmaß R2 (Skalar)
#
# Hinweis: Benutzen Sie LR_predict
#
def r2_score(X, y, theta):
    # TODO: berechne r2
    return r2
