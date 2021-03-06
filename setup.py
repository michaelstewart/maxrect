from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='maxrect',
      version='0.0.1',
      description=u"Find the maximal area rectangle from a polygon.",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Amit Kapadia",
      author_email='amit@planet.com',
      url='https://github.com/planetlabs/maxrect',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'numpy',
          'shapely',
          'cvxpy'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      max-rect=maxrect.scripts.cli:maxrect
      poly-intersect=maxrect.scripts.cli:polyinter
      """
      )
