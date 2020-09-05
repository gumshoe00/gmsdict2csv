from setuptools import setup, find_packages

# classifiers list ref: https://pypi.org/pypi?%3Aaction=list_classifiers
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: OS INDEPENDENT',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='gmsdict2csv',
  version='0.0.1',
  description='Convert a data list to a csv file.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='Gumshoe Media Inc. Team',
  author_email='gumshoe.media.inc@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords=['data', 'list', 'csv', 'file'],
  packages=find_packages(),
  install_requires=['']
)
