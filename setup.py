from setuptools import setup, find_packages

setup(
    name='Analysepack',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Package consisting of Sort and Recursive functions',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/keanugee/Analysepack.git',
    author='<Keanu Gertse>',
    author_email='<keanugee@gmail.com>'
)
