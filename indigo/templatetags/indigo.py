from django import template
from django.forms.widgets import RadioSelect, CheckboxInput, CheckboxSelectMultiple

from ..utils import get_page_numbers


register = template.Library()


def _add_class(field, klass):
    attrs = field.field.widget.attrs
    classes = attrs.get('class', '').split()
    if klass not in classes:
        classes.append(klass)
        attrs['class'] = ' '.join(classes)


@register.inclusion_tag('indigo/includes/forms/field.html')
def indigo_field(field, group_classes=''):
    group_classes = group_classes.split()
    params = {'field': field}

    if isinstance(field.field.widget, (RadioSelect, CheckboxInput, CheckboxSelectMultiple)):
        group_classes.append('options')
    else:
        _add_class(field, 'form__control')

    if isinstance(field.field.widget, (CheckboxInput)):
        params['is_check'] = True

    group_classes.append(field.name)

    params['group_classes'] = ['form__group--{}'.format(klass)
                               for klass in group_classes]

    return params


@register.inclusion_tag('indigo/includes/forms/form_errors.html')
def indigo_form_errors(form):
    return {'form': form}


@register.inclusion_tag('indigo/includes/forms/field_errors.html')
def indigo_field_errors(field):
    return {'field': field}


@register.inclusion_tag('indigo/includes/forms/form.html')
def indigo_form(form):
    return {'form': form}


@register.inclusion_tag('indigo/includes/forms/formset.html')
def indigo_formset(formset,
                   add_row_text='add another',
                   add_row_classes='btn btn--gradient'):
    has_data = any(
        hasattr(form, 'cleaned_data') and form.cleaned_data
        for form in formset.forms
    )

    return {
        'formset': formset,
        'has_data': has_data,
        'add_row_text': add_row_text,
        'add_row_classes': add_row_classes,
    }


@register.inclusion_tag('indigo/includes/pagination.html')
def indigo_pagination(page, parameter_name='page'):
    page_numbers = get_page_numbers(
        page.number, page.paginator.num_pages
    )
    return {
        'page_numbers': page_numbers,
        'page': page,
        'parameter_name': parameter_name,
    }
