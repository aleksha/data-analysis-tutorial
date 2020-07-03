# Simple classification methods

  * Statistical classification
  * k-nearest neighbors algorithm
  * Support vector machine

## Classification

In general, things we are doing in this tutorial are a **machine learning (ML)**.
ML are computer algorithms that improve automatically through experience. 
ML algorithms build a mathematical model based on sample data (training data), 
in order to make predictions or decisions without being explicitly programmed 
to do so.

ML algorythms could be splited into:
  * Supervised learning
  * Unsupervised learning
Note, that the spliting is not exhausive.

**Supervised learning algorithms** build a mathematical model of a set of data 
that contains both the inputs and the desired outputs. The training data consists 
of a set of training examples. Each example has one or more inputs and the desired 
output (supervisory signal). Through iterative optimization of an objective function, 
supervised learning algorithms learn a function that can be used to predict the 
output associated with new inputs. An optimal function will allow the algorithm 
to correctly determine the output for inputs that were not a part of 
the training data. 

In contrast, **unsupervised learning algorithms** take a set of data that 
contains only inputs (no labels or upervisory signal). These algorythms find 
structure in the data, like grouping or clustering of data points. 
Uunsupervised learning algorithms identify commonalities in the data and react 
based on the presence or absence of such commonalities in each new piece of data. 


Now, let's look in general on the problem of **classification**. 
This is the problem of identifying  to which of a set of categories (sub-populations)
a new observation belongs, on the basis of a training set of data containing 
observations (or instances) whose category membership is known. 
We do already touch it, when trying to distinguish between signal and background events.

## k-nearest neighbors algorithm (k-NN)

k-NN classification, the output is a class membership. An object is classified 
by a plurality vote of its neighbors, with the object being assigned to 
the class most common among its k nearest neighbors (k is a positive integer, 
typically small). If k = 1, then the object is simply assigned to the class of 
that single nearest neighbor.

The k-nearest neighbors algorithm (k-NN) is a non-parametric method.

## Support vector machine (SVM)

An SVM model is a representation of the examples as points in space, 
mapped so that the examples of the separate categories are divided 
by a clear gap that is as wide as possible. More formally, a support-vector 
machine constructs a hyperplane or set of hyperplanes in a high- or 
infinite-dimensional space, which can be used for classification, as well as 
for regression, or other tasks like outliers detection.
