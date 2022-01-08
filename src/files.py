import json

def readCustomers():
    try:
        f1=open('../resources/customers.json','r')
        customers=json.load(f1)
        f1.close()
        return customers
    except:
        return ("Error reading from file")
        f1.close()
