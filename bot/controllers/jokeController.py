from parsingBashOrg import parsingBash


def randomJoke():
  try:
    return parsingBash.getRandomJoke()
  except:
    return "Ошибка запроса данных =("  

def BestRandomJoke():
  try:
    return parsingBash.getBestJoke() 
  except:
    return "Ошибка запроса данных =("  


def PageOrYearJoke(data): 
  try:
    if data: 
      pageOrYear, amountJokes = data
      if pageOrYear.isdigit() and (amountJokes.isdigit() and int(amountJokes) <= 5): 
          return parsingBash.getPageOrYearJoke(int(pageOrYear), int(amountJokes)) 
      else: return ["Введите команду /jokeyop [номер страници] [колличество цитат]"]    
    else: return ["Введите команду /jokeyop [номер страници] [колличество цитат]"]
  except:
      return "Ошибка запроса данных =("       

    

  
