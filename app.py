from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'GET':
        # Lógica para manipular requisições GET
        return 'Endpoint GET'

    elif request.method == 'POST':
        # Lógica para manipular requisições POST
        data = request.json  # Supondo que os dados são enviados como JSON
        tipo = data.get('tipo')
        valor = data.get('valor')

        if tipo is not None and valor is not None:
            # Aqui você pode realizar ações com base nos valores recebidos
            # Por exemplo, imprimir o tipo e o valor no console
            print(f'Tipo: {tipo}, Valor: {valor}')

            # Pode retornar uma resposta JSON indicando sucesso
            return jsonify({'success': True, 'message': 'Dados recebidos com sucesso.'})
        else:
            # Se os parâmetros esperados não foram fornecidos, retornar um erro
            return jsonify({'error': 'Parâmetros ausentes ou inválidos.'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5555)
