import mock
from unittest import TestCase, main

from hsl_builder.elements import CarouselItem, Actionable
from .mocks import MockActionable


class CarouselItemTest(TestCase):

    def setUp(self):
        self.carousel_item = CarouselItem("title", "subtitle")
        self.expected_hsl = {
            'title': 'title',
            'sub_title': 'subtitle',
            'description': '',
            'actionables': [],
            'meta': '',
            'thumbnail': {
                'image': ''
            }
        }

    def test_hsl_default(self):
        """
        verify the default hsl generated
        """
        self.assertDictEqual(self.carousel_item.to_hsl(), self.expected_hsl)

    def test_hsl_description(self):
        """
        verify descrption is updated in the hsl
        """
        self.expected_hsl['description'] = 'mock string'
        self.carousel_item.description = 'mock string'
        self.assertDictEqual(self.carousel_item.to_hsl(), self.expected_hsl)

    def test_hsl_meta(self):
        """
        verify meta is updated in the hsl
        """
        self.expected_hsl['meta'] = 'mock string'
        self.carousel_item.meta = 'mock string'
        self.assertDictEqual(self.carousel_item.to_hsl(), self.expected_hsl)

    def test_hsl_thumbnail(self):
        """
        verify thumbnail is updated in the hsl
        """
        self.expected_hsl['thumbnail']['image'] = 'mock string'
        self.carousel_item.thumbnail = 'mock string'
        self.assertDictEqual(self.carousel_item.to_hsl(), self.expected_hsl)

    @mock.patch.object(Actionable, 'to_hsl')
    def test_hsl_actionables(self, mock_hsl):
        """
        verify actionable objects are added in the hsl
        """
        self.carousel_item.actionables.append(MockActionable())
        mock_hsl.return_value = {
            'key': 'value'
        }
        self.expected_hsl['actionables'] = [
            {
                'key': 'value'
            }
        ]
        self.assertDictEqual(self.carousel_item.to_hsl(), self.expected_hsl)
        mock_hsl.assert_called_once()


if __name__ == '__main__':
    main()
