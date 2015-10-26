from ctypes import c_float, c_double, POINTER
from pogs.types.constants import DEFAULTS
from pogs.types.low_level import SettingsS, SettingsD, InfoS, InfoD, SolutionS, SolutionD
from numpy import inf 

def cptr(np_arr,dtype=c_float):
	return np_arr.ctypes.data_as(POINTER(dtype))

def change_settings(settings, **kwargs):
	
	# all settings (except warm_start) are persistent and change only if called
	if 'rho' in kwargs: settings.rho=kwargs['rho']
	if 'abs_tol' in kwargs: settings.abs_tol=kwargs['abs_tol']
	if 'rel_tol' in kwargs: settings.rel_tol=kwargs['rel_tol']
	if 'max_iters' in kwargs: settings.max_iters=kwargs['max_iters']
	if 'verbose' in kwargs: settings.verbose=kwargs['verbose']
	if 'adaptive_rho' in kwargs: settings.adaptive_rho=kwargs['adaptive_rho']
	if 'gap_stop' in kwargs: settings.gap_stop=kwargs['gap_stop']
	
	# warm_start must be specified each time it is desired
	if 'warm_start' in kwargs: 
		settings.warm_start=kwargs['warm_start']
	else:
		settings.warm_start=0


def make_settings(double_precision=False, **kwargs):
	rho = kwargs['rho'] if 'rho' in kwargs.keys() else DEFAULTS['rho'] 
	relt = kwargs['abs_tol'] if 'abs_tol' in kwargs.keys() else DEFAULTS['abs_tol'] 
	abst = kwargs['rel_tol'] if 'rel_tol' in kwargs.keys() else DEFAULTS['rel_tol'] 
	maxit = kwargs['max_iters'] if 'max_iters' in kwargs.keys() else DEFAULTS['max_iters'] 
	verb = kwargs['verbose'] if 'verbose' in kwargs.keys() else DEFAULTS['verbose'] 
	adap = kwargs['adaptive_rho'] if 'adaptive_rho' in kwargs.keys() else DEFAULTS['adaptive_rho'] 
	gaps = kwargs['gap_stop'] if 'gap_stop' in kwargs.keys() else DEFAULTS['gap_stop']
	warm = kwargs['warm_start'] if 'warm_start' in kwargs.keys() else DEFAULTS['warm_start']
	if double_precision:
		return SettingsD(rho, relt, abst, maxit, verb, adap, gaps, warm)
	else:
		return SettingsS(rho, relt, abst, maxit, verb, adap, gaps, warm)

def change_solution(pysolution, **kwargs):
	try:
		if 'x_init' in kwargs: pysolution.x[:] = kwargs['x_init'][:]
		if 'nu_init' in kwargs: pysolution.nu[:] = kwargs['nu_init'][:]
	except:
		#TODO: message about vector lengths? 
		raise

def make_solution(pysolution):
	if pysolution.double_precision:
		return SolutionD(cptr(pysolution.x,c_double),cptr(pysolution.y,c_double),
							cptr(pysolution.mu,c_double),cptr(pysolution.nu,c_double))
	else:
		return SolutionS(cptr(pysolution.x,c_float),cptr(pysolution.y,c_float),
		 					cptr(pysolution.mu,c_float),cptr(pysolution.nu,c_float))

		
def make_info(double_precision):
	if double_precision:
		return InfoD(0,0,inf,0,0)
	else:
		return InfoS(0,0,inf,0,0)
