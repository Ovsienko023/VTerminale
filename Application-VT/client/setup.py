from cx_Freeze import setup, Executable



setup(name='client',
      options={'build.exe':{'packages': ['requests']}},
      executables = [Executable('client.py')]

)