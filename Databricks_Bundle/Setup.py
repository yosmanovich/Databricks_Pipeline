from setuptools import setup, find_packages

import src

setup(
  name = "databricks_app",
  version = "0.0.1",
  author = "William Yosman",
  url = "https://github.com/wiyosman/databricks_app",
  author_email = "wiyosman@microsoft.com",
  description = "A Databricks application bundle",
  packages=find_packages(where='./src'),
  package_dir={'': 'src'},
  entry_points={
    "packages": [
      "main=databricks_app.main:main"
    ]
  },
  install_requires=[
    "setuptools"
  ]
)