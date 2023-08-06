# Practice course

**__“Probieren geht über studieren” (Trying beats studying).__**

This repository contains documentation and code, which are needed for a PhD-practice in a Laboratory of baryonic physics of High energy physics department of Petersburg Nuclear Physics Institute (LBP HEPD PNPI). Main goal of the practice to show an analysis chain in Particle Physics.

Practice is organized as a bunch of sessions followed by homeworks. At the end of the practice reports from students are expected.

## Software stack
 * **Ubuntu 20.04 LTS**, as operation system (possible _via_ VirtualBox).
 * **Ostap** for data analysis (default is a _conda_-way).
 * **CERN ROOT** will be used _via_ Ostap, but it has much better documentation.
 * **Git** to store code.
 * **Markdown**  way to style text on the web.
 * **LaTeX** to prepare report.

Note, that ths software list reflects LBP's stack. Other solutions are also possible, though they will not be covered by the practice.
 
## Precursors
* **PNPI PhD course of statistics and data analysis** mainly to have a proper vocabular.
* **Python programming language**. Here are some documentation, tutorials as well as a couple of courses (in Russian):
  - Dive into Python3 https://diveintopython3.problemsolving.io/table-of-contents.html ;
  - Python documantation and tutorals https://docs.python.org/3/ ; 
  - More tutorials https://pythonprogramming.net/ ;
  - Applied Python (in Russian): https://www.youtube.com/watch?v=oLN3-1UX0-A&list=PLrCZzMib1e9qM62lMXC90SiFy7-1-kAPJ&index=1ps://www.youtube.com/watch?v=oLN3-1UX0-A&list=PLrCZzMib1e9qM62lMXC90SiFy7-1-kAPJ&index=1 ;
  - Algorithms with Python 3 (in Russian): https://www.youtube.com/watch?v=KdZ4HF1SrFs ;
  - Practice of programming with Python 3 (in Russian): https://www.youtube.com/watch?v=fgf57Sa5A-A .

## Practice synopsis
  * **Setup session:** Introdution to:
    * **Git** - a distributed version control system to store the code.
    * **Markdown** - a plain text formatting syntax.
    * **Introdution to statistics** - some basics we need to start coding.
      - Measurements and uncertainties;
      - Probability distribution functions and their basic properties;
      - Three special distributions:
        - Binomial
        - Poisson
        - Gaussian
      - Central limit theorem.
      - Uncertainty propagation.
    * **ROOT / RooFit / Ostap** - meet the system we'll use.
    * **LaTeX** - to prepare nice scientific reports.
  * **Session 1:** On how to extract a signal.
    * Fitting a signal:
      - Chi-square and maximum likelihood fits.
      - Extended and non-extended fits.
    * Uncertainty validation using Toy-Monte-Carlo.
    * Distributions for a signal and a background components:
      - Sideband subtruction;
      - Fit-in-bin technique;
      - _sPlot_ unfolding techinque.
  * **Session 2:** More on fitting + cut-based technique.
    * Are 2D fits important?
    * How good is your fit?
      - Pull distributions;
      - Toys to obtain likelihood distributions;
    * How to find best requirements?
    * Are requirements optimal?
      - Fluctuations
      - Look elsewhere effect
      - When to use signal for background rejection optimisations?
  * **Session 3:** Simple classification methods
    * Statistical classification
    * Support vector machine (SVM)
    * k-nearest (kNN)
  * **Session 4:** Multivariate analysis with ROOT.TMVA package 
    * Boosting Decision Trees (BDT)
    * Neural Networks (NN).
  * **Session 5:** Dealing with Monte-Carlo
    * Random number generators in ROOT
    * How to re-weight MC to data?
    * Weighted fit for efficiency evaluation.
    * How to estimate efficiency for not-well reconstructed events?
  * **Session 6:** Regression problem / Fourier transformation
    * Why Fourier transform is needed?
    * Using SciPy for FFT
    * What is regression?
    * Least square and Maximum Likelihood methods
    * Using TMVA to solve regression problem (NN, BTD).
  * **Session 7:** Statistical tests
    * Paired samples
    * Wilcoxon and t-test

