#!/usr/bin/env python3
import os
import sys 


script = sys.argv[1]

cmd = f"docker run -it --rm -v $(pwd):$(pwd) -w $(pwd) web3py python3 {script}"

print(f"{cmd}")
os.system(cmd)
