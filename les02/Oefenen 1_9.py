import math

lengte = 12

hoekInGraden = 0

hoekInRadialen = (math.pi * hoekInGraden) / 180

hoogte = lengte * math.sin(hoekInRadialen)

print(hoogte)

import math

lengte = 10

hoekInGraden = 75

#eerst hoek omrekenen naar radialen
hoekInRadialen = (math.pi * hoekInGraden) / 180

hoogte = lengte * math.sin(hoekInRadialen)

print(hoogte)

import math

lengte = 18
hoekInGraden = 45

#eerst hoek omkeren naar radialen
hoogteInRadialen = (math.pi * hoekInGraden) / 180

hoogte = lengte*math.sin(hoekInRadialen)

print(hoogte)

