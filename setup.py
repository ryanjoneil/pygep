from setuptools import setup, find_packages
import sys


# TODO: once issue 7 goes away, remove this code
if sys.version_info[:2] < (2, 5):
    raise Exception('PyGEP requires Python 2.5')


setup(
    name         = 'PyGEP',
    version      = '0.2.1',
    license      = 'GPL',
    description  = 'Gene Expression Programming for Python',
    author       = "Ryan J. O'Neil",
    author_email = 'ryanjoneil@gmail.com',
    url          = 'http://code.google.com/p/pygep',
    download_url = 'http://code.google.com/p/pygep/downloads/list',

    #install_requires = ['python>=2.5'], # 7: setuptools issue for win32

    package_dir = {'': 'src'},
    packages    = find_packages('src', exclude=['tests', 'tests.*']),
    zip_safe    = True,
    test_suite  = 'tests',

    keywords    = 'gene expression programming genetic evolutionary',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ]
)
