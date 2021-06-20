from unittest import TestCase
from app import app

class Forex_Test(TestCase):
    def test_page_working(self):
        """Testing to make sure the page loads correctly"""
        with app.test_client() as client:
            response = client.get('/')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn("<h1>Foreign Currency Exchange Rate Calculator</h1>", html)
    
    def test_calculations(self):
        with app.test_client() as client:
            response = client.get('/handle-conversion?currency-from=USD&currency-to=USD&amount=50')
            html = response.get_data(as_text=True)

            self.assertIn("<h2>The result is US$50.0</h2>", html)
            self.assertEqual(response.status_code, 200)

    def test_invalid_amount(self):   
        with app.test_client() as client:     
            response = client.get('/handle-conversion?currency-from=USD&currency-to=USD&amount=0')
            html = response.get_data(as_text=True)

            #self.assertIn('<p id="message">This is not a valid amount!</p>', html)
            self.assertEqual(response.status_code, 302)

    def test_invalid_currency(self):   
        with app.test_client() as client:     
            response = client.get('/handle-conversion?currency-from=USD&currency-to=ZZZ&amount=50')
            html = response.get_data(as_text=True)

            #self.assertIn('<p id="message">This is not a valid amount!</p>', html)
            self.assertEqual(response.status_code, 302)

            