# Setup session

Here we'll meet a key components, which will be needed for the practice.

## Git

A component of software configuration management, _version control_, also known as _revision control_ or _source control_, is the management of changes to documents, computer programs, large web sites, and other collections of information. 

A _distributed version control_ (also known as _distributed revision control_) is a form of version control in which the complete codebase, including its full history, is mirrored on every developer's computer. Nowdays, [Git](https://en.wikipedia.org/wiki/Git) is _de-facto_ a standatd everyone uses.

### Quick start

Here we follow [this explanation](https://youtu.be/oLN3-1UX0-A).

Main commands:
  * **git clone URL** - clone a repository (with history and branches);
  * **git init** - create a new empty repository;
  * **git status** - show current status: branch, changes made and added files;
  * **git diff** - changes, which you made for the files at staging.
  * **git add** - add file to staging, they will be used in a foreseen commit;
  * **git commit** - commit changes to repository;
  * **git log** - history of commits
  * **git show COMIMT_HASH** - shows a commit you want to see (main information and changes made);

Typical workflow with the repository you have:
  1. Make chnges in a code (for example in _file.py_).
  2. **git add file.py**
  3. **git commit -m "We did that and that"**

The main code 'line' is calles _master_. It contains a code of the project. Anothe branches of the code are also posiible.

Branches are quite a powerfull concept:
  * **git branch BRANCH_NAME** - to create a new branch, for example, to develope a new feature.
  * Change files and commit changes. They will be done in our new branch.
  * **git checkout master** - switch to master. For example, if you find a bug in the previous code base and want to fix it.
  * Change files and commit changes. They will be done in master.
  * **git branch BRANCH_NAME** - switch back to the branch.
  * **git merge master** - bring changes we made in master into the branch.
  * Change files and commit changes. They will be done in our new branch.
  * **git checkout master** - switch to master agiain.
  * **git merge master** - bring changes we made in the branch into the master.
  * **git br -d BRANCH_NAME** - remove the branch as the feature we finished to develope is already in the master.

Undo changes:
  * **git reset --hard HEAD** - undo all local changes. Note, here _HEAD_ is not a variable you need to subsititute (type this command as is)!
  * **git checkout myfile.py** - undo changes in one file.

### Remote code storage
There are several providers, which allow to store a code remotely. Here are some examples:
  * [GitHub](https://github.com/)
  * [GitLab](https://about.gitlab.com/)
  * [BitBucket](https://bitbucket.org/)

You need to have an account for these sites, if you'd like to use them (create change repository).
 * **git push origin master** - will put your updated master (with all the commits you've made) into this remote storage.

It's better to have a README file in the each folder of the repository or at least in the root-folder of the project. This file will be automatically shown in your web-browser. Now, let's turn to a formatting for these files.

## Markdown
It's preferable to use [Markdown](https://daringfireball.net/projects/markdown/) to prepare documentation for repositories . As authors say, “Markdown” is two things:
  1. A plain text formatting syntax;
  2. A software tool, written in Perl, that converts the plain text formatting to HTML.
We will use the first, as the second is already implemented all over the web. 

Let's follow github guide to see how easy Markdown formating is:
  * https://guides.github.com/features/mastering-markdown/

## Basics of statistics
Here we will discuss:
  * Measurements and uncertainties;
  * Probability distribution functions and their basic pproperties;
  * Three special distributions:
    - Binomial
    - Poisson
    - Gaussian
  * Central limit theorem.
  * Uncertainty propagation.

Let's follow an introduction lecture by [Prof. Mark Thompson](https://www.hep.phy.cam.ac.uk/~thomson/lectures/lectures.html):
  * https://www.hep.phy.cam.ac.uk/~thomson/lectures/statistics/Introduction_Handout.pdf
  * https://www.hep.phy.cam.ac.uk/~thomson/lectures/statistics/GaussianStatistics_Handout.pdf

## Python3

In python3 a basic statistics is impemented into a standard library as a special module, which  provides functions for calculating statistics of data, including averages, variance, and standard deviation.

```python
import statistics as stat
help(stat) # press q to exit back into command line
```

More functionality is provided by special module entering [scipy](https://docs.scipy.org/doc/scipy/reference/) open-source software for mathematics, science, and engineering. Here is a tutorial on **scipy.stats**:
  * https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html

## ROOT, RooFit and Ostap

In our practice we use a three ([matryoshka](https://en.wikipedia.org/wiki/Matryoshka_doll) way packed) frameworks:
  * [ROOT](https://root.cern.ch/) - a modular scientific software toolkit. It provides all the functionalities needed to deal with big data processing, statistical analysis, visualisation and storage. It is mainly written in **C++** but integrated with other languages such as **Python** and **R**.
  * [RooFit](https://root.cern.ch/roofit-20-minutes) - is a package that allows for modeling probability distributions in a compact and abstract way. It is distributed with **ROOT**.
  * [Ostap](https://github.com/OstapHEP/ostap) - is a community-driven initiative aiming to provide more user friendly and more intuitive interface to **ROOT** and extending the existing functionality. It provides (as authors insist):
    - very easy manipulations with **ROOT** and **RooFit** objects: histograms, trees, datasets, _etc_;
    - very easy interface to **RooFit** machinery;
    - extended set of model (probability density functions) for **RooFit**;
    - powerful, pickle-based persistency for object;
    - interactive **ostap** analysis environment (which will be a default one for the practice).

## LaTeX

**LaTeX** -  is a document preparation system. When writing, the writer uses plain text. The writer uses markup tagging conventions to define the general structure of a document (such as article, book, and letter), to stylise text throughout a document (such as bold and italics), and to add citations and cross-references.

There are several TeX-distributions, which can be used on stand-alone computes. Popular are:
  * [TeX Live](https://www.tug.org/texlive/)
  * [MikTeX](https://miktex.org/)

One can use web solution to create and edit LaTeX projects. [Overleaf](https://www.overleaf.com/) is a recommended one.

## Homework

### Task

Create a documentaion about one of special probability density function (requested by a teacher).

### Expected outcome
  * Document in pdf-format containig proper information 
  * Link to a git repository (_github_, _gitlab_, _bitbucket_ or whatsoever), which contains a source code for figures in the report. Repository must contain a documentation on what is going on. 