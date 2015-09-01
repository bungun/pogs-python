from ctypes import c_int, c_float, c_double
from numpy import zeros, ones

class Solution(object):
	def __init__(self,double_precision,m,n):
		T = c_double if double_precision else c_float
		self.double_precision = double_precision
		self.x=zeros(n,dtype=T)
		self.y=zeros(m,dtype=T)
		self.mu=zeros(n,dtype=T)
		self.nu=zeros(m,dtype=T)


class FunctionVector(object):
	def __init__(self, length, double_precision=False):
		T = c_double if double_precision else c_float
		self.a = ones(length,T)
		self.b = zeros(length,T)
		self.c = ones(length,T)
		self.d = zeros(length,T)
		self.e = zeros(length,T)
		self.h = zeros(length, c_int)
		self.double_precision = double_precision

	def length(self):
		return len(self.a)

	def copyfrom(self,f):
		self.a[:]=f.a[:]
		self.b[:]=f.b[:]
		self.c[:]=f.c[:]
		self.d[:]=f.d[:]
		self.e[:]=f.e[:]
		self.h[:]=f.h[:]

	def copyto(self,f):
		f.a[:]=self.a[:]
		f.b[:]=self.b[:]
		f.c[:]=self.c[:]
		f.d[:]=self.d[:]
		f.e[:]=self.e[:]
		f.h[:]=self.h[:]


	def to_double(self):
		if self.double_precision:
			return self
		else:
			f=FunctionVector(self.length(),double_precision=True)
			self.copyto(f)
			return f

	def to_float(self):
		if self.double_precision:
			f=FunctionVector(self.length())
			self.copyto(f)
			return f 
		else:
			return self

