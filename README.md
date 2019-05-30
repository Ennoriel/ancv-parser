# ANCV data parser

## Principe

Le site guide.ancv.com n'étant pas optimisé pour la recherche, ce petit script permet d'extraire les données du site de manière semi-automatisée pour importer les données dans un map Google.

L'API du site permet de :
  * récupérer les identifiants et position des lieux d'une part ;
  * récupérer les informations des lieux à partir de leur identifiant d'autre part.

Seule la deuxième partie est automatisée.

Résultat consultable sur cette [carte](https://drive.google.com/open?id=1qgsPg5uSUMEzHDfm8JM4jRhSFHO0f7tf&usp=sharing).

## Fonctionnement

Réaliser une recherche sur le site guide.ancv.com et sauvegarder un fichier json (volet dev de Mozilla / Chrome) obtenue à l'url https://guide.ancv.com/arcgis/search/ajax?<...>&page=1 au nom de ancv.json.

Placer le fichier à côté du script.

Exécuter le script.

Un fichier ancv_out.csv sera automatiquement créé et pourra directement être importé sur un map Google.

## Amélioration

Récupération automatique des données depuis https://guide.ancv.com/arcgis/search/ajax?<...>&page=1 au nom de ancv.json.
