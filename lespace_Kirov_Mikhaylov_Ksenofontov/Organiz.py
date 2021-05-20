import pdb
import json
import os
import Check
from bottle import post, request 


@post('/home1', method='post')
def prepare_organiz():  #Метод для добавления нового партнера
    name = request.forms.get('NAME') #Считывание данных
    telephone = request.forms.get('Telep')
    desc = request.forms.get('DESC')
    if not name: #Проверка на заполненность
        return "Enter name"
    if not telephone:
        return "Enter telephone"
    if not desc:
        return "Enter description"
    if not Check.check_phone(telephone): #Проверка на правильность написания номера
        return "Enter correct phone number!"
    organz = { 
    "Name": name,
    "Telephone": telephone,
    "Description": desc }
    create_organiz(organz)
    return "You are new partner"

def create_organiz(organz): #Выгрузка новой записи в файл
    organiz = []
    try:
        with open('C:/Users/79522/Desktop/organiz.json') as f:
            file_content = f.read()
            organiz = json.loads(file_content)
    except:
        organiz = []
    organiz.append(organz)
    file = open('C:/Users/79522/Desktop/organiz.json', 'w')
    file.write(json.dumps(organiz))
    file.close()

def get_all_organization(): #Получение существующих партнеров
    organiz = []
    with open('C:/Users/79522/Desktop/organiz.json') as f:
        file_content = f.read()
        organiz = json.loads(file_content)
    return organiz