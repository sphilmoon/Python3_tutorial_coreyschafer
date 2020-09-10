import os # os module let you navigate and change files etc.

os.chdir('Users/philmoon/Downloads')

for files in os.listdir():
    file_name, file_ext = os.path.splitext(files)

    file_name, file_course, file_number = file_name.split('-') # getting rid of the '-' in the original file names.

    file_title = file_title.strip() # getting rid of the blank spacings.
    file_course = file_course.strip()
    file_number = file_number.strip()[1:].zfill(2) # starting with the 2nd index. Making digits to two.

    new_name = '{}-{}{}'.format(file_number, file_title, file_ext)

    os.rename(files, new_name)
