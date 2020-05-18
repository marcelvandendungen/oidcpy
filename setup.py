import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oidcpy",
    version="0.0.1",
    author="Marcel van den Dungen",
    author_email="author@example.com",
    description="OpenID Connect library code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcelvandendungen/oidcpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)