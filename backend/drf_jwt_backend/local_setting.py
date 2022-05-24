# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ijl6zpb$1rxe+yw6b02kixrgd^_=xwury+&(-=u%n_vmxfq+h$'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_database',
        'USER': 'root',
        'PASSWORD': 'example',
        'HOST': 'db',
        'OPTIONS': {
                'autocommit': True
        }
    }
}
