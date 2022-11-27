from travel import thailand
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from travel import * #__init__ 필수
trip_to = thailand.ThailandPackage()
trip_to.detail()




import inspect
import random
print(inspect.getfile(random)) #random 위치출력
print(inspect.getfile(thailand))