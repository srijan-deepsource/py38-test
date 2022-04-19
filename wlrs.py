import os
import pdb
from pdb import set_trace


a = [1, 2, 3, 4]
if (n := len(a)) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")

    
pdb.set_trace()
set_trace()
breakpoint()
