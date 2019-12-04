# Projet sur Arduino : développement d'un Cookie Clicker physique

Inputs :
  * Bouton
  * Potentiomètre pour la sélection des upgrades

Serveur web :
  * En python avec flask (cf. [le  jukebox](https://github.com/matthias4217/jukebox-ultra-nrv)
  * Get avec paramètre pour envoyer un clic, style localhost:8082/?clic=1
  * Affiche la page web en réponse plus envoie un JSON avec la réponse (si jamais on voulait faire deux interfaces)

## Install & Run

Pour le serveur web :

  1. Editer le fichier `config.py`
  2. Se placer dans le dossier internet-server
  2. `pip install -r requirements.txt`, dans un virtual environment ou pas, au choix
  3. `python3 run.py`

Normalement c'est bon !
