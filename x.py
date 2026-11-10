#!/usr/bin/python3

import math
import numpy as np
import sys

W =  70.0
L = 120.0

#              .
#             . .
#         a  . Q .  a    height of triangle with angle Q = 90 is a / sqrt(2.0)
#           .     .
#          .       .
#         ...sr2*a...
#     h   .         .  h
#         .         .
#         ...........

#  sr2 = sqrt(2.0)
#  area of square     = h * sr2 * a
#  area of triangle   = 0.5 * sr2 * a * a / sr2
#  volume of square   = L * area of square
#  volume of triangle = L * 0.50 * a * a

#  2 * a + 2 * h + sqrt(2.0) * a = 70
#  a (1 + sqrt(2.0) / 2) + h = 35
#  h = 35 - a * 1.0 + sqrt(2.0) / 2.0)

def xh(a):
   return (35.0 - a * (1.0 + 0.50 * np.sqrt(2.0)))

da = 0.010
a  = da

fo = open('out','w')
hdr = '#'+' ' * 10+'a'+' ' * 13+'h'+' ' * 15+'vol'+' ' * 12 \
      +'sum_sid'+' ' * 9+'angle'+' ' * 10+'sqrt(2.0)*a'
fo.write('%s\n' % (hdr))

mv = 0.0
while (a < W):
   h = xh(a)

   if (h < 0.0):
      break

   vp  = a*a / 2.0 * np.sqrt(2.0) * a * h * L
   vr  = np.sqrt(2.0) * a * h * L
   v   = vp + vr

#  check sum of sides
   sm  = 2.0 * a + 2.0 * h + np.sqrt(2.0) * a

#  check angle

   th  = np.arccos((a/np.sqrt(2.0)) / a) * 180.0 / np.pi

#  keep up with max

   if (v >= mv):
      mv = v
      hm = h
      am = a
   fo.write('%15.5f %15.5f %15.5f %15.5f %15.5f %15.5f\n' % (a,h,v,sm,th,np.sqrt(2.0)*a))
   
   a = a + da

fo.close()

fo = open('max','w')
hdr = '#'+' ' * 9+'a'+' ' * 15+'h'+' ' * 10+'vol'
fo.write('%s\n' % (hdr))
fo.write('%15.5f %15.5f %15.5f\n' % (am,hm,mv))
fo.close()
