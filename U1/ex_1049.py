# https://www.urionlinejudge.com.br/judge/pt/problems/view/1049

v1 = input()
v2 = input()
v3 = input()

results = {
    'vertebrado': {
        'ave': {
            'carnivoro': 'aguia',
            'onivoro': 'pomba'
        },
        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca'
        }
    },
    'invertebrado': {
        'inseto': {
            'hematofago': 'pulga',
            'herbivoro': 'lagarta'
        },
        'anelideo': {
            'hematofago': 'sanguessuga',
            'onivoro': 'minhoca'
        }
    }
}

try:
    animal = results[v1][v2][v3]
    print(animal)
except KeyError as e:
    x = 50
