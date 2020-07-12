# Regression problem
    * Some theory
    * Least square and Maximum Likelihood methods
    * Using TMVA to solve regression problem (kNN, BTD, NN).
  
## Theory

In statistical modeling, **regression analysis** is a set of statistical processes 
for estimating the relationships between a dependent variable (often called 
the 'outcome variable') and one or more independent variables (often called 
'predictors', 'covariates', or 'features'). 

It's quite a bad term, as can be confused with a 
[regression toward the mean](https://en.wikipedia.org/wiki/Regression_toward_the_mean),
a "result" of the first paper about regression analysis by John Galton.

We did alredy regression, when were construction classification variables.

As physicsts we have try to avoid pure regression and try to understand 
underlying nature of phenomena (see cow example below). But sometimes,
it's hard to avoid it --- we  have some data and need to evaluate best 
value of other variable out of it. Plus, someone can gives up and go
to a finance sector, where they care only about money...

## Assumptions
By itself, a regression is simply a calculation using the data. In order to interpret the output 
of a regression as a meaningful statistical quantity that measures real-world relationships, 
researchers often rely on a number of classical assumptions. These often include:

  * The sample is representative of the population at large.
  * The independent variables are measured with no error.
  * Deviations from the model have an expected value of zero. 
  * The variance of the residuals is constant across observations (homoscedasticity).
  * The residuals are uncorrelated with one another. Mathematically, the variance–covariance 
    matrix of the errors is diagonal.

## Least square

1st component of PCA and linear regresion is a bit different but quite close concepts.
For the 2D case **x** and **y** are equally important, so the total length perpendicular
to a line is minimised. Instead, for the least square method the lines are parallel
to the y-direction.

Least square liniear regressions are sensitive to the outliers.




### Typical mistakes

  * Non-homoscedasticity (American TV example)
  * Strondly correlated predictors (height and foot length example)
  * Non-adecvate model (cow example)
  * Parameter correlated with another "hidden" paramtters 
     (clouds and enemy palane number on successfull bombing)
