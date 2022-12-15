from setuptools import find_packages, setup

setup(
    name="bfilter",
    packages=find_packages(include=["bfilter"]),
    version="0.1.1",
    description="Python simple implementation for the bloom filter.",
    author="alexandrbakhmachr@gmail.com",
    license="MIT",
    install_requires=["bitarray==2.6.0", "mmh3==3.0.0"],
    setup_requires=["pytest-runner"],
    tests_require=[
        "pytest==7.1.3",
        "mmh3==3.0.0",
        "bitarray==2.6.0",
    ],
    test_suite="tests",
    python_requires=">=3.10",
)
