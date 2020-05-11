from cx_Freeze import setup, Executable

exe=Executable(
     script="client.py",
     )
includefiles=["config.txt"]
includes=[]
excludes=[]
packages=['requests']
setup(

     version = "1.1",
     description = "No Description",
     author = "Name",
     name = "App name",
     options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
     executables = [exe]
     )











# from cx_Freeze import setup, Executable



# setup(name='client',
#       version='1.1',
#       options={'build.exe':{'packages': ['requests'], 
#                             'include_files': ['config.txt'],}},
#       executables = [Executable('client.py')]

# )

# options = {
#     'build_exe': {
#         'include_msvcr': True,
#       #   'excludes': excludes,
#         'includes': includes,
#         'zip_include_packages': zip_include_packages,
#         'build_exe': 'build_windows',
#         'include_files': include_files,
#     }
# }