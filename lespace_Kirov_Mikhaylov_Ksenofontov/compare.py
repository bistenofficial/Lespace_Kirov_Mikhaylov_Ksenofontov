import re
def compare(string):
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@][\w\.]+[.]\w{2,3}$'
    return re.search(regex,string)