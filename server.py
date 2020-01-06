#!/usr/bin/env python

import os, sys
# Import and set environment variables for the project
from dotenv import load_dotenv, dotenv_values
load_dotenv()

from src import create_app


print("module search path:", sys.path)


app = create_app()

#################################
# Load dotenv values (Overwrite)
#################################
for key_, val_ in dotenv_values().items():
	if val_ == 'True' or val_ == 'False':
		app.config[key_] = eval(val_)
	else:
		app.config[key_] = val_

app.run(host='0.0.0.0')
