## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Déploiement

### Configuration de la pipeline CI/CD

#### DockerHub

- Créer un compte <a href="https://hub.docker.com/" target="_blank">Dockerhub</a>
- Créer un nouveau repository depuis votre dashboard


#### Circleci

- Créer un compte <a href="https://circleci.com/" target="_blank">Circleci</a>
- Configurer votre projet sur Circleci en suivant <a href="https://circleci.com/docs/getting-started/" target="_blank">cette documentation</a>

#### Heroku

- Créer un compte <a href="https://dashboard.heroku.com/apps" target="_blank">Heroku</a>
- Créer une nouvelle application
- Récupérer la clé API que vous trouverez dans "account settings > API Key"

#### Sentry

- Créer un compte <a href="https://sentry.io" target="_blank">Sentry</a>
- Créer un nouveau projet Django, et récupérer la variable **dsn** indiqué
![sentry.png](..%2F..%2F..%2F..%2FDownloads%2Fsentry.png)

### Variables d'environnements

Afin que toutes ces applications communiquent entre elles correctement, 
il faut y indiquer des variables d'environnement.

**Par exemple:**  
La variable `DH_username` qu'il faut renseigner dans **CircleCI**, permet à l'application **CircleCi**
d'authentifier votre compte **DockerHub**, puis d'envoyer l'image **docker** du projet sur votre repo **DockerHub**.

#### V-E CircleCI

Une fois configuré, aller dans le menu : organization settings ->Contexts -> Create Context  
- Nommer ce context **OCP13_context**  

Ajouter les variables d'environement dans ce context

- DH_username : Votre nom d'utilisateur DockerHub
- DH_password : Votre mot de passe DockerHub
- DH_repo : Le nom du repo DockerHub créé précédemment
- DNS : la clé dns récupéré précédement sur Sentry
- HEROKU_API_KEY : la clé API Heroku récupéré precedement
- HEROKU_APP_NAME : le nom de votre app Heroku

#### V-E Heroku

Ajouter les variables d'environement dans votre projet > settings > config vars

- ENV : "PRODUCTION"
- SECRET_KEY : secret_key Django
- DNS : la clé dns récupéré précédement sur Sentry

### Déploiement de l'application


