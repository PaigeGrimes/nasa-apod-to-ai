import sqlite3
import openai
from flask import Flask, render_template, request, jsonify, session
import datetime
from datetime import datetime, timedelta

app = Flask(__name__, static_url_path='/static', static_folder='static')
openai.api_key = "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"
app.secret_key = 'applesauce'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)


# Before using the session, set it as permanent
@app.before_request
def make_session_permanent():
    session.permanent = True


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['GET'])
def hello_world():
    # Get the explanation from APOD API
    # Use args to get the query parameter
    title = request.args.get('title', '')
    date = request.args.get('date', '')
    pic = request.args.get('pic')
    explanation = request.args.get('explanation', '')

    print(explanation)
    sentences = explanation.split(".")

    # Join sentences until the total length is <= 1000 characters
    modExplanation = ""
    for i in range(len(sentences)):
        if len(modExplanation) + len(sentences[i]) <= 1000:
            modExplanation += sentences[i] + "."
        else:
            break

    # Remove the last sentence
    modExplanation = '.'.join(modExplanation.split('.')[:-1])

    print(modExplanation)  # This will display the modified explanation

    # Generate the AI image
    response = openai.images.generate(
        model="dall-e-2",  # DALL-E-2 model
        prompt=modExplanation,  # Image Prompt
        n=1,  # Number of images to create (1)
        size="1024x1024"  # Size of the image to create
    )
    print(response)
    image_url = response.data[0].url
    values = (title, date, explanation, pic, image_url)
    print(f"title: {title}, date: {date}, pic: {pic}, explanation: {explanation}")
    add_sql(values)

    return jsonify({'image': image_url})


def add_sql(data):
    conn = sqlite3.connect("ApodToAI")
    cursor = conn.cursor()
    curr_time = datetime.utcnow()
    cursor.execute('INSERT INTO ImageHistory(apod_title, date, description, apod_image, dalle_image, timestamp_column)'
                   ' VALUES(?,?,?,?,?,?)', (data[0], data[1], data[2], data[3], data[4], curr_time))
    conn.commit()
    conn.close()


# Function to fetch all images from the database
def get_images():
    conn = sqlite3.connect("ApodToAI")
    cursor = conn.cursor()
    cursor.execute('SELECT apod_title, date, description, apod_image, dalle_image FROM ImageHistory')
    rows = cursor.fetchall()

    # Convert the fetched data into a list of dictionaries
    data_list = []
    for row in rows:
        data_dict = {
            'Title': row[0],  # Replace with the actual column names
            'Date': row[1],  # Replace with the actual column names
            'Description': row[2],
            'APOD': row[3],
            'DALLE': row[4]
        }
        data_list.append(data_dict)

    conn.close()

    # Pass the data to the HTML template
    return data_list


# Function to delete records older than two hours
def delete_old_records():
    conn = sqlite3.connect("ApodToAI")
    cursor = conn.cursor()
    delete_query = "DELETE FROM ImageHistory WHERE timestamp_column <= datetime('now', '-1 hours')"
    cursor.execute(delete_query)
    conn.commit()
    # Close the database connection when done
    conn.close()



# Route for displaying the gallery
@app.route('/gallery')
def gallery():
    delete_old_records()
    data = get_images()
    test_dict = {}
    print(data)

    if data == test_dict:
        return render_template('emptyGallery.html')

    return render_template('gallery.html', data=data)


if __name__ == '__main__':
    app.run(port=5000)
