import unittest
from city_functions import city_functions

class CityCountryTestCase(unittest.TestCase):
    
    def test_city_country(self):
        city_country = city_functions('beijing', 'china')
        self.assertEqual(city_country, 'Beijing, China')
        
if __name__ == '__main__':
    unittest.main()
    
