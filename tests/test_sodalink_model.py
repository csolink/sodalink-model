import unittest

from biolinkml.utils.schemaloader import SchemaLoader

from sodalink import SODALINK_MODEL_YAML


class SodalinkModelTestCase(unittest.TestCase):
    def test_sodalink_model(self):
        """ Make sure the sodalink model is valid """
        schema = SchemaLoader(SODALINK_MODEL_YAML)
        errors = []
        try:
            schema.resolve()
        except ValueError as e:
            errors.append(str(e))
        if not errors:
            errors = schema.synopsis.errors()
        self.assertEqual([], errors, "sodalink-model.yaml - errors detected")


if __name__ == '__main__':
    unittest.main()
