import smtplib


def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login("assistantaivoice@gmail.com", "assistant7531")
    server.sendmail("assistantaivoice@gmail.com", to, content)
    server.close()
