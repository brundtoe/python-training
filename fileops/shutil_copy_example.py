# kræver at aktuelt directory er training
import shutil
import os

shutil.copy('fileops/hello.py','fileops/welcome.py')
print("Copy Sucessful")
shutil.copystat('fileops/hello.py','fileops/welcome.py')
os.remove("fileops/welcome.py")