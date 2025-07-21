'''
1: !!! First navigate to the correct directory !!!

2: python3 -m venv <name>

3: source <name>/bin/activate <-- for mac/linux
    <name>\Scripts\activate <-- for windows

4: python3 -m pip list <-- shows what is installed & what versions

pypi.org <-- search for packages online (documentation)
'''

import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

requestURL = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}&units=imperial'
