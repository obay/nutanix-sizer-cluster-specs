#!/bin/bash

pyenv virtualenv nutanix-sizer-cluster-specs
pip install --quiet -r requirements.txt
python main.py