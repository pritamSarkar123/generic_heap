from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = "0.0.2"
DESCRIPTION = """Heap data structure similar to priority queue in Java and C++."""


# Setting up
setup(
	name="generic_heap",
	version=VERSION,
	author="Pritam Sarkar (Vanu)",
	author_email="pritamsarkar84208220@gmail.com",
	description=DESCRIPTION,
	long_description=(
		f"{open('README.md', 'r').read()}\n\n{open('CHANGELOG', 'r').read()}"
	),
	packages=find_packages(),
	url="https://github.com/pritamSarkar123/generic_heap.git",
	license="MIT",
	install_requires=["deprecation"],
	keywords=["python", "Heap"],
	classifiers=[
		"Development Status :: 1 - Production/Stable",
		"Intended Audience :: Developers/Students",
		"Programming Language :: Python :: 3",
		"Operating System :: Unix",
		"Operating System :: MacOS :: MacOS X",
		"Operating System :: Microsoft :: Windows",
		"License :: OSI Approved :: MIT License",
	],
	package_data={"generic_heap": ["py.typed"]},
)