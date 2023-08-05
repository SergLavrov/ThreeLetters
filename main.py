# Создать класс User, у которого будут:
# Имя
# Фамилия
# Логин (не менее 5 символов)
# Пароль (не меньше 8 символов и должен содержать минимум 3 буквы).

# Все поля должны быть скрытыми.
# К каждому атрибуту написать по два метода.

# Для вывода пользователя метод str не использовать.

class User:

    def __init__(self, first_name, sur_name, login, password):

        self.__firstName = first_name
        self.__surName = sur_name
        self.__loginUser = login
        self.__passwordUser = password

    def get_name(self):
        return self.__firstName

    def get_surname(self):
        return self.__surName

    def get_login(self):
        return self.__loginUser

    def get_password(self):
        return self.__passwordUser

    def set_first_name(self, new_name):
        self.__firstName = new_name

    def get_name(self):
        return self.__firstName

    def set_sur_name(self, new_sur_name):
        self.__surName = new_sur_name

    def get_surname(self):
        return self.__surName

    # def change_first_name(self, new_first_name):
    #     self.firstName = new_first_name

    # def change_sur_name(self, new_sur_name):
    #     self.surName = new_sur_name

    def set_login(self, new_login):
        if new_login != '' and len(new_login) >= 5:
            self.__loginUser = new_login
        else:
            print('Enter login once again: ')

    def get_login(self):
        return self.__loginUser

    def set_password(self, new_password):
        if new_password != '' and len(new_password) >= 8:
            cnt = 0
            for index in range(len(new_password)):
                if new_password[index].isalpha():
                    cnt += 1
                    # print(new_password[index])
            if cnt < 3:
                print('Error: ')

            self.__passwordUser = new_password
        else:
            print('Error: ')

            #     if new_password[index].isalpha:
            #         list1.add(new_password[index])
            #     if len(list1) >= 3:
            #         self.__passwordUser = new_password
            # else:
            #     print('Enter password once again: ')

    def get_password(self):
        return self.__passwordUser

    # def change_login(self, new_login):
    #     if new_login != '' and len(new_login) >= 5:
    #         self.loginUser = new_login
    #     else:
    #         print('Enter login once again: ')

    # def change_password(self, new_password):
    #     self.passwordUser = new_password


# login1 = '77777'
login1 = input('Enter login: ')
if len(login1) < 5:
    print('Enter login once again: ')

# password1 = 'rtf55555'
password1 = input('Enter password: ')
if len(password1) < 8:
    print('Enter password once again: ')

user = User('Иван', 'Иванов', login1, password1)

print(user.get_name())
print(user.get_surname())
print('------------')
print(user.get_login())
print(user.get_password())

print('------------')

user.set_first_name('Петр')
user.set_sur_name('Петров')
print(user.get_name())
print(user.get_surname())

print('------------')

user.set_login('44445')
print(user.get_login())
user.set_password('ttt434343')
print(user.get_password())



# ВЫВОД:
#
# Enter
# login: 77777
# Enter
# password: rtf55555
# Иван
# Иванов
# ------------
# 77777
# rtf55555
# ------------
# Петр
# Петров
# ------------
# 44445
# ttt434343

# user.change_first_name('Ivan')
# user.change_sur_name('Ivanov')
# # # print(user.firstName)
# # # print(user.surName)
# print(user.firstName + '\n' + user.surName)
#
# print('------------')
#
# user.change_login('5555tr')
# user.change_password('uta77755')
#
# print(user.loginUser + '\n' + user.passwordUser)

