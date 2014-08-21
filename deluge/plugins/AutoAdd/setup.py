# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 GazpachoKing <chase.sterling@gmail.com>
# Copyright (C) 2011 Pedro Algarvio <pedro@algarvio.me>
#
# Basic plugin template created by:
# Copyright (C) 2008 Martijn Voncken <mvoncken@gmail.com>
# Copyright (C) 2007-2009 Andrew Resch <andrewresch@gmail.com>
# Copyright (C) 2009 Damien Churchill <damoxc@gmail.com>
#
# This file is part of Deluge and is licensed under GNU General Public License 3.0, or later, with
# the additional special exception to link portions of this program with the OpenSSL library.
# See LICENSE for more details.
#

from setuptools import setup, find_packages

__plugin_name__ = "AutoAdd"
__author__ = "Chase Sterling, Pedro Algarvio"
__author_email__ = "chase.sterling@gmail.com, pedro@algarvio.me"
__version__ = "1.05"
__url__ = "http://dev.deluge-torrent.org/wiki/Plugins/AutoAdd"
__license__ = "GPLv3"
__description__ = "Monitors folders for .torrent files."
__long_description__ = """"""
__pkg_data__ = {'deluge.plugins.'+__plugin_name__.lower(): ["template/*", "data/*"]}

setup(
    name=__plugin_name__,
    version=__version__,
    description=__description__,
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    license=__license__,
    long_description=__long_description__ if __long_description__ else __description__,
    packages=find_packages(),
    namespace_packages=["deluge", "deluge.plugins"],
    package_data=__pkg_data__,

    entry_points="""
    [deluge.plugin.core]
    %s = deluge.plugins.%s:CorePlugin
    [deluge.plugin.gtkui]
    %s = deluge.plugins.%s:GtkUIPlugin
    [deluge.plugin.web]
    %s = deluge.plugins.%s:WebUIPlugin
    """ % ((__plugin_name__, __plugin_name__.lower())*3)
)