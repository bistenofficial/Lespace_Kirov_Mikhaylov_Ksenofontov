import re
import pdb
import json
import os
from bottle import post, request 
@post('/home', method='post')
def my_form():
    questions = {}
    pattern = r'^\w+[@](\D{2,6})\.(\D{1-10}\.\D{2,4)|(\D{2,4})$'
    mail = request.forms.get('ADRESS')
    text = request.forms.get('QUEST')
    number_re=re.compile(pattern)
    if(text == ""):
        if(mail == ""):
            return "Fill in both fields"
        else: return "Fill in the question field"
    else:
        if(mail == ""):
            return "Fill in mail field"
    if(number_re.findall(mail)):
        if(os.stat('C:/Users/79522/Desktop/data.txt').st_size !=0):
            with open ('C:/Users/79522/Desktop/data.txt') as fr:
                questions = json.load(fr)
                fr.close
        with open ('C:/Users/79522/Desktop/data.txt','w') as outfile:
            questions[mail] = text
            json.dump(questions,outfile)
        return "Thanks! The answer will be sent to the mail %s" %mail
    else: return "Mail does not match format"