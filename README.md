# Headers_Check
<img src="https://i.imgur.com/LDRmfNM.png" width="480px" height="338px">
Script automatizado para verificar si un sitio web posee las cabeceras de seguridad.
***
# INSTALACIÓN

Clonamos el repositorio con GIT CLONE:
``` bash
git clone https://github.com/Pindinga1/Headers_Check.git
```

Ingresamos al repositorio:
```bash
cd Headers_Check
```

Instalamos los requerimientos:
``` bash
sudo pip install -r requirements.txt
```

# USO
Tiene dos modos de operación, uno donde seguirá las redirecciones y otro donde no las seguirá:

Sin redirección:
``` bash
python3 headers.py https://github.com/ false
```

Con redirección
``` bash
python3 headers.py https://github.com/ true
```