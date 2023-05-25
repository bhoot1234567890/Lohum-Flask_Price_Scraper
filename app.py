from flask import Flask, jsonify, request, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/price', methods=['GET'])
def price():
    source = requests.get('https://www.metal.com/Lithium-ion-Battery/202303240001').text
    soup = BeautifulSoup(source,'lxml')
    data={'Prismatic Lithium Iron-phosphate Battery Cell (ESS, 100Ah) (weekly) Price, USD/wh':soup.find(class_="strong___1JlBD priceDown___2TbRQ").text}
    return jsonify(data)
    # return(soup.find(class_="strong___1JlBD priceDown___2TbRQ").text)

if __name__ == '__main__':
    # app.run(debug=False)
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
