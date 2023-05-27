import pathlib

import setuptools

HERE = pathlib.Path(__file__).parent.resolve()
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf-8")
setuptools.setup(
    name="salary_analyser",
    version="1.0.0",
    description="Analyse the expected salary based on census data",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="luke bennett",
    packages=setuptools.find_namespace_packages(include=["salary_analyser.*"]),
    package_data={"": ["*.json"]},
    python_requires=">=3.9.0,<3.11.0",
)
