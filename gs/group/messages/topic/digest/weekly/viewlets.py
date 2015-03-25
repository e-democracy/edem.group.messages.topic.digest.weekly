# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2013, 2015 OnlineGroups.net and Contributors.
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
from __future__ import absolute_import, unicode_literals
from gs.group.messages.topic.digest.base import TopicsDigestViewlet
from .topicsdigest import WeeklyTopicsDigest


class WeeklyTopicsDigestViewlet(TopicsDigestViewlet):
    """ Viewlet used to pull data for weekly topics digests. """

    def __init__(self, context, request, view, manager):
        super(WeeklyTopicsDigestViewlet, self).__init__(context, request,
                                                        view, manager)
        self.__topicsDigest__ = WeeklyTopicsDigest(self.context,
                                                   self.siteInfo)
