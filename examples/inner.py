import numpy as np

from parla.array import copy
from parla.cuda import gpu
from parla.cpu import cpu
from parla.ldevice import LDeviceSequenceBlocked
from parla.tasks import *
import time
import os

def main():
    n = 3*100000000
    a = np.random.rand(n)
    b = np.random.rand(n)

    divisions = 100

    start = time.perf_counter()
    # Map the divisions onto actual hardware locations
    devs = list(gpu.devices) + list(cpu.devices)
    if "N_DEVICES" in os.environ:
        devs = devs[:int(os.environ.get("N_DEVICES"))]
    mapper = LDeviceSequenceBlocked(divisions, devices=devs)

    a_part = mapper.partition_tensor(a)
    b_part = mapper.partition_tensor(b)

    inner_result = np.empty(1)

    @spawn(placement=cpu(0))
    async def inner_part():
        partial_sums = np.empty(divisions)
        async with finish():
            for i in range(divisions):
                @spawn(placement=mapper.device(i))
                def inner_local():
                    copy(partial_sums[i:i+1], a_part[i] @ b_part[i])
        res = 0.
        for i in range(divisions):
            res += partial_sums[i]
        inner_result[0] = res

    end = time.perf_counter()
    print(end - start)

    assert np.allclose(np.inner(a, b), inner_result[0])


if __name__ == '__main__':
    main()
