# -*- coding: utf-8 -*-
"""
:Copyright: 2013 Reading Makerspace Ltd.
:Licence: GPL v2
:Authors: Barnaby Shearer <b@Zi.iS>
"""

from __future__ import division, absolute_import, print_function, unicode_literals

DEBUG = True

EMAIL_SERVER = 'localhost'
EMAIL_FROM = 'rfid@rlab.org.uk'
EMAIL_ERRORS_TO = 'b@Zi.iS'

LDAP_URL = 'ldap://localhost'
LDAP_USER = 'cn=admin, dc=rlab, dc=org, dc=uk'
LDAP_PASSWORD = 'hackmenow'
LDAP_BASE = 'ou=Cards, dc=rlab, dc=org, dc=uk'

ENTER = ('Mock', '/dev/null', 115200)
EXIT = ('Mock', '/dev/null', 19200)

SECTOR = 1

PUBLIC_KEYS = [
"""
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEApQJzwUeeeXWI4Wh5JLBf
UlB/wBfmPtVqOXSKvAFvAmXM3j6DnPqevbyiUxst1vCgTotv0Xs9unyJQFNimm77
15xqQAvZU/x+sjKPxLFhiiJa8/T6Tohiv9DNqM+VwTh9hom2GUtlb+a30a65OMaY
Mx0XdwlzEYRejZKd0bfEhhBQvfdx+S2R2STZzNp+lSsu468YfbMq2+WjMvSmXZPY
JeM3ZSo4GHRP+IGlZxqpqC/v1rJI7QPvETxp38OXvtWNLYVBZZ1QFlIGnPqa+4m2
tqipYl19afO91cVBB2Lvfwhj3ztwcJeXZ7voRr24m+JatjI/ioLkzb2uywMQYoQC
0bvUzba8CkE0qy93YZZyU2gilOuFRaAy9nY/2+xR/5Tl7NreOsD4dXtpOlZs+0CW
V1YNqWePVKXpQpcSkZKIJ0AeujQg/oOEuqzbT0tbs0ZbgfjyLZ7Iusl43YwIlfZ8
7lSZDdkURPEHt311chIt4x7h3aZJsPUpPDFvG4ou4c4ZP590OfHZVNqcFjMAt1Rj
S97Vir9Fe5fJWiZsZSEbQ4+Nh4cGH9nNb7J9LV+mAxUvuAaOuzWZ2z6Jxbx+9k8F
l5bmiVH4KgzlE0bckravRfo9WdveO2IVpz40MEuOysiyytO7y2LOsDWULpH+pjSG
ufPunZpfRiQRejx33qUsJHMCAwEAAQ==
-----END PUBLIC KEY-----
""",
"""
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA2ZIeTHh9dX9LS/6wH8U+
FOHF30+JZBP5mmaWSp5gPda3eoSadwBLmJXzwfKOJA0kHgtszfZEgm/VgqhozyB8
AsWuuTC0Ld6u7hpq6z9pa97xIpAbhKbeHJ8r0Afjl/BpPiL3GhH4jdswSp/rJWje
KNoyphcY/vtSXrzO1TuuK3YuDgM/mnIQns3WiPw3/soKXy8L6aRjL2M4JVIdeFBh
h3KUmIPmoah43rfKhOu1A1PyAoI8kV1lmFTSY2qc0n7InK8FcD2VN0bgfpGoIWXB
QrMhQom+NGgXejil2hDoR4gRRqQjEFeLc+K8ca0JTXdNYrrAARBsEtIFJveQced0
z4IRMvyfKmjD4TiRXFJCz1e//W05HkgDwTLDjSkqt6n+WSKJ5OwHBfj38qALKOFS
jSdmRJMi3tdvPM0YJnn20k2rSaKybfGsEVV+KFBIt7wabCWpxkvhgi91PXGFULjT
jvVcTdYMhol1BZKOqq99crxUYhUz1m7GleUUIU95gOUs0Mea5wYR+QtT9hcsu6na
88hrk1JiDKDyLIQFYOO5vh5/65u43qZuKFwDbXpgAxAfLCKoj5TaZv3ywnXrp7SY
3K7jtWHQC8Rxf90yf35G2AlrRwEwxSDo0DkqFGV48f2yyh2kGcUe/o5TkLDqM9yl
1a3rOL25fQLoFxgGLFmeTEsCAwEAAQ==
-----END PUBLIC KEY-----
""",
"""
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA2zovXyrIEUJab/NhV6x5
dE9GfqkHH8ztjZ8zPA8QyxrjMf/o2N+OQPsjP/tWRxs55ZpvdCg7a7QPNGbiVD/I
Y9CBQ3SK1E86KN8ILVyP4ooTZZYGaNvqUJtwQ8+fB1AZq+GRj1I6GDMuNBWWoCTP
gU/T1hjcccgTGd0DifOVtD8vPt5Kl/AvVmYuoWN6X3trR0e4QrCjubeH9/Usxtos
xId/+1jxn/jOaKO298ZAOM4JSv4skDi4Fas4SA0KCo1GJK6vO9zVbdebFzXGHZOG
LrySVfF/jpcfkVFQspWko4DyN6q4/Tz4WczWOoYeVzEQ90jSZCvxIu8S13W4OmPR
UWYiW9nEV1LVvmITS4Jpkgfypo/S6ZPQUk+AuQ2D37iB4W+LaTyZ/Oqx2Mx1Kp1z
9tDnsHnFiwt6AqH1qwKQcXArwhxqFhafjOkBvOo8RDYJq+8soGHQxpJqV/S/jglr
A/1Go3pgRai5+XkLTM/ZytTu8z87qu72c3sBGrcUi8qfJPRhGk2Scnxqnw7nNwep
t/VOptqZb4bN6GTPX58O7eXBlE66kGbmJvPKTj/P56jVdIg88X13/Z981u11i83L
cOYnEsddzrC7Wj2FJeYmwWKTHsXvra62cRUX1szPzn9UstR/AsCCQHlYf0cN+9uy
LAAcrmQ9ko86o5S+T4uwXOkCAwEAAQ==
-----END PUBLIC KEY-----
""",
"""
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAvYLjYP7oXh9pcJFiSH17
OMpncTxWKUZFtelfpJfh1PjukBMzws16qNUTsy4XJAAuE6NHb1o6yUjfJfNqfkSB
q7+zmd8u4aC7qMkhaVpxuIIOJBuzaWP5fa23r4sH40NcwAk6oFkOavskU9myPwbV
EPNxEsqF+JCMm+uRktVYUtW8Rg3EyhaFJZ/l35pp+FSHtglpd2E7GOFgOO0k7Sre
eBwLWZxQ7bDvGpWF4+mlUgLRNBuo6O3RaswpD6FN+tV0rWg4ywiaYGS/VdFmnUg6
KIiB7bTTt59YIfrdzAcPz4I478juG9l6XziON1TxGyLMvWX1MqzVl9F+Z0Tbi5gb
NFt7iknMquc/rIz1wcwT8oD8i5HkhV3BGu+7/+GF0iaQUWPn6q8MrBkKVIUxzROq
shUELHkixbJko2W9xZJL7v2gH7z/JZUW8kgtuYOw9r3KY4lIWbJ43r3NL4Ejv65H
t3SYZNXy7jPjS4GY6dDPDdE673ERAxAXjQ+4fkf5FQ4APM83MuDQoHJlb1WgyAF0
XK16CntIn68sHEZw5q8sG7/tEUC4zQKEDoGeBHqOZySEncRFYgPQveyTJOdbBOQC
4AbxdwYCRG+5YsfAPiN4ELcwmNYF0AJG52KdC/IIbg4thk9KRWkVd8Zun2vmHQJy
4TFXVtr2OCuNzDH16kkbTAsCAwEAAQ==
-----END PUBLIC KEY-----
""",
"""
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA3c63oNQgusnKtwgRdtxR
i/MzL9TqKDrH0iDmkaQzEgZi6Gq+4ex8xiU7Js11/5x+GcvYWKCp8JWJ4vb2df4S
D1WXbAV6f3Gwyy/c5+dCSenbCLjwBPewZDGIsxUSZKk8088IJxYPJzytmAIdPvma
ELH8f4NB91fEyq2i+hj9I0zHMMxzsy/funD8vOg0qkjKAHJ8yVo5ezqG7p+G9h7J
Gpo6vUk1y7xJJs3SrVtgjMVfORETHmLECKvojLxdPhcKDbSE/hQh0i05Yi0wHtAx
DYGYN9OgApADdx9QLQxTSf1TkDepWHfnMoIoELKiaQT0oIfdAVAqo8W4NJxzzvQH
8zu4f0H1rACT7/Vo+YBXvwmeYkSkel6k2zjdM8x3aB6oGs9M13xLvGGot+IM0f1z
Hyo8kUvQqGdahzX/+bMcVvi/JEBB99Y8DU9v2S8HHSSUzUph8WHEXA/oWV+Z2sYc
NINtQkat2qMMnTlEs7sPLzB4TOFfG9gJrEms5MODl+yvmyHbGhYLQU79Knecv/MS
tAI/uUREMPUVFqMskFOxx2Mczvlw1pm21vQvc6z+lUdOrTtxykBPBBuiZbUy9Bfy
yv8iZXCyZTOcjve801NKnaC+2MTZ1nIxERadNIHFvuXgB4uky9PE5WYZdYfk37+F
QRLhF2bIltBzZc6ja08M3acCAwEAAQ==
-----END PUBLIC KEY-----
""",
"""
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAzVbrteTCwMvn300TbFdZ
iCZ1eU0iJBpvPyX1ayGXawNcAa6fldDMrqwsT+amwlM7QXK90gSet55V4PsHuQJg
ku/9pbJKlsEaYslEeHtBcjSNGUQbZw+//2z1XbIXMLpQhNjKxijOGl029fQ6Wox6
pbdI86h+fR1Y0U70NPUaGXPp8QFd19YhFvRgs65QgBImdeIBjCexyrV91qZh9x3B
FEys1XeDF5F4kmR0jKV+H7/apY3SBWXNSwlHJvf7lERECROI/EUA9aoH+KFG0Pu6
WOTYyqnWPcIvikDVoPuzhcL6xJclDVEK8NxBvsc/ul9j/9Qd5nvJV+Ql5kZcsVih
L4RrDB3Efbq2lVZW97Y2NnyKvVKh8Xi6NPlLjm5CyR7qOk1sjf+BWsugZKw0lUq3
o+Yrl1k/Z5heEtIQbuQupIarJqp0S2cZcAj1zxGCIkP3n6qzKZlm9xExacmgYvbA
Ne55PQGm+fFE7M3qmtGPKY1bMyAK3LE9W0IyOsqOfraJii0wlbyiQdsaMSDgUrbJ
l6pv1mhwknrEnbkaUsw8+vORnjEkgvpM57Rlo1HQY8sPxDMMu4gEeAaYvm62PsSn
vElySpIBvH308RQ+8iSs4PRKXSeMv6bu/EggXiQbBBqN26Zat+jDcmmBLZwxpQGy
Hv86abN75ilZU3Ka4BG2ZT8CAwEAAQ==
-----END PUBLIC KEY-----
""",
"""
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAo58+69Abuz1OshyWr/TJ
XK1FwXgaxfjW13TLHAAmzDBFfVbQ7dl9PFfucPvo3qjR47+VTCu9sOzZ2kl4WE81
nStDgmNfJCFC5iag3EuZnNKt/IDdiGcQyGf6ITE47IeU/ln9+thKG2TfwEJbajAG
UbdoM/CFSGmVHTE4zCMCzE8mAe8LiO0dX/GIqzWrMmGStdUswH2IfJeoFMH6f1J9
N/KqxkIUNr230P36r+YcdFvgtYi7mA6J0HCSc94DgD2/bwsISKxOP26CRlrDuE+H
yYDTNiyupld+pDgm7hXQD84e8BrtVbMTQrDall3OEpKXohpmAHRxpEvoxvsZS6ef
lHVJobjU8ZELqjStxOOiWLqLMz1As3dgaAwU0UvrugTlOk3ypHoq7Qa/tywWM21C
+Lb+WkcuxVHhjG0i1yBeBvq2p7jkOBcrAH3OcEfFdVidLBnVxtOE57d8zjPOdLb6
Kb5rmtXGvJzth/uC5CGt90LsdLMq7gWkKKKOyzKuCra9uYF7jm2F15b8H6AOgZfI
m33NVrWi4/FkXGhjvSN29xUq1fhJTp7dkp6Fbag8lihNUptDXRpopxpQ2HZl7sOz
zcpMGvHUG6fYFiQxtUSPNqBYRFwWSPrm9yFYH8yiBQqDeV8DAnOA44kOxFoa+grH
ImwzeamiSG+RGswbILLZNH0CAwEAAQ==
-----END PUBLIC KEY-----
""",
"""
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAuLuQSwOuu356JBJmMJP9
9XqfrVltifbl6gLpMfdw13l3bh2t876qKKZkPM8hz3lPIiDVSEn6H22vp7xgx1zK
YaS1Np/haOqES7P4Ntn/tA8r2whxf9aV/OoEmR6uQvT8ona0CIRSfY6zHiFL4ovl
c1AUSWYN4UiGh9GE5r4gYtyL7g5z2s97yZ3yMcaMwLfg+e5L6fDkAvGfLUjFvVho
CXBHekkjB6y9qQUfFcZ5Pv/e+Pbb9no9VIs5k1c/SShp38lx7TiTH9KIkGayBZdh
bQE7MHv8augmLftWG4w+aPCym+ULyClJfKn2CO5E7lFQ5fc9KdHGA3yfOkyaGMHK
bDI+0JQscgl6N3+twaqhnV/7kuQM2zSjkZporDOnMojIjXbpwB1pLCMqEfn48S91
PhxbTR47bVGwyHbX55YIMIe0v7C8pBxcKZK1eDn/56LYDYYSickcmFETaAV0FvxJ
fIHNG0zt+myA9UO5FIiujKg5KS6OBkjXv0eOm/UlYvXPhGGOuYyWmSiy3U4od097
N1zsuk1lkzd0b0yYqG+ed5bgri8Rlj6lfgwpvkNzgwdKRmBfPJOW3mEckhYqdVZJ
ZJOC8jC5hiVHyZWwX7VF1jTUqnQv7jh/SXWUkmM8I/s89M1wgBP7IKh8CJAO2+tP
aYcsvaV89Dv24wTUy6mCin8CAwEAAQ==
-----END PUBLIC KEY-----
""",
"""
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAupzUZV9uqNW0h8KS5AGz
dPKuiN1npdMYUR55aGBqV5icVUYIlAYVnW/gbxAQRup2tKbukfZuiT54whB/N4xO
j4TaT91tVAMg9k9vKc6UnXgTnyD5nLEU0NsSAJU0uK8NVgvGlJ23v3UyXCsT2rrY
Dh4QvCq1YKo4dbSX1jegB+XHkIYZUOnjpfrK2HhX/s/GmsSbeZg7JMFU6YdyQgkj
nzzMSZNJ+mlZBdixFYRZMdVR5zuShS0T9+5F7L4SJn/NoKNMdpHwBuv0w6W6413p
VzpmnKX93i79XgHpSA/b7pfdMh1WYYXAWTBC2SWS2EbfgjJvu213go2Rhz1asFiF
YY/lLP9z48zgFxXBqL8VUHOxeVp5wTdBwbE5Akti8Qyw6CJNECjwBChXbeCqyfJ7
7r1KM6epep5TmN3jeUIroGp4kTkIXrpWhyaa9/OZz+kzZ+MEwtQJ6Y28o2mzeyuT
xOcqSY4LS85XkGeyb8yrl0gGPaIFoxcfPImwrWI7m3iFdtt6WajOE+gDPVuj7Ql4
MlP9lVWqWfOPY1prmKkJTIzyTun4vWO9iNEpsZVJZhXOCFM6UTojuF6KN0/yP/dm
cU0IpG47+/4xcfooSSFLmY/dp146N1OCVZynU1hgj6YXm8YeYtGxt3xKnVS1vtb0
uIsoE7T/BCsuQlx3qYwmaK0CAwEAAQ==
-----END PUBLIC KEY-----
""",
"""
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA6//0P2hcgNscNO7U/5TY
jOMBSYV0upcfJoKj4AcnWT70UxO+67P4h1AIs/d6QIWIZtDUrd9boCeXv7NQ6yqG
JXxxiAnjinlo3bpmpfrIwLZ9Au1dmL5N6NnYqei6BdfPamiOebPgmDwo00CECydb
176y7YHnLyRlEZsJfFnDgUA04qqtjw7r0XMeTESSEaBVqUx6fTgFSF3rhFLXFE/4
iBUhkKae/j84qR/zS4ma1GiPwnwDuyuN52+LkXXbhUeANs/5AX833zGYj69t0/rl
k9yZ5c9kOULnew3SJ0GZ2LIVmq1oDEwnz8BArueqYSqiFBadpe8Bp5/iuphwTYiY
HmOKz95uXLZ99WFvYTuj3oMvxZnuFlRnQPjbV9DTXck87fZTqGZ+QnyAwEjjPwEl
4JHCuY3/u5nGDy2Id+DVxqdSukBOs44ONTACA/gbwRGWzkPuS18/pxVG9owckAwW
F1Trp6L/yIl5bvrFdPk8kqffId1rAzWC7W4FoX75bIcXzHyYB4PuMSTUD6kkHXd3
mcGixJyItFzb6mC+nQ43LGccs0mYTR//V45FHFeP7QsuomniCzKD2yMQ0+6HSCtw
zl4avEiJbKK1u7j0G3NCIVlaT9kuDFoDH8zx7tNiGH5SSHv9F7j5e2vVY0YEe/Ek
zAeAKEDoVHOM4lBWEPOdIrcCAwEAAQ==
-----END PUBLIC KEY-----
""",
"""
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAiggMF09CsF6DEALd7nxW
5uPMLsXNghvx53v5y4P34lcM92Yf2Ax+OXPpjvp+XD6cZxtOUilZfACf12YRcG4m
gzeNa/HJnptKcxOoEpNfuXsvI3Tr0kI2U9j4uwjumRzOmtBzP6Azgzoh3wj/oocU
mYfLrXiez8g8dYpNTqZW5SncGLNCdrLCWq3wBJU+LKCWXl2KlvL/cYyTmEe6SlYc
Od1HyrFE95eMVJCs9TR5kXnxcvldVQDFPuzrpBw0l297d3+QihSLBRXAT7Mzzftz
jpPJ76TGHHcCE4JEgEDtcgxo8iZP6gOc7QnxEjl+vKqbRd/nQuwU1LEFg/NwP74f
ymuM0SZn9DZ8AZYKAWdXcqPsJBznA7s5lPiG00Rt1XmTQSZcFgG8mU5ltxHk1GRF
pA30OAqUUVuEMgxvPC1eY40XHdsX3aSOFr7S/W0g1wIJujIciM811VtCx6y+Yo0Y
irxYn1lVUx0TuhUaWe66L91dVUUQJdAoDm3RanFOu+c9mwIuSViw6t2EfNHTEEVQ
Nai76qFiwIee9Lls0oBghUTbJYwMITwL3eD1k5odsaqZQAKfK6cpTqmNb4lAo4gp
lIUKy3CqEOX6y4VKE9zE5GXAf0LAfsEzFSwqU5PXOjfk9j1L+Sr96AuCqJKdF4bR
djva6qCP0TfTZrm8aXn/kv8CAwEAAQ==
-----END PUBLIC KEY-----
""",
"""
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAm1sXUwL2e2GabdQZVzfz
gddYczUVR8vvyxwl71rLQtWS55KBj4gGUud3hph9vif5UYR9fts0TRQ/73okL6iU
/5eKyCy6dHSNGI+bfDiKH6jJutQZCpa1WGsxYDAQUAf572lShvjAl8w87G3W5b4q
MOR6m4znzNceulkCSdGXkZij0fNHdz6/veczKO7u3GZqf11rfLkNpJIeA+dBGCZG
1AW+F3PkzJYw2opVmAfTyMqo2qXKwwmd1/Az4l7Q9YntBmjZyhK8cvvpJ6ConfBn
jV4M50KMdNT/Rm7p1e2i0LojzxwMJ/QmMpnGFAjWVQzTCh23V45tkWLh/IL5V3ic
Sbw8tK3g7c2oHXQonXbp3XXs6KnzwWS2IrGRL7PkFjFdXjjF1Xh5iGjGXtUcr/lO
hGRvhuaC5A4/VmR2w22tINqxfvWLKTqR86LUl0dPHhCtXHRvl3JoLMVxGIkRRF5U
w/pdSAa9OLaqHzTSyrjCUXv5u9ysHZbqboGZGyf6zPlMfdzmhr7aBUmXhdmXNlIM
V2SiIHOXVvEFVKMlQAZokcPiQcF1dGKxbDWbqD2JJdj/FUnMrNaNBSvxIyKNqKjW
mosvZv1GDVqs9mqQG/VMMGTZiaXF5Dq5+R/gS6+SeNMKJBGlGAyUGzmNK5prXOVi
SRuT7y6B56MxNjacjVBheb8CAwEAAQ==
-----END PUBLIC KEY-----
""",
"""
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAsbj8ia1Om+UfKJ/9MAvE
ixz0N8CWj5zgQtEHiTnN2sfkOX7zxeVbT2ge/dUrnBoDRmiPeGMoaB52Wgli0xz9
JidlGIRu533nOuHmrhWSGYWFTUWmaK28IQntHrs8nIbh8/XBZhHsdXzJ2aDdFM95
fOrDvW8MdEYFIYZ/eD0ommITwYwilLEDo1sUbEbP9kX2vmwi2OvyxnfDl0pM9yAJ
riX+G0AsAt8Ry3vE6fgMndPoBEGwAW2SQHY4kK6igb9R4Oh4XBTmg60puVTJZOv5
JeuAZd4fsnqv7u719rAyd6S2AzJrrsAwmt82sse2zC2P4yg8bk0G2+oL9gLyBfRR
dc9TY8t4DGqx6RIduAl9Pxs9BSSbpVVkGBYCgJvMqZ913s1PFD27aLsOSEQpsLXQ
0z08VIMxIi36IbXC8mQAopo/guY4WFAWMcTZz7jTPf8NK8v1Ubl0T+N6whrxGrFl
8vvgGnoMRmPU/FcweFxW1HsNWKoqAw3X50cOW0Zj66Wf+1FX6RMzhnOgwYA36DI6
Atqid5zpqBbTpG1xQ715LhpKbBjtezMfDOPjS+cESnzh1PCiV9t+e4/4nq1LZ7jt
MWzPlwhjL392Q0LTDef8IeOttFoy0/4FT0IFEn3nnbwnzUw5AJmUl22HWTf7im4v
lMrG+Xg98sArDKnTbUiKp4UCAwEAAQ==
-----END PUBLIC KEY-----
""",
"""
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEApIyGONvgWggGw0GLfgnW
C72dXzNyrGSCCTO6wIDxTmfhlydOkhnrS4wBDMWbxZrfB4ctwGSJF2K1wRQHBX5W
NHyKYyc0bJ9i4pvlUVO58hRBySePhjsn3ZddiKuxH80wW4LjKQiZWXanGqtsO0TJ
NjCoDjtI1c+esvHnFkZ3b3W69PTy7jndCedMpI2itKM51WiMyMX1dK8nRwU3pcGr
WeEh2mD1dFus9LlOMLd8xPJ39+qY1uXJAohpbKd5RPy4jLvUWatBIB2MCXmMX5iP
o4MHOyZlMtdR1fykY9iFy8S1imRSrXxMFUyzXZt6dII5l80m/0nUPGOD3goyR/HH
InHbkH5nkdL7ysh9fpbD8ekh2SjPK7rDQDqG6h3IxYKBM4RYvk8PD9e6yOYQzUFY
BEOwdZXlo9D4LVf1sxN6TudDet6eh7u6bj00UuMjiA92pB/3bUPeenBIpDbiUUbc
iweqEJ/BD2FiVJoTJbZ4hiedatb+7scTMJQJ7w9Syplz3OnbNOYN1RsO2qBm1gbr
3QwiXa+tPBRewwmm83KHOvTkVT4At6MntwVi9df0Wp7GiwqXLvcXHXqi36g80qWS
0Qp6XNByjXjQCQhOeFYGAOvk1lBA5TF2ucot+DDFmShQ92yBgYERVcgnd4kNcjYY
qvedHOb63HNHjTnKmpvBQa8CAwEAAQ==
-----END PUBLIC KEY-----
""",
"""
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAnockyS8M6oD7D3yjIUkY
qC11Aqqli0jUZfdm5P95xh1Tv4A05HNnwK7Bc8+w/r+/k+S2pcVLiNYJpAKuHnZA
g+Skp2tBjsODYS2mkvW2XsnPMPODd2ieaaMKdFx1D7vp4zu934K3m9pCJx6XIDWu
rlsu34yFLfN4wxWRFmy8mKhc5lroSwngfZZDBGuHa8wbTZ4aJ245nuUh8j/OIIVP
821U8xu2EWiWp2o89grh5goFWjROCZuWZn7tGqbfn+2hTXFYjBR86gVnrjWHaojZ
FOsfaS/gtM3N4tNOaUAaqTSHZkv8hbkYR4wibB1l6s94s1dp+E0+UAbUpGcCxuMg
kwuQstrRUs9UphqSyLk6C38huq/Mv1mE0HJqphoat4Vm+/baiBp7Vq3OMWJzbVdu
myPuFvB0iO+XybaFKngWxmxlB5IqzuO+D8oR11tASz71kWCIQprzNhk9OkcJfRht
cV7T5cDcbwkpgBUuZU8rlv64CBGWoLjRQfw2Ck/jFwmUJaZ9CYodJBNr/wSKYMz2
/bvWl4LEPkJ+oKNwHKDHlDcHyF8owG40Ue9bgySYqeZY3nNqtF3JXDd06q7AwvOp
q+kRu7fJjWtRIGeacTTcl9927y6Z7KhEnGKL8QcHnXvvkcmCSWFcxPh3nhCrwMDa
P/tslseWy16UP2WdPjJ0BEsCAwEAAQ==
-----END PUBLIC KEY-----
""",
"""
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAznKKdP07KDwvQyVZcX7E
wV08oKpSwu4HJWSXbbbZmiBbWdvCO7CX/CBRkXUi+10pax2rDnBIU3fKyiSKCsYn
d1Sy69/zlJ87UhEzwtdZy0DkbhEJCChsZgPXwhMCts7yKAjoWdEy84hiwu2iQ25m
oEjiQPROW9qVphuj/8tThKlJXvopam2HfiAySNB8qvJp+sVJbCd93AWab2JDRo/C
376Iqd8OxQiZz2XP0qkmTdvlm+lOvxIgDipnYO4IUYubwHVldqNHLasO4dkFC1Qk
HgwLFK3NgvcoZ4OELyHJMcp8+yK8E/Nqihk/mtYhmH3ywZDFRMUd8cqCiUTfCrle
sTdMAk8SFZuNVmdeJ9oMB2JVCurspYo1k1ycrt5zZzusiSIZQzAJ2F/Cl0ePjnmt
DxUphEvlNUBqg12Cm6gqMnwFiLF/lcZ1hfaNBiugoTqG8yKwjD/1w/Y485U6/b54
DyCd/8vje1w9QJzq2OXMTKPbazrP0eescBi1iJdHoyDElydeCv2YmFJRZANTcR91
Gv3uNy/L4xM8aFlO4qKMQRIJ8Ap3gw6fprOOGb6yo1Z+NqN8LWNBaPeidbct23qm
82p36TMBIPX3ji+H6U9vdrxBcyVT2O60BdB37KCjR8aqTYJxQhgBSWS083Sia/CE
b4I6n5WHI35bPFcdrtM2kyECAwEAAQ==
-----END PUBLIC KEY-----
""",
]
