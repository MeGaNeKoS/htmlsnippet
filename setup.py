from setuptools import setup, find_packages

setup(
    name='htmlsnippets',
    version='0.0.2',
    description='Renders and processes HTML snippets',
    author='めがねこ',
    author_email='meganeko@example.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
    ],
)
