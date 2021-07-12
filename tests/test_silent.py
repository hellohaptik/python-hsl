from unittest import TestCase, main
import mock

from hsl_builder import Silent
from hsl_builder.elements import SilentAction
from .mocks import MockSilentAction


class SilentTest(TestCase):

    def setUp(self):
        self.silent = Silent("title")

    def test_initialization(self):
        """
        verify that silent hsl is initialized with correct options
        """
        self.assertEqual(self.silent.text, "title")
        self.assertEqual(self.silent.type, "SILENT")
        self.assertEqual(self.silent.actions, [])

    def test_hsl_default(self):
        """
        verify the default hsl generated
        """
        self.assertDictEqual(self.silent.to_hsl(), {
            'text': 'title',
            'type': 'SILENT',
            'voice_text': '',
            'data': {
                'silent_actions': []
            }
        })

    @mock.patch.object(SilentAction, 'to_hsl')
    def test_hsl_with_silent_action(self, mock_hsl):
        """
        verify that silent actions are added in the hsl
        """
        mock_hsl.return_value = {
            'key': 'value'
        }
        self.silent.actions.append(MockSilentAction())
        self.assertDictEqual(self.silent.to_hsl(), {
            'text': 'title',
            'type': 'SILENT',
            'voice_text': '',
            'data': {
                'silent_actions': [
                    {
                        'key': 'value'
                    }
                ]
            }
        })
        mock_hsl.assert_called_once()


if __name__ == '__main__':
    main()
