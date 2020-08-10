from unittest import TestCase,main
import mock

from hsl_builder.Elements import FormField,FormFieldType,FormKeyboardType

class FormFieldTest(TestCase):

    def setUp(self):
        self.field = FormField("key", FormFieldType.TEXT,1,"hint", "icon")
        self.default_expected_hsl = {
            'key': 'key',
            'type': 'text',
            'keyboard_type': 'normal',
            'order': 1,
            'icon': 'icon',
            'hint': 'hint',
            'options': [],
            'search_source': '',
            'search_placeholder': '',
            'autofill': '',
            'autofill_source': ''
        }

    def test_default_hsl(self):
        """
        verify the default hsl generated
        """
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_type_picker(self):
        """
        verify that Field type picker is updated in the hsl
        """
        self.default_expected_hsl['type'] = 'picker'
        self.field.type = FormFieldType.PICKER
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_type_time(self):
        """
        verify that Field type time is updated in the hsl
        """
        self.default_expected_hsl['type'] = 'time'
        self.field.type = FormFieldType.TIME
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_type_data(self):
        """
        verify that Field type date is updated in the hsl
        """
        self.default_expected_hsl['type'] = 'date'
        self.field.type = FormFieldType.DATE
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_type_contactpicker(self):
        """
        verify that Field type contactpicker is updated in the hsl
        """
        self.default_expected_hsl['type'] = 'contactpicker'
        self.field.type = FormFieldType.CONTACT_PICKER
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_type_startdate(self):
        """
        verify that Field type startdate is updated in the hsl
        """
        self.default_expected_hsl['type'] = 'startdate'
        self.field.type = FormFieldType.START_DATE
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_type_enddate(self):
        """
        verify that Field type enddate is updated in the hsl
        """
        self.default_expected_hsl['type'] = 'enddate'
        self.field.type = FormFieldType.END_DATE
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_type_search(self):
        """
        verify that Field type search is updated in the hsl
        """
        self.default_expected_hsl['type'] = 'search'
        self.field.type = FormFieldType.SEARCH
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_type_searcheditable(self):
        """
        verify that Field type searcheditable is updated in the hsl
        """
        self.default_expected_hsl['type'] = 'searcheditable'
        self.field.type = FormFieldType.SEARCH_EDITABLE
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_type_savedaddress(self):
        """
        verify that Field type savedaddress is updated in the hsl
        """
        self.default_expected_hsl['type'] = 'savedaddress'
        self.field.type = FormFieldType.SAVED_ADDRESS
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_type_dob(self):
        """
        verify that Field type dob is updated in the hsl
        """
        self.default_expected_hsl['type'] = 'dob'
        self.field.type = FormFieldType.DOB
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_type_multidaypicker(self):
        """
        verify that Field type multidaypicker is updated in the hsl
        """
        self.default_expected_hsl['type'] = 'multidaypicker'
        self.field.type = FormFieldType.MULTI_DAY_PICKER
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_type_multiselectpicker(self):
        """
        verify that Field type multiselectpicker is updated in the hsl
        """
        self.default_expected_hsl['type'] = 'multiselectpicker'
        self.field.type = FormFieldType.MULTI_SELECT_PICKER
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_keyboard_type_number(self):
        """
        verify that keyboard type number is updated in the hsl
        """
        self.default_expected_hsl['keyboard_type'] = 'number'
        self.field.keyboard_type = FormKeyboardType.NUMBER
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_keyboard_type_email(self):
        """
        verify that keyboard type email is updated in the hsl
        """
        self.default_expected_hsl['keyboard_type'] = 'email'
        self.field.keyboard_type = FormKeyboardType.EMAIL
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_order_hsl(self):
        """
        verify that order is updated in the hsl
        """
        self.default_expected_hsl['order'] = 33
        self.field.order = 33
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_icon_hsl(self):
        """
        verify that icon is updated in the hsl
        """
        self.default_expected_hsl['icon'] = 'mock icon url'
        self.field.icon = 'mock icon url'
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_hint_hsl(self):
        """
        verify that hint is updated in the hsl
        """
        self.default_expected_hsl['hint'] = 'mock hint'
        self.field.hint = 'mock hint'
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_options_hsl(self):
        """
        verify that options is updated in the hsl
        """
        self.default_expected_hsl['options'] = ['option1', 'option 2']
        self.field.options = ['option1', 'option 2']
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_search_source_hsl(self):
        """
        verify that search_source is updated in the hsl
        """
        self.default_expected_hsl['search_source'] = 'mock search source'
        self.field.search_source = 'mock search source'
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_search_placeholder_hsl(self):
        """
        verify that search_placeholder is updated in the hsl
        """
        self.default_expected_hsl['search_placeholder'] = 'mock search placeholder'
        self.field.search_placeholder = 'mock search placeholder'
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_autofill_hsl(self):
        """
        verify that autofill is updated in the hsl
        """
        self.default_expected_hsl['autofill'] = 'mock autofill'
        self.field.autofill = 'mock autofill'
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

    def test_field_autofill_source_hsl(self):
        """
        verify that autofill_source  is updated in the hsl
        """
        self.default_expected_hsl['autofill_source'] = 'mock autofill source'
        self.field.autofill_source = 'mock autofill source'
        self.assertDictEqual(self.field.to_hsl(),self.default_expected_hsl)

