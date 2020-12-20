# Dictionary output the key words as well. No need to dig thru the csv file.
# Dictionary writer must provide a 'fieldnames' variable.
import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

#    for line in csv_reader:
#        print(line['email'])

    with open('new_names.csv', 'w') as new_csv_file:
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_csv_file, fieldnames = fieldnames, delimiter = '\t')
        csv_writer.writeheader() # this is my fieldnames as a header in the 1st row.

        for line in csv_reader:
            del line['email'] # deleting the email key from the line.
            csv_writer.writerow(line)
