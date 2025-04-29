from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='universal-json-converter',
    version='1.0.0',
    packages=find_packages(),
    py_modules=['main'],
    install_requires=[
        'pandas',
        'pyyaml',
        'openpyxl',
        'pyarrow'
    ],
    entry_points={
        'console_scripts': [
            'ujconvert=main:main',
        ],
    },
    author='Siddharth Lal',
    author_email='siddharthlal99@gmail.com',
    description='A CLI tool to convert files to/from JSON efficiently with large file support',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Siddharth-lal-13/universal-json-converter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
