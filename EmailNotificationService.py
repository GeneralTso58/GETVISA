import smtplib as smtp
import Credentials

def sendSuccessEmail():
    connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
        
    email_addr = Credentials.GMAIL_BOT_ADDRESS
    email_passwd = Credentials.GMAIL_APP_PASSWORD
    connection.login(email_addr, email_passwd)
    connection.sendmail(from_addr=email_addr, to_addrs=Credentials.GMAIL_PERSONAL_ADDRESS, msg="you got a slot in vancouver!")
    connection.close()

def sendCrashEmail():
    connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
        
    email_addr = Credentials.GMAIL_BOT_ADDRESS
    email_passwd = Credentials.GMAIL_APP_PASSWORD
    connection.login(email_addr, email_passwd)
    connection.sendmail(from_addr=email_addr, to_addrs=Credentials.GMAIL_PERSONAL_ADDRESS, msg="your H1B bot crashed :(")
    connection.close()