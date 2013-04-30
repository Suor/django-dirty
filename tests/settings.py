INSTALLED_APPS = [
    'tests',
]

# Django replaces this, but it still wants it. *shrugs*
DATABASE_ENGINE = 'django.db.backends.sqlite3',
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite.db'
    }
}

# TIME_ZONE = 'Asia/Krasnoyarsk'

SECRET_KEY = 'abc'
