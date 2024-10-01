from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Configura tu clave de API de OpenAI
openai.api_key = "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"

@app.route('/procesar', methods=['POST'])
def procesar_texto():
    datos = request.get_json()
    
    if 'texto' not in datos:
        return jsonify({"error": "Falta el campo 'texto' en la solicitud"}), 400

    texto = datos['texto']

    # Enviar el texto al Custom GPT de OpenAI
    respuesta = openai.Completion.create(
        model="tu_modelo_personalizado",  # Aquí va el ID de tu GPT personalizado
        prompt=f"Convierte este texto en un guion: {texto}",
        max_tokens=500
    )

    guion = respuesta.choices[0].text.strip()

    return jsonify({"guion": guion})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
