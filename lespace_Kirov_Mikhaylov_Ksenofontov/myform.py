from bottle import post, request, re

@post('/home', method='post')
def my_form():
    reg = re.compile(r'\w+@\w+\.\w')
    mail = request.forms.get('ADRESS')
    if(mail=="" or request.forms.get('QUEST'=="")):
        return "Some field is empty"
    elif reg.match(mail):
        return "Thanks! The answer will be sent to the mail %s" % mail
    else:
        return "Mail input error"