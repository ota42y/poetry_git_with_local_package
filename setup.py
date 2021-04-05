import os
from setuptools import setup

PKG_DIR = os.path.dirname(os.path.abspath(__file__))
setup(
    name="poetry_git_with_local_package",
    version="0.0.1",
    install_requires=[
        f"subdir_package @ file://{PKG_DIR}/subdir_package"
    ]
)
