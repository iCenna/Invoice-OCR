from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in icenna_pacs/__init__.py
from invoice_ocr import __version__ as version

setup(
	name="invoice_ocr",
	version=version,
	description="Invoice OCR",
	author="iCenna",
	author_email="info@icenna.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
