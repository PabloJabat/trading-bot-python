import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trading-bot-pjabat",
    version="0.0.1",
    author="Pablo Jabat",
    author_email="pablojabat@gmail.com",
    description="Trading bot library",
    long_description=long_description,
    long_description_tupe="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7"
)
