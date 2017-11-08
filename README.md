# Email-brute-force
+ This is a program that attempts to get access to an email account by 'brute-forcing' it's way in.

+ It tries to log in using passwords from a pre-defined wordlist that may be thousands of lines long.

+ The program prompts you to type an email address. Then it asks for a .txt file from which passwords can be loaded.

+ You can download wordlists from the internet and use the program to try and break into an email account.

+ Currently it is set to the Gmail SMTP server. But you can access other email providers' servers by searching their server and port and inputting this information in the code file.

+ Note that Gmail's server has rate limiting so this program will be disconnected from the server after continuous attempts (around 50 or so from my knowledge).

+ Also, you may want to add a 'time.sleep()' method so that the server does not disconnect you instantly. Again, this is shown as a comment in the code file.

**Note**: *I do not hold any responsibility to any actions caused by other people because of this program. You are accountable for your actions and hold responsibility for any illegal acts that you may commit. You must always test this on your email and your email only. It is only acceptable to try and break into other peoples' email accounts only if you have their permission to do so. Otherwise it is considered an illegal act.*
