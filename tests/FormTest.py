from unittest import TestCase,main
import mock

from hsl_builder import Form
from hsl_builder.Elements import FormField
from .mocks import MockFormField

class FormTest(TestCase):

    def setUp(self):
        self.form = Form("title", "subtitle")

    def test_initialization(self):
        """
        verify that form is initialized with the correct options
        """
        self.assertEqual(self.form.title, "title")
        self.assertEqual(self.form.type, "FORM")
        self.assertEqual(self.form.subtitle, "subtitle")
        self.assertEqual(self.form.fields, [])

    @mock.patch.object(FormField, 'to_hsl')
    def test_hsl(self, mock_hsl):
        """
        verify the default hsl generated
        """
        mockfield = MockFormField()
        mock_hsl.return_value = {
            "text": "mock text"
        }
        self.form.fields.append(mockfield)
        self.assertDictEqual(self.form.to_hsl(),{
            'title': 'title',
            'type': 'FORM',
            'subtitle': 'subtitle',
            'data': {
                'fields': [
                    {
                        "text": "mock text"
                    }
                ]
            }
        })
        mock_hsl.assert_called_once()

if __name__ == '__main__':
    main()
