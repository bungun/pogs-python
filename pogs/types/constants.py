from ctypes import c_int



# POGS constants
ORD = {}
ORD["COL_MAJ"]=c_int(0)
ORD["ROW_MAJ"]=c_int(1)

FUNCTION={}
FUNCTION["ABS"]=c_int(0)
FUNCTION["EXP"]=c_int(1)
FUNCTION["HUBER"]=c_int(2)
FUNCTION["IDENTITY"]=c_int(3)
FUNCTION["INDBOX01"]=c_int(4)
FUNCTION["INDEQ0"]=c_int(5)
FUNCTION["INDGE0"]=c_int(6)
FUNCTION["INDLE0"]=c_int(7)
FUNCTION["LOGISTIC"]=c_int(8)
FUNCTION["MAXNEG0"]=c_int(9)
FUNCTION["MAXPOS0"]=c_int(10)
FUNCTION["NEGENTR"]=c_int(11)
FUNCTION["NEGLOG"]=c_int(12)
FUNCTION["RECIPR"]=c_int(13)
FUNCTION["SQUARE"]=c_int(14)
FUNCTION["ZERO"]=c_int(15)

STATUS={}
STATUS[0]='POGS_SUCCESS'
STATUS[1]='POGS_INFEASIBLE'
STATUS[2]='POGS_UNBOUNDED'
STATUS[3]='POGS_MAX_ITER'
STATUS[4]='POGS_NAN_FOUND'
STATUS[5]='POGS_ERROR'

# Default POGS solver settings
DEFAULTS={}
DEFAULTS['rho']=1. # rho = 1.0
DEFAULTS['abs_tol']=1e-4 # abs_tol = 1e-4
DEFAULTS['rel_tol']=1e-4 # rel_tol = 1e-4
DEFAULTS['max_iters']=2500 # max_iters = 2500
DEFAULTS['verbose']=2 # verbose = 2
DEFAULTS['adaptive_rho']=1 # adaptive_rho = True
DEFAULTS['gap_stop']=0 # gap_stop = false
DEFAULTS['warm_start']=	0 # warm_start = False