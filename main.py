import re
import math
from dateutil.parser import parse

# Strength Estimation
def check_common_password(password):
    with open("commonpass.txt", "r") as f:
        common_passwords = f.read().splitlines()
        for common_pass in common_passwords:
            if common_pass in password:
                return 0
        return 1

def check_credentials(password, first_name, last_name):
    str1 = password
    aux_score = 0
    pattern1 = r'\b{}\b'.format(re.escape(first_name.lower()))
    match1 = re.search(pattern1, str1)
    if match1:
        aux_score -= 2
    else:
        aux_score += 2
    pattern2 = r'\b{}\b'.format(re.escape(last_name.lower()))
    match2 = re.search(pattern2, str1)
    if match2:
        aux_score -= 2
    else:
        aux_score += 2
    date_patterns = [
        r'\b(0?[1-9]|[12][0-9]|3[01])[./-](0?[1-9]|1[012])[./-]\d{4}\b', # dd/mm/yyyy or dd-mm-yyyy or dd.mm.yyyy
        r'\b\d{4}[./-](0?[1-9]|1[012])[./-](0?[1-9]|[12][0-9]|3[01])\b', # yyyy/mm/dd or yyyy-mm-dd or yyyy.mm.dd
        r'\b(0?[1-9]|1[012])[./-](0?[1-9]|[12][0-9]|3[01])[./-]\d{4}\b', # mm/dd/yyyy or mm-dd-yyyy or mm.dd.yyyy
        r'\b(0?[1-9]|[12][0-9]|3[01])(0?[1-9]|1[012])\d{2}\b', # ddmmyy or ddmmyy
        r'\b\d{2}(0?[1-9]|1[012])(0?[1-9]|[12][0-9]|3[01])\b', # yymmdd
    ]
    date_regex = '|'.join(date_patterns)
    match4 = re.search(date_regex, str1)
    if match4:
        aux_score -= 1
    else:
        aux_score += 1
    pattern4 = r'(.)\1{2,}' # Repeated characters
    pattern5 = '0123456789' # Sequential digits
    pattern6 = 'qwertyuiopasdfghjklzxcvbnm' # Keyboard patterns
    if re.search(pattern4, str1):
        aux_score -= 2
    for i in range(len(pattern5)):
        for k in range(i, len(pattern5)):
            str2 = pattern5[i:k+1]
            if (len(str2) > 1) and str2 in password:
                aux_score = 0
            else:
                continue
    for i in range(len(pattern6)):
        for k in range(i, len(pattern6)):
            str3 = pattern6[i:k+1]
            if (len(str3) > 1) and str3 in password:
                aux_score = 0
            else:
                continue
    N = len(password)
    char_set = set(password)
    L = len(char_set)
    entropy = (L * (math.log(N))) / math.log(2)
    if round(entropy) > 80:
        return aux_score+5
    else:
        return aux_score-3


def password_estimation(first_name, last_name, password):
    score = 0
    if len(password) >= 8:
        score += 2
    else:
        for i in range(len(password)-1):
            if not password[i].isalnum() and not password[i+1].isalnum():
                score += 0
            else:
                continue
        else:
            score += 1

    if password.isalnum():
        score -= 2
    else:
        score += 4

    aux_score = check_common_password(password)
    if aux_score == 0:
        score -= 4
    else:
        score += 4

    aux_score = check_credentials(password, first_name, last_name)
    if aux_score == 0:
        aux_score -= 5

    score += aux_score

    if score < 0:
        return f"{score}  Bad"
    elif score >= 0 and score <= 7:
        return f"{score}  Easy"
    elif score >= 10 and score <= 14:
        return f"{score}  Moderate"
    else:
        return f"{score}  Hard"


fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
password = input("Enter your password to check strength: ")

score = password_estimation(fname, lname, password)
print("Score: " + score)
