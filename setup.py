__author__ = "Sivadon Chaisiri"
__copyright__ = "Copyright (c) 2020 Sivadon Chaisiri"
__license__ = "MIT License"


from setuptools import setup, find_packages

setup(
    name='pykaru',
    packages=['pykaru'],
    author='Sivadon Chaisiri',
    author_email='sivadon@ieee.org',    
    version=0.01,
    license='MIT',
    description = 'Simple AWS CMDB',
    url = 'https://github.com/boomary/pykaru',   
    download_url = 'https://github.com/boomary/pyhanga/archive/v_9002.tar.gz', 
    keywords = ['AWS', 'CloudFormation', 'CLI'],    
    install_requires=[
        'click',
        'boto3',
        'tablib',
	    'openpyxl',
    ],
    include_package_data=True,   
    entry_points={
        'console_scripts': ['pykaru=pykaru.commands:cli']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
