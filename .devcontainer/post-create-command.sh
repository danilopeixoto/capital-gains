#!/bin/sh

conda env create -f environment.yaml
echo "conda activate capital-gains" >> ${HOME}/.bashrc
