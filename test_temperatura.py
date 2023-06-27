import unittest

def celsius_a_Fahrenheit(celcius):
        return (celcius * 9/5) +32

class TestTemperatura(unittest.TestCase):

    def test_celsius_a_fahrenheit(self):

        resultado = celsius_a_Fahrenheit(0)
        self.assertEqual(resultado, 32)

        resultado = celsius_a_Fahrenheit(100)
        self.assertEqual(resultado ,222) #ESTA VA A FALLAR
    
    

if __name__=='__main__':
    unittest.main() 
        
