from secrets import choice



def generate(length):
    simbols = ascii()
    password = []
    for i in range(length):
        password.append(choice(simbols))
    return ''.join(password)


def ascii():
    simbols = []
    for i in range(ord('!'), ord('~') + 1):
        if i == 36 or i == 46 or i == 47 or i == 63:
            continue
        simbols.append(chr(i))
    return simbols


def write_in_file(passwords):
    try:
        with open('pass.txt', 'a') as file:
            for i in passwords:
                file.write(i + '\n')
    except Exception:
        with open('pass.txt', 'w') as file:
            file.write('\n'.join(passwords) + '\n')


