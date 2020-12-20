import csv # csv module makes parsing files a lot easier.

with open('names.csv', 'r') as csv_file: # 'read' and defining a csv_file variable.
    csv_reader = csv.reader(csv_file) # use the READER method.
    # need to loop the csv_reader variable as below:
    next(csv_reader) # starting with the 2nd row.

    with open('new_names.csv', 'w') as new_csv_file: # opening another file to write inside 'names.csv'
        csv_writer = csv.writer(new_csv_file, delimiter = '\t') # using 'tab' instead of commas in the new_csv_file.

        for line in csv_reader: # creating a new_csv_file witn '-' written in the original 'names.csv'
            # print(line[1:3]) # only the last name and emails by index.
            csv_writer.writerow(line)
