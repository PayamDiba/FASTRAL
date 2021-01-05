import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.5.12'
PACKAGE_NAME = 'FASTRAL'
AUTHOR = 'Payam Dibaeinia'
AUTHOR_EMAIL = 'dibaein2@illinois.edu'
URL = 'https://github.com/PayamDiba/FASTRAL'

LICENSE = 'MIT License'
DESCRIPTION = 'A hybrid summary method for reconstructing species tree from gene trees.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'numpy',
      'pandas',
      'absl-py'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      include_package_data=True,
      packages=find_packages(),
      entry_points ={'console_scripts': [ 'fastral = FASTRAL.fastral_infer:main']},
      python_requires='>3.5.2',
      classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License", ),

      )
