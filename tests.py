import unittest
from main import app, AstraZip


class TestAstraZip(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_astra_products_number(self):
        response = self.client.get('/products_number/')
        self.assertEqual(response.status_code, 200)

    def test_astra_products_names(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_astra_product_parts(self):
        product_code = 'TRA8866'
        response = self.client.get(f'/product/{product_code}/')
        self.assertEqual(response.status_code, 200)


class TestAstraZipMethods(unittest.TestCase):

    def test_get_products_number(self):
        astra_zip = AstraZip()
        products_number = astra_zip.get_products_number()
        self.assertIsInstance(products_number, int)
        self.assertGreaterEqual(products_number, 0)

    def test_get_products_names(self):
        astra_zip = AstraZip()
        products_names = astra_zip.get_products_names()
        self.assertIsInstance(products_names, list)
        for name in products_names:
            self.assertIsInstance(name, str)

    def test_get_products_parts(self):
        astra_zip = AstraZip()
        product_code = 'TRA8866'
        parts = astra_zip.get_products_parts(product_code)
        self.assertIsInstance(parts, list)
        for part in parts:
            self.assertIsInstance(part, str)


if __name__ == '__main__':
    unittest.main()
