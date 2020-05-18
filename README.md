# Practice course

This part of repository contains documentation and code, which are needed for a practice in a Laboratory of baryonic physics of High energy physics department of PNPI.

Practice is organized as a bunch o sessions followed by homeworks. At the end of the practice student reports are expected.

## Precursors
* **PNPI PhD course of statistics and data analysis** mainly to have a proper vocabular.
* **Python programming language**. Here are some documentation, tutorials as well as a couple of courses (in Russian):
  - Python documantation and tutorals https://docs.python.org/3/ ; 
  - More tutorials https://pythonprogramming.net/ ;
  - Applied Python (in Russian): htthttps://www.youtube.com/watch?v=oLN3-1UX0-A&list=PLrCZzMib1e9qM62lMXC90SiFy7-1-kAPJ&index=1ps://www.youtube.com/watch?v=oLN3-1UX0-A&list=PLrCZzMib1e9qM62lMXC90SiFy7-1-kAPJ&index=1 ;
  - Algorythms with Python 3 (in Russian): https://www.youtube.com/watch?v=KdZ4HF1SrFs ;
  - Practice of programming with Python 3 (in Russian): https://www.youtube.com/watch?v=fgf57Sa5A-A .

## Practice synopsis
  * **Setup session:** Introdution to:
    * **Git** - a distributed version control system to store the code.
    * **Markdown** - a plain text formatting syntax.
    * **Introdution to statistics** - some basics we need to start coding.
      - Measurements and uncertainties;
      - Probability distribution functions and their basic pproperties;
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
      - Chi-square and maximum likelyhood fits.
      - Extended and non-extended fits.
    * Uncertainty validation using Toy-Monte-Carlo.
    * Distributions for a signal and a background components:
      - Sideband subtruction;
      - Fit-in-bin technique;
      - _sPlot_ unfolding techinque.
  * **Session 2:** Cut-based techique.
    * How to find best requirements?
    * Are requirements optimal?
      - Fluctuations
      - Look elswhere effect
      - When to use signal for background rejection optimisations?
  * **Session 3:** Simple classification methods
    * Support vector machine
    * k-nearest
  * **Session 4:** Multivariate analysis with ROOT.TMVA package 
    * Boosting Decision Trees
    * Neural Networks.
  * **Session 5:** Dealing with Monte-Carlo
    * How to re-weight MC to data?
    * Weighted fit for efficiency evaluation.
    * How to estimate efficiency for not-well reconstructed events?
  

## Software stack
 * **Ubuntu 18.04 LTS**, as operation system (possible _via_ VirtualBox).
 * **Ostap** for data analysis (default is a _conda_-way).
 * **CERN ROOT** will be used _via_ Ostap, but it has much better documentation.
 * **Git** to store code.
 * **Markdown**  way to style text on the web.
 * **LaTeX** to prepare report.

For details of instalation see **_man/_** in the root of repository.
