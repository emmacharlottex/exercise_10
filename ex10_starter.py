
# imported the sys, glob and os module
import sys, glob, os

# Using sys.platform method to retrieve the directory name.
# if the platform is equal to 'win32', the os.environ is 'HOMEPATH'
if sys.platform == 'win32':
# os.environ is changed by software.
    hdir = os.environ['HOMEPATH']

# if it is not equal to 'win32', the os.environ is 'HOME'
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
# The * is the wildcard which will be used by glob.glob method
# hdir variable is defined at the start which will determine which filepath is retrieved.
pattern = os.path.join(hdir,'*')
search_dir = 'C:\Code\Homework\week2_ayishat\exercise_10\*.py'

# Use the glob.glob() function to obtain the list of filenames
# defined the search_dir variable and added this to glob.glob method
# to retrieve the file name which matches the pathname pattern defined above
for file in glob.glob(search_dir):
# Use os.path.getsize to find each file's size
# defined size variable using os.path.getsize method with the file variable
    size = os.path.getsize(file)
# print the file name and size in the console
    print(file, size)

# Add a test to only display files that are not zero length
# if statement shows that if the file is not equal to 0, print the file name in console
if file != 0:
    print(file)
# if it is equal to 0, it will print file is 0
else:
    print("file is 0")

# used the os.path.basename method and inserted file variable to remove the
# leading directory names and just print the file name in the console
print(os.path.basename(file))