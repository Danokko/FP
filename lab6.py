import requests

class CurrencyConverter:
    def __init__(self, base_currency='USD'):
        self.base_currency = base_currency
        self.rates = {}
        self.update_rates()

    def update_rates(self):
        try:
            response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{self.base_currency}")
            data = response.json()
            self.rates = data['rates']
            print("Rates updated successfully.")
        except Exception as e:
            print(f"Error fetching rates: {e}")

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        try:
            rate = self.rates[to_currency] / self.rates[from_currency]
            return amount * rate
        except KeyError:
            print("Currency not found in rates")

def main():
    converter = CurrencyConverter()

    while True:
        print("Enter 'quit' to exit.")
        from_currency = input("Enter source currency: ").upper()
        if from_currency == 'QUIT':
            break
        to_currency = input("Enter target currency: ").upper()
        if to_currency == 'QUIT':
            break
        amount = float(input("Enter amount: "))
        if amount == 'QUIT':
            break

        result = converter.convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {result} {to_currency}")

main()
