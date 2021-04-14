from setuptools import find_packages, setup


setup(
    name='django-page-transitions',
    version='1.0.0',
    author='Maximilian Schulke',
    url='https://github.com/schulke-214/django-page-transitions',
    packages=find_packages('src', exclude=['testing']),
    package_dir={'': 'src'},
    include_package_data=True,
    tests_require=[],
    install_requires=[],
    dependency_links=[],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
