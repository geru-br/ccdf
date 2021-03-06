import os
import sys


from setuptools import setup, find_packages

long_description = '''
Segment is the simplest way to integrate analytics into your application.
One API allows you to turn on any other analytics service. No more learning
new APIs, repeated code, and wasted development time.

This is the official python client that wraps the Segment REST API (https://segment.com).

Documentation and more details at https://github.com/segmentio/analytics-python
'''

install_requires = [
    "requests>=2.7,<3.0",
    "six>=1.5",
    "python-dateutil>2.1"
]

test_require = [
    'pytest',
    'pytest-cov',
    'pyramid',
    'celery',
    'redis',
]


setup(
    name='geru.ccdf',
    version='0.0.4',
    url='https://github.com/segmentio/analytics-python',
    author='Segment',
    author_email='friends@segment.com',
    maintainer='Segment',
    maintainer_email='friends@segment.com',
    test_suite='geru.ccdf.test.all',
    packages=find_packages(),
    license='MIT License',
    install_requires=install_requires,
    description='The hassle-free way to integrate analytics into any python application.',
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    extras_require={'testing': test_require},
)
