#!/usr/bin/python
# -*- coding: utf-8 -*-
#################################################################################
# LAYMAN MERCURIAL OVERLAY HANDLER
#################################################################################
# File:       darcs.py
#
#             Handles darcs overlays
#
# Copyright:
#             (c) 2005 - 2008 Gunnar Wrobel, Andres Loeh
#             Distributed under the terms of the GNU General Public License v2
#
# Author(s):
#             Gunnar Wrobel <wrobel@gentoo.org>
#             Andres Loeh <kosmikus@gentoo.org>
#
''' Mercurial overlay support.'''

__version__ = "$Id: mercurial.py 236 2006-09-05 20:39:37Z wrobel $"

#===============================================================================
#
# Dependencies
#
#-------------------------------------------------------------------------------

from   layman.utils             import path
from   layman.overlays.overlay  import Overlay
from   layman.overlays.source   import OverlaySource

#===============================================================================
#
# Class MercurialOverlay
#
#-------------------------------------------------------------------------------

class MercurialOverlay(OverlaySource):
    ''' Handles mercurial overlays.'''

    type = 'Mercurial'
    type_key = 'mercurial'

    def __init__(self, xml, config, ignore = 0, quiet = False):

        super(MercurialOverlay, self).__init__(xml, config, ignore)

    def add(self, base, quiet = False):
        '''Add overlay.'''

        self.supported()

        return self.cmd(self.command() + ' clone "' + self.src + '/" "' +
                        path([base, self.name]) + '"')

    def sync(self, base, quiet = False):
        '''Sync overlay.'''

        self.supported()

        return self.cmd('cd "' + path([base, self.name]) + '" && ' +
                        self.command() + ' pull -u "' + self.src + '"')

    def supported(self):
        '''Overlay type supported?'''

        return super(MercurialOverlay, self).supported([(self.command(),  'mercurial',
                                         'dev-util/mercurial'),])
