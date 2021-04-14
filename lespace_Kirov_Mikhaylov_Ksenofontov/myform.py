from bottle import post, request 

import json
import re
#import pdb
@post('/home', method='post')

def my_form():
    mail = request.forms.get('ADRESS')
    Question = request.forms.get('QUEST')
    Hystory = {}
    data = {}
    Hystory[mail] = Question
    with open('data.txt') as f:
        data = json.load(f)
    newData = data.update(Hystory)
    pattern=r"^\w+[@][a-z]{2,6}(\.[a-z]{2,4}){1,2}$"
    number_re=re.compile(pattern)
    #pdb.set_trace()
    with open('data.txt', 'w') as outfile:
         json.dump(newData, outfile)
    if number_re.findall(mail) and Question:
        return "Thanks! The answer will be sent to the mail %s" % mail
    else:
        return "Error, make suer the mail is entered correctly and that all fields are filled"
    

    