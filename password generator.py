from secrets import choice 

def main():
  generator()


def generator():
  flag = True
  passwords = []
  i = 0
  while(flag):
    length = int(input("Введите длинну пароля: "))
    passwords.append(generate(length))
    print(passwords[i])
    i+=1
    userAnswer = input("Создать новый пароль: y/n ")
    if userAnswer.lower().strip() == 'n':
      flag = False
  userAnswer = input("Записать пароли в файл: y/n ")
  if userAnswer.lower().strip() == 'y':
    try:
      with open('pass.txt', 'a') as file:
        for i in passwords:
          file.write(i + '\n')
    except Exception:
      with open('pass.txt', 'w') as file:
        file.write('\n'.join(passwords) + '\n')
  else:
    print("Нажмите любую клавишу, чтобы выйти...")
    input()



def generate(length):
  simbols = ascii()
  password = []
  for i in range(length):
    password.append(choice(simbols))
  return ''.join(password)


def ascii():
  simbols = []
  for i in range(ord('!'), ord('~')+1):
    if i == 36 or i == 46 or i == 47 or i == 63:
      continue
    simbols.append(chr(i))
  return simbols

main()