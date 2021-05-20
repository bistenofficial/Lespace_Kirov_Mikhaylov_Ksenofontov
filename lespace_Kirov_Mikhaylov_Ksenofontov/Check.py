import re

def check_phone(str):
    pattern=r"^([+]{1}[0-9]{1})|([0-9]{1}) [(]{1}[0-9]{3}[)]{1} [0-9]{3}[-]{1}[0-9]{2}[-]{1}[0-9]{2}$"
    number_re=re.compile(pattern)
    return bool(number_re.findall(str))
