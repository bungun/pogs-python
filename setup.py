
import os
from sys import platform
from setuptools import setup
from setuptools.command.install import install
from distutils.command.build import build
from subprocess import call
from multiprocessing import cpu_count

BASEPATH = os.path.dirname(os.path.abspath(__file__))
POGSPATH = os.path.join(BASEPATH, '_POGS')
POGSLIBPATH = os.path.join(POGSPATH, 'src/interface_c/')
LONG_DESC='`pogs` provides a Python interface for Chris Fougner and \
Stephen Boyd\'s CPU- and GPU-compatible convex solver library POGS \
(please see the http://github.com/foges/pogs for details)'

class PogsBuild(build):
  def run(self):
    NVCC = os.popen("which nvcc").read()!=""
    CPULIB='libpogs'
    GPULIB='pypogs_gpu'
    EXT=".dylib" if os.uname()[0] == "Darwin" else ".so"

    # run original build code
    build.run(self)

    # build POGS
    # (0) make sure pogs library is in correct state
    # call('git submodule update --init --recursive', cwd=POGSPATH)

    # (1) prepare Make operation
    cmd = [ 'make' ]

    # set Make target to cpu + gpu or cpu only, depending on whether nvcc is exists in environment    
    targets= [ CPULIB, GPULIB ] if NVCC else [ CPULIB ]
    cmd.extend(targets)

    message = 'Compiling POGS---CPU and GPU' if NVCC else 'Compiling POGS---CPU only'
 
    # (2) run Make 
    def compile():
      call(cmd, cwd=POGSLIBPATH)

    self.execute(compile, [], message)

    # (3) get Make output
    # form absolute paths to pogs shared libraries
    CPU_LIBPATH = os.path.join(POGSLIBPATH, CPULIB + EXT)
    GPU_LIBPATH = os.path.join(POGSLIBPATH, GPULIB + EXT)

    # set target files (Make output) to cpu + gpu or cpu only
    target_files = [ CPU_LIBPATH, GPU_LIBPATH ] if NVCC else [ CPU_LIBPATH ]


    # copy resulting tool to library build folder
    self.mkpath(self.build_lib)
    for target in target_files:
          self.copy_file(target, self.build_lib)


class PogsInstall(install):
    def initialize_options(self):
        install.initialize_options(self)
        self.build_scripts = None

    def finalize_options(self):
        install.finalize_options(self)
        self.set_undefined_options('build', ('build_scripts', 'build_scripts'))

    def run(self):
        # run original install code
        install.run(self)

        # install POGS executables
        self.copy_tree(self.build_lib, self.install_lib)

setup(
    name='pogs',
    version='0.0.1',
    author='Baris Ungun',
    author_email='fougner@stanford.edu, ungun@stanford.edu, boyd@stanford.edu',
    url='http://github.com/bungun/pogs-python/',
    package_dir={'pogs-python': 'pogs'},
    packages=['pogs', 
              'pogs.types',
              'pogs.libs',
              'pogs.solvers'],
    license='GPLv3',
    zip_safe=False,
    description='Python Interface for POGS (Proximal Operator Graph Solver)',
    long_description=LONG_DESC,
    install_requires=["numpy >= 1.8",
                      "scipy >= 0.13"],
    cmdclass={'build' : PogsBuild, 'install' : PogsInstall}
)
