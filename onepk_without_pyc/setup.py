#  * ------------------------------------------------------------------
#  * setup.py
#  * 
#  * Copyright (c) 2010-2014 by cisco Systems, Inc.
#  * All rights reserved.
#  * ------------------------------------------------------------------
#

from distutils.core import setup
from distutils.command.build_py import build_py as _build_py 
from glob import glob
import os, shutil, sys

# Extract the version from the PKG-INFO file
try:
    f = open('PKG-INFO')
    cfinfo = f.read()
    version = [cf for cf in cfinfo.splitlines() if cf.lstrip().startswith('Version')][0].split(':')[1]
    f.close()
except:
    version = '?.?.?'

class build_py_binary(_build_py):
    """Copy .pyc files in addition to .py"""
    
    def find_package_modules(self, package, package_dir):
        module_files  = glob(os.path.join(package_dir, "*.py"))
        module_files += glob(os.path.join(package_dir, "*.pyc"))
        setup_script = os.path.abspath(self.distribution.script_name)

        modules = []
        for f in module_files:
            abs_f = os.path.abspath(f)
            if abs_f != setup_script:
                module = os.path.splitext(os.path.basename(f))[0]
                modules.append((package, module, f))
            else:
                self.debug_print("excluding %s" % setup_script)
        return modules
        
    def get_module_outfile(self, build_dir, package, module):
        f = _build_py.get_module_outfile(self, build_dir, package, module)
        if not f.endswith('__init__.py'):
            if f.endswith('.py'):
                f += 'c'
        return f
        
    def byte_compile(self, files):
        path = files[0]
        path = path[:path.index('onep')]
        for path, subdir, files in os.walk(path):
            for name in files:
                if name.startswith('__init__'):
                    continue
                if name.endswith('.py'):
                    os.remove(os.path.join(path, name))

packages = []
for path, subdirs, files in os.walk('./onep'):
    if subdirs:
        p = path.lstrip('./')
        packages.append(p)
        for d in subdirs:
            if p:
                packages.append(p + '.' + d)
            else:
                packages.append(d)

setup(name='onep-python-sdk',
      version=version.strip(),
      author='Cisco Systems, Inc',
      author_email='onepk-feedback@cisco.com',
      description='Cisco onePK Python SDK',
      url='http://developer.cisco.com/web/onepk',
      license='Cisco onePK Software Development Kit License Agreement',
      long_description='Cisco onePK Python Software Development Kit',
      platforms = ["Any"],
      cmdclass={'build_py':build_py_binary},
      packages=packages,
      )

if __name__=='__main__':
    sys.argv.append("--no-compile")

