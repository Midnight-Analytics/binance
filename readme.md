# Download Python
We'll be using python 3.9 throughout this poject, you can find this here - https://www.python.org/downloads/
At the time of writing this, the latest release was - python 3.9.7

If using windows, make sure to tick "Add Python 3.9 to PATH" before installing
You will likely need to restart for you're environment variables to update before continuing

Select the python3.9 interpreter by pressing Ctrl+Shift+P and searching select interpreter
You should see python 3.9 in the ist of available environments

# Create a virtual environment#
To create a virtual environment, use the following command, where ".venv" is the name of the environment folder:
for sake of ease i recommand leaving this as is

# macOS/Linux
# You may need to run sudo apt-get install python3-venv first
`python3 -m venv .binance`

# Windows
# You can also use py -3 -m venv .venv
`python -m venv .binance`

# Activate your environment
`.binance\Scripts\Activate`

If successful you will see (.binance) before the path in your terminal

# Installing dependencies
`pip install -r requirements.txt`


# Configure Telegram

You will need to follow the instructions here - https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580

Once done, configure telegram - `telegram-send --configure`


# Binance information

Useful information pertaining to the API can be found here - https://binance-docs.github.io/apidocs/spot/en/#change-log