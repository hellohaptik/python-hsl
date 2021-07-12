from unittest import TestCase, main

from hsl_builder import NativeAction


class NativeActionTest(TestCase):

    def setUp(self):
        self.native = NativeAction("title", "METHOD")

    def test_initialization(self):
        """
        verify that native_action is initialized with the correct options
        """
        self.assertEqual(self.native.text, "title")
        self.assertEqual(self.native.type, "NATIVE_ACTION")
        self.assertEqual(self.native.method, "METHOD")

    def test_hsl_default(self):
        """
        verify the default hsl generated
        """
        self.assertDictEqual(self.native.to_hsl(), {
            'text': 'title',
            'type': 'NATIVE_ACTION',
            'voice_text': '',
            'data': {
                'method': 'METHOD'
            }
        })


if __name__ == '__main__':
    main()
