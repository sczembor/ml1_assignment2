# -*- coding: utf-8 -*-
"""
Created on Wed May 12 18:19:52 2021

@author: kubam
"""
import statistics as s


print("labAA1:")
phase1=[127,75,139, 131,117]
phase2=[151,179,175,169,169]
phase3=[81, 175, 179,181,183]
phase4=[183,181,181,183,181]
print(s.mean(phase1))
print(s.mean(phase2))
print(s.mean(phase3))
print(s.mean(phase4))

print()
print("labAA2:")
phase12=[263, 303, 353, 273, 231]
phase22=[335,357,357,359,359]
phase32=[371,373,373,363,371]
phase42=[383,381,383,383,383]
print(s.mean(phase12))
print(s.mean(phase22))
print(s.mean(phase32))
print(s.mean(phase42))

print()
print("labAA3:")
phase13=[-517, 420, 180, 418, -463]
phase23=[-3014, -1009, -1012, -853] #dnf,dnf, dnf, dnf
phase33=[0]
phase43=[0]
print(s.mean(phase13))
print(s.mean(phase23))
print(s.mean(phase33))
print(s.mean(phase43))

print()
print("labAA4:")
phase14=[-645, 451, 413, 539, 309 ] #0 no dots left, 1 2 dots left, 2 2 dots left, 3 0dl, 4 0dl
phase24=[431,605,551, -49, 511] #0dl, 0dl, 0dl, 0dl, 0dl
phase34=[ 0]
phase44=[0]
print(s.mean(phase14))
print(s.mean(phase24))
print(s.mean(phase34))
print(s.mean(phase44))

print()
print("labAA5:")
phase15=[116,-166,-318,578, 852] #0dl, 0dl, 1 dl, 3dl, 0dl
phase25=[ 722,524, 514, 422,704] #4dl, 5dl, 4dl, 5dl, 0dl
phase35=[268, 700,224, 124,292 ]
phase45=[0]
print(s.mean(phase15))
print(s.mean(phase25))
print(s.mean(phase35))
print(s.mean(phase45))