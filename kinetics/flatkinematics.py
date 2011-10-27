import math

from numpy import *
from transformations import *

def T2R(a):
  if a.shape[0] == 3:
    return a
  else:
    return a[:3,:3] 

def inv(a):
  if a.shape[0] == 3:
    return a.T
  else:
    R = T2R(a).T
    return vstack((hstack((R,-dot(R,a[:3,3]))),matrix([[0,0,0,1]])))


def NotImplemented(*args,**kwargs):
  raise Exception("Not implemented in kinetics.flatkinematics")

Tquat  = full   = TfullR = fullR =  NotImplemented
