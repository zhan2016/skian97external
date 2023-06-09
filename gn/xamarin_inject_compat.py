#!/usr/bin/env python

import os
import sys

root = sys.argv[1]

files = [
    "third_party/externals/dng_sdk/source/dng_string.cpp",
    "third_party/externals/dng_sdk/source/dng_utils.cpp",
    "third_party/externals/dng_sdk/source/dng_pthread.cpp",
    "third_party/externals/zlib/deflate.c",
    "third_party/externals/libpng/pngpriv.h",
    "third_party/externals/libjpeg-turbo/simd/jsimd_x86_64.c",
    "third_party/externals/libjpeg-turbo/simd/jsimd_i386.c",
    "third_party/externals/libjpeg-turbo/simd/jsimd_arm.c",
    "third_party/externals/libjpeg-turbo/simd/jsimd_arm64.c",
]

for f in files:
    af = os.path.join(root, f)
    # some targets don't have all the dependencies
    if not os.path.isfile(af):
        continue
    # read the file
    with open(af, 'r') as original:
        data = original.read()
    # create the include
    slashes = "../" * f.count('/')
    inc = '#include "' + slashes + 'include/xamarin/WinRTCompat.h"'
    # write it to the file
    if not data.startswith(inc):
        with open(af, 'w') as modified:
            modified.write(inc + '\n' + data)
