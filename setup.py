from setuptools import setup
import setuptools

setup(
    name='AutoApiTestRunner',
    version='1.0.1',
    url="https://github.com/kshamashuttl",
    author="Kshama Singh",
    author_email="kshama.singh@shuttl.com",
    description="A Command Line Interface",
    packages=setuptools.find_packages(),
    py_modules=['AutoApiTestRunner'],
    install_requires=[
        'Click', 'Requests',
    ],
    entry_points='''
        [console_scripts]
        auto=AutoApiTestRunner.auto:cli
    '''
)