from unittest import TestCase, main
import mock

from hsl_builder import Button
from hsl_builder.elements import Actionable
from .mocks import MockActionable


class ButtonTest(TestCase):

    def setUp(self):
        self.button = Button("title")
        self.expected_hsl = {
            'text': 'title',
            'type': 'BUTTON',
            'voice_text': '',
            'data': {
                'items': []
            }
        }

    def test_initialization(self):
        """
        verify that button is initialized with the correct options
        """
        self.assertEqual(self.button.text, "title")
        self.assertEqual(self.button.type, "BUTTON")
        self.assertEqual(self.button.actionables, [])

    def test_hsl_default(self):
        """
        verify the default hsl generated
        """
        self.assertDictEqual(self.button.to_hsl(), self.expected_hsl)

    @mock.patch.object(Actionable, 'to_hsl')
    def test_hsl_actionable(self, mock_hsl):
        """
        verify that button generates correct hsl for added actionables
        """
        mock_hsl.return_value = {
            "key": "value"
        }
        mock_actionable = MockActionable()
        self.button.actionables.append(mock_actionable)
        self.expected_hsl['data']['items'] = [
            {
                "key": "value"
            }
        ]
        self.assertDictEqual(self.button.to_hsl(), self.expected_hsl)
        mock_hsl.assert_called_once()


if __name__ == '__main__':
    main()
