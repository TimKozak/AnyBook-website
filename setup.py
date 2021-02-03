import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="any_book",
    version="0.0.1",
    author="Tymofii Kozak",
    author_email="tymofii.kozak@ucu.edu.ua",
    description="^ANY.BOOK Robert Louis Stevenson",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" ",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_data={
        'any_book_project':'static'
    }
)