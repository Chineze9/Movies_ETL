# This file is generated by numpy's setup.py
# It contains system_info results at the time of building this package.
__all__ = ["get_info","show"]



import os
import sys

extra_dll_dir = os.path.join(os.path.dirname(__file__), '.libs')

if sys.platform == 'win32' and os.path.isdir(extra_dll_dir):
    os.environ.setdefault('PATH', '')
    os.environ['PATH'] += os.pathsep + extra_dll_dir

lapack_mkl_info={'libraries': ['mkl_rt', 'pthread'], 'library_dirs': ['/opt/concourse/worker/volumes/live/4eabb14c-0fb3-4254-5fd3-317c14f470de/volume/scipy_1630606815835/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold/lib'], 'define_macros': [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)], 'include_dirs': ['/opt/concourse/worker/volumes/live/4eabb14c-0fb3-4254-5fd3-317c14f470de/volume/scipy_1630606815835/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold/include']}
lapack_opt_info={'libraries': ['mkl_rt', 'pthread'], 'library_dirs': ['/opt/concourse/worker/volumes/live/4eabb14c-0fb3-4254-5fd3-317c14f470de/volume/scipy_1630606815835/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold/lib'], 'define_macros': [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)], 'include_dirs': ['/opt/concourse/worker/volumes/live/4eabb14c-0fb3-4254-5fd3-317c14f470de/volume/scipy_1630606815835/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold/include']}
blas_mkl_info={'libraries': ['mkl_rt', 'pthread'], 'library_dirs': ['/opt/concourse/worker/volumes/live/4eabb14c-0fb3-4254-5fd3-317c14f470de/volume/scipy_1630606815835/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold/lib'], 'define_macros': [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)], 'include_dirs': ['/opt/concourse/worker/volumes/live/4eabb14c-0fb3-4254-5fd3-317c14f470de/volume/scipy_1630606815835/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold/include']}
blas_opt_info={'libraries': ['mkl_rt', 'pthread'], 'library_dirs': ['/opt/concourse/worker/volumes/live/4eabb14c-0fb3-4254-5fd3-317c14f470de/volume/scipy_1630606815835/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold/lib'], 'define_macros': [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)], 'include_dirs': ['/opt/concourse/worker/volumes/live/4eabb14c-0fb3-4254-5fd3-317c14f470de/volume/scipy_1630606815835/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold/include']}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + "_info", {}))

def show():
    for name,info_dict in globals().items():
        if name[0] == "_" or type(info_dict) is not type({}): continue
        print(name + ":")
        if not info_dict:
            print("  NOT AVAILABLE")
        for k,v in info_dict.items():
            v = str(v)
            if k == "sources" and len(v) > 200:
                v = v[:60] + " ...\n... " + v[-60:]
            print("    %s = %s" % (k,v))
    