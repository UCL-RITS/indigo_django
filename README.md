# Indigo Django

Based on release 2 of the UCL Design Language (https://github.com/UCL-WAMS/indigo)

This is a django app providing templates, statics and example components for Indigo based sites.

## Instructions

1. Add to `INSTALLED_APPS`

```python
       INSTALLED_APPS = (
           ...
           'indigo',
       )
```

1. Extend one of the provided templates to create a page with the desired layout.
```htmldjango
       {% extends "indigo/template-combi-nav-3-col.html" %}
```

1. Refer to files in `indigo/templates/indigo/examples/` for example component markup.
