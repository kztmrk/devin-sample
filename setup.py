from setuptools import setup, find_packages

setup(
    name="streamlit_app",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "streamlit>=1.24.0",
        "pandas>=1.5.3",
        "numpy>=1.24.3",
        "matplotlib>=3.7.1",
        "plotly>=5.14.1",
    ],
    python_requires=">=3.8",
)
