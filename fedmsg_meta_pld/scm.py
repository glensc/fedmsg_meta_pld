# -*- coding: utf-8 -*-
# This file is part of fedmsg.
# Copyright (C) 2016 Elan Ruusamäe <glen@pld-linux.org>
#
# fedmsg is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Elan Ruusamäe <glen@pld-linux.org>
#

from fedmsg_meta_pld import BaseProcessor

class SCMProcessor(BaseProcessor):
    __name__ = "git"
    __description__ = "The PLD Linux Git repo"
    __link__ = "http://git.pld-linux.org"
    __obj__ = "Package Commits"

    def subtitle(self, msg, **config):
        if '.git.receive' in msg['topic']:
            try:
                repo = msg['msg']['commit']['repo']
            except KeyError:
                repo = '.'.join(msg['topic'].split('.')[5:-1])

            try:
                user = msg['msg']['commit']['username']
            except KeyError:
                user = msg['msg']['commit']['email']

            summ = msg['msg']['commit']['summary']
            whole = msg['msg']['commit']['message']
            if summ.strip() != whole.strip():
                summ += " (..more)"

            branch = msg['msg']['commit']['branch']
            tmpl = self._('{user} pushed to {repo} ({branch}).  "{summary}"')
            return tmpl.format(user=user, repo=repo,
                               branch=branch, summary=summ)

    def link(self, msg, **config):
        prefix = "http://git.pld-linux.org"
        if '.git.receive' in msg['topic']:
            try:
                repo = msg['msg']['commit']['repo']
            except KeyError:
                repo = '.'.join(msg['topic'].split('.')[5:-1])
            rev = msg['msg']['commit']['rev']
            branch = msg['msg']['commit']['branch']
            tmpl = "{prefix}/?p=packages/{repo}.git;a=commitdiff;h={rev}"
            return tmpl.format(prefix=prefix, repo=repo,
                               branch=branch, rev=rev)
