import mail


def enterSait ():
    lS = str(input('Enter the login:'))
    if len(lS) <= 4:
        print('Sorry, very short login!')
        return enterSait()
    else:
        def enterPass():
            xS = str(input('Enter the password!'))
            if len(xS) < 8:
                print ('Sorry, very short password!')
                return enterPass()
        enterPass()

    mail.send_mail()
    print('Отчёт отправлен')


enterSait()
