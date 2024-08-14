from setuptools import setup, find_packages
import os

# Read the contents of your README file
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Import the version
directory = os.path.dirname(__file__)

setup(
    name='spacy-chunks',
    version="0.0.2",
    author='William J. B. Mattingly',
    description='An easy way to chunk spacy docs.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wjbmattingly/spacy-chunks',
    packages=find_packages(),
    entry_points={
      "spacy_factories": ["spacy_chunks = spacy_chunks:Chunking"],
    },
    install_requires=[
        'spacy>=3.0.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
)