# coding: utf-8
from crogull_sync.http import HttpResponse
from crogull_sync.settings import settings
from crogull_sync.signals import template_rendered, before_render_template

from jinja2 import PackageLoader, ChoiceLoader, Environment, select_autoescape


def render_template(template_name, request, **context):

    loader = ChoiceLoader([PackageLoader(app) for app in settings.INSTALLED_APPS])
    jinja_env = Environment(loader=loader, autoescape=select_autoescape(['html',]))
    jinja_env.globals.update(
        request=request,
    )
    template = jinja_env.get_template(template_name)

    before_render_template.send(request, template=template, context=context)
    content = template.render(context)
    template_rendered.send(request, template=template, context=context)

    return HttpResponse(content, content_type='text/html')
