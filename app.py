import sqlite3
import openai
from flask import Flask, render_template, request, jsonify, session
import datetime
from datetime import datetime, timedelta
from config import OPENAI_API_KEY, SESSION_KEY

# Start the app and import keys
app = Flask(__name__, static_url_path='/static', static_folder='static')
openai.api_key = OPENAI_API_KEY
app.secret_key = SESSION_KEY
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)


# Before using the session, set it as permanent
@app.before_request
def make_session_permanent():
    session.permanent = True


# Call the homepage
@app.route('/')
def home():
    return render_template('index.html')


# /submit processes the AI information and sends it back to index.html
@app.route('/submit', methods=['GET'])
def hello_world():
    # Use args to get the query parameter's
    title = request.args.get('title', '')
    date = request.args.get('date', '')
    pic = request.args.get('pic')
    explanation = request.args.get('explanation', '')

    # Print the explanation to ensure it is being received
    print(explanation)

    # Join sentences until the total length is <= 1000 characters
    # The prompt cannot except and explanation longer than 1000 characters.
    sentences = explanation.split(".")  # Split by sentence
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
    print(response)     # print the response

    image_url = response.data[0].url    # Save the AI image URL to image_url
    # Save the values in a tuple, so they can be added to the database
    values = (title, date, explanation, pic, image_url)
    print(f"title: {title}, date: {date}, pic: {pic}, explanation: {explanation}")
    add_sql(values)  # Add values to the database before returning the AI image_url

    return jsonify({'image': image_url})


def add_sql(data):
    # Open the database
    conn = sqlite3.connect("ApodToAI")
    cursor = conn.cursor()
    # Get the current date and time to keep track of when a DALL-E image later expires
    curr_time = datetime.utcnow()
    # Insert the data values into the database
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
    if rows:    # If rows exist
        for row in rows:    # Iterate throw the rows and save them to the dictionary
            data_dict = {
                'Title': row[0],
                'Date': row[1],
                'Description': row[2],
                'APOD': row[3],
                'DALLE': row[4]
            }
            data_list.append(data_dict)
        conn.close()
    else:
        # If the dictionary is empty, return 0
        return 0

    # Pass the data to the HTML template
    return data_list


# Function to delete records older than one hour
def delete_old_records():
    conn = sqlite3.connect("ApodToAI")
    cursor = conn.cursor()
    # Query to DELETE rows that are expired
    delete_query = "DELETE FROM ImageHistory WHERE timestamp_column <= datetime('now', '-1 hours')"
    # Execute the query
    cursor.execute(delete_query)
    conn.commit()
    conn.close()


# Route for displaying the gallery
@app.route('/gallery')
def gallery():
    # Get the information on images that have already been created in the database
    data = get_images()
    # If data is empty, return a webpage informing the user that there are no images
    if data == 0:
        return render_template('emptyGallery.html')
    # Check if there are any records in data that need to be deleted
    delete_old_records()
    # Print data to ensure information is correct
    print(data)

    return render_template('gallery.html', data=data)


if __name__ == '__main__':
    app.run()
