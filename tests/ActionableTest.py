import mock
from unittest import TestCase, main
from hsl_builder.Elements import Actionable, URI, ActionableType

class ActionableTest(TestCase):

    def setUp(self):
        self.actionable = Actionable("title", ActionableType.TEXT_ONLY, URI.NONE)
        self.expected_hsl = {
            'actionable_text': 'title',
            'type': 'TEXT_ONLY',
            'uri': '',
            'is_default': 0,
            'location_required': False,
            'payload': {

            }
        }

    def test_default_hsl(self):
        """
        verify the default hsl generated
        """
        self.assertDictEqual(self.actionable.to_hsl(),self.expected_hsl)

    def test_actionable_type_APP_ACTION(self):
        """
        verify that actionable type app_action is updated in the hsl
        """
        self.actionable.type = ActionableType.APP_ACTION
        self.expected_hsl['type'] = 'APP_ACTION'
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)

    def test_actionable_type_MESSAGE_BAR(self):
        """
        verify that actionable type message_bar is updated in the hsl
        """
        self.actionable.type = ActionableType.MESSAGE_BAR
        self.expected_hsl['type'] = 'MESSAGE_BAR'
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)

    def test_actionable_type_FORM_SHOW(self):
        """
        verify that actionable type form_show is updated in the hsl
        """
        self.actionable.type = ActionableType.FORM_SHOW
        self.expected_hsl['type'] = 'FORM_SHOW'
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)

    def test_actionable_type_SHARE_RECEIPT(self):
        """
        verify that actionable type share_receipt is updated in the hsl
        """
        self.actionable.type = ActionableType.SHARE_RECEIPT
        self.expected_hsl['type'] = 'SHARE_RECEIPT'
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)

    def test_actionable_type_APP_FEEDBACK(self):
        """
        verify that actionable type app_feedback is updated in the hsl
        """
        self.actionable.type = ActionableType.APP_FEEDBACK
        self.expected_hsl['type'] = 'APP_FEEDBACK'
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)

    def test_actionable_type_SHARE(self):
        """
        verify that actionable type share is updated in the hsl
        """
        self.actionable.type = ActionableType.SHARE
        self.expected_hsl['type'] = 'SHARE'
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)

    def test_hsl_URI_type_SEND_LOCATION(self):
        """
        verify that URI type send_location is updated in the hsl
        """
        self.actionable.uri = URI.SEND_LOCATION
        self.expected_hsl['uri'] = 'SEND_LOCATION'
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)

    def test_hsl_URI_type_CAROUSEL_DETAIL(self):
        """
        verify that URI type carousel_detail is updated in the hsl
        """
        self.actionable.uri = URI.CAROUSEL_DETAIL
        self.expected_hsl['uri'] = 'CAROUSEL_DETAIL'
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)

    def test_hsl_URI_type_GALLERY_PICKER(self):
        """
        verify that URI type gallery_picker is updated in the hsl
        """
        self.actionable.uri = URI.GALLERY_PICKER
        self.expected_hsl['uri'] = 'GALLERY_PICKER'
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)

    def test_hsl_URI_type_IMAGE_UPLOAD(self):
        """
        verify that URI type image_upload is updated in the hsl
        """
        self.actionable.uri = URI.IMAGE_UPLOAD
        self.expected_hsl['uri'] = 'IMAGE_UPLOAD'
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)

    def test_hsl_URI_type_DOCUMENT_PICKER(self):
        """
        verify that URI type document_picker is updated in the hsl
        """
        self.actionable.uri = URI.DOCUMENT_PICKER
        self.expected_hsl['uri'] = 'DOCUMENT_PICKER'
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)

    def test_hsl_URI_type_LAUNCH_CHANNEL(self):
        """
        verify that URI type launch_channel is updated in the hsl
        """
        self.actionable.uri = URI.LAUNCH_CHANNEL
        self.expected_hsl['uri'] = 'LAUNCH_CHANNEL'
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)

    def test_hsl_URI_type_LINK(self):
        """
        verify that URI type link is updated in the hsl
        """
        self.actionable.uri = URI.LINK
        self.expected_hsl['uri'] = 'LINK'
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)

    def test_hsl_URI_type_SELF_SERVE_WEB(self):
        """
        verify that URI type self_serve_web is updated in the hsl
        """
        self.actionable.uri = URI.SELF_SERVE_WEB
        self.expected_hsl['uri'] = 'SELF_SERVE_WEB'
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)

    def test_hsl_location_required(self):
        """
        verify that location_required is updated in the hsl
        """
        self.actionable.location_required = True
        self.expected_hsl['location_required'] = True
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)

    def test_hsl_is_default(self):
        """
        verify that is_default is updated in the hsl
        """
        self.actionable.is_default = True
        self.expected_hsl['is_default'] = 1
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)

    def test_hsl_payload(self):
        """
        verify that payload is added in the hsl
        """
        self.actionable.payload = {
            'key': 'value'
        }
        self.expected_hsl['payload'] = {
            'key': 'value'
        }
        self.assertDictEqual(self.actionable.to_hsl(), self.expected_hsl)


if __name__ == '__main__':
    main()
