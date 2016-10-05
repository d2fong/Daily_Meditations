# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sdf*21)k*u1#s#%&kq%s)*^nz+y8()o9hny&_fi8&@*ay1yr!qfe43$@G'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'dylanfong',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
