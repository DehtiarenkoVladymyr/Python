import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail():
    global server
    login = "master-com@ukr.net"
    password = "*******"
    url = "smtp.ukr.net"
    toaddr = "master-com@ukr.net"

    msg = MIMEMultipart()
    msg ['Subject'] = 'Вы выполнили вход'
    msg ['From'] = "master-com@ukr.net"
    body = 'Привет! Вы выполнили вход по логином: '
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP_SSL(url, 465)
    except TimeoutError:
        print("No connect")
    server.login(login, password)
    server.sendmail(login, toaddr, msg.as_string())
    server.quit()

def main():
    send_mail()

if __name__ == '__main__':
    main()