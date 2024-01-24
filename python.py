Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import unittest
from city_functions import city_functions

class CityCountryTestCase(unittest.TestCase):
    
    def test_city_country(self):
        city_country = city_functions('beijing', 'china')
        self.assertEqual(city_country, 'Beijing,China')
        
if __name__ == '__main__':
    unittest.main()
    
SyntaxError: multiple statements found while compiling a single statement
>>> import test_city_country
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import test_city_country
ModuleNotFoundError: No module named 'test_city_country'
>>> import city_country
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import city_country
ModuleNotFoundError: No module named 'city_country'
>>> 