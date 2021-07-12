from unittest import TestCase, main
import mock

from hsl_builder import Text
from hsl_builder.elements import Actionable
from .mocks import MockActionable


class TextTest(TestCase):

    def setUp(self):
        self.text = Text("title")

    def test_initialization(self):
        """
        verify that text is initialized with proper options
        """
        self.assertEqual(self.text.text, "title")
        self.assertEqual(self.text.type, "TEXT")
        self.assertEqual(self.text.quick_replies, [])

    def test_hsl_default(self):
        """
        verify the default hsl generated
        """
        self.assertDictEqual(self.text.to_hsl(), {
            'text': 'title',
            'type': 'TEXT',
            'voice_text': '',
            'data': {
                'quick_replies': []
            }
        })

    @mock.patch.object(Actionable, 'to_hsl')
    def test_hsl_qr(self, mock_hsl):
        """
        verify that Quick_replies is updated in the hsl
        """
        mock_hsl.return_value = {
            "key": "value"
        }
        mock_qr = MockActionable()
        self.text.quick_replies.append(mock_qr)
        self.assertDictEqual(self.text.to_hsl(), {
            'text': 'title',
            'type': 'TEXT',
            'voice_text': '',
            'data': {
                'quick_replies': [
                    {
                        "key": "value"
                    }
                ]
            }
        })
        mock_hsl.assert_called_once()

    @mock.patch.object(Actionable, 'to_hsl')
    def test_hsl_multiple_qr(self, mock_hsl):
        """
        verify that Quick_replies is updated in the hsl
        """
        mock_hsl.return_value = {
            "key": "value"
        }
        mock_qr1 = MockActionable()
        mock_qr2 = MockActionable()
        self.text.quick_replies.append(mock_qr1)
        self.text.quick_replies.append(mock_qr2)
        self.assertDictEqual(self.text.to_hsl(), {
            'text': 'title',
            'type': 'TEXT',
            'voice_text': '',
            'data': {
                'quick_replies': [
                    {
                        "key": "value"
                    },
                    {
                        "key": "value"
                    }
                ]
            }
        })
        self.assertEqual(mock_hsl.call_count, 2)


if __name__ == '__main__':
    main()
