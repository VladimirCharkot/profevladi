from pizza import Pizza
from horno import Horno
from persona import Persona
from pizzeria import Pizzeria

muzza = Pizza(['muzzarela'])
napo = Pizza(['muzzarela', 'tomate', 'ajo'])
cebolla = Pizza(['muzzarela' , 'cebolla'])
jamon = Pizza(['muzzarela', 'jamón'])

muzza.status()

napo.status()

horno = Horno(4)
horno.meter(muzza)
horno.meter(napo)
horno.meter(jamon)
horno.meter(cebolla)
horno.cocinar()
cena = horno.sacar_todo()
print(cena)

jorge = Persona("Jorge", 3500)
ana = Persona("Ana", 4000)

jorge.comer()

hornito = Horno(4)
Arizzepi = Pizzeria("Arizzepi", hornito)

jorge.entrar(Arizzepi)
ana.entrar(Arizzepi)

Arizzepi.atender([muzza, napo, cebolla, jamon])
jorge.comer()

Arizzepi.atender([muzza, napo, cebolla, jamon])
ana.comer()