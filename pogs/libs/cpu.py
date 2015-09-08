import os
from ctypes import CDLL, c_int, c_size_t, c_void_p
from pogs.types.low_level import c_int_p, c_float_p, c_double_p, settings_s_p, settings_d_p, solution_s_p, solution_d_p, info_s_p, info_d_p
from subprocess import check_output

ext = ".dylib" if os.uname()[0] == "Darwin" else ".so"
# this covers site-packages/<lib> (OSX) and dist-packages/<lib> (Linux)
lib = "packages/libpogs" + ext
lib_path=check_output(['locate', lib])

try:
	if lib_path[-1]=='\n': lib_path=lib_path[:-1]
	pogsCPU = CDLL(lib_path)

	#argument types
	pogsCPU.pogs_init_dense_single.argtypes = [c_int, c_size_t, c_size_t, c_float_p]
	pogsCPU.pogs_init_dense_double.argtypes = [c_int, c_size_t, c_size_t, c_double_p]
	pogsCPU.pogs_init_sparse_single.argtypes = [c_int, c_size_t, c_size_t, c_size_t, c_float_p, c_int_p, c_int_p]
	pogsCPU.pogs_init_sparse_double.argtypes = [c_int, c_size_t, c_size_t, c_size_t, c_double_p, c_int_p, c_int_p]
	pogsCPU.pogs_solve_single.argtypes = [c_void_p, settings_s_p, solution_s_p, info_s_p,
										c_float_p, c_float_p, c_float_p, c_float_p, c_float_p, c_int_p,
										c_float_p, c_float_p, c_float_p, c_float_p, c_float_p, c_int_p]
	pogsCPU.pogs_solve_double.argtypes = [c_void_p, settings_d_p, solution_d_p, info_d_p,
										c_double_p, c_double_p, c_double_p, c_double_p, c_double_p, c_int_p,
										c_double_p, c_double_p, c_double_p, c_double_p, c_double_p, c_int_p]
	pogsCPU.pogs_finish_single.argtypes = [c_void_p]
	pogsCPU.pogs_finish_double.argtypes = [c_void_p]



	#return types
	pogsCPU.pogs_init_dense_single.restype = c_void_p
	pogsCPU.pogs_init_dense_double.restype = c_void_p
	pogsCPU.pogs_init_sparse_single.restype = c_void_p
	pogsCPU.pogs_init_sparse_double.restype = c_void_p
	pogsCPU.pogs_solve_single.restype = c_int
	pogsCPU.pogs_solve_double.restype = c_int
	pogsCPU.pogs_finish_single.restype = None
	pogsCPU.pogs_finish_double.restype = None

	print '\nLoaded POGS CPU library'
except OSError:
	print '\nWarning: POGS CPU shared object (dynamic library) not found at ' + lib_path
	pogsCPU=None




