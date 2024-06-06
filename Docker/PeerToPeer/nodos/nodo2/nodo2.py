from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

nodos_vecinos = {
    "nodo1": "http://172.18.0.11:5001",
    "nodo3": "http://172.18.0.13:5003"
}

numero_nodo2 = 2
sumatoria_actual_del_nodo2 = 2

@app.route('/ofrecer_numeros_nodo2', methods=['GET'])
def ofrecer_numeros_nodo2():
    return jsonify({
        "numero_nodo2": numero_nodo2,
        "sumatoria_actual_del_nodo2": sumatoria_actual_del_nodo2
    }), 200

@app.route('/obtener_nodo<id>/sumar_su_numero', methods=['GET'])
def sumar_numero_vecino(id):
    nodo = f"nodo{id}"
    try:
        response = requests.get(nodos_vecinos[nodo] + f"/ofrecer_numeros_{nodo}")
        if response.status_code == 200:
            datos_nodo = response.json()
            numero_nodo = datos_nodo.get(f"numero_{nodo}", 0)
            global sumatoria_actual_del_nodo2
            sumatoria_actual_del_nodo2 += numero_nodo
            return jsonify({
                "mensaje": f"Numero del {nodo} sumado exitosamente",
                "sumatoria_actual_del_nodo2": sumatoria_actual_del_nodo2
            }), 200
        else:
            return jsonify({"error": f"No se pudo obtener el numero del {nodo}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/obtener_nodo<id>/sumatoria_actual', methods=['GET'])
def obtener_sumatoria_vecino(id):
    nodo = f"nodo{id}"
    try:
        response = requests.get(nodos_vecinos[nodo] + f"/ofrecer_numeros_{nodo}")
        if response.status_code == 200:
            datos_nodo = response.json()
            sumatoria_actual_del_nodo = datos_nodo.get(f"sumatoria_actual_del_{nodo}", 0)
            global sumatoria_actual_del_nodo2
            sumatoria_actual_del_nodo2 += sumatoria_actual_del_nodo
            return jsonify({
                f"sumatoria_actual_del_{nodo}": sumatoria_actual_del_nodo,
                "sumatoria_actual_del_nodo2": sumatoria_actual_del_nodo2
            }), 200
        else:
            return jsonify({"error": f"No se pudo obtener la sumatoria del {nodo}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

