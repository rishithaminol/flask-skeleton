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
list_ = []
for rule in app.url_map.iter_rules():
	matched = re.match("^(.*)\..*$", str(rule.endpoint))

	if matched and len(matched.groups()) > 0:
		master_endpoint = matched.group(1)
	else:
		master_endpoint = None

	list_.append({master_endpoint: {'rule': rule.rule, 'methods': list(rule.methods), 'endpoint': rule.endpoint}})

for k in list_:
	for k1, v1 in k.items():
		print(green_output(v1['rule']), v1['methods'], green_output(v1['endpoint']))
print("==================================[Endpoints]=====================================")

app.run(port=os.getenv('PORT'))
