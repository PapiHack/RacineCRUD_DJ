# RacineCRUD_DJ
## Installation des dépendances  
Vous pouvez utilisé un virtual environment comme `venv` ou `virtualenv`  
Ces dépendances se situent dans le fichier `requirements.txt`  
`pip install -r requirements.txt`  
## Puis appliquez les migrations
Par défaut, `sqlite` est utilisé comme SGBD  
`python manage.py makemigrations`  
`python manage.py migrate`
