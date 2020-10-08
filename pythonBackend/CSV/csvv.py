import csv

with open('C:\\MySpace\\pythonEmpirical\\PythonBackendAutomation\\pythonBackend\\utilties\\registration.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimiter= ',')
    #print(list(csvReader))
    # for row in csvReader:
    #     print(row)
    names = []
    status = []
    for row in csvReader:
        names.append(row[0])
        status.append(row[1])
       #print(row[0])
       #print(row[1])
#print[names]
#print[status]
Index = names.index("jim")
print(Index)
loanstatus = status[Index]
print("jim status"+" "+ loanstatus)
