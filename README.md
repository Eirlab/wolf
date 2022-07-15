# Wolf 🐺

Le projet Wolf est une application Flask permettant de faire le lien entre les adhérents d'EirLab Community et Dolibarr

Le projet comporte actuellement les fonctionnalités suivantes :

1. Onglet Adhérents
    - Obtenir la fiche d'un adhérent à partir de sa carte étudiante ou autre
    - Lier le profil d'un adhérent à partir de sa carte étudiante ou autre, son nom et prénom
2. Onglet Formations
    - Donner de nouvelles formations aux adhérents

## Installation

Pour installer le projet il est nécessaire d'avoir un environnement python3 avec Flaks installé. Il suffit ensuite de
lancer le projet avec la commande :

Pour une installation sur un PC, il faut déployer et activer `wolf.service`. Il faut copier le fichier
das `/etc/systemd/system/` puis lancer la commande `systemctl enable wolf.service`. Le service ce lancera alors
automatiquement, si il meurt il sera aussi relancé automatiquement.

```python
python3
run_api.py
```

Le site sera accessible sur `http://localhost:5000/`. ou `http://<ip_adress>:5000`.

