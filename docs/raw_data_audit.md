# Audit des données brutes - Migration camerounaise 2015-2024

Date de l'audit : 2026-04-21

## Objectif analytique

Analyser l'évolution de la migration camerounaise sur 2015-2024, avec trois périodes comparables :

- Pré-Covid : 2015-2019
- Covid : 2020-2021
- Post-Covid : 2022-2024

Les données disponibles ne sont pas complètes pour toutes les périodes.
Il faudra donc mener des analyses adaptées : certaines par année, d'autres à des moments précis, et d'autres de manière partielle selon les sources.

## Synthèse exécutive

Les sources les plus solides pour l'analyse 2015-2024 sont :

- Eurostat : très bonne source pour l'Europe (2015-2024), surtout sur les permis, les résidents de longue durée, les acquisitions de nationalité et les changements de statut.
- UN DESA : très utile pour les données mondiales, mais seulement à certaines années précises (2015, 2020, 2024).
- Canada IRCC : données très riches (2015-2026), mais les fichiers sont complexes et demandent beaucoup de nettoyage.
- USA DHS / réfugiés : utile pour les États-Unis, mais les données sur les résidents permanents vont jusqu'à 2022, alors que celles sur les réfugiés couvrent 2015-2024.
- OCDE : bon complément pour plusieurs pays, mais les données s'arrêtent à 2022 et les fichiers sont volumineux.

Les sources à utiliser avec prudence :

- UNHCR : les fichiers locaux s'arrêtent surtout en 2016 ou 2017 ; ils ne permettent pas l'analyse Covid/post-Covid sans mise à jour.
- Japon : les visas Cameroun couvrent seulement 2009-2017 ; les fichiers inbound/outbound s'arrêtent en 2005.
- StatCan recensement : exploitable comme point de contexte 2021, pas comme série annuelle.
- Contexte démographique : utile pour normaliser ou contextualiser, mais pas pour mesurer les flux migratoires 2015-2024.

## Inventaire et diagnostic par source

- UN DESA
  - Fichier : `data/raw/global/undesa_cameroon_global_destination.csv`
  - Couverture : 1990-2024 (points disponibles : 2015, 2020, 2024)
  - Statut : prioritaire pour les destinations mondiales, mais non annuel
  - Nettoyage :
    - Filtrer `Origin == Cameroon`
    - Convertir les nombres qui contiennent des espaces
    - Garder `Total`, `Male`, `Female`
    - Supprimer les agrégats selon l'analyse

- Eurostat - Permis
  - Fichier : `data/raw/europe/eurostat_first_permits_cameroon.xlsx`
  - Couverture : 2015-2024
  - Statut : prioritaire pour les motifs d'entrée en Europe
  - Nettoyage :
    - Extraire les feuilles 1 à 4
    - Supprimer les métadonnées
    - Transformer le format large en format long
    - Gérer les flags (`:`, `b`, `e`, `p`)

- Eurostat - Résidents de longue durée
  - Fichier : `data/raw/europe/eurostat_long_term_residents_cameroon.xlsx`
  - Couverture : 2015-2024
  - Statut : prioritaire pour les trajectoires après l'arrivée
  - Nettoyage :
    - Extraire les données par cadre légal
    - Structurer en format long avec pays, année et cadre

- Eurostat - Changements de statut
  - Fichier : `data/raw/europe/eurostat_status_changes_cameroon.xlsx`
  - Couverture : 2020-2024
  - Statut : utile pour la période Covid / post-Covid
  - Nettoyage :
    - Gérer les nombreuses feuilles âge/sexe
    - Commencer avec les agrégats totaux

- Eurostat - Acquisition de nationalité
  - Fichier : `data/raw/europe/eurostat_citizenship_acquisition_cameroon.xlsx`
  - Couverture : 2015-2024
  - Statut : prioritaire pour l'intégration / naturalisation
  - Nettoyage :
    - Filtrer `Age = Total` et `Sex = Total`
    - Réduire le nombre de feuilles utilisées

- Canada IRCC
  - Fichier : `data/raw/canada/ircc_*.xlsx`
  - Couverture : 2015-2026
  - Statut : prioritaire pour le Canada
  - Nettoyage :
    - Gérer les en-têtes multi-lignes
    - Traiter les données mensuelles/trimestrielles
    - Remplacer les valeurs `--`
    - Limiter l'analyse à 2015-2024

