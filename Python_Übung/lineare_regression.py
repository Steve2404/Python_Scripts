# -*- coding: utf-8 -*-

# lineare_regression
#
# Routinen zur Berechnung der multivariaten linearen Regression mit Modell-
# funktion
#
# h_theta(x) = theta_0 + theta_1 * x_1 + ... + theta_n * x_n
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
#        [ - x^(1) - ]
#   X = [    .      ]    (m Zeilen und n Spalten)
#       [ - x^(m) - ]
#


import numpy as np


# %% extend_matrix

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
    vek_one = np.ones((X.shape[0], 1))
    X_ext = np.concatenate((vek_one, X), axis=1)
    return X_ext


# %% LR_fit

# Berechnung der optimalen Parameter der multivariaten linearen Regression
# mithilfe der Normalengleichung.
#
# theta = LR_fit(X, y)
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
    Xn = extend_matrix(X)
    Xt = Xn.T
    a = Xt.dot(Xn)
    b = Xt.dot(y)
    theta = np.linalg.solve(a, b)
    return theta


# %% LR_predict

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
    y = extend_matrix(X).dot(theta)
    return y


# %% r2_score

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
    r1 = extend_matrix(X).dot(theta)
    c = (r1 - y) ** 2
    r2 = np.sum(c) / 2 * X.shape[0]
    return r2
