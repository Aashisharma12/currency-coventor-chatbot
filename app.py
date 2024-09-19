from flask import Flask,request

app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']

    print(source_currency)
    print(amount)
    print(target_currency)
    return "Hello"




if __name__ == "__main__":
    app.run(debug=True)
