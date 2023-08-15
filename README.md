# Astra Store XML Stock Data Analysis Flask App

This Flask application is designed to analyze XML stock data from Astra Store. It provides a simple API to retrieve information about products and their parts from the Astra Store export XML file.

## Features

- Retrieve the total number of products available in the Astra Store XML data.
- Get a list of product names present in the XML data.
- Retrieve the parts of a specific product using its product code.

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment (recommended) and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask app:
   ```
   python app.py
   ```
2. Open a web browser and go to `http://localhost:5000/` to see the API's name.
3. To retrieve the total number of products, visit `http://localhost:5000/products_number/`.
4. To get a list of product names, visit `http://localhost:5000/products/`.
5. To retrieve the parts of a specific product, replace `<product_code>` with the desired product code in the following URL: `http://localhost:5000/product/<product_code>`.

## Example

Let's say you want to get the parts of a product with the code "12345". You would visit `http://localhost:5000/product/12345` to see the list of parts.

## Notes

- The Astra Store export XML file is automatically downloaded and extracted when the Flask app is run.
- The app uses the `xml.etree.ElementTree` library to parse the XML data.
