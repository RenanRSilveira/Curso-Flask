import requests

informacoes = '{"Nome": "Joao", "Sobrenome": "Candiotto", "Idade": 29}' # deletar informações
requisicao = requests.delete("https://teste-hashtag-fc87c-default-rtdb.firebaseio.com/1/.json", data=informacoes)
print(requisicao)
print(requisicao.json())