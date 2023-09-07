import unittest
from io import StringIO
from unittest.mock import patch
from vending_machine import VendingMachineParser

class TestVendingMachineParser(unittest.TestCase):
    def setUp(self):
        self.parser = VendingMachineParser()

    def test_parse_temperature(self):
        data = b'\xc0d\xdf>\xef100,+04.5\xdf\xc0'
        expected_output = "TEMPERATURE: 4.5"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            for byte in data:
                self.parser.read_byte(byte)
        self.assertIn(expected_output, mock_stdout.getvalue())

    def test_parse_product_dispense(self):
        data = b'\xc0d\xdf?0102,2,3\xc2\xc0'
        expected_output = "PRODUCT_VEND: shelf 2, channel 3"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            for byte in data:
                self.parser.read_byte(byte)
        self.assertIn(expected_output, mock_stdout.getvalue())

    def test_parse_packet_error(self):
        data = b'\xc0d\xdfm\xdb\xdc100,-11.2\xdc\xc0'  # Invalid error check
        expected_output = "PACKET_ERROR:"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            for byte in data:
                self.parser.read_byte(byte)
        self.assertIn(expected_output, mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
