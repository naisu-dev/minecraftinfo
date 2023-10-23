from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'

setup(
    name='minecraftinfo',
    version="1.11",
    description="Request information Minecraft JavaEdition and BedrockEdition",
    author='naisu',
    packages=find_packages(),
    license='MIT',
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE
)
