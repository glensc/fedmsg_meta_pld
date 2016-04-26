# -*- coding: utf-8 -*-

from fedmsg.meta.base import BaseProcessor as FedmsgBaseProcessor

class BaseProcessor(FedmsgBaseProcessor):
    topic_prefix_re = 'org\\.pld-linux\\.(dev|stg|prod)'

    def emails(self, msg, **config):
        usernames = self.usernames(msg, **config)
        emails = [name + "@pld-linux.org" for name in usernames]
        return dict(zip(emails, usernames))
