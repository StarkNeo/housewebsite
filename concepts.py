import csv

list_of_terms=[

]
question_types =["text","option"]
def populateList():
    with open("diseases2.csv", "r") as diseases:
        reader = csv.reader(diseases)
        next(reader, None)  # Skip the header row
        for line in reader:
            prompt=line[10]
            list_of_terms.append(prompt)

populateList()
#print(list_of_terms)

