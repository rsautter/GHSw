from setuptools import setup

setup(
    name='GHSw',
    version='1.0',
    url='https://github.com/rsautter/GHSw',
    author='Rubens Andreas Sautter',
    author_email='rubens.sautter@gmail.com',
    keywords='histogram GHS statistic',
    description=u'Geometric Histogram of Separation',
    packages=['ghsw'],
	package_dir={'': 'ghsw'},
	packages=find_packages(where='ghsw')
)