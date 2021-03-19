import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latte-project",
    version="0.0.1-alpha",
    author="Tani Nevins-Klein",
    author_email="nottani@pm.me",
    description="An easy-to-use math typesetting language based on Python-Markdown",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NotTani/LaTTe",
    project_urls={
        "Bug Tracker": "https://github.com/NotTani/LaTTe/issues",
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "latte"},
    packages=setuptools.find_packages(where="latte"),
    python_requires=">=3.6",
)
