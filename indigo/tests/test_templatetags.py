from bs4 import BeautifulSoup
from django import forms
from django.forms.formsets import formset_factory
from django.template import Context, Template
from django.test import TestCase

from indigo.templatetags.indigo import _add_class


class CheeseForm(forms.Form):
    name = forms.CharField(max_length=8)
    hidden = forms.CharField(widget=forms.HiddenInput())


class AddClassTestCase(TestCase):

    def setUp(self):
        form = CheeseForm({'name': 'Cheddar'})
        self.field = form['name']

    def test_add_class_empty(self):
        _add_class(self.field, 'extra-strong')
        self.assertIn('class="extra-strong"', self.field.as_widget())

    def test_add_class_new(self):
        self.field.field.widget.attrs['class'] = 'yellow'
        _add_class(self.field, 'extra-strong')
        self.assertIn('class="yellow extra-strong"', self.field.as_widget())

    def test_add_class_existing(self):
        self.field.field.widget.attrs['class'] = 'extra-strong yellow'
        _add_class(self.field, 'extra-strong')
        self.assertIn('class="extra-strong yellow"', self.field.as_widget())


class FormTagsTestCase(TestCase):

    def test_field(self):
        """
        Show individual field
        """
        form = CheeseForm({'name': 'Cheddar'})
        form._errors = {'name': ['Field error']}
        context = Context({'form': form})

        tpl = Template("{% load indigo %}{% indigo_field form.name %}")
        soup = BeautifulSoup(tpl.render(context))

        # Control and label should both be present
        self.assertIsNotNone(soup.find('input', class_='form__control'))
        self.assertIsNotNone(soup.find('label', **{'for': 'id_name'}))

        # Field error should be visible
        self.assertIsNotNone(soup.find(class_='error', text='Field error'))

    def test_form_errors(self):
        form = CheeseForm({'name': 'Cheddar'})
        form._errors = {'__all__': ['Form is not valid']}
        context = Context({'form': form})

        tpl = Template("{% load indigo %}{% indigo_form_errors form %}")
        soup = BeautifulSoup(tpl.render(context))

        # Form-level errors shoudl be visible.
        self.assertIsNotNone(soup.find(class_='error', text='Form is not valid'))

    def test_field_errors(self):
        form = CheeseForm({'name': 'Chicken'})
        form._errors = {'name': ['This is not a cheese']}
        context = Context({'form': form})

        tpl = Template("{% load indigo %}{% indigo_field_errors form.name %}")
        soup = BeautifulSoup(tpl.render(context))

        self.assertIsNotNone(soup.find(
            class_='error', text='This is not a cheese'))

    def test_field_errors_no_errors(self):
        form = CheeseForm({'name': 'Brie'})
        context = Context({'form': form})

        tpl = Template("{% load indigo %}{% indigo_field_errors form.name %}")
        soup = BeautifulSoup(tpl.render(context))

        # Error list should not display at all if no errors
        self.assertIsNone(soup.find('.error-list'))

    def test_form(self):
        form = CheeseForm()
        form._errors = {'__all__': ['Form is not valid']}
        context = Context({'form': form})

        tpl = Template("{% load indigo %}{% indigo_form form %}")
        soup = BeautifulSoup(tpl.render(context))

        # Make sure the form is present
        self.assertIsNotNone(soup.find(class_='form__control'))

        # Make sure hidden fields are displayed
        self.assertIsNotNone(soup.find('input', id='id_hidden'))

        # Make sure form level errors are displayed
        self.assertIsNotNone(soup.find(class_='error', text='Form is not valid'))

    def test_formset(self):
        formset = formset_factory(CheeseForm, extra=2)()
        context = Context({'formset': formset})

        tpl = Template("{% load indigo %}{% indigo_formset formset %}")
        soup = BeautifulSoup(tpl.render(context))

        # make sure there are two forms
        self.assertEqual(len(soup.find_all(class_='form__control')), 2)

        # check for the management form
        self.assertIsNotNone(soup.find(id="id_form-TOTAL_FORMS"))
