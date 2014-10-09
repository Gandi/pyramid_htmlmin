"""
Binding betwen Pyramid and htmlmin

"""

import logging

from htmlmin import minify
from pyramid.tweens import EXCVIEW
from pyramid.request import Response

__version__ = '0.1'

log = logging.getLogger(__name__)


def htmlmin_tween_factory(handler, registry):
    def tween_view(request):
        response = handler(request)
        try:
            if response.content_type.startswith('text/html'):
                response.text = minify(response.text)
        except Exception:
            log.exception('Unexpected exception while minifying content')
        return response

    return tween_view


def includeme(config):
    """
    Add pyramid_htmlmin n your pyramid include list.
    """
    config.add_tween('pyramid_htmlmin.htmlmin_tween_factory', under=EXCVIEW)
