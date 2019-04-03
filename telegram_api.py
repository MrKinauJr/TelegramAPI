import requests

def telegram_text(message, chat_id, token):
      print('Sending Text: ' + message)
      return requests.post('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(chat_id) + '&text=' + message).text

def telegram_getMe(message, chat_id, token):
      print('Sending Text: ' + message)
      return requests.post('https://api.telegram.org/bot' + str(token) + "/getMe").text
