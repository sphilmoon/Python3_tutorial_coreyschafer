import os # importing the built-in os module
from datetime import datetime # importing datetime function from datetime module.
print(os.getcwd()) # printing the os current working directory.

os.chdir('/Users/philmoon/Documents/Python/Schafer_YT') # changing os directory.
os.mkdir('os_demo') # OR
# os.makedirs('os_demo/sub_dir')

print(os.getcwd())

# to remove:
# os.removedirs('os_demo')

# to rename:
os.rename('os_demo', 'new_os_demo') # renaming the directory.

print(os.stat('new_os_demo')) # using the stats function
modi_time = os.stat('new_os_demo').st_mtime # setting a human readable time.
print(datetime.fromtimestamp(modi_time))

# generate traverse directory trees: # from top to bottom:

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path:', dirpath) # start from my current working path.
    print('Directories:', dirnames) # then, my directory.
    print('Files:', filenames) # then, my files.
    print()

# accessing my environment variable and creating a file within:
print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'os_test.txt')
print(file_path)
print(os.path.exists('/tmp/module_test.md')) # checking if the file exists.
