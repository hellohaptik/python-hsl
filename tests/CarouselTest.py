from unittest import TestCase,main
import mock

from hsl_builder import Carousel,CarouselWidth
from hsl_builder.Elements import CarouselItem

class CarouselTest(TestCase):

    def setUp(self):
        self.carousel = Carousel("title")

    def test_initialization(self):
        """
        verify the default properties on initialization
        """
        self.assertEqual(self.carousel.text, "title")
        self.assertEqual(self.carousel.type, "CAROUSEL")
        self.assertEqual(self.carousel.items, [])
        self.assertEqual(self.carousel.aspect_ratio, 1)
        self.assertEqual(self.carousel.width, CarouselWidth.THIN)
        self.assertEqual(self.carousel.isNew, False)

    def test_hsl_default(self):
        """
        verify the default hsl generated
        """
        self.assertDictEqual(self.carousel.to_hsl(),{
            'text': 'title',
            'type': 'CAROUSEL',
            'voice_text': '',
            'data': {
                'image_aspect_ratio': 1,
                'width': 'THIN',
                'items': []
            },
            'isNew': False
        })

    @mock.patch.object(CarouselItem,'to_hsl')
    def test_hsl_carousel_item(self,mock_hsl):
        """
        verify that hsl for carouselItem is added in the Carousel
        """
        mock_hsl.return_value = {
            "key": "value"
        }
        mock_carousel_item = CarouselItem("title", "subtitle")
        self.carousel.items.append(mock_carousel_item)
        self.assertDictEqual(self.carousel.to_hsl(),{
            'text': 'title',
            'type': 'CAROUSEL',
            'voice_text': '',
            'data': {
                'image_aspect_ratio': 1,
                'width': 'THIN',
                'items': [
                    {
                        "key": "value"
                    }
                ]
            },
            'isNew': False
        })
        mock_hsl.assert_called_once()

    def test_hsl_aspect_ratio(self):
        """
        verify that aspect ratio is updated in the generated hsl
        """
        self.carousel.aspect_ratio = 23
        self.assertDictEqual(self.carousel.to_hsl(),{
            'text': 'title',
            'type': 'CAROUSEL',
            'voice_text': '',
            'data': {
                'image_aspect_ratio': 23,
                'width': 'THIN',
                'items': []
            },
            'isNew': False
        })

    def test_hsl_width_FAT(self):
        """
        verify that FAT width is updated in the generated hsl
        """
        self.carousel.width = CarouselWidth.FAT
        self.assertDictEqual(self.carousel.to_hsl(),{
            'text': 'title',
            'type': 'CAROUSEL',
            'voice_text': '',
            'data': {
                'image_aspect_ratio': 1,
                'width': 'FAT',
                'items': []
            },
            'isNew': False
        })

    def test_hsl_width_BIG(self):
        """
        verify that BIG width  is updated in the generated hsl
        """
        self.carousel.width = CarouselWidth.BIG
        self.assertDictEqual(self.carousel.to_hsl(),{
            'text': 'title',
            'type': 'CAROUSEL',
            'voice_text': '',
            'data': {
                'image_aspect_ratio': 1,
                'width': 'BIG',
                'items': []
            },
            'isNew': False
        })

    def test_hsl_width_MEDIUM(self):
        """
        verify that MEDIUM width  is updated in the generated hsl
        """
        self.carousel.width = CarouselWidth.MEDIUM
        self.assertDictEqual(self.carousel.to_hsl(),{
            'text': 'title',
            'type': 'CAROUSEL',
            'voice_text': '',
            'data': {
                'image_aspect_ratio': 1,
                'width': 'MEDIUM',
                'items': []
            },
            'isNew': False
        })

    def test_hsl_is_new(self):
        """
        verify that isNew flag is updated in the generated hsl
        """
        self.carousel.isNew = True
        self.assertDictEqual(self.carousel.to_hsl(),{
            'text': 'title',
            'type': 'CAROUSEL',
            'voice_text': '',
            'data': {
                'image_aspect_ratio': 1,
                'width': 'THIN',
                'items': []
            },
            'isNew': True
        })

if __name__ == '__main__':
    main()