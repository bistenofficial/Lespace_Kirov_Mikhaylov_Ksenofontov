from bottle import post, request, re
import pdb
import json

questions ={}
questions['question'] =[]

@post('/home', method='post')
def my_form():
    reg = re.compile(r'\w+@\w+\.\w')

    mail = request.forms.get('ADRESS')
    data = request.forms.get('QUEST')
    if(mail=="" or data==""):
        return "Some field is empty"
    elif reg.match(mail):
        ###pdb.set_trace()
        questions['question'].append({'email':mail,'ask':data})
        with open('questions.txt','w') as outfile:
            json.dump(questions, outfile)
        return "Thanks! The answer will be sent to the mail %s" % mail
    else:
        return "Mail input error"
