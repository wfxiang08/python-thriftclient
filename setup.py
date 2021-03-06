from distutils.core import setup

setup(
    name = 'ThriftClient',
    author = 'Curt Micol',
    author_email = 'asenchi@asenchi.com',
    description = 'Python ThriftClient ported from http://github.com/fauna/thrift_client',
    long_description = open('README').read(),
    version = __import__('thriftclient').__version__,
    license = 'Apache License v2.0',
    packages = ['thriftclient'],
    classifiers = [
        'Development Status :: 0.9 alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)
