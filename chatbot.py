def greet(bot_name):
    print("Hello! My name is {0}.".format(bot_name))


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print("\nWhat a great name you have, {0}!".format(name))


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("\nYour age is {0}".format(age))

def end():
    print('Have a nice day!')
    input()

greet('Chatter')
remind_name()
guess_age()
end()
