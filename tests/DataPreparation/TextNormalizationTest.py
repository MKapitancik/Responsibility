import unittest
from src.DataPreparation.TextNormalization import TextNormalization

class TextNormalizationTest(unittest.TestCase):
    def test_when_text_contains_upper_case_then_output_is_lower_case(self):
        txt = """delivered with a REQUEST command cannot be written into subsample or sample variable of another type than "use as" result. (#1756)"""
        n = TextNormalization()

        result = n.Normalize(txt)
        self.assertFalse(any(x.isupper() for x in result))
        self.assertFalse(any(x.isdigit() for x in result))

    def test_when_text_contains_special_characters_then_all_are_removed(self):
        txt = "*-+.!@#$%^&^)(*%)+_|}"
        expected_result = "test"
        n = TextNormalization()

        result = n.Normalize(txt + expected_result)

        self.assertEqual(result, expected_result)

    def test_when_text_have_camel_case_then_words_are_splitted(self):
        txt = "MetaModelSeparation and result Monitoring in EquipmentUseCase"
        expectedResult = "Meta Model Separation and result Monitoring in Equipment Use Case"

        n = TextNormalization()
        result = n.RemoveCamelCase(txt)

        self.assertEqual(result, expectedResult)
        


