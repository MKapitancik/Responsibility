import unittest
from src.DataPreparation.ConvertToTypes import ConvertToTypes

class ConvertToTypesTest(unittest.TestCase):
    def test_when_convert_then_used_types_are_valid(self):
        data = ['0.15', '15', 'test']
        types = [float, int, str]

        converter = ConvertToTypes(*types)
        
        data = converter.Convert(data)

        for column, type in zip(data, types):
            self.assertTrue(isinstance(column, type))

    def test_when_convert_with_NONE_then_column_is_skipped(self):
        data = ['0.15', '15', 'test']
        types = [float, None, str]
        expectedTypes = [float, str]

        converter = ConvertToTypes(*types)
        
        data = converter.Convert(data)

        self.assertEqual(len(data), len(expectedTypes))
        for column, type in zip(data, expectedTypes):
            self.assertTrue(isinstance(column, type))
    
    def test_when_convert_fails_then_exception_is_thrown(self):
        data = ['0.15', '15', 'test']
        types = [int, str, float]

        converter = ConvertToTypes(*types)
        
        with self.assertRaises(ValueError):
            data = converter.Convert(data)

