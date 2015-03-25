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
from datetime import (datetime, timedelta)
import pytz
from zope.cachedescriptors.property import Lazy
from gs.group.messages.topic.digest.base import BaseTopicsDigest


class WeeklyTopicsDigest(BaseTopicsDigest):
    """ Represents the content of a weekly digest."""

    def __init__(self, context, siteInfo):
        super(WeeklyTopicsDigest, self).__init__(context, siteInfo)
        self.__weeklyDigestQuery__ = None
        self.__last_author_key__ = 'last_post_user_id'
        self.__subject_key__ = 'subject'
        self.frequency = 7

    def __getTopics__(self):
        if self.__weeklyDigestQuery__ is None:
            self.__weeklyDigestQuery__ = \
                self.messageQuery.recent(
                    self.siteInfo.id, self.groupInfo.id, limit=7, offset=0)

        retval = self.__weeklyDigestQuery__
        assert type(retval) == list
        return retval

    @Lazy
    def show_digest(self):
        """ True if there are posts in the group, the most recent post is
            not from today, and today is the weekly anniversary of the most
            recent post in the group."""
        time_since_last_post = timedelta(0)
        if self.post_stats['existing_topics'] != 0:
            time_since_last_post = datetime.now(pytz.UTC) - \
                self.topics[0]['last_post_date']
        retval = ((self.post_stats['existing_topics'] != 0) and
                  (time_since_last_post.days != 0) and
                  (time_since_last_post.days % self.frequency == 0))
        assert type(retval) == bool
        return retval
