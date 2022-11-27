import re
import json

def count_size(string):
    return len(string)

def count_special(string, chars="!@#$%^&*()-+\/{}[]"): 
    count = 0 
    for c in string: 
        if c in chars: 
            count += 1 
    return count 

def count_uppercase(string):
    uppercase_characters = re.findall(r"[A-Z]", string)
    return len(uppercase_characters)

def count_lowercase(string):
    lowercase_characters = re.findall(r"[a-z]", string)
    return len(lowercase_characters)
 
def count_numerical(string):
    numerical_characters = re.findall(r"[0-9]", string)
    return len(numerical_characters)

def is_repeated(string):
    teste=re.search(r"^(?!.*(.)\1{1,}).+$",string)
    return teste == None

def verify_minsize_data(password: str, rules: list):
    rule = [cdict for cdict in rules if cdict["rule"] == "minSize"]
    return count_size(password)>= rule[0]["value"] if rule else True

def verify_min_special_char_data(password: str, rules: list):
    rule = [cdict for cdict in rules if cdict["rule"] == "minSpecialChars"]
    return count_special(password)>= rule[0]["value"] if rule else True

def verify_min_uppercase_data(password: str, rules: list):
    rule = [cdict for cdict in rules if cdict["rule"] == "minUppercase"]
    return  count_uppercase(password)>= rule[0]["value"] if rule else True
    
def verify_min_lowercase_data(password: str, rules: list):
    rule = [cdict for cdict in rules if cdict["rule"] == "minLowercase"]
    return count_lowercase(password)>= rule[0]["value"] if rule else True

def verify_min_digit_data(password: str, rules: list):
    rule = [cdict for cdict in rules if cdict["rule"] == "minDigit"]
    return count_numerical(password)>= rule[0]["value"] if rule else True

def verify_no_repeated_data(password: str, rules: list):
    rule = [cdict for cdict in rules if cdict["rule"] == "minDigit"]
    return not(is_repeated(password)) if rule else True

def verify_is_valid_password(password: str, rules: list):
    result=[]
    result.append(verify_minsize_data(password, rules))
    result.append(verify_min_special_char_data(password, rules))
    result.append(verify_min_uppercase_data(password, rules))
    result.append(verify_min_lowercase_data(password, rules))
    result.append(verify_min_digit_data(password, rules))
    result.append(verify_no_repeated_data(password, rules))
    return sum(result) == 6
    
