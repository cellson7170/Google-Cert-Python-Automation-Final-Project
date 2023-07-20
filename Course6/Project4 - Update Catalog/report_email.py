#!/usr/bin/env python3

import os
import reports
import datetime
import sys
import emails


def create_directory(path):
  os.makedirs(os.path.dirname(path), exist_ok=True)
  return open(path, 'w')

def main(argv):

    cwd = os.getcwd() + "/Course6/Project4 - Update Catalog/supplier-data/descriptions/"
    files = os.listdir(cwd)
    title = "Processed update on {}".format(datetime.datetime.now().date())
    paragraph = ""

    for item in files:
        file = os.path.join(cwd, item)
        with open(file, "r") as desc:
            name, weight, extra = desc.readlines()
        paragraph += "name: {}{}weight: {}{}".format(name.rstrip('\n'), "<br/>", weight.rstrip('\n'), "<br/><br/>")

    with create_directory("/tmp/processed.pdf"):
        reports.generate_report("/tmp/processed.pdf", title, paragraph)

    message = emails.generate_email("automation@example.com", 
                          "<username>@example.com", 
                          "Upload Completed - Online Fruit Store",
                          "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
                          "/tmp/processed.pdf")
    
    emails.send_email(message)

if __name__ == "__main__":
    main(sys.argv)
