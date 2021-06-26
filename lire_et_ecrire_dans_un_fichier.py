#!/usr/bin/env python
# coding: utf-8

# # Fichiers .txt
# 
# Salut à tous! Je m'appelle Quentin et bienvenue dans mon cours “Comment lire et écrire un fichier .txt”.

# In[1]:


# Chemin de mon fichier texte.
txt_file_path = "F:/OctopusLab/dev/git/les_fichiers_avec_python/ressources/txt/Python_zen.txt"
out_txt_file = "F:/OctopusLab/dev/git/les_fichiers_avec_python/ressources/txt/outfile.txt"
mode_path = "F:/OctopusLab/dev/git/les_fichiers_avec_python/ressources/txt/opening_modes.txt"


# Nous allons voir comment ouvrir et fermer un fichier texte
# 
# - **open(file_path, mode)** : Ouvrir le fichier donné pour realiser une opération en fonction du mode.
# - **close()** : Fermer le fichier.

# In[2]:


# Ouverture en mode lecture et fermeture du fichier texte.
f = open(txt_file_path,'r')
f.close()


# Il existe une autre facon d'ouvrir et fermer un fichier.
# 
# - **with** : permet de fermer correctement et automatiquement le fichier même si une exception est levée. De plus c’est beaucoup plus court que d’utiliser l'équivalent avec try … finally
# 
# - **read()** : Lire le contenu du fichier et renvoie une string.

# In[3]:


# Ouverture et fermeture du fichier texte en utilisant with.
with open(mode_path) as f:
    # Stocker le texte du fichier dans une string.
    text = f.read()
    print(text)


# Il est possible d'ouvrir plusieurs fichiers en meme temps.
# Nous allons lire un fichier, puis ecrire son contenu dans un autre fichier.
# 
# - **write()** : Écrire dans le fichier.

# In[4]:


with open(out_txt_file, 'w') as dst_file_obj, open(txt_file_path, 'r') as src_file_obj:
    data = src_file_obj.read()
    dst_file_obj.write(data)


# Nous pouvons lire un fichier ligne par ligne.
# 
# - **readline()** : Lire une ligne du fichier.

# In[5]:


f = open(mode_path,'r')
# Afficher la premiere ligne du fichier.
print(f.readline())
# Afficher la ligne suivante du fichier.
print(f.readline())
f.close()


# Pour lire toutes les lignes d'un fichier.
# 
# - **readlines()** : Lire chaque ligne du fichier et renvoie un liste contenant les lignes.

# In[6]:


with open(txt_file_path) as f:
    # Stocker les lignes du fichier dans une liste.
    lines = f.readlines()
    print(lines)


# Il est possible de recuperer le contenu d'un fichier ligne par ligne en utilisant une boucle for.

# In[7]:


with open(txt_file_path) as f:
    for line in f:
        print(line.strip())


# Et pour terminer ce cours nous allons voir comment faire pour ecrire un fichier ligne par ligne.

# In[8]:


end_file = "F:/Workspaces/devenv/OctopusLab/end_file.txt"
with open(end_file, "w") as f:
    # Ecrire dans le fichier.
    f.write("Abonnez-vous :)\n")
    f.write("N'oubliez pas le pouce bleu et d'activer la cloche!\n")


# 
# 
# 
# # Fichiers .csv
# 
# Salut à tous! Je m'appelle Quentin et bienvenue dans mon cours “Comment lire et écrire un fichier .csv”.
# 
# - **import csv** : Importer la librairie CSV.

# In[9]:


import csv

sample_csv = "F:/OctopusLab/dev/git/les_fichiers_avec_python/ressources/csv/sample.csv"


# - **csv.reader()** : Lire les lignes du fichier CSV (list).

# In[10]:


