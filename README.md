# Network Wizard

NetworkWizard est une application Python pour aider les administrateurs réseau à configurer les switchs et routeurs de différentes marques, notamment Cisco, HP et Huawei.

# Comment installer
1. Téléchargez et installez Python 3.8 ou une version ultérieure.
2. Téléchargez ou clonez le code source du projet depuis GitHub.
3. Ouvrez un terminal et accédez au répertoire du projet.

# Comment utiliser
## Bash
Il suffi exécuter le script pour génère fichier .txt qui contient les commande a copier coller dans la console de configuration de votre switch.

(Ce fichier sera contenu dans le dossier arubaConfigGenerator répéter exécution génèrera un nouveau fichier )

```bash
wget https://raw.githubusercontent.com/medaey/NetworkWizard/main/network_wizard.sh
chmod +x network_wizard.sh
./network_wizard.sh HP-2530
```


## Python
1. Modifier le code python de `network_wizard.py` pour appeler les fonctions.
- Par exemple pour obtenir les commandes pour configurer une route static :

```python
	# Genere un script de config cisco de config cisco pour une route statique
	route.route_static (
		reseauDest = "172.16.4.0",
	 	reseauDestCIDR = "/22",
		ipNextRouter = "192.168.0.1"
	)
```
2. Exécutez le fichier principal `python network_wizard.py`.
3. Copier la configurations générées dans le terminal d'éxécution pour une utilisation ultérieure.
```
enable
configure terminal
ip route 172.16.4.0 255.255.252.0 192.168.0.1
end
```

# Contribuer
Si vous souhaitez contribuer à ce projet, veuillez suivre les étapes suivantes :

1. Forker le projet.
2. Créez une nouvelle branche pour vos modifications : `git checkout -b feature/your-feature-name`.
3. Faites vos modifications et testez-les localement.
4. Soumettez une pull request en expliquant vos modifications et les raisons de celles-ci.

# Auteur
- Cossu Médéric mederic@cossu.tech

# Licence
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus d'informations.
