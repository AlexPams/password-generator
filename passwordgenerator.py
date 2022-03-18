from secrets import choice


def generate(length, banned_symbols):
    symbols = ascii(banned_symbols)
    password = []
    for i in range(length):
        password.append(choice(symbols))
    return ''.join(password)


def ascii(banned_symbols):
    symbols = []
    for i in range(ord('!'), ord('~') + 1):
        if chr(i) in banned_symbols:
            continue
        symbols.append(chr(i))
    return symbols


def write_in_file(passwords):
    try:
        with open('pass.txt', 'a') as file:
            for i in passwords:
                file.write(i + '\n')
    except Exception:
        with open('pass.txt', 'w') as file:
            file.write('\n'.join(passwords) + '\n')
