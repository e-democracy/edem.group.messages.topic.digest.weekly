=========================================
``gs.group.messages.topic.digest.weekly``
=========================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The weekly digest of topics
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_; `Bill Bushey`_
:Contact: Michael JasonSmith <mpj17@onlinegroups,net>
:Date: 2015-04-27
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

Introduction
============

The *Weekly digest of topics* is a notification that reminds a
group-member that the group exists. It is made up of an adaptor_
and a notification_.

Adaptor
=======

The named-adaptor
``gs-group-messages-topic-digest-weekly-notifier`` takes a group
and a browser request and returns an instance that can send a
daily digest of topics.

* The ``weight`` attribute is ``20``, which normally places it
  behind any other digest adaptors.
* The ``canSend`` attribute is ``True`` when there have been no
  posts to the group in the last seven days, and it is the
  weekly-anniversary of the most recent post being sent.

The notification_ itself is contained within the ``text`` and
``html`` attributes.

Notification
============

The notification is provided by the page
``gs-group-messages-topic-digest-weekly.html`` in the *group*
context. The page is made up of several viewlets_.

Viewlets
--------

There are three viewlet that make up the daily digest: one for
the header, one for the body, and one for the footer.

Resources
=========

- Code repository:
  https://github.com/groupserver/gs.group.messages.topic.digest.weekly
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Bill Bushey: http://groupserver.org/p/wbushey
.. _Michael JasonSmith: http://groupserver.org/p/mpj17

..  LocalWords:  Viewlets wbushey mpj github Bushey viewlets
