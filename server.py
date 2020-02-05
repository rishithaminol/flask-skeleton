#!/usr/bin/env python

import os, sys, json, re
from dotenv import load_dotenv, dotenv_values
load_dotenv()

from src import create_app
from src.core import green_output

app = create_app()

#################################
# Load dotenv values (Overwrite)
#################################
for key_, val_ in dotenv_values().items():
	if val_ == 'True' or val_ == 'False':
		app.config[key_] = eval(val_)
	else:
		app.config[key_] = val_

print("==================================[Endpoints]=====================================")
endpoints_ = {}
for rule in app.url_map.iter_rules():
	endpoints_.update({rule.endpoint: {'rule': rule.rule, 'methods': list(rule.methods)}})

for key in sorted(endpoints_.keys()):
	print(green_output(endpoints_[key]['rule']), endpoints_[key]['methods'], green_output(key))
print("==================================[Endpoints]=====================================")

if __name__ == '__main__':
	app.run(port=os.getenv('PORT'))
