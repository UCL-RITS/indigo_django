from django import template
from django.forms.widgets import Select


register = template.Library()


def _add_class(field, klass):
    attrs = field.field.widget.attrs
    classes = attrs.get('class', '').split()
    if klass not in classes:
        classes.append(klass)
        attrs['class'] = ' '.join(classes)


@register.inclusion_tag('indigo/includes/forms/field.html')
def indigo_field(field):

    params = {'field': field}

    if isinstance(field.field.widget, Select):
        params['group_classes'] = 'form__group--options'
    else:
        _add_class(field, 'form__control')

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
    return {'formset': formset}
