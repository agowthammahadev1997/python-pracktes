
#crating a csv file
import csv
#open the file for writing moade, newline="" is used to prevent blank lines between rows in the CSV file.
with open("students.csv", "w", newline="") as file:
#csv.writer(file) – CSVలో రాయడానికి writer తయారు చేస్తుంది.
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])

    writer.writerow(["Gowtham", 22, 90])
    writer.writerow(["Ravi", 21, 85])
    writer.writerow(["Suresh", 23, 95])


"""Read CSV file"""
with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

"""add new data to the existing CSV file"""

with open("students.csv", "a", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Kiran", 22, 88])


