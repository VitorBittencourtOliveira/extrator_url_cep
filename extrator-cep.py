endereco = "Rua Francisco Piffer, Lote N9A, Vale Verde, Valinhos, 13279-025"

import re # Regular Expression -- RegEx

# 5 dígitos = hífen (opcional) + 3 dígitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)