# Ouvrir un fichier CSV et le lire ligne par ligne. 
with open(sample_csv,'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)


# - **csv.DictReader()** : Lire les lignes du fichier CSV (ordered dict).

# In[11]:


# Ouvrir un fichier CSV et le lire ligne par ligne avec DictReader. 
with open(sample_csv,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print("{first_name} {last_name} works "
              "in the {department} department "
              "at {city} office.".format(first_name=line["First name"],
                                        last_name=line["Last name"],
                                        department=line["Department"],
                                        city=line["Location"]))


# - **csv.writer()** : Utiliser une liste de string pour écrire la ligne.
# - **writerow()** : Écrire une ligne.

# In[12]:


employee_file = "F:/Workspaces/devenv/OctopusLab/employee_file.csv"

header = ['emp_name', 'dept', 'birth_month']

with open(employee_file, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(header)
    writer.writerow(['John Smith', 'Accounting', 'November'])
    writer.writerow(['Erica Meyers', 'IT', 'March'])


# - **writerows()** : Écrire plusieurs ligne en donnant une liste de dict.
# - **writeheader()** : Écrire le nom des champs des valeurs.
# - **csv.DictWriter()** : Utiliser un dict pour remplir les champs à écrire.

# In[13]:


employee_file = "F:/OctopusLab/dev/git/les_fichiers_avec_python/ressources/csv/employee_file2.csv"

persons=[{'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'}, 
         {'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'}]

with open(employee_file, mode='w', newline='') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(persons)


# In[14]:


with open(employee_file,'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)


# 
# 
# 
# # Fichiers .json
# 
# Salut à tous! Je m'appelle Quentin et bienvenue dans mon cours “Comment lire et écrire un fichier .json”.
# 
# - **import json** : Importer la librairie JSON.
# - **json.load()** : Lire un objet JSON et retourne un dict.

# In[15]:


import json
import pprint

read_json = "F:/OctopusLab/dev/git/les_fichiers_avec_python/ressources/json/sample.json"
write_json = "F:/OctopusLab/dev/git/les_fichiers_avec_python/ressources/json/sample2.json"


# In[16]:


# Lire un fichier JSON.
with open(read_json, "r") as json_file:
    data = json.load(json_file)
    print(type(data))
    pprint.pprint(data)


# - **json.dump()** : Créer un objet JSON à partir d'un dict.
# - **json.dumps()** : Convertir un objet Python en une string.

# In[17]:


data = {"Sugar": [{ "id": "5001", "type": "Glazed" },
                  { "id": "5002", "type": "Powdered Sugar" },
                  { "id": "5003", "type": "Sugar" }],
        "Chocolate": [{ "id": "5004", "type": "Chocolate with Sprinkles" },
                      { "id": "5005", "type": "Chocolate" }],
        "Sirop": [{ "id": "5006", "type": "Maple" }]
       }

# Ecrire un objet Python dans un fichier JSON.
with open(write_json, "w") as json_file:
    json.dump(data, json_file, indent = 4)
    
    
    json_string = json.dumps(data, sort_keys=True, separators=(',',':'), indent=4)
    print(type(json_string))
    print(json_string)


# - **json.loads()** : Lire un objet JSON et retourne un dict.
# 

# In[18]:


# Convertir une string en dict.
data = '{"console": "Playstation 5", "games": ["Spiderman", "FIFA", "NBA", "Gran Turismo", "Grand Theft Auto"]}'
data = json.loads(data)

print(type(data))
pprint.pprint(data)


# # Fichiers .yaml
# 
# Salut à tous! Je m'appelle Quentin et bienvenue dans mon cours “Comment lire et écrire un fichier .yaml”.

# - **import yaml** : Importer la librairie YAML.
# - **yaml.load()** : Lire un objet YAML et retourne un dict.

# In[19]:


import yaml

read_yaml = "F:/OctopusLab/dev/git/les_fichiers_avec_python/ressources/yml/sample.yaml"

with open(read_yaml, "r") as yaml_file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    fruits_dict = yaml.load(yaml_file, Loader=yaml.FullLoader)

    print(fruits_dict)


# - **yaml.full_load()** : Lire un objet YAML et retourne un dict.

# In[20]:


with open(read_yaml, "r") as yaml_file:
    document = yaml.full_load(yaml_file)

    for item, nb in document.items():
        print(item, ":", nb)
        
    print("-"*10) 
    
    data = yaml.dump(document, sort_keys=True)
    print(data)


# - **yaml.dump()** : Créer un objet YAML à partir d'une liste ou un dictionnaire.

# In[21]:


write_yaml = "F:/OctopusLab/dev/git/les_fichiers_avec_python/ressources/yml/output.yaml"

dict_file = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']},
{'countries' : ['Canada', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

with open(write_yaml, 'w') as yaml_file:
    yaml.dump(dict_file, yaml_file)

