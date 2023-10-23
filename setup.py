from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'

setup(
    name='minecraftinfo',
    version="1.12",
    description="minecraftinfo is a library that allows you to get information about minecraft servers, skins, etc. in python",
    author='naisu',
    packages=find_packages(),
    license='MIT',
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE
)
