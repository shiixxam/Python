import smtplib
from email.message import EmailMessage





server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()


server_login_mail=("shivamgpk9766@gmail.com")
server_login_password = ("pkmxsgjkxruoofjh")


server.login(server_login_mail,server_login_password)



email = EmailMessage()

email['from'] = server_login_mail
email ['to'] = ('kanchangpr@gmail.com')
email['subject'] = 'sending email using pyhton'

email.set_content('''Dear Ma'am/Sir,

I trust this email finds you well. Regrettably, I couldn't complete the entire Module 3 today. Lesson 4 remains pending due to a sudden illness. I apologize for any inconvenience this may cause. On a positive note, I would like to inform you that I am sending this email programmatically using Python SMTP, a skill I acquired today.

Thank you for your understanding.

Best regards,
Shivam Gupta''')


server.send_message(email)