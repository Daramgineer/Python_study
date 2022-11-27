import theater_module
theater_module.price(3) #일반 3명
theater_module.price_morning(4) #조조4명
theater_module.price_soldier(2) #군인2명

import theater_module as movie
movie.price(3)
movie.price_morning(4)
movie.price_soldier(2)

from theater_module import *
price(3)
price_morning(4)
price_soldier(2)

from theater_module import price, price_morning
price(3)
price_morning(4)
