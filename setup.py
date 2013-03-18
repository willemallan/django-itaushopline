#!/usr/bin/env python

# from distutils.core import setup
from setuptools import setup, find_packages
import metadata

app_name = metadata.name
version = metadata.version

setup(
    name = "django-%s" % app_name,
    version = version,

    packages = find_packages(),
    include_package_data = True,
    author = "Willem Allan",
    author_email = "willemarf@gmail.com",
    description = "Django itaushopline - Package Python for django-itaushopline",
    license = "MIT License",
    keywords = "django itaushopline integracao",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms = ['any'],
    url = "https://github.com/willemallan/django-itaushopline",
    download_url = ""
)
