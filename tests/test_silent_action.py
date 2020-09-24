from unittest import TestCase, main

from hsl_builder.elements import SilentAction


class SilentItemTest(TestCase):

    def setUp(self):
        self.silent_action = SilentAction("Action", 1, "via_name")
        self.expected_hsl = {
            'type': 'Action',
            'data': {
                'Id': 1,
                'via_name': 'via_name'
            }
        }

    def test_default_hsl(self):
        """
        verify the default hsl generated
        """
        self.assertDictEqual(self.silent_action.to_hsl(), self.expected_hsl)

    def test_hsl_action_id(self):
        """
        verify that action_id is updated in the hsl
        """
        self.silent_action.action_id = 23
        self.expected_hsl['data']['Id'] = 23
        self.assertDictEqual(self.silent_action.to_hsl(), self.expected_hsl)

    def test_hsl_via_name(self):
        """
        verify that via_name is updated in the hsl
        """
        self.silent_action.via_name = 'mock string'
        self.expected_hsl['data']['via_name'] = 'mock string'
        self.assertDictEqual(self.silent_action.to_hsl(), self.expected_hsl)

    def test_hsl_data_payload(self):
        """
        verify that data payload is included in the hsl
        """
        self.silent_action.data = {
            'key': 'value'
        }
        self.expected_hsl['data']['key'] = 'value'
        self.assertDictEqual(self.silent_action.to_hsl(), self.expected_hsl)

if __name__ == '__main__':
    main()
