from services.helper import helper

helper()
from services.routing.routing import Routing
from services.mapping.mapping import Mapping
r = Routing()
m = Mapping()
result1 = r.create(1, "meisam", 27)
result2 = m.test()
final = {}
final.update(result1)
final.update(result2)

print(final)
