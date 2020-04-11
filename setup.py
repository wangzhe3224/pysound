import setuptools

with open("./Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_soundbox",
    version="0.0.2",
    author="Zhe Wang",
    author_email="wangzhetju@gmail.com",
    description="Python and sound tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wangzhe3224/pysound",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