- StatCan
  - Fichier : `data/raw/canada/statcan_cameroon_immigrant_status.csv`
  - Couverture : recensement 2021
  - Statut : contexte ponctuel
  - Nettoyage :
    - Ignorer les métadonnées initiales
    - Lire à partir de l'en-tête principal

- USA - LPR
  - Fichier : `data/raw/usa/usa_lawful_permanent_residents_cameroon.xlsx`
  - Couverture : 2013-2022
  - Statut : utilisable jusqu'en 2022 (2023-2024 manquent)
  - Nettoyage :
    - Extraire `Table 3d`
    - Filtrer Cameroun
    - Utiliser les années fiscales

- USA - Réfugiés
  - Fichier : `data/raw/usa/usa_refugee_arrivals_cameroon.xlsx`
  - Couverture : 2015-2024
  - Statut : utile pour les réfugiés
  - Nettoyage :
    - Extraire `Table 14`
    - Filtrer la ligne Cameroun
    - Harmoniser les années fiscales

- USA - ACS
  - Fichier : `data/raw/usa/usa_acs_selected_population_cameroon.xlsx`
  - Couverture : 2024
  - Statut : contexte ponctuel sur la diaspora
  - Nettoyage :
    - Extraire la feuille `Data`
    - Conserver l'estimation et la marge d'erreur

- OCDE
  - Fichier : `data/raw/global/oecd_migration_database_raw.csv`
  - Couverture : 1995-2022 (Cameroun : 2015-2022)
  - Statut : complément OCDE
  - Nettoyage :
    - Filtrer `CO2 == CMR`
    - Sélectionner les variables pertinentes
    - Faire attention aux doubles comptages

- UNHCR
  - Fichier : `data/raw/unhcr/*.csv`
  - Couverture : jusqu'à environ 2016/2017
  - Statut : insuffisant pour la période récente
  - Nettoyage :
    - Mettre à jour si l'axe réfugiés/asile devient prioritaire

- Japon
  - Fichier : `data/raw/japan/*.csv`
  - Couverture : 2009-2017 pour les visas, plus ancien pour les autres fichiers
  - Statut : faible pertinence pour 2015-2024
  - Nettoyage :
    - Gérer l'encodage CP932 / Shift-JIS
    - Noter que les données récentes manquent

- Chypre
  - Fichier : `data/raw/europe/cyprus_migration_foreign_born_population.xls`
  - Couverture : à confirmer
  - Statut : faible priorité
  - Nettoyage :
    - Convertir le fichier `.xls` avec LibreOffice / xlrd si nécessaire

- Contexte Cameroun
  - Fichier : `data/raw/context/*.csv`
  - Couverture : variable, souvent jusqu'en 2017
  - Statut : contexte uniquement
  - Nettoyage :
    - Corriger les lignes vides
    - Transformer le format large en format long

## Détails importants par thème analytique

### 1. Évolution des destinations

Source principale : UN DESA.

Le fichier contient 736 lignes pour `Origin == Cameroon`, 92 destinations/agrégats et les années 1990, 1995, 2000, 2005, 2010, 2015, 2020 et 2024. Pour la fenêtre d'étude, il ne donne donc que trois observations : 2015, 2020 et 2024.

Implication analytique : on peut comparer les stocks pré-Covid, au moment Covid et post-Covid, mais pas produire une évolution annuelle complète. Pour une analyse annuelle, il faut compléter avec Eurostat, Canada, USA et OCDE.

### 2. Raisons d'entrée

Source principale : Eurostat premiers permis.

Le fichier `eurostat_first_permits_cameroon.xlsx` est très propre conceptuellement : 4 feuilles correspondent aux raisons familiales, éducationnelles, professionnelles et autres. Les données commencent autour de la ligne `TIME`, avec les pays en lignes et les années 2015-2024 en colonnes. Les colonnes de flags alternent avec les valeurs.

Source complémentaire : Canada IRCC.

