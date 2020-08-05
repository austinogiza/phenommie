
import os

from django.core.wsgi import get_wsgi_application

# for whitenoise, remove in development
# from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phenommie.settings')

application = get_wsgi_application()
# # for whitenoise, remove in development
# application = DjangoWhiteNoise(application)
