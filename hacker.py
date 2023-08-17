import csv
import json

# Create an empty list to store compromised usernames
compromised_users = []

# Open 'passwords.csv' and read usernames into 'compromised_users' list
with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for item in password_csv:
        compromised_users.append(item['Username'])

# Write compromised usernames to 'compromised_users.csv'
with open('compromised_users.csv', 'w') as compromised_user_file:
    writer = csv.writer(compromised_user_file)
    for username in compromised_users:
        writer.writerow([username])

# Create a dictionary for the boss message and write it to 'boss_message.json'
with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
    json.dump(boss_message_dict, boss_message)

# Create the signature multiline string
slash_null_sig = r'''
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
'''

# Open 'new_passwords.csv' and write the signature
with open('new_passwords.csv', 'w') as new_passwords_obj:
    new_passwords_obj.write(slash_null_sig)
