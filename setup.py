import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='hsl_builder',
      version='0.1',
      description='HSL Builder for creating hsl elements',
      license='MIT',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['hsl_builder'],
      zip_safe=False,
      url="https://github.com/hellohaptik/python-hsl")
