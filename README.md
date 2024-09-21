# Weather App

This is a simple Weather App built using Python's Flask framework. The app fetches weather information based on user input (city name) using the OpenWeatherMap API.

## Features
- Fetches current weather information for any city worldwide.
- Displays temperature, weather conditions, and other related data.
- Simple and easy-to-use web interface.

## Technologies Used
- **Flask**: A lightweight web framework for Python.
- **HTML/CSS**: For the frontend UI.
- **OpenWeatherMap API**: For fetching real-time weather data.

## Prerequisites
To run this project locally, you will need the following installed:
- Python 3. x
- Flask
- Requests

## Installation
**Clone the repository:**
   ```bash
   git clone https://github.com/mounikasrinivasarao/Weather_App
   cd weather-app-flask
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt

**Copy code**
Flask==2.1.1
requests==2.27.1
Get an API key from OpenWeatherMap and update your .env or config.py file with the key.

**Run the app:**
bash
Copy code
python app.py
Open your browser and go to http://127.0.0.1:5000.

**How It Works**
Users enter a city name.
The app sends a request to the OpenWeatherMap API to fetch weather data for that city.
The weather information is displayed on the page, including temperature, weather description, etc.

**Project Structure**
**Copy code**
├── app.py                 # Main Flask application file
├── templates/
│   └── index.html         # HTML template for the user interface
├── static/
│   ├── style.css          # CSS for styling the webpage
├── config.py              # API Key configuration (optional)
└── README.md              # This file
Screenshots

Future Improvements
Add a 5-day weather forecast.
Improve error handling for invalid city names.
Add geolocation support for automatic location-based weather information.
License
This project is licensed under the MIT License - see the LICENSE file for details.

vb net
Copy code

### Instructions for Customization:
- **API Key**: Ensure you obtain an API key from OpenWeatherMap and add it to your `config.py` or `.env` file as needed.
- **Project Structure**: Adjust the project structure depending on how you've set up the folders in your app.
- **Screenshots**: If you have screenshots, you can add a placeholder or a link to them in the README.

This `README.md` file provides a clear and concise overview of the Weather App, its features, in
