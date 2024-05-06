import requests
import json
#Get data from forex API

request = requests.get("https://v6.exchangerate-api.com/v6/31e6837d9bf5717e3d305eaf/latest/USD")
#Check if API works
print(request.status_code)
forex_data = request.json()
#start converting
conversion_rates = forex_data["conversion_rates"]
USD = conversion_rates["USD"]
PHP = conversion_rates["PHP"]
#inputs
currencyIn = conversion_rates[input("Enter Currency 1 (Input Currency) Here:   ")] 
currencyOut = conversion_rates[input("Enter Currency 1 (Output Currency) Here:   ")]
valueIn = float(input("Enter amount of currency 1 you want to convert (float):   "))

print(valueIn/currencyIn*currencyOut)