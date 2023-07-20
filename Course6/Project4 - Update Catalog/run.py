#! /usr/bin/env python3

import os
import requests
import re

url = "http://[linux-instance-external-IP]/fruits"
cwd = os.getcwd() + "/Course6/Project4 - Update Catalog/supplier-data/descriptions/"
files = os.listdir(cwd)

for item in files:
    file = os.path.join(cwd, item)
    with open(file, "r") as desc:
        f, e = os.path.splitext(item)
        image_name = f + ".jpg"
        name, weight, description = desc.readlines()
        weight = re.sub("[^0-9.\-]", "", weight)
        dictionary = {"name":name.rstrip('\n'),
                        "weight":int(weight),
                        "description":description.rstrip('\n'),
                        "image_name":image_name}
    response = requests.post(url, data=dictionary)
    print(response.status_code)