from flask import Flask, request, jsonify
from transcripter import transcribe

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/submit', methods=['POST'])
async def handle_submit():
    data = request.json
    url = data.get('link')
    if not url:
        return "Link not provided!", 500

    result = await transcribe(url)
    print("result", result)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
