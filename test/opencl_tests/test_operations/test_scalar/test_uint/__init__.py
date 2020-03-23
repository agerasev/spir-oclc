#!/usr/bin/env python3

import numpy as np
import pyopencl as cl
from pyopencl import cltypes

from opencl import Mem, run_kernel


def run(ctx, src):
    n = 256
    a = (np.arange(n, dtype=cltypes.uint) % 13)
    b = (np.arange(n, dtype=cltypes.uint) % 17)
    c = (np.arange(n, dtype=cltypes.uint) % 5)
    buf = [a, b, c]
    
    for i in range(23):
        buf.append(np.zeros(n, dtype=cltypes.int))
    
    for i in range(18):
        buf.append((np.arange(n, dtype=cltypes.int) % 7))

    run_kernel(ctx, src, (n,), *[Mem(x) for x in buf])
    return buf
