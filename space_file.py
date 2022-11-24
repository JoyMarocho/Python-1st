import requests

respose = requests.get('http://api.open-notify.org/astros.json')
json = respose.json()

print ('The people currently in space are:')
for person in json['people']:
    # print(person) - this prints the name and the craft. the dictonary
    #to print only the name of the people 
    
    print(person['name'])