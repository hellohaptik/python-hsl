from unittest import TestCase,main
import mock

from hsl_builder import BaseElement

class BaseTest(TestCase):

    def setUp(self):
        self.base = BaseElement("title", "type")

    def test_initialization(self):
        """
        verify that base is initialized with correct options
        """
        self.assertEqual(self.base.text, "title")
        self.assertEqual(self.base.type, "type")

    def test_hsl_default(self):
        """
        verify the default hsl generated
        """
        self.assertDictEqual(self.base.to_hsl(),{
            'text': 'title',
            'type': 'type',
            'voice_text': ''
        })

    def test_hsl_voice(self):
        """
        verify that voice text is updated in the hsl
        """
        self.base.voice_text = "voice"
        self.assertDictEqual(self.base.to_hsl(),{
            'text': 'title',
            'type': 'type',
            'voice_text': 'voice'
        })

if __name__ == '__main__':
    main()