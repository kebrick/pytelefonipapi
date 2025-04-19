from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
VERSION = '0.0.1'
setup(
    name='pytelefonipapi',
    version=VERSION,
    description='Python services for convenient work with telefon-ip.ru api',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['pytelefonipapi'],
    author='kebrick',
    author_email='ruban.kebr@gmail.com',
    license='MIT',
    project_urls={
        'Source': 'https://github.com/kebrick/pytelefonipapi',
        'Tracker': 'https://github.com/kebrick/pytelefonipapi/issues',
    },
    install_requires=['requests', 'pydantic'],

    python_requires='>=10',
    zip_safe=False
)
