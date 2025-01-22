from setuptools import setup, find_packages

setup(
    name='fastsaverclient',
    version='0.1.0',
    description='FastSaver API Client',
    author='coder2077',
    author_email='abdullatif.developer@gmail.com', 
    url='https://github.com/coder2077/fastsaverclient', 
    packages=find_packages(),
    install_requires=[
        'aiofiles==24.1.0',
        'anyio==4.8.0',
        'certifi==2024.12.14',
        'h11==0.14.0',
        'httpcore==1.0.7',
        'httpx==0.28.1',
        'idna==3.10', 
        'setuptools==75.8.0', 
        'shortuuid==1.0.13',
        'sniffio==1.3.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)