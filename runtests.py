""" run tests for pagetree

$ virtualenv ve
$ ./ve/bin/pip install Django==1.8.1
$ ./ve/bin/pip install -r test_reqs.txt
$ ./ve/bin/python runtests.py
"""
import django
from django.conf import settings
from django.core.management import call_command


def main():
    # Dynamically configure the Django settings with the minimum necessary to
    # get Django running tests
    settings.configure(
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'pagetree',
            'django_markwhat',
            'django_jenkins',
            'quizblock',
            'quizblock_random'
        ),
        TEST_RUNNER='django.test.runner.DiscoverRunner',
        MIDDLEWARE_CLASSES=[],
        PROJECT_APPS = [
            'quizblock_random',
        ],
        COVERAGE_EXCLUDES_FOLDERS = ['migrations', 'south_migrations'],
        ROOT_URLCONF = [],
        PAGEBLOCKS = ['pagetree.TestBlock', 'quizblock.Quiz'],
        SOUTH_TESTS_MIGRATE=False,

        # Django replaces this, but it still wants it. *shrugs*
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
                'HOST': '',
                'PORT': '',
                'USER': '',
                'PASSWORD': '',
                }
            }
    )

    django.setup()

    # Fire off the tests
    call_command('jenkins', '--enable-coverage')

if __name__ == '__main__':
    main()
