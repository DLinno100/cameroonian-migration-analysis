# Audit des donnees brutes - Migration camerounaise 2015-2024

Date de l'audit: 2026-04-21

## Objectif analytique

Analyser l'évolution de la migration camerounaise sur 2015-2024, avec trois periodes comparables:

- Pré-Covid: 2015-2019
- Covid: 2020-2021
- Post-Covid: 2022-2024

Les données disponibles ne sont pas complètes pour toutes les périodes.
Il faudra donc faire des analyses différentes : certaines par année, d’autres à des moments précis, et d’autres partielles selon les sources.

## Synthèse executif

Les sources les plus solides pour l'analyse 2015-2024 sont:

- Eurostat : très bonne source pour l’Europe (2015–2024), surtout sur les permis, les résidents longue durée, les nationalités et les changements de statut.
- UN DESA : très utile pour les données mondiales, mais seulement à certaines années (2015, 2020, 2024).
- Canada IRCC : données très riches (2015–2026), mais les fichiers sont complexes et demandent beaucoup de nettoyage.
- USA DHS / réfugiés : utile pour les États-Unis, mais les données sur les résidents permanents vont jusqu’à 2022, alors que celles sur les réfugiés couvrent 2015–2024.
- OECD : bon complément pour plusieurs pays, mais s’arrête à 2022 et les fichiers sont volumineux.

Les sources à utiliser avec prudence:

- UNHCR: les fichiers locaux s'arretent surtout en 2016 ou 2017; ils ne permettent pas l'analyse Covid/post-Covid sans mise à jour.
- Japon: les visas Cameroun couvrent seulement 2009-2017; les fichiers inbound/outbound s'arrêtent en 2005.
- StatCan recensement: exploitable comme point de contexte 2021, pas comme serie annuelle.
- Contexte demographique: utile pour normaliser ou contextualiser, mais pas pour mesurer les flux migratoires 2015-2024.

## Inventaire et diagnostic par source

- UN DESA
   - Fichier : data/raw/global/undesa_cameroon_global_destination.csv
   - Couverture : 1990–2024 (points disponibles : 2015, 2020, 2024)
   - Statut : prioritaire pour les destinations mondiales (non annuel)
   - Nettoyage :
      - Filtrer Origin == Cameroon
      - Convertir les nombres (espaces)
      - Garder Total, Male, Female
      - Supprimer les agrégats selon l’analyse

- Eurostat – Permis
   - Fichier : data/raw/europe/eurostat_first_permits_cameroon.xlsx
   - Couverture : 2015–2024
   - Statut : prioritaire pour les motifs d’entrée en Europe
   - Nettoyage :
      - Extraire feuilles 1–4
      - Supprimer les métadonnées
      - Transformer wide → long
      - Gérer les flags (:, b, e, p)

- Eurostat – Résidents longue durée
   - Fichier : data/raw/europe/eurostat_long_term_residents_cameroon.xlsx
   - Couverture : 2015–2024
   - Statut : prioritaire pour les trajectoires post-arrivée
   - Nettoyage :
      - Extraire par cadre légal
      - Structurer en format long (pays–année–cadre)

- Eurostat – Changements de statut
   - Fichier : data/raw/europe/eurostat_status_changes_cameroon.xlsx
   - Couverture : 2020–2024
   - Statut : utile pour la période Covid / post-Covid
   - Nettoyage :
      - Nombreuses feuilles (âge/sexe)
      - Commencer avec agrégats totaux

- Eurostat – Acquisition de nationalité
   - Fichier : data/raw/europe/eurostat_citizenship_acquisition_cameroon.xlsx
   - Couverture : 2015–2024
   - Statut : prioritaire pour l’intégration / naturalisation
   - Nettoyage :
      - Filtrer Age = Total, Sex = Total
      - Réduire le nombre de feuilles

- Canada IRCC
   - Fichier : data/raw/canada/ircc_*.xlsx
   - Couverture : 2015–2026
   - Statut : prioritaire pour le Canada
   - Nettoyage :
      - Gérer les en-têtes multi-lignes
      - Traiter les données mensuelles/trimestrielles
      - Remplacer --
      - Limiter à 2015–2024

