import mypackage.module1
import mypackage.module2
mypackage.module1.greet('Alibaba')
mypackage.module2.depart('Alibaba')

import mypackage.module1 as m1
import mypackage.module2 as m2
m1.greet('Alibaba')
m2.depart('Alibaba')

from mypackage.module1 import greet as g
from mypackage.module2 import depart as d
g('Alibaba')
d('Alibaba')
