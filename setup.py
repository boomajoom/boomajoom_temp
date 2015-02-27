import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

install_requires = [
    'django',
    'django-debug-toolbar',
    'django_extensions',
    'psycopg2',
    'gunicorn',
    'newrelic',
]

test_requires = [
    'nose',
    'django-nose',
    'coverage',
    'django_coverage',
    'nose-cov',
    'selenium',
]

setup(name='boomajoom_temp',
      version='0.0.1',
      description='boomajoom temp home',
      author='Brandon J. Schwartz',
      author_email='brandon@boomajoom.com',
      url='http://www.boomajoom.com',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='boomajoom_temp',
      install_requires=install_requires,
      test_requires=test_requires,
      )