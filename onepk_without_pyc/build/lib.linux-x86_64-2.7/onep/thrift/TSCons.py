# 2015.02.05 17:20:16 IST
from os import path
from SCons.Builder import Builder

def scons_env(env, add = ''):
    opath = path.dirname(path.abspath('$TARGET'))
    lstr = 'thrift --gen cpp -o ' + opath + ' ' + add + ' $SOURCE'
    cppbuild = Builder(action=lstr)
    env.Append(BUILDERS={'ThriftCpp': cppbuild})



def gen_cpp(env, dir, file):
    scons_env(env)
    suffixes = ['_types.h', '_types.cpp']
    targets = map(lambda s: 'gen-cpp/' + file + s, suffixes)
    return env.ThriftCpp(targets, dir + file + '.thrift')



# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:16 IST
