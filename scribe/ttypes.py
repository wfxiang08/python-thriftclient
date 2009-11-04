#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.protocol.TProtocol import *
import fb303.ttypes


class ResultCode:
  OK = 0
  TRY_LATER = 1

class LogEntry:

  def __init__(self, d=None):
    self.category = None
    self.message = None
    if isinstance(d, dict):
      if 'category' in d:
        self.category = d['category']
      if 'message' in d:
        self.message = d['message']

  def read(self, iprot):
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.category = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    oprot.writeStructBegin('LogEntry')
    if self.category != None:
      oprot.writeFieldBegin('category', TType.STRING, 1)
      oprot.writeString(self.category)
      oprot.writeFieldEnd()
    if self.message != None:
      oprot.writeFieldBegin('message', TType.STRING, 2)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __str__(self): 
    return str(self.__dict__)

  def __repr__(self): 
    return repr(self.__dict__)

