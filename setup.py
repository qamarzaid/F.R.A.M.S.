import cx_Freeze
import sys
import os
base=None

if sys.platform=='win32':
    base='Win32GUI'

os.environ['TCL_LIBRARY']=r'C:\Users\zaid\AppData\Local\Programs\Python\Python310\tcl\tcl8.6'
os.environ['TK_LIBRARY']=r'C:\Users\zaid\AppData\Local\Programs\Python\Python310\tcl\tk8.6'

executables=[cx_Freeze.Executable('FRAMS.py',base=base,icon='fram_icon.ico')]

cx_Freeze.setup(
    name='F.R.A.M.S',
    options={'build_exe':{'packages':['tkinter','os'],'include_files':['fram_icon.ico','tcl86t.dll','tk86t.dll','tasveer','Student_DB.db','data','lbph_data.xml','haarcascade_frontalface_default.xml','Attendance Sheets']}},
    version='1.0',
    description='Face Recognition Attendance Management System',
    executables=executables
)




