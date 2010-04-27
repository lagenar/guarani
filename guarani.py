from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import subprocess

USUARIO, CLAVE = ("usuario", "clave")
br = Browser()
br.open("https://guarani.exa.unicen.edu.ar/Guarani3w/")
br.open("https://guarani.exa.unicen.edu.ar/Guarani3w/includes/barra.inc.php")
br.follow_link(text_regex="Iniciar")
br.select_form(nr=0)
br["fUsuario"] = USUARIO
br["fClave"] = CLAVE
br.submit()
br.open("https://guarani.exa.unicen.edu.ar/Guarani3w/operaciones.php")
br.follow_link(url_regex="consultarActProvisoria")
r = br.response()
soup = BeautifulSoup(''.join(r.readlines()))
s_notas = soup.findAll('tr', {'class' : 'normal'})
notas = []
for s_nota in s_notas:
    materia, nota = [x.text for x in s_nota.findAll('td')[:2]]
    notas.append([materia, nota])

for nota in notas:
    if nota[1] != '':
        subprocess.Popen(['notify-send', '-t', '0', ' '.join(nota)])
