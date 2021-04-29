import re

reg = re.compile(r'^\w+[@](\D{2,6})\.(\D{1-10}\.\D{2,4)|(\D{2,4})$')
def correct (mail):
     if (reg.fullmatch(mail) == None):
         return i
     else:
         return True
     
def uncorrect(mail):
    if (reg.fullmatch(mail) != None):
        return i 
    else:
        return False
