import setuptools

with open("README.md", "r") as handle:
    long_description = handle.read()

setuptools.setup(
    name="toolbox",
    version="0.0.1",
    author="Igor Popkov",
    author_email="popkov97.97.97@gmail.com",
    description="A set of tools for data science.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/theonewiththegun/toolbox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)
