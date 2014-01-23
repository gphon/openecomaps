# Django settings for openecomaps project.
from openecomaps import LOCAL_MASCHINE

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname( os.path.dirname(__file__) )


# Make this unique, and don't share it with anybody.
SECRET_KEY = '496db235=@j-w*ple75+6i538i@%lj5(z+f=+_n&1djsc99nil'


DEBUG = True
TEMPLATE_DEBUG = DEBUG


TEMPLATE_DIRS = (
    os.path.join( BASE_DIR, 'templates' ),
)


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []


###############################################################################
###   Application definition
###############################################################################

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.oem',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


AUTH_USER_MODEL = 'auth.OEMUser'

ROOT_URLCONF = 'openecomaps.urls'

WSGI_APPLICATION = 'openecomaps.wsgi.application'


###############################################################################
###   Database
###############################################################################

if LOCAL_MASCHINE:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.sqlite3',
            'NAME':     os.path.join( BASE_DIR, 'sqlite.db' ),
            'USER':     '',
            'PASSWORD': '',
            'HOST':     '',
            'PORT':     '',
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql_psycopg2',
            'NAME':     'openecomaps',
            'USER':     'openecomaps',
            'PASSWORD': 'oem',
            'HOST':     '127.0.0.1',
            'PORT':     '',
        },
    }
#endif


###############################################################################
###   Internationalization
###############################################################################

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


###############################################################################
###   Static files (CSS, JavaScript, Images)
###############################################################################

# URL prefix for static files.
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join( BASE_DIR, 'static_files' ),
)








class InvalidVarException(object):
    def __mod__(self, missing):
        try:
            missing_str=unicode(missing)
        except:
            missing_str='Failed to create string representation'
        raise Exception('Unknown template variable %r %s' % (missing, missing_str))
    def __contains__(self, search):
        if search=='%s':
            return True
        return False


TEMPLATE_STRING_IF_INVALID = InvalidVarException()


ADMINS = (
    ('Stefan Bunde', 'openecomaps@gmail.com'),
)

MANAGERS = ADMINS


SITE_ID = 1


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join( BASE_DIR, 'static_user_content/' )

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/user_content/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''



# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)





# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}