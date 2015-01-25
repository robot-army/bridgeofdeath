#! /usr/bin/python2.7 -OO
# -*- coding: utf-8 -*-
"""
:References:
    `coverage <../../../cover/bingpp_generate_keys.html>`_

Our security is based upon 16 public-keys one for each application/sector of our Mifare 1k cards.

Each application should have all 16 public keys so it can generate new cards, but only the one
private key for its sector.

The other 15 private keys must be stored somewhere safe and secure.

.. warning::

    Without the other private keys our cards can not be reused.

"""
from __future__ import division, absolute_import, print_function, unicode_literals
from Crypto.PublicKey import RSA
import settings

def main():
    """
    Create 16 new public/private key pairs.
    Public keys are output to STDOUT ready to pipe into `settings.py`.
    Private keys are writen to numbered PEM files.
    """
    print("PUBLIC_KEYS = [")
    for key in range(16):
        private = RSA.generate(1024 * 4)
        if key == settings.SECTOR:
            filename = 'private.pem'
        else:
            filename = 'private%d.pem' % key
        with open(filename,'wb+') as privatefile:
            privatefile.write(private.exportKey())
        print('"""')
        print(private.publickey().exportKey())
        print('""",')
    print("]")

if __name__ == "__main__":
    main()
