from setuptools import setup

setup(
    name='tcwallet',
    version='0.1',
    py_modules=['tcwallet'],
    include_package_data=True,
    install_requires=[
        'click',
        'emoji',
        'numpy',
    ],
    entry_points='''
        [console_scripts]
        tcwallet=tcwallet:cli
    ''',
)
