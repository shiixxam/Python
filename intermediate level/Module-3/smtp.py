

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_address= "shivamgpk9766@gmail.com"
password= "skhb risp wqia idad"   #here come the password from google account 
to_address = 'shivamgupta4g143@gmail.com'


msg = MIMEMultipart()

#storing the senders email address


msg ['from'] = from_address
msg['to'] = to_address
msg['subject']='hey i am sending this mail using python coding'


#string to store the body of email

body ='body_of_the_email'

#attach the body with the msg instance

msg.attach(MIMEText(body,'plain'))


#open the file to be sent

filename = 'intermediate level/Module-3/hey.png'

attachment = open(filename,'rb')


#instance of mimebase and named as p
p= MIMEBase('application','octet-stream')  #it is use to send the packets in small parts

#to change the paylaod into encoded 
p.set_payload((attachment).read())


#encode into base64(p)
encoders.encode_base64(p)


p.add_header("content-Disposition","attachment; filename= %s"% filename)

#atach the instance 'p' to instance 'msg'

msg.attach(p)

#create smtp session

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
server.login(from_address,password)


#converts the multipart msg into a string

text = msg.as_string

server.send_message(msg)

server.quit