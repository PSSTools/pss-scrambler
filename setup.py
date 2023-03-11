
import os, stat
from setuptools import setup
from setuptools.command.install import install

rootdir = os.path.dirname(os.path.realpath(__file__))

version="0.0.1"

if "BUILD_NUM" in os.environ.keys():
    version += "." + os.environ["BUILD_NUM"]

setup(
  name = "pss-scrambler",
  version = version,
  packages=['pss_scrambler'],
  package_dir = {'' : 'src'},
#  package_data = {'pss_scrambler': ['scripts/*', 'templates/*', 'share/*', 'share/cmake/*']},
  author = "Matthew Ballance",
  author_email = "matt.ballance@gmail.com",
  description = ("PSS Scrambler replaces user-specified identifiers with random names."),
  long_description="""
  IVPM fetches Python and non-Python packages from package and source
  repositories. Python packages are installed into a local Python 
  virtual environment. Source packages are installed in editable mode
  """,
  license = "Apache 2.0",
  keywords = ["PSS", "Portable Test and Stimulus", "RTL", "Coverage"],
  url = "https://github.com/psstools/pss-scrambler",
  entry_points={
    'console_scripts': [
      'pss-scrambler = pss_scrambler.__main__:main'
    ]
  },
  setup_requires=[
    'setuptools_scm',
  ],
  install_requires=[
      'jsonschema',
      'pyyaml',
      'pyyaml-srcinfo-loader',
      'requirements-parser',
      'toposort'
  ],
)

