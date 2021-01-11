from setuptools import setup

# Get package version
import os
version = {}
with open(os.path.join('dykstra', 'version.py')) as fp:
    exec(fp.read(), version)
__version__ = version['__version__']

setup(
    name='Dykstra',
    version=__version__,
    description="An implementation of Dykstra's projection algorithm with robust stopping criteria.",
    author='Matthew Hough',
    author_email='matt@hough.tv',
    url='https://github.com/mjhough/Dykstra/',
    download_url='https://github.com/numericalalgorithmsgroup/Dykstra/archive/v0.0.0.tar.gz',
    packages=['dykstra'],
    license='MIT',
    keywords = 'mathematics optimization projection Dykstra',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Framework :: IPython',
        'Framework :: Jupyter',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        ],
    install_requires = ['numpy >= 1.11'],
    zip_safe = True,
    )

