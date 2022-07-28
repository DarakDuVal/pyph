"""reference: page 20"""

import sys

print(sys.float_info)

print("max possible value: " + str(sys.float_info.max))
print("min possible value: " + str(sys.float_info.min))
print("min delta between decimals: " + str(sys.float_info.epsilon))
