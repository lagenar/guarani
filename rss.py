# -*- coding: latin-1 -*-
from guarani import Guarani
import config

g = Guarani(config.usuario, config.clave)
notas = g.getNotasFinales()

DOC = '''<?xml version="1.0"?>
<rss version="2.0">
   <channel>
      <title>Notas Guaraní</title>
      %(items)s
   </channel>
</rss>
'''

ITEM = '''<item>
    <title>%(materia)s: %(nota)s</title>
    <description>%(materia)s: %(nota)s</description>
</item>
'''

items = ''
for nota in notas:
    items += ITEM % {'materia' : nota[0], 'nota' : nota[1]}

print DOC % {'items' : items}
