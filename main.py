# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
# Your application specific imports
from User.models import *

# Add user
user = User(username="mstumb",
            name="marko",
            surname="Štumberger",
            role='admin',
            email="marko.stumberger@gmail.com",
            api_key='lsdjsasahdedenhusjsaha9asisah',
            password='testpass',
            settings={"json": 123},
            created_by="ADMIN")
user.save()

# Application logic
first_user = User.objects.all()[0]

print(first_user.name)
print(first_user.email)
