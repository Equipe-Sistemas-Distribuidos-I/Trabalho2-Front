from flask import Flask, render_template, request, jsonify, send_from_directory
import os

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

@app.route('/public/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(root_dir, 'public'), filename)

if __name__ == '__main__':
    app.run(debug=True, port=5555)
