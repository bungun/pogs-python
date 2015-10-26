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
	def __init__(self, length, double_precision=False,**kwargs):
		T = c_double if double_precision else c_float
		self.a = ones(length,T)
		self.b = zeros(length,T)
		self.c = ones(length,T)
		self.d = zeros(length,T)
		self.e = zeros(length,T)
		self.h = zeros(length, c_int)
		self.double_precision = double_precision

		# list of attributes and symbols
		attr_sym=[(self.a,'a'),
				  (self.b,'b'),
				  (self.c,'c'),
				  (self.d,'d'),
				  (self.e,'e'),
				  (self.h,'h')]

		# optional instantiation with keyword arguments
		for s in attr_sym:
			if s[1] in kwargs: 
				vals=kwargs[s[1]]
				# instatiation with a vector
				try:
					assert(len(vals)==length)
					s[0][:]=vals[:]
				# instantiation with a scalar (fill)
				except TypeError:
					s[0][:]=vals



	def length(self):
		return len(self.a)

	def copy(self, dest, source):
		dest.a[:]=source.a[:]
		dest.b[:]=source.b[:]
		dest.c[:]=source.c[:]
		dest.d[:]=source.d[:]
		dest.e[:]=source.e[:]
		dest.h[:]=source.h[:]		


	def copyfrom(self,f):
		self.copy(self,f)

	def copyto(self,f):
		self.copy(f,self)


	def to_double(self):
		if self.double_precision:
			return self
		else:
			f=FunctionVector(self.length(),double_precision=True)
			self.copyto(f)
			return f

	def to_single(self):
		if self.double_precision:
			FunctionVector(self.length())
			self.copyto(f)
			return f 
		else:
			return self

	def deepcopy(self, double_precision=None):
		if double_precision is None:
			double_precision = self.double_precision
		if double_precision:
			return self.to_double()
		else:
			return self.to_single()

