
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
  packages=['pss_scrambler', 'pss_scrambler.cmds'],
  package_dir = {'' : 'src'},
#  package_data = {'pss_scrambler': ['scripts/*', 'templates/*', 'share/*', 'share/cmake/*']},
  author = "Matthew Ballance",
  author_email = "matt.ballance@gmail.com",
  description = ("PSS Scrambler replaces user-specified identifiers with random names."),
  long_description="""
  PSS Scrambler obfuscates PSS source files by replacing user-specified
  identifiers with randomly-selected ones.
  """,
  license = "Apache 2.0",
  keywords = ["PSS", "Portable Test and Stimulus", "obfuscator"],
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
  ],
)

