from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({ 'name': '' })
        # test form is not valid
        self.assertFalse(form.is_valid())
        # error occuring on nem field
        self.assertIn('name', form.errors.keys())
        # specific error message is what we expect
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({ 'name': 'Test Todo Item' })
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])