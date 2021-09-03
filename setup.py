from cx_Freeze import setup, Executable
import sys
import configparser


#############################################################################
########################### IMPORT CONFIG FILE ##############################
config = configparser.RawConfigParser() 
config.read('setup.cfg')


# parse data config file for Include_files
a_dict_includes_files = dict(config.items('include_files'))
array_include_files = []
for value in a_dict_includes_files.values():
    key_config_file_include_files = value
    array_include_files.append(key_config_file_include_files)


# parse data config file for Packages
a_dict_packages = dict(config.items('packages'))
array_packages = []
for value in a_dict_packages.values():
    key_config_file_packages = value
    array_packages.append(key_config_file_packages)


# parse data config file for Include_modules
a_dict_include = dict(config.items('includes'))
array_includes = []
for value in a_dict_include.values():
    key_config_includes = value
    array_includes.append(key_config_includes)


# parse data config file for Exclude_modules
a_dict_exclude = dict(config.items('excludes'))
array_exclude_packages = []
for value in a_dict_exclude.values():
    key_config_exclude_module = value
    array_exclude_packages.append(key_config_exclude_module)


#############################################################################
############################## OS CONTROL ###################################
base = None
if sys.platform == "win32":
    base = 'Win32Service'


# construction du dictionnaire des options
options = {
        'build_exe': {
            'includes': array_includes,
            'packages': array_packages,
            'excludes' : array_exclude_packages,
           }
        }


#############################################################################
############################ Creation du Setup ##############################
executables = [
    Executable('config.py', base=base, targetName='NAME_SERVICE.exe')
]

setup(name='NAME SERVICE',
      version='1.00',
      description='DESCRIPTION',
      executables=executables,
      options=options
      )

