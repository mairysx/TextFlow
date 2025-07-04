from setuptools import setup, find_packages

setup(
    name='TextFlow',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'nltk',
        'scikit-learn',
        'numpy',
        'pandas',
    ],
    author='mairysx',
    description='Streamlined tools for text processing and analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mairysx/TextFlow',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)


