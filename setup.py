from setuptools import setup, find_packages

setup(
    name="credit_default_analysis1",
    version="1.1b3",
    description="Credit default analysis package",
    author="Ivan_Kuznetsov",
    packages=find_packages(),
    install_requires=[
        # все зависимости сюда
    ],
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)