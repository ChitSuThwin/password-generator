import random
import string

from django.shortcuts import render
from zxcvbn import zxcvbn


def home(req):
    return render(req, 'index.html')  # this return index.html


def password(request):
    strengthText = {
        0: "The Worst",
        1: "Very Bad",
        2: "Still Weak",
        3: "Good",
        4: "Strong"
    }
    password_char = ''  # specific characters will be added to this string for randomization
    password = ''
    password_length = int(request.GET['pwLength'])

    # this check form value of checkboxes from html
    # 4 checkboxes = uppercase, lowercase, number, special characters
    if request.GET.get('uppercase'):
        password_char += string.ascii_uppercase
    if request.GET.get('lowercase'):
        password_char += string.ascii_lowercase
    if request.GET.get('number'):
        password_char += string.digits
    if request.GET.get('special_characters'):
        password_char += string.punctuation

    # character randomization according to password length chosen by user
    for x in range(password_length):
        password += random.choice(password_char)

    strength = zxcvbn(password)  # getting the strength of generated password
    str_strength = strengthText[strength['score']]

    return render(request, 'password.html',
                  {'password': password, 'pwStrength': strength['score'],
                   'strengthText': str_strength})

    # this return password.html with following values: password,
    # passwordStrength and strengthText(weak or strong)
