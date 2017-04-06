#!/bin/bash
## Setup the conda environment (python 2)
## First install Anaconda from www.anaconda.org

conda create --name pythway python=2.7 -y
conda install -n pythway distribute nose -y
source activate pythway

## in Anaconda on Windows:
## activate pythway

## figure oout how to set execute permissions on github?
## do permissions set locally then pushed persist?
