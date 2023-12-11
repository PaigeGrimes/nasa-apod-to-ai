# README.md
## nasa-apod-to-ai
### Galaxy Canvas Web Application

## Project Overview: A concise description of your application
This application empowers users to harness NASA's Astronomy Photo of the Day (APOD) API for AI-driven image development. It seamlessly integrates the APOD image’s with OpenAI’s DALL-E-2 API, generating captivating AI-rendered images based on the provided photo explanations. Users can explore their creations in the Gallery, downloading these original, beautiful images inspired by NASA's visuals for personal use. Explore a captivating, fun way to craft unique images inspired by the wonders of space.

# Installation and Setup instructions: Steps to get your application up and running.
1. Get a free APOD API key at https://api.nasa.gov/
   -- this will replace the DEMO_KEY in js-api.js file.
   
   ``` var api_key = 'DEMO_KEY' ```
   
3. Create an account at https://openai.com/ and access their API's then navigate to 'API keys' to create a secret key for DALL-E-2. This will replace OPENAI_API_KEY in app.py. _Note_: The size field will affect the price of the api for each time you run it. Visit https://openai.com/pricing to learn more about pricing.

   ``` openai.api_key = 'OPENAI_API_KEY' ```
   
5. The virtual environment will need to install the following packages in the application terminal:
   * openai:
   ```pip install openai```
  * sqlite3:
   ```pip install sqlite3```

# Usage Guide: How users can navigate and use your application.
## Home Page:
* APOD Image Display:
* Upon landing on the home page, users will immediately see the Astronomy Photo of the Day (APOD) image, accompanied by its title, date, and a brief description.

## DALL-E-2 Image Output:
* Below the APOD image, users will find the AI-generated image created by the DALL-E-2 API based on the provided photo explanation.
  
## Gallery Tab:
### Viewing AI Images:
* Navigate to the "Gallery" tab located in the navigation bar.
* Users will find a collection of AI images created within the past hour.
* Select an image to view and save it for personal use.

# Testing Procedures: Instructions on how to test your application


# Contrubutions and Acknowledgments: Credit any collaborators or sources.
