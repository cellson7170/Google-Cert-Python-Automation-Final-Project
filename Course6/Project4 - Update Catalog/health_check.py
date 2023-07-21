#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails
import time




def check_disk_usage(disk):
    # Returns disk usage (total, used, and free) in bytes
    du = shutil.disk_usage(disk)
    # Finds the percentage of disk space used
    free = du.free/du.total*100
    return free >= 20

def check_cpu_usage():
    # Checks the average percentage of CPU usage over 1 second
    usage = psutil.cpu_percent(1)
    return usage <= 80

def check_memory_usage():
    # Returns info about system memory (total, available, percent)
    minMem = 500 * 1024 * 1024 # 500MB
    avail = psutil.virtual_memory()
    return avail.available >= minMem

def resolve_hostname():
    host = socket.gethostbyname('localhost')
    return host == '127.0.0.1'

body = "Please check your system and resolve the issue as soon as possible."

starttime = time.time()

while True:
    if not check_cpu_usage():
        message = emails.generate_simple_email('automation@example.com', 
                                        '<username>@example.com', 
                                        "Error - CPU usage is over 80%",
                                        body)
        emails.send_email(message)

    if not check_disk_usage('/'):
        message = emails.generate_simple_email('automation@example.com', 
                                        '<username>@example.com', 
                                        "Error - Available disk space is less than 20%",
                                        body)
        emails.send_email(message)

    if not check_memory_usage():
        message = emails.generate_simple_email('automation@example.com', 
                                        '<username>@example.com', 
                                        "Error - Available memory is less than 500MB",
                                        body)
        emails.send_email(message)

    if not resolve_hostname():
        message = emails.generate_simple_email('automation@example.com', 
                                        '<username>@example.com', 
                                        "Error - localhost cannot be resolved to 127.0.0.1",
                                        body)
        emails.send_email(message)
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))