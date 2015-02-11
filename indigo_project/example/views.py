import glob
import os

from django.shortcuts import render
from django.template.loader import render_to_string


def home(request):
    template_names = [
        os.path.basename(f) for f in glob.glob('templates/*template*.html')
    ]

    return render(request, 'home.html', {
        'template_names': template_names,
    })


def template(request, template_name):
    return render(request, 'demo.html', {
        'template_name': 'indigo/{}'.format(template_name),
    })
