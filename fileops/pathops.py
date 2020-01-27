import os

abspath = os.path.abspath('fileops/hello.py')
print('abspath:\t',abspath)

dirname = os.path.dirname(abspath)
print('dirname:\t',dirname)

basename = os.path.basename(abspath)
print('basename\t',basename)