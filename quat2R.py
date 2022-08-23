import sys
import numpy as np
from scipy.spatial.transform import Rotation as R
r = R.from_quat([float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])])
print(r.as_matrix())
