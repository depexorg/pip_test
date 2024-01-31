import setuptools


setuptools.setup(
    name="pip_test",
    version="0.1.0",
    author="Antonio German Marquez Trujillo",
    author_email="germanoctako@gmail.com",
    description="Prove setup.py files",
    python_requires='>=3.9',
    install_requires=[
        "urllib3>=1.21.5,<1.27",
        "flask>1.0,<2.0",
        "Werkzeug>=2.2.2"
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-mock',
            'prospector',
            'mypy',
            'coverage',
        ]
    }
)
