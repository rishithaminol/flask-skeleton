#!/usr/bin/env python

import os, sys
from dotenv import load_dotenv, dotenv_values
load_dotenv()

from src import create_app

app = create_app()

#################################
# Load dotenv values (Overwrite)
#################################
for key_, val_ in dotenv_values().items():
	if val_ == 'True' or val_ == 'False':
		app.config[key_] = eval(val_)
	else:
		app.config[key_] = val_

app.run(port=os.getenv('PORT'))
