import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'cd91109263a86aac88d52a850c802570'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
TRAINER_NAME = "naschkatze" 
TRAINER_ID = "29633"
POKEMON_ID = "297963"  # Было имя "Будь ласка"
NEW_NAME = "bud laska"  # Новое имя латиницей

# 1 Проверь, что ответ запрос GET /trainers приходит с кодом 200

def test_get_trainers_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

# 2 Проверь, что в ответе приходит строчка с именем твоего тренера
def test_get_my_trainer_id_in_response():
    response = requests.get(url = f'{URL}/trainers',params = {"trainer_id": TRAINER_ID})
    assert response.status_code == 200
    
    trainers = response.json()["data"]
    
    my_trainer = next(t for t in trainers if t["id"] == TRAINER_ID)
    
    assert my_trainer["trainer_name"] == TRAINER_NAME