- StatCan
   - Fichier : data/raw/canada/statcan_cameroon_immigrant_status.csv
   - Couverture : recensement 2021
   - Statut : contexte ponctuel
   - Nettoyage :
      - Ignorer les métadonnées initiales
      - Lire à partir de l’en-tête principal

- USA – LPR
   - Fichier : data/raw/usa/usa_lawful_permanent_residents_cameroon.xlsx
   - Couverture : 2013–2022
   - Statut : utilisable jusqu’en 2022 (manque 2023–2024)
   - Nettoyage :
      - Extraire Table 3d
      - Filtrer Cameroun
      - Utiliser les années fiscales

- USA – Réfugiés
   - Fichier : data/raw/usa/usa_refugee_arrivals_cameroon.xlsx
   - Couverture : 2015–2024
   - Statut : utile pour les réfugiés
   - Nettoyage :
      - Extraire Table 14
      - Filtrer ligne Cameroun
      - Années fiscales

- USA – ACS
   - Fichier : data/raw/usa/usa_acs_selected_population_cameroon.xlsx
   - Couverture : 2024
   - Statut : contexte ponctuel diaspora
   - Nettoyage :
      - Extraire feuille Data
      - Conserver estimation + marge d’erreur

- OECD
   - Fichier : data/raw/global/oecd_migration_database_raw.csv
   - Couverture : 1995–2022 (Cameroun : 2015–2022)
   - Statut : complément OCDE
   - Nettoyage :
      - Filtrer CO2 == CMR
      - Sélectionner variables pertinentes
      - Attention aux doubles comptages

- UNHCR
   - Fichier : data/raw/unhcr/*.csv
   - Couverture : jusqu’à ~2016/2017
   - Statut : insuffisant pour période récente
   - Nettoyage :
      - À mettre à jour si axe réfugiés/asile

- Japon
   - Fichier : data/raw/japan/*.csv
   - Couverture : 2009–2017 (visas), plus ancien pour autres
   - Statut : faible pertinence pour 2015–2024
   - Nettoyage :
      - Gérer encodage (CP932 / Shift-JIS)
      - Données récentes manquantes

- Chypre
   - Fichier : data/raw/europe/cyprus_migration_foreign_born_population.xls
   - Couverture : à confirmer
   - Statut : faible priorité
   - Nettoyage :
      - Conversion .xls (LibreOffice / xlrd)

- Contexte Cameroun
   - Fichier : data/raw/context/*.csv
   - Couverture : variable (souvent ≤ 2017)
   - Statut : contexte uniquement
   - Nettoyage :
      - Corriger lignes vides
      - Transformer wide → long

## Détails importants par thème analytique

### 1. Evolution des destinations

Source principale: UN DESA.

Le fichier contient 736 lignes pour `Origin == Cameroon`, 92 destinations/agrégats et les années 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2024. Pour la fenêtre d'étude, il ne donne donc que trois observations: 2015, 2020 et 2024.

Implication analytique: on peut comparer les stocks pré-Covid, au moment Covid et post-Covid, mais pas produire une evolution annuelle complète. Pour une analyse annuelle, compléter avec Eurostat, Canada, USA et OECD.

### 2. Raisons d'entrée

Source principale: Eurostat premiers permis.

Le fichier `eurostat_first_permits_cameroon.xlsx` est très propre conceptuellement: 4 feuilles correspondent aux raisons familiales, educationnelles, professionnelles et autres. Les données commencent autour de la ligne `TIME`, avec les pays en lignes et les années 2015-2024 en colonnes. Les colonnes de flags alternent avec les valeurs.

Source complementaire: Canada IRCC.

Les fichiers IRCC donnent admissions permanentes par catégorie, permis d'études et transitions permis temporaire vers résidence permanente. Ils sont riches, mais plus complexes que les fichiers Eurostat: en-tetes sur plusieurs lignes, mois, trimestres, categories hierarchiques et valeurs `--`.

### 3. Trajectoires post-arrivee

Sources principales:

- Eurostat résidents longue durée: 2015-2024.
- Eurostat acquisition de nationalite: 2015-2024.
- Eurostat changements de statut: 2020-2024.
- Canada `temp_to_pr`: 2015-2026, à limiter à 2015-2024.
- USA LPR: 2015-2022 seulement dans le fichier actuel.

Implication analytique: l'Europe et le Canada permettent une lecture plus complète du post-arrivée; les Etats-Unis demandent une mise à jour 2023-2024 si on veut une série complète.

## Problèmes de qualité et risques

1. Couverture temporelle incomplète.
   Plusieurs fichiers ne couvrent pas 2023-2024 ou s'arrêtent avant Covid. Il faut éviter d'interpréter une baisse comme un phénomene migratoire si elle vient d'une source arrétée.

2. Différence flux vs stocks.
   UN DESA mésure des stocks de migrants; Eurostat/IRCC/DHS mésurent souvent des flux administratifs ou statuts. Il ne faut pas les additionner directement.

3. Années calendaires vs fiscal years.
   Les fichiers USA DHS sont en fiscal years. Ils doivent être marqués comme tels dans les données nettoyées.

4. Formats larges et métadata.
   Beaucoup de fichiers Excel contiennent des lignes de titre, notes, feuilles multiples et flags. Le nettoyage doit extraire explicitement les zones tabulaires.

5. Valeurs spéciales.
   Eurostat utilise `:` pour indisponible et des flags comme `b`, `e`, `p`. Canada utilise `--` pour des petites valeurs ou suppressions. USA utilise parfois `D` pour suppression.

6. Encodage.
   `data/raw/japan/japan_translation_mapping.csv` apparait en mojibake si lu en UTF-8; utiliser CP932/Shift-JIS.

7. Fichiers temporaires.
   `data/raw/.~lock.MIG_01032024110110429.csv#` est un fichier de verrouillage temporaire et doit etre ignore.

## Recommandations de nettoyage

### Modele commun recommande

Creer une table analytique longue avec les colonnes suivantes:

- `source`
- `dataset`
- `indicator`
- `origin_country`
- `destination_country`
- `destination_region`
- `year`
- `period` avec valeurs `pre_covid`, `covid`, `post_covid`
- `measure_type` avec valeurs comme `stock`, `flow`, `permit`, `status_change`, `naturalisation`, `refugee_arrival`
- `reason` si disponible
- `sex` si disponible
- `age_group` si disponible
- `value`
- `unit`
- `flag`
- `year_type` avec valeurs `calendar` ou `fiscal`
- `notes`

### Règles de période

- 2015-2019: `pre_covid`
- 2020-2021: `covid`
- 2022-2024: `post_covid`

### Ordre de priorite pour le pipeline

1. Nettoyer Eurostat first permits, long-term residents, citizenship acquisition.
2. Nettoyer UN DESA destinations Cameroun.
3. Nettoyer Canada IRCC admissions, study permits, temp-to-PR.
4. Nettoyer USA refugees et LPR.
5. Ajouter OECD filtre Cameroun pour completer les destinations OCDE jusqu'a 2022.
6. Garder UNHCR/Japon/contexte comme annexes ou mettre a jour les sources avant analyse principale.

## Actions conseillées avant l'analyse

- Installer les dépendances du projet (`pandas`, `openpyxl`) avant d'écrire les notebooks/pipelines.
- Ajouter `xlrd` seulement si le fichier `.xls` Chypre doit etre exploite.
- Ajouter une regle d'exclusion pour `.~lock*` dans le chargement des fichiers raw.
- Documenter pour chaque table nettoyée si l'année est calendaire ou fiscale.
- Produire un rapport de couverture par source avec les années 2015-2024 manquantes.
- Ne pas interpoler UN DESA entre 2015, 2020 et 2024 pour l'analyse principale; si une interpolation est faite, la marquer comme estimation.

