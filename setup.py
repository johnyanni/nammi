from setuptools import setup, find_packages

setup(
    name="nammi",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "manim>=0.18.0",
        "manim-voiceover>=0.3.0",
        "numpy>=1.22.0",
        "pillow>=9.0.0",
        "pycairo>=1.21.0",
        "pygments>=2.11.0",
        "rich>=12.0.0",
        "scipy>=1.7.0",
        "tqdm>=4.62.0",
        "watchdog>=2.1.0",
    ],
) 