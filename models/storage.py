# -*- coding: utf-8 -*-
"""
Storage
-------

LDAP storage

:Copyright: 2013 Reading Makerspace Ltd.
:Licence: GPL v2
:Authors: Barnaby Shearer <b@Zi.iS>
"""

from __future__ import division, absolute_import, print_function, unicode_literals
import ldap
import ldap.modlist
import settings
import base64

class TargetStore(object):
    """A LDAP based backend for storing our data"""
    
    def __init__(self, url = settings.LDAP_URL, user = settings.LDAP_USER, password = settings.LDAP_PASSWORD):
        self._ldap = ldap.initialize(url, trace_level=0)
        self._ldap.simple_bind(user, password)

    def write(self, dname, data):
        """Update an entry"""
        self._ldap.add_s(
            dname,
            ldap.modlist.addModlist(data)
        )

    def read(self, dname):
        """Read an entry"""
        return self._ldap.search_s(
            dname,
            ldap.SCOPE_BASE
        )[0][1]

        
class Target(object):
    """An LDAP model for a NFC target"""

    def __init__(self, store, uid):
        self._store = store
        self._uid = uid

    def _dn(self):
        """Construct dn"""
        return "cn=%s, %s" % (self._uid, settings.LDAP_BASE)

    def write(self, data):
        """
        Save the data back to the store

        .. WARNING::

            For now we store the cards data in the description attribute
        """
        self._store.write(
            self._dn(),
            {
                'objectclass': [b'device',],
                'cn': str(self._uid),
                'description': base64.b64encode(data)
            }
        )

    def read(self):
        """
        Read the data from the store
        """
        return base64.b64decode(self._store.read(self._dn())['description'][0])

