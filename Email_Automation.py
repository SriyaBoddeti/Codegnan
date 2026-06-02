'''
SMTP (Simple Mail Transfer Protocol)
-------------------------------------
--> This is used to send e-mails from server to another.
--> server to server

NOTE:
-----
1. SMTP SSL PORT
-----------------
465

2. SMTP TLS PORT
-------------------
587

import smtplib

EmailMessage Class - contains sender mail,receiver mail,text
-------------------
msg['Subject'] = 'SMTP ON Mail'
msg['From'] = 'sender@mail.com'
msg['To'] = 'Receiver@mail.com'


import smtplib
from email.message import EmailMessage
sender = 'sriyaboddeti05@gmail.com'
password = 'ogfkhamhyllrcfth'


msg['Subject'] = 'Welcome mail'
msg['From'] = sender
msg['To'] = 'poornimapappu18@gmail.com'

msg.set_content('Hai Pappu')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()

'''
import smtplib
from email.message import EmailMessage

sender ='sriyaboddeti05@gmail.com'
password = 'pfnskyhwobvmwvrg'
receiver = ['poornimapappu18@gmail.com','girishaaa57@gmail.com']
server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()
server.login(sender,password)
for email in receiver:
    msg = EmailMessage()

    msg['Subject'] = 'Welcome mail'
    msg['From'] = sender
    msg['To'] = email
    msg.set_content("Hai /n Happy Coding " )

    server.send_message(msg)
server.quit()
