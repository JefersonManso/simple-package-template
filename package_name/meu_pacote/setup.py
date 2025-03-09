from setuptools import setup, find_packages

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='meu_pacote',
    version='0.1',
    packages=find_packages(),
    description='Este é um pacote Python simples com operações básicas de soma e subtração.',
    author='Jeferson Gomes',
    author_email='jrpsb@outlook.com',
    url='https://github.com/JefersonManso/simple-package-template',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
