users = {
    "admin": "password228",
    "developer": "iamagod",
    "user": "12345"
}

action = int(input("Яку дію ви хочете зробити? Уведіть номер дії. \nМожливі дії: \nУвійти в існуючий акаунт[1] \nЗареєструватися[2]\nЗавершити роботу[3]\n"))
if action != 3:
    if action == 1:
        while True:
            login = input("\nУведіть ваш нікнейм: ")
            if login in users.keys():
                password = input("Уведіть ваш пароль: ")
                if password in users[login]:
                    print("Ви увійшли в систему!")
                    break
                else:
                    print("Невірний пароль!")
            else:
                print("Невірний нікнейм!")
            attempt_status = False
            while attempt_status == False:
                attempt_status = True
                attempt = input("Спробуєте ще? (Так/Ні) ")
                match attempt:
                    case "Ні" | "ні":
                        login_status = False
                    case "Так" | "так":
                        login_status = True
                    case _:
                        print("Незрозуміла команда, уведіть Так або Ні")
                        attempt_status = False             
    elif action == 2:
        new_login_status = True
        while new_login_status == True:
            login = input("\nПридумайте логін: ")
            if login in users.keys():
                print("Цей логін вже зайнятий, спробуйте ще.\n")
            else:
                password = input("Придумайте пароль: ")
                users[login] = password
                new_login_status = False
                print(users)
    elif action > 3 or action < 1:
        print("Незрозуміла команда, уведіть число від 1 до 3.\n")