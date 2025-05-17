from flask import Flask, request
import request

requisicao = request.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
print(requisicao)