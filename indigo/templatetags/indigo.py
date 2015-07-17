from django import template
from django.forms.widgets import RadioSelect, CheckboxInput, CheckboxSelectMultiple


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
def indigo_formset(formset):
    has_data = any(
        hasattr(form, 'cleaned_data') and form.cleaned_data
        for form in formset.forms
    )

    return {
        'formset': formset,
        'has_data': has_data,
    }


@register.inclusion_tag('indigo/includes/pagination.html')
def indigo_pagination(page, parameter_name='page'):
    return {
        'page': page,
        'parameter_name': parameter_name,
    }
