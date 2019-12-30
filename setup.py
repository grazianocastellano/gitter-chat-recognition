from setuptools import setup

setup(name='gitter_chat_recognition',
      version='0.1',
      description='identification of the \
          gitter links for an open source project',
      author='Graziano Castellano',
      author_email='grazianocastellano@live.it',
      packages=['gitter_chat_recognition'],
      install_requires=[
         'google-search',
         'requests',
         ]
      )
