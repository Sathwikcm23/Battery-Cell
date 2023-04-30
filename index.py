from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/price', methods=['GET'])
def get_price():
    url = 'https://www.metal.com/Lithium-ion-Battery/202303240001'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())
    price_tag = soup.select_one('span.strong___1JlBD.priceDown___2TbRQ')

    print(price_tag)
    print(type(price_tag))

    if price_tag:
        price = price_tag.text.strip()
        return jsonify({'price': price})
    else:
        return jsonify({'error': 'Failed to retrieve price'}), 500

if __name__ == '__main__':
    app.run(debug=True)
