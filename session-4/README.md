# Multivariate analysis with ROOT.TMVA package
  * Boosting Decision Trees
  * Neural Networks.

## TMVA

### BDT

In particular, for the **BDT**, important parameters are the the learning rate, 
number of boost steps and maximal tree depth:
  * `AdaBoostBeta=0.5`: learning rate for AdaBoost, smaller (~0.1) is better, but takes longer
  * `nTrees=800`: number of boost steps, too large mainly costs time and can cause overtraining
  * `MaxDepth=3`: maximum tree depth, ~2-5 depending on interaction of the variables
  * `nCuts=20`: grid points in variable range to find the optimal cut in node splitting
  * `SeparationType=GiniIndex`: separating criterion at each splitting node 
      to select best variable. The Gini index is one often used measure
  * `MinNodeSize=5%`: minimum percentage of training events required in a leaf node

### MLP

Important **MLP** parameters to tune are the number of neurons on each hidden layer, 
learning rate and the activation function:
 * `HiddenLayers=N,N-1`: number of nodes in each hidden layer for N variables
     - `N` = one hidden layer with N nodes
     - `N,N` = two hidden layers
     - `N+2,N` = two hidden layers, with N+2 nodes in the first
 * `LearningRate=0.02`
 * `NeuronType=sigmoid`: other neuron activation function is `tanh`


## Homework

### Tasks
  1. Optimize signal selection for the Xi_c+ dataset using BDT and NN techiques.
  2. Find the best optimization techique.

### Expected outcome
 1. A reportin PDF-file.
 2. Code in a git repo
