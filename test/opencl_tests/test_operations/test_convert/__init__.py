#!/usr/bin/env python3

import numpy as np
import pyopencl as cl
from pyopencl import cltypes

from opencl import Mem, run_kernel


def run(ctx, src):
    n = 64
    #b = np.arange(4*n, dtype=cltypes.float)/(2*n**0.5)
    b = np.arange(4*n, dtype=cltypes.uint) - (4*n)//2
    a = np.zeros(4*n, dtype=cltypes.int)
    run_kernel(ctx, src, (n,), *[Mem(x) for x in [a, b]])
    #print(a, b)
    return (a, b)
