from flask import Flask, request, jsonify
from faker import Faker
import random

app = Flask(__name__)

medicines = ["ACETATO DE CLOSTEBOL/SULFATO DE NEOMICINA CREME 55MG COM 30G",
"ACICLOVIR 400MG COM 30 COMPRIMIDOS",
"ACTONEL CHRONOS 35MG COM 4 COMPRIMIDOS",
"AIXA COM 21 COMPRIMIDOS",
"ALENTHUS XR 150MG COM 30 CÁPSULAS",
"ALENTHUS XR 37,5MG COM 30 CÁPSULAS GEL",
"ALENTHUS XR 75MG COM 30 CÁPSULAS",
"ALLENASAL SPRAY 16,5ML COM 120 DOSES",
"ALPRAZOLAM 0,25MG COM 30 COMPRIMIDOS",
"ALPRAZOLAM 0,5MG COM 30 COMPRIMIDOS",
"ALPRAZOLAM 1MG COM 30 COMPRIMIDOS",
"AMOXICILINA 500MG COM 15 CÁPSULAS",
"NEULEPTIL 10MG COM 20 COMPRIMIDOS",
"NEULEPTIL SUSPENSÃO 1% COM 20ML",
"NORFLOXACINO 400MG COM 14 COMPRIMIDOS",
"OSTEONUTRI 400UI COM 30 COMPRIMIDOS",
"OSTEONUTRI 400UI COM 60 COMPRIMIDOS",
"OXALATO DE ESCITALOPRAM 10MG COM 30 COMPRIMIDOS",
"OXALATO DE ESCITALOPRAM 15MG COM 30 COMPRIMIDOS",
"OXALATO DE ESCITALOPRAM 20MG COM 30 COMPRIMIDOS",
"OXCARBAZEPINA 300MG COM 30 COMPRIMIDOS",
"OXCARBAZEPINA 300MG COM 60 COMPRIMIDOS",
"OXCARBAZEPINA 600MG COM 30 COMPRIMIDOS",
"PLAQUINOL 400MG COM 30 COMPRIMIDOS"]

faker = Faker()
api_mock = []

for i in medicines:
    api_mock.append(dict(
        medicamento = i,
        drogaria = "Farma Direta",
        estoque = random.randrange(100),
        endereco = faker.street_address(),
        cidade = faker.city(),
        latitude = float(faker.coordinate()),
        longitude = float(faker.coordinate())
    ))

@app.route('/products')
def home():
    if 'search' in request.args:
        query = request.args['search']

        results = []

        for item in api_mock:
            if query in item['medicamento']:
                results.append(item)
        if len(results) == 0:
            return jsonify( { 'message': 'No results found.' })
        else:
            return jsonify(results)

    else:
        return jsonify(api_mock)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)