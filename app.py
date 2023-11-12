from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'GET':
        return 'Endpoint GET'

    elif request.method == 'POST':
        data = request.json
        tipo = data.get('tipo')
        valor = data.get('valor')

        if tipo is not None and valor is not None:

            print(f'Tipo: {tipo}, Valor: {valor}')

            return jsonify({
                'success': True, 
                'message': 'Dados recebidos com sucesso.',
                'object': data
                })
        else:
            return jsonify({'error': 'Parâmetros ausentes ou inválidos.'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5555)
