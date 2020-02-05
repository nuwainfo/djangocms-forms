__version__ = '0.2.5'

default_app_config = 'djangocms_forms.apps.DjangoCMSFormsConfig'

try:
    import django

    DJANGO_VERSION = (django.VERSION[0] * 10000 + django.VERSION[1] * 100 +
                      django.VERSION[2])
except ImportError:
    warnings.warn("Unable to import django, many Iuno packages require it.")
