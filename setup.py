from setuptools import setup, find_packages

setup(
    name="ldap2json",
    version="1.0.0",
    author="KcanCurly",
    description="The ldap2json script allows you to extract the whole LDAP content of a Windows domain into a JSON file..",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/ldap2json",
    packages=find_packages(),
    install_requires=[
        "impacket",
        "ldap3",
        "sectools",
        "pycryptodome"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "ldap2json=src.ldap2json:main",  
        ],
    },
)