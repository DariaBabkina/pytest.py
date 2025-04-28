import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'cd91109263a86aac88d52a850c802570'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
POKEMON_ID = "297963"  # Было имя "Будь ласка"
NEW_NAME = "bud laska"  # Новое имя латиницей

# 1 Создание покемона POST pokemons
body_registation = {
    "trainer_token": TOKEN,
    "email": "babkinadasha@gmail.com",
    "password": "Dasha21321321"
}

# 2 Смена имени покемона PUT pokemons
body_changename = {
    "pokemon_id": POKEMON_ID,
    "name": NEW_NAME,
    "photo_id": 2
}

# 3 Поймать покемона в покебол POST /trainers/add_pokeball
body_addpokeball = {
    "pokemon_id": POKEMON_ID
}

# 1 Создание покемона POST pokemons

response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registation)
print(response.text)

# 2 Смена имени покемона PUT pokemons

response_changename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_changename)
response_data = response_changename.json()
print(response_data['message']) 

# 3 Поймать покемона в покебол POST /trainers/add_pokeball
response_addpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_addpokeball)
response_data = response_addpokeball.json()
print(response_data['message']) 
