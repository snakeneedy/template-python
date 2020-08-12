import setuptools


REPO_NAME = 'template-python'
REPO_DESCRIPTION = 'Python Template'
VERSION = '0.0.1'
URL = 'https://github.com/snakeneedy/template-python'
EXCLUDE_PACKAGES = (
    '.sphinx',
    'docs',
    'requirements',
    'tests',
)

with open('README.md', 'r') as fp:
    long_description = fp.read()

setuptools.setup(
    name=REPO_NAME,
    version=VERSION,
    author='Pin-Xuan She',
    author_email='snakeneedy@gmail.com',
    description=REPO_DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=URL,
    packages=setuptools.find_packages(exclude=EXCLUDE_PACKAGES),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.5',
)
