from utilties.configuration import *

################ USE THE METHOD FOR STORING THE PAYLOAD DATA ########################################

def addpayload(isbn):
    body = {
        "name": "Learn  Automation with Java",
        "isbn": isbn,
        "aisle": "124",
        "author": "John foe"
    }
    return body

def getpayloadFromdb(query):
    addBody ={}
    tp = getQuery(query)
    name['name'] = 'tp[0]',
    isbn['isbn'] =  'tp[1]',
    aisle['aisle'] = 'tp[2]',
    author['author'] = 'tp[3]'
    return addBody
