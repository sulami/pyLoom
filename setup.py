from setuptools import setup

import pyloom

def readme():
    try:
        with open('readme.rst') as f:
            return f.read()
    except: # FileNotFound?
        return ''

setup(name='pyloom',
      version=pyloom.VERSION,
      description='Pen&Paper storyline planning tool',
      long_description=readme(),
      url='https://github.com/sulami/pyloom',
      author='Robin Schroer',
      author_email='sulami@peerwire.org',
      license='MIT',
      packages=['pyloom'],
      test_suite = 'pyloom.tests',
      zip_safe=False,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Environment :: Console',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Software Development',
          'Topic :: Software Development :: Testing',
      ],
      )


