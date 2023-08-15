from flask import Flask, render_template
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
from xml.etree import ElementTree as et


def download_and_unzip(url, extract_to='.'):
    http_response = urlopen(url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=extract_to)


class AstraZip:
    def __init__(self):
        file_url = 'https://www.retailys.cz/wp-content/uploads/astra_export_xml.zip'
        file_path = 'export_full.xml'
        download_and_unzip(file_url)
        self.data = et.parse(file_path).getroot()
        self.products = self.data.find('items').findall('item')

    def get_products_number(self):
        return len(self.products)

    def get_products_names(self):
        return [p.attrib['name'] for p in self.products]

    def get_products_parts(self, product_code):
        for p in self.products:
            if p.attrib['code'] == product_code:
                parts = p.find('parts')
                if parts is not None:
                    parts = parts.findall('part')
                    parts_names = [pt.attrib['name'] for pt in parts]
                    for pt in parts:
                        for it in pt.findall('item'):
                            parts_names.append(it.attrib['name'])
                    return parts_names
        return []


astra_zip = AstraZip()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products_number/')
def astra_products_number():
    products_number = astra_zip.get_products_number()
    return render_template('products_number.html', products_number=str(products_number))


@app.route('/products/')
def astra_products_names():
    products_names = astra_zip.get_products_names()
    return render_template('products.html', products_names=products_names)


@app.route('/product/<product_code>/')
def astra_product_parts(product_code):
    product_parts = astra_zip.get_products_parts(product_code)
    return render_template('product_parts.html', product_parts=product_parts)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='2222')
