from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import subprocess

class Guarani(object):
    def __init__(self, user, passwd):
        self.br = Browser()
        self.user = user
        self.passwd = passwd
        self._login()

    def _login(self):
        self.br.open("https://guarani.exa.unicen.edu.ar/Guarani3w/")
        self.br.open("https://guarani.exa.unicen.edu.ar/Guarani3w/includes/barra.inc.php")
        self.br.follow_link(text_regex="Iniciar")
        self.br.select_form(nr=0)
        self.br["fUsuario"] = self.user
        self.br["fClave"] = self.passwd
        self.br.submit()

    def _parseNotas(self, html):
        soup = BeautifulSoup(html)
        s_notas = soup.findAll('tr', {'class' : 'normal'})
        notas = []
        for s_nota in s_notas:
            materia, nota = [x.text for x in s_nota.findAll('td')[:2]]
            if nota != '':
                notas.append([materia, nota])
        return notas
    
    def getNotasFinales(self):
        self.br.open("https://guarani.exa.unicen.edu.ar/Guarani3w/operaciones.php")
        self.br.follow_link(url_regex="consultarActProvisoria")
        return self._parseNotas(self.br.response().read())

if __name__ == "__main__":
    import config
    g = Guarani(config.usuario, config.clave)
    notas = g.getNotasFinales()
    for nota in notas:
        subprocess.Popen(['notify-send', '-t', '0', ' '.join(nota)])