Les fichiers IRCC donnent les admissions permanentes par catégorie, les permis d'études et les transitions du permis temporaire vers la résidence permanente. Ils sont riches, mais plus complexes que les fichiers Eurostat : en-têtes sur plusieurs lignes, mois, trimestres, catégories hiérarchiques et valeurs `--`.

### 3. Trajectoires après l'arrivée

Sources principales :

- Eurostat résidents de longue durée : 2015-2024.
- Eurostat acquisition de nationalité : 2015-2024.
- Eurostat changements de statut : 2020-2024.
- Canada `temp_to_pr` : 2015-2026, à limiter à 2015-2024.
- USA LPR : 2015-2022 seulement dans le fichier actuel.

Implication analytique : l'Europe et le Canada permettent une lecture plus complète des trajectoires après l'arrivée. Les États-Unis demandent une mise à jour 2023-2024 si on veut une série complète.

## Problèmes de qualité et risques

1. Couverture temporelle incomplète.
   Plusieurs fichiers ne couvrent pas 2023-2024 ou s'arrêtent avant Covid. Il faut éviter d'interpréter une baisse comme un phénomène migratoire si elle vient d'une source arrêtée.

2. Différence entre flux et stocks.
   UN DESA mesure des stocks de migrants ; Eurostat, IRCC et DHS mesurent souvent des flux administratifs ou des statuts. Il ne faut pas les additionner directement.

3. Années calendaires vs années fiscales.
   Les fichiers USA DHS sont en années fiscales. Ils doivent être marqués comme tels dans les données nettoyées.

4. Formats larges et métadonnées.
   Beaucoup de fichiers Excel contiennent des lignes de titre, des notes, plusieurs feuilles et des flags. Le nettoyage doit extraire explicitement les zones tabulaires.

5. Valeurs spéciales.
   Eurostat utilise `:` pour les valeurs indisponibles et des flags comme `b`, `e`, `p`. Canada utilise `--` pour des petites valeurs ou suppressions. USA utilise parfois `D` pour suppression.

6. Encodage.
   `data/raw/japan/japan_translation_mapping.csv` apparaît en mojibake s'il est lu en UTF-8 ; utiliser CP932/Shift-JIS.

7. Fichiers temporaires.
   `data/raw/.~lock.MIG_01032024110110429.csv#` est un fichier de verrouillage temporaire et doit être ignoré.

## Recommandations de nettoyage

### Modèle commun recommandé

Créer une table analytique longue avec les colonnes suivantes :

- `source`
- `dataset`
- `indicator`
- `origin_country`
- `destination_country`
- `destination_region`
- `year`
- `period` avec les valeurs `pre_covid`, `covid`, `post_covid`
- `measure_type` avec des valeurs comme `stock`, `flow`, `permit`, `status_change`, `naturalisation`, `refugee_arrival`
- `reason` si disponible
- `sex` si disponible
- `age_group` si disponible
- `value`
- `unit`
- `flag`
- `year_type` avec les valeurs `calendar` ou `fiscal`
- `notes`

### Règles de période

- 2015-2019 : `pre_covid`
- 2020-2021 : `covid`
- 2022-2024 : `post_covid`

### Ordre de priorité pour le pipeline

1. Nettoyer Eurostat first permits, long-term residents et citizenship acquisition.
2. Nettoyer UN DESA destinations Cameroun.
3. Nettoyer Canada IRCC admissions, study permits et temp-to-PR.
4. Nettoyer USA refugees et LPR.
5. Ajouter le filtre Cameroun dans l'OCDE pour compléter les destinations OCDE jusqu'à 2022.
6. Garder UNHCR/Japon/contexte comme annexes ou mettre à jour les sources avant l'analyse principale.

## Actions conseillées avant l'analyse

- Installer les dépendances du projet (`pandas`, `openpyxl`) avant d'écrire les notebooks/pipelines.
- Ajouter `xlrd` seulement si le fichier `.xls` Chypre doit être exploité.
- Ajouter une règle d'exclusion pour `.~lock*` dans le chargement des fichiers raw.
- Documenter pour chaque table nettoyée si l'année est calendaire ou fiscale.
- Produire un rapport de couverture par source avec les années 2015-2024 manquantes.
- Ne pas interpoler UN DESA entre 2015, 2020 et 2024 pour l'analyse principale ; si une interpolation est faite, la marquer comme estimation.
