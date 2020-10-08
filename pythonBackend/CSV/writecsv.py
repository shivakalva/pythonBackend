import csv

with open('C:\\MySpace\\pythonEmpirical\\PythonBackendAutomation\\pythonBackend\\utilties\\registration.csv','a') as Write:
    wobject = csv.writer(Write)
    wobject.writerow(["shivaam", "Approved"])
