import bottle
from bottle import post, request
import json, checks
import datetime

@post('/articles', method='post')

def add_article():
    
    title = request.forms.get('TITLE')
    description = request.forms.get('DESCRIPTION')
    author = request.forms.get('AUTHOR')
    phone = request.forms.get('PHONE')
    published_date = datetime.date.today().isoformat()
    author_email = request.forms.get('AUTHOR_EMAIL')
    written_date = request.forms.get('WRITTEN_DATE')

    
    if title=="" or description=="" or author=="" or author_email=="":
        return "Fill all the fields!"


    if not checks.author_email_correct(author_email):
        return "Please, put a correct email"

    
    if not checks.written_date_correct(written_date):
        return "Data should have a format 'YYYY-MM-DD' and not be after today"

    
    if not checks.author_phone(phone):
        return "Enter correct phone number!"

   
    with open('articles.json', 'r') as file:
        articles=json.load(file)
        articles_number = len(articles)

    
    with open('articles.json', 'w') as file:
        articles[articles_number+1] = {'author':author, 'title':title,'description':description,
                                       'published_date': published_date,'written_date': written_date, 'phone':phone, 'author_email': author_email}
        json.dump(articles, file)

    return "The article is added!"
