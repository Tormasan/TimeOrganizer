from cx_Freeze import setup, Executable

setup(name='TimeOrganizer',
      version='0.1',
      description='2hour alarm to do usefull stuff',
      executables= [Executable("timeOrganizer.py")]

      )