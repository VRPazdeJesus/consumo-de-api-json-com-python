import requests 
import json
import pandas
import decimal

url = "http://data.fixer.io/api/latest?access_key=64190d6452dc9af6dfe85d179a27cb99"
print("Acessando base de dados do Fixer.io...")
resposta = requests.get(url)
if resposta.status_code == 200:
    print("Acesso realizado com sucesso!")
    print("Buscando informações...")
    dados = resposta.json()
    dolar_real = round(dados['rates']['BRL']/dados['rates']['USD'], 2)
    euro_real = round(dados['rates']['BRL']/dados['rates']['EUR'], 2)
    btc_real = round(dados['rates']['BRL']/dados['rates']['BTC'], 2)
    print('1 dollar vale ',dolar_real, 'reais')
    print('1 euro vale ',euro_real, 'reais')
    print('1 Bitcoin vale ',btc_real, 'reais')
    print("Exportando resultado em tabela excell...")
    tela = pandas.DataFrame({'Moedas':['Dolar','Euro','Bitcoin'],
                        'Valores':[dolar_real, euro_real, btc_real]})
    tela.to_csv('valores.csv', index=False, sep=";", decimal=",")
    print("Arquivo exportado com sucesso!")
else:
    print("Erro na base de dados")
