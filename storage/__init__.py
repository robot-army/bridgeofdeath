# -*- coding: utf-8 -*-
"""
Storage
=======

LDAP storage backend for RFID targts

:Copyright: 2013 Reading Makerspace Ltd.
:Licence: GPL v2
:Authors: Barnaby Shearer <b@Zi.iS>
:References:
    `pylint <../../../cover/storage.lint.html>`_,
    `coverage <../../../cover/storage___init__.html>`_,
    :doc:`storage.test`
"""

from __future__ import division, absolute_import, print_function, unicode_literals
import ldap
import settings

class TargetStore(object):
    """A LDAP based backend for storing our data"""
    
    def __init__(self):
        self._ldap = ldap.initialize(settings.LDAP_URL, trace_level=0)
        self._ldap.simple_bind(settings.LDAP_USER, settings.LDAP_PASSWORD)

    def write(self, dname, delta):
        """Update an entry"""
        #TODO: Make more generic based on dict
        self._ldap.modify_s(
            dname,
            delta
        )

    def read(self, dname):
        """Read an entry"""
        #TODO: Make more generic based on dict
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
        return "cn=%s,%s" % (self._uid, settings.LDAP_BASE)

    def write(self, data):
        """
        Save the data back to the store

        .. WARNING::

            For now we store the cards data in the description attribute
        """
        self._store.write(
            self._dn(),
            [
                (
                    ldap.MOD_REPLACE,
                    'description',
                    data
                ),
            ]
        )

    def read(self):
        """
        Read the data from the store
        """
        return self._store.read(self._dn())['description'][0]

