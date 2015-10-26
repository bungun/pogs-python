from ctypes import c_int, c_uint, c_float, c_double, POINTER, Structure

# pointers to C types
c_int_p = POINTER(c_int)
c_float_p = POINTER(c_float)
c_double_p = POINTER(c_double)

# POGS types
class SettingsS(Structure):
	_fields_ = [('rho', c_float), 
				('abs_tol', c_float), 
				('rel_tol', c_float),
				('max_iters', c_uint), 
				('verbose', c_uint), 
				('adaptive_rho', c_int), 
				('gap_stop', c_int),
				('warm_start', c_int)]

class SettingsD(Structure):
	_fields_ = [('rho', c_double), 
				('abs_tol', c_double), 
				('rel_tol', c_double),
				('max_iters', c_uint), 
				('verbose', c_uint), 
				('adaptive_rho', c_int), 
				('gap_stop', c_int),
				('warm_start', c_int)]

class InfoS(Structure):
	_fields_ = [('iter', c_uint), 
				('status', c_int), 
				('obj',c_float), 
				('rho',c_float),
				('solvetime',c_float)]

class InfoD(Structure):
	_fields_ = [('iter', c_uint), 
				('status', c_int), 
				('obj',c_double), 
				('rho',c_double),
				('solvetime',c_float)]


class SolutionS(Structure):
	_fields_ = [('x', c_float_p), 
				('y', c_float_p), 
				('mu', c_float_p), 
				('nu', c_float_p)]

class SolutionD(Structure):
	_fields_ = [('x', c_double_p), 
				('y',c_double_p), 
				('mu',c_double_p), 
				('nu',c_double_p)]

# pointers to POGS types
settings_s_p = POINTER(SettingsS)
settings_d_p = POINTER(SettingsD)
info_s_p = POINTER(InfoS)
info_d_p = POINTER(InfoD)
solution_s_p = POINTER(SolutionS)
solution_d_p = POINTER(SolutionD)