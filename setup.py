from setuptools import setup, find_packages
setup(
    name="credit_default_analysis",
    version="1.1b",
    description="Credit default analysis package",
    author="Max",
    packages=find_packages(),
    install_requires=[
        # тут все зависимости
    ],
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)