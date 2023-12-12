# README.md
nasa-apod-to-ai

__Title:__ Galaxy Canvas

## Project Overview: 
This application empowers users to harness NASA's Astronomy Photo of the Day (APOD) API for AI-driven image development. It seamlessly integrates the APOD image’s with OpenAI’s DALL-E-2 API, generating captivating AI-rendered images based on the provided photo explanations. Users can explore their creations in the Gallery, downloading these original, beautiful images inspired by NASA's visuals for personal use. Explore a captivating, fun way to craft unique images inspired by the wonders of space.

## Installation and Setup instructions:
1. Get a free APOD API key at https://api.nasa.gov/
   
   _this will replace the DEMO_KEY in js-api.js file._
   
   ``` var api_key = 'DEMO_KEY' ```
   
3. Create an account at https://openai.com/ and access their API's then navigate to 'API keys' to create a secret key. This will replace __OPENAI_API_KEY__ in app.py.

 _Note_: The size field will affect the price of the api. Visit https://openai.com/pricing to learn more about pricing.

   ``` openai.api_key = 'OPENAI_API_KEY' ```
   
4. The virtual environment will need to install the following packages in the application terminal:
   *  openai:
     
   ```pip install openai```
   
   * sqlite3:
    
   ```pip install sqlite3```

## Usage Guide:

### Home Page:

__APOD Image Display__

* Upon landing on the home page, users will immediately see the Astronomy Photo of the Day (APOD) image, accompanied by its title, date, and a brief description.

__DALL-E-2 Image Output__

* Below the APOD image, users will find the AI-generated image created by the DALL-E-2 API based on the provided photo explanation.
  
### Gallery Tab:

__Viewing AI Images__

* Navigate to the "Gallery" tab located in the navigation bar.
* Users will find a collection of AI images created within the past hour.
* Select an image to view and save it for personal use.

## Testing Procedures:

To test the application, follow these steps:

### 1. Clone the Repository:

Clone the repository to your local machine:

   ``` gh repo clone PaigeGrimes/nasa-apod-to-ai ```
   
### 2.**Setup Environment:** Navigate to the project directory and install dependencies:

   ``` cd your-repository ```
   
   * Create a virtual environment (optional but recommended):
     
     ``` python -m venv venv ```
     
   * Activate the virtual environment:
     
     * On Windows:
       
       ``` venv\Scripts\activate ```
       
     * On MacOS and Linux:
       
       ``` source venv/bin/activate```
       
   * Install Dependencies:
     
        ```pip install -r requirements.txt ```
     
### 3. Running the Flask Application:
   * Set environment variables or configurations if necessary.
   * Start the Flask development server:
     
     ``` flask run ```

### 4. Access in Browser: Open a web browser and go to http://localhost:5000 to view the application.

### 5. Perform Testing: Interact with different features and functionalities to ensure they work as expected.

### 6. Test Cases: Execute specific test cases outlined in the project's testing documentation or create your own to validate different scenarios.

### 7. Reporting Issues: If you encounter any issues or bugs, create an issue on the GitHub repository with detailed steps to reproduce the problem.

  
## Contrubutions and Acknowledgments:

### API Credits

The following API was used in this project:

- [NASA APOD](https://api.nasa.gov/) -  NASA Astronomy Picture of the Day (APOD) API - Used to retrieve daily astronomical images and information.
- [DALL-E-2](https://openai.com/dall-e-2) -DALL·E is an AI system that can create realistic images and art from a description in natural language.


