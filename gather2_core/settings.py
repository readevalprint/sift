from configurations import Configuration, values

import os


class Base(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)

    SECRET_KEY = 'n)&_bvxfe$g)gfa4b-uy&aqt$vx!w7jw%fyi9mc8#onh2^$m=='

    DEBUG = True

    ALLOWED_HOSTS = values.ListValue([])

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'django_extensions',
        'gather2_core',
    ]

    MIDDLEWARE_CLASSES = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'gather2_core.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'gather2_core.wsgi.application'

    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',  # this is default
    )

    ANONYMOUS_USER_ID = -1

    REST_FRAMEWORK = {
        'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.TemplateHTMLRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework.parsers.JSONParser',
        )

    }

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    STATIC_URL = '/static/'

    STATICFILES_DIRS = [
    ]


class Dev(Base):
    DEBUG = True
    DATABASES = values.DatabaseURLValue("postgres://postgres@localhost/gather2_dev")


class Test(Dev):
    DATABASES = values.DatabaseURLValue("postgres://postgres@localhost/gather2_test")


class Travis(Test):
    DATABASES = values.DatabaseURLValue("postgres://postgres@localhost/travis_ci_test")


class Docker(Base):
    DEBUG = False
    STATIC_ROOT = '/var/www/data/'
    DATABASES = values.DatabaseURLValue()


class Staging(Docker):
    pass


class Production(Docker):
    pass