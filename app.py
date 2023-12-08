import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static', static_folder='static')

openai.api_key = "OPENAI_API_KEY"


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/submit', methods=['GET'])
def hello_world():
    explanation = request.args.get('explanation', '')  # Use args to get the query parameter
    print(explanation)
    response = openai.images.generate(
        model="dall-e-2",
        prompt=explanation,
        n=1,
        size="1024x1024"
    )
    print(response)
    image_url = response.data[0].url
    return jsonify({'image': image_url})


if __name__ == '__main__':
    app.run(port=5000)
