from random import randint as randomiser

# Пишем игру. Программа выбирает из диапазона чисел (пусть для начала будет 1-100) случайное число и предлагает
# пользователю его угадать. Пользователь вводит число. Если пользователь не угадал - предлагает пользователю угадать
# еще раз, пока он не угадает. Если угадал - спрашивает хочет ли он повторить игру (Y/N). Если Y - повторить. N - Прекратить.
# Опционально - добавьте в задание вывод сообщения-подсказки. Если пользователь ввел число, и не угадал - сообщать:
# "Холодно" если разница между загаданным и введенным числами больше 10, "Тепло" - если от 5 до 10 и "Горячо" если от 4 до 1.

def user_choice():
    rand = randomiser(1, 100)
    message = 'Try to guess the number 1-100: '
    diff = 0

    while True:
        user_input = int(input(message))
        if user_input > rand:
            diff = user_input - rand
        elif user_input < rand:
            diff = rand - user_input
        else:
            print('You guessed the number!')
            break

        if user_input > 100:
            print('Wrong!')
        elif user_input < 1:
            print('Wrong!')
        else:
            if diff > 10:
                print('Cold!')
            elif diff >= 5 and diff <= 10:
                print('Warm!')
            else:
                print('Hot!')

user_choice()

def prod():

    while True:
        print('Do you want to continue the game? (Y/N): ')
        res = input()

        if res == 'Y' or res == 'y':
             user_choice()
        elif res == 'N' or res == 'n':
            print('Thank you!')
            break
        else:
            print("Wrong value: {}".format(res))
    return res

prod()





