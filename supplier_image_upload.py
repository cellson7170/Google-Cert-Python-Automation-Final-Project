#!/usr/bin/env python3
import os
import requests
from PIL import Image

url = "https://173-255-214-250.ip.linodeusercontent.com"
cwd = os.getcwd() + "/Course6/Project4 - Update Catalog/supplier-data/images/"

def upload(file):
    with open(cwd + file, 'rb') as opened:
        r = requests.post(url, files={'files': opened})
        print(r.status_code)


for item in os.listdir(cwd):
    img = Image.open(cwd + item)
    if img.format == 'JPEG':
        upload(item)
    else:
        continue