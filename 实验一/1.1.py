def login(attempts=1, saved_psw=123456):
    while attempts <= 3:
        temp = int(input())
        attempts += 1
        if temp == saved_psw:
            print('Login success!')
            break
        else:
            print('Wrong password or invalid input, Remaining attempts: ' + str(4 - attempts))
            if attempts > 3:
                print('Your account has been suspended')
            continue


login()
