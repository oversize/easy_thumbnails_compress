#! /usr/bin/env python

from setuptools import setup

setup(name="easy_thumbnails_compress",
      version="0.1",
      author="Dennis Schwertel",
      author_email="s@digitalkultur.net",
      packages=['easy_thumbnails_compress'],
      license = 'LGPLv3',
      description = "ties in with easy_thumbnail, picopt and celery to compress thumbnails of easy_thumbnails after they are created.",
      install_requires = [ 'django', 'easy-thumbnails']#, 'picopt'], #picopt muss von https://github.com/ScholzVolkmer/picopt
)
