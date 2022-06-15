from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in project_task/__init__.py
from project_task import __version__ as version

setup(
	name="project_task",
	version=version,
	description="Sync task template begin and duration with project template",
	author="GreyCube Technologies",
	author_email="admin@greycube.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
