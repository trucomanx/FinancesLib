#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name   ='FinancesLib',
    version='0.0.1',
    author='Fernando Pujaico Rivera',
    author_email='fernando.pujaico.rivera@gmail.com',
    packages=[  'FinancesLib',
                'FinancesLib.Stocks'],
    #scripts=['bin/script1','bin/script2'],
    url='https://github.com/trucomanx/FinancesLib',
    license='GPLv3',
    description='Path Filling Points',
    #long_description=open('README.txt').read(),
    install_requires=[
       "numpy",
       "scikit-learn",
       "yfinance"
    ],
)

#! python setup.py sdist bdist_wheel
# Upload to PyPi
# or 
#! pip3 install dist/FinancesLib-0.1.tar.gz 
