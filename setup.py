from setuptools import setup, find_packages


setup(
    name='django_airbrake',
    version='0.0.3',
    description='A Django middleware for submitting exceptions to Airbrake.io.',
    long_description='',
    keywords='django, airbrake',
    author='Hubert Piotrowski',
    author_email='hubert.piotrowski@hotmail.com',
    url='https://github.com/darkman66/django-airbrake',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires = ['decorator'],
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ]
)
