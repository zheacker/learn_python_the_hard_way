# Learn Python The Hard Way
This is my repo for working through the *Learn Python the Hard Way* book, found [here](https://learnpythonthehardway.org/book/). This will be my foundational crash course in python before I move on to *Test Driven Development* and, eventually, the python data science realm.

This book is in python 2, which dude says is 100% the way to go. Whatever. I'll just learn both and say fuck it... Regardless, I'm not going to use Docker at all. I've installed Anaconda 3, and I'm going to try to use a conda python 2 environment for this whole book. We'll see how it goes.

Final point: this is *Learn Python* ***the Hard Way***. Read every single sentence. Type every single command. I have a hunch this book is more about programming "muscle memory" than anything else.

## Setup and run
Run `setup.sh` to create the conda environment, install any necessary packages, and activate the environment. Everything must be run in this conda environment to ensure stability and reproducibility. Note to self: this setup file should perfectly recreate the environment, which means that at any given time you should be able to destroy the environment with `conda remove --name pythway --all` and rebuild it by running `setup.sh`.

Activating/deactivating the conda environment is pain in the ass, so add these aliases to your `.bashrc`:

* `alias pygo='source activate pythway && cd ~/gitrepos/LearnPythonTheHardWay/'`
* `alias pyno='source deactivate pythway && cd ~'`

Now you can just use `pygo` to start the environment and `cd` into it, and `pyno` to kill it (revert back to the root conda environment) and `cd` out.
