from unittest import TestCase,main
import mock

from hsl_builder import System,SystemEvents

class SystemCompleteTest(TestCase):

    def setUp(self):
        self.system = System("complete", SystemEvents.COMPLETE)

    def test_initialization(self):
        """
        verify that System Message  is initialized with the correct options
        """
        self.assertEqual(self.system.text, "complete")
        self.assertEqual(self.system.event, SystemEvents.COMPLETE)
        self.assertEqual(self.system.type, "SYSTEM")

    def test_hsl_default(self):
        """
        verify the default hsl generated
        """
        self.assertDictEqual(self.system.to_hsl(),{
            'text': 'complete',
            'type': 'SYSTEM',
            'voice_text': '',
            'data': {
                'event_name': 'chat_complete',
                'payload': {}
            }
        })

    def test_hsl_payload(self):
        """
        verify that payload is added in the generated hsl
        """
        self.system.payload = {"key": "value"}
        self.assertDictEqual(self.system.to_hsl(),{
            'text': 'complete',
            'type': 'SYSTEM',
            'voice_text': '',
            'data': {
                'event_name': 'chat_complete',
                'payload': {"key": "value"}
            }
        })

class SystemWaitingTest(TestCase):

    def setUp(self):
        self.system = System("waiting", SystemEvents.PINNED)

    def test_initialization(self):
        """
        verify that System Message  is initialized with the correct options
        """
        self.assertEqual(self.system.text, "waiting")
        self.assertEqual(self.system.event, SystemEvents.PINNED)
        self.assertEqual(self.system.type, "SYSTEM")

    def test_hsl_default(self):
        """
        verify the default hsl generated
        """
        self.assertDictEqual(self.system.to_hsl(),{
            'text': 'waiting',
            'type': 'SYSTEM',
            'voice_text': '',
            'data': {
                'event_name': 'chat_pinned',
                'payload': {}
            }
        })

    def test_hsl_payload(self):
        """
        verify that payload is added in the generated hsl
        """
        self.system.payload = {"key": "value"}
        self.assertDictEqual(self.system.to_hsl(),{
            'text': 'waiting',
            'type': 'SYSTEM',
            'voice_text': '',
            'data': {
                'event_name': 'chat_pinned',
                'payload': {"key": "value"}
            }
        })

if __name__ == '__main__':
    main()
