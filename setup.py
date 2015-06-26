# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2015 E-Democracy.org and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
import codecs
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()
name = 'edem.group.messages.topic.digest.weekly'

with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()
with codecs.open(os.path.join("docs", "HISTORY.rst"),
                 encoding='utf-8') as f:
    long_description += '\n' + f.read()

setup(name=name,
      version=version,
      description='The "Weekly digest of topics" notification',
      long_description=long_description,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          "Environment :: Web Environment",
          "Framework :: Zope2",
          "Intended Audience :: Developers",
          'License :: OSI Approved :: Zope Public License',
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: Implementation :: CPython",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='groupserver, email, digest, topic, notification',
      author='Bill Bushey',
      author_email='wbushey@acm.org',
      url='https://github.com/e-democracy/{0}'.format(name),
      license='ZPL 2.1',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['.'.join(name.split('.')[:i])
                          for i in range(1, len(name.split('.')))],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'pytz',
          'zope.browserpage',
          'zope.cachedescriptors',
          'zope.i18n[compile]',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.tal',
          'zope.tales',
          'zope.viewlet',
          'Zope2',
          'gs.group.base',
          'gs.group.messages.topic.digest.base',
          'gs.viewlet',
      ],
      entry_points="""
          # -*- Entry points: -*-
      """,)
