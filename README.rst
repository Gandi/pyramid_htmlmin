pyramid-htmlmin
===============

Binding of the htmlmin_ library for Pyramid.


 .. _htmlmin: https://pypi.python.org/pypi/htmlmin/


Usage::

    pyramid.includes =
      pyramid_htmlmin

    # uncomment lines to override default settings.
    # the settings here are default value of htmlmin.minify methods,
    # provided by htmlmin version 0.1.5
    # htmlmin.remove_comments = False
    # htmlmin.remove_empty_space = False
    # htmlmin.remove_all_empty_space = False
    # htmlmin.reduce_empty_attributes = True
    # htmlmin.reduce_boolean_attributes = False
    # htmlmin.remove_optional_attribute_quotes = True
    # htmlmin.keep_pre = False
