import subprocess

subprocess.call(["touch",'processdemo/sample.txt'])
subprocess.call(["ls"])
print("Sample file created")
subprocess.call(["rm","processdemo/sample.txt"])