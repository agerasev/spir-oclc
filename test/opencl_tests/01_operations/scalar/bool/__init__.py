#!/usr/bin/env python3

import numpy as np
import pyopencl as cl
from pyopencl import cltypes

from opencl import Mem, run_kernel


def run(ctx, src):
    n = 64
    a = np.arange(n, dtype=cltypes.uchar) % 2
    b = (np.arange(n, dtype=cltypes.uchar) + 1) % 2
    c = (np.arange(n, dtype=cltypes.uchar)//2) % 2
    buf = [a, b, c]
    
    for i in range(23):
        buf.append(np.zeros(n, dtype=cltypes.uchar))
    
    for i in range(18):
        buf.append(np.clip(np.arange(n, dtype=cltypes.uchar) % 3, 0, 1))

    run_kernel(ctx, src, (n,), *[Mem(x) for x in buf])

    #buf = [b & 1 for b in buf]
    return buf
