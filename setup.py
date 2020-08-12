from distutils.core import setup
import py2exe

from distutils.filelist import findall
import os
import matplotlib
matplotlibdatadir = matplotlib.get_data_path()
matplotlibdata = findall(matplotlibdatadir)



setup(
    console=['DET14.py'],
    options={
             'py2exe': {
                    'packages' : ['matplotlib', 'pytz','easygui',\
                                  'statsmodels','pandas','patsy'],
                    'dll_excludes':['MSVCP90.DLL',
                                    'libgdk-win32-2.0-0.dll',
                                    'libgobject-2.0-0.dll',
                                    'libgdk_pixbuf-2.0-0.dll'],
                    'includes':['scipy.sparse.csgraph._validation',
                        'scipy.special._ufuncs_cxx']
                   }
        },
    data_files=matplotlib.get_py2exe_datafiles()
)
share  improve this answer  follow 