import re
from bottle import post, request 
@post('/home', method='post')
def my_form():
    pattern = r'^\w+[@]\D{2,6}\.\D{2,4}$'
    mail = request.forms.get('ADRESS')
    question = request.forms.get('QUEST')
    number_re=re.compile(pattern)
    if(question == ""):
        if(mail == ""):
            return "Fill in both fields"
        else: return "Fill in the question field"
    else: 
        if(mail == ""):
            return "Fill in mail field"
    if(number_re.findall(mail)): return "Thanks! The answer will be sent to the mail %s" %mail
    else: return "Mail does not match format"