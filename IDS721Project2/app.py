from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/pokemon/<name>')
def get_pokemon(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}/'

    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({'error': 'Unable to retrieve Pokemon data.'}), 500

    data = response.json()

    pokemon = {
        'name': data['name'],
        'id': data['id'],
        'height': data['height'],
        'weight': data['weight'],
        'types': [type_data['type']['name'] for type_data in data['types']],
        'abilities': [ability_data['ability']['name'] for ability_data in data['abilities']],
        'stats': {stat_data['stat']['name']: stat_data['base_stat'] for stat_data in data['stats']}
    }

    return jsonify({'pokemon': pokemon}), 200

if __name__ == '__main__':
    app.run(port=8080, debug=True)
