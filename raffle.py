import os, random, csv

print("A CSV file with no header should be placed in the directory with this script.\nOne row will randomly be selected from that file.\n...")

filename = input('What is the name of the CSV file for the contact list to be selected from?\n')

if not os.path.isfile(filename):
    print('Can not find file.')
else: 

    with open(filename) as f:
        reader = csv.reader(f)
        chose_row = random.choice(list(reader)) 
print("The random row is: ")
print(chose_row)


