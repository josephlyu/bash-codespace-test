from setuptools import setup

setup(
    name='dflint',
    packages=['dflint'],
    version='0.0.1',
    entry_points='''
    [console_scripts]
    dflint=dflint.main:main
    ''',
    install_requires=[]
)