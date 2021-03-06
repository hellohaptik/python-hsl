from unittest import TestCase,main
import mock

from hsl_builder import Form
from hsl_builder.elements import FormField
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

    @mock.patch.object(FormField, 'to_hsl')
    def test_hsl_multiple_fields(self, mock_hsl):
        """
        verify the default hsl generated
        """
        mockfield1 = MockFormField()
        mockfield2 = MockFormField()
        mock_hsl.return_value = {
            "text": "mock text"
        }
        self.form.fields.append(mockfield1)
        self.form.fields.append(mockfield2)
        self.assertDictEqual(self.form.to_hsl(),{
            'title': 'title',
            'type': 'FORM',
            'subtitle': 'subtitle',
            'data': {
                'fields': [
                    {
                        "text": "mock text"
                    },
                    {
                        "text": "mock text"
                    }
                ]
            }
        })
        self.assertEqual(mock_hsl.call_count,2)

if __name__ == '__main__':
    main()
