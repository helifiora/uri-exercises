# https://www.urionlinejudge.com.br/judge/pt/problems/view/1050

ddd = int(input())

results = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte'
}

city = results.get(ddd, None)
if city:
    print(city)
else:
    print('DDD nao cadastrado')
