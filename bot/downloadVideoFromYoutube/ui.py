

def linkReques():
  link = input("Введите  ссылку для скачивания видео/аудио с Youtube: ")
  return link  


def RequestResolution(resolution):
  print("Доступны слеующие разрешния видео:") 
  [print(f"{i}. {value} ") for i, value in enumerate(resolution, start=1)]
  number = int(input("Выберите желаемое разрешение (номер из списка): "))
  return resolution[number-1]

def audioOrVideo():
  print("Что бы вы хотели загрузить с Youtube:")
  print("1. Видео")
  print("2. Аудио")
  print("0. Выход")
  number = int(input("Ответ: "))
  return number


def downoladStatusCheck(status):
  if status:
    return print("Все ОК, загрузка прошла успешно!") 
  else:
    return print("При загруке видео произошла ошибка!")
