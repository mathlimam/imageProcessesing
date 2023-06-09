import os
from setuptools import setup



def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "normal_map_image_processing",
    version="0.0.1",
    author="Matheus Lima Moreira",
    author_email="math.lima.m@gmail.com",
    description=('''A image processing tool that generates normal maps'''),
    url=""

)