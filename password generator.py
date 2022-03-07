from secrets import choice 

def main():
  length = int(input("Введите длинну пароля: "))
  password = generate(length)
  print(password)
  print("Записать пароль в файл: y/n")
  userAnswer = input()
  if userAnswer.lower() == 'y':
    with open('pass.txt', 'w') as file:
      file.write(password)
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
  result = []
  for i in range(ord('0'), ord('~')+1):
    result.append(chr(i))
  return result

main()