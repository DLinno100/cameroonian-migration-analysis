# Catalogue des données

Voir aussi : [raw_data_audit.md](raw_data_audit.md)

## Jeux de données principaux

### UN DESA

- Rôle : destinations mondiales des migrants camerounais
- Couverture : 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2024
- Utilisation principale : Q1
- Fichier brut : `data/raw/global/undesa_cameroon_global_destinations.csv`
- Note de nettoyage : filtrer `Origin == Cameroon` ; utiliser 2015, 2020 et 2024 pour la période d'étude.

### Eurostat migr_resfirst

- Rôle : premiers permis par raison pour les citoyens camerounais en Europe
- Couverture : 2015-2024
- Utilisation principale : Q2
- Fichier brut : `data/raw/europe/eurostat_first_permits_cameroon.xlsx`
- Note de nettoyage : une feuille par raison ; transformer les colonnes d'années au format long et conserver les flags Eurostat.

### Eurostat migr_reslong

- Rôle : résidents de longue durée
- Couverture : 2015-2024
- Utilisation principale : Q3
- Fichier brut : `data/raw/europe/eurostat_long_term_residents_cameroon.xlsx`
- Note de nettoyage : une feuille par cadre juridique ; commencer par le cadre total.

### Eurostat migr_acq

- Rôle : acquisition de citoyenneté / naturalisation
- Couverture : 2015-2024
- Utilisation principale : Q3
- Fichier brut : `data/raw/europe/eurostat_citizenship_acquisition_cameroon.xlsx`
- Note de nettoyage : nombreuses feuilles âge/sexe ; commencer par âge total et sexe total.

### Eurostat migr_reschst

- Rôle : changements de statut d'immigration
- Couverture : 2020-2024
- Utilisation principale : Q3, Covid et post-Covid uniquement
- Fichier brut : `data/raw/europe/eurostat_status_changes_cameroon.xlsx`

### Canada IRCC

- Rôle : résidents permanents, permis d'études et transitions du temporaire vers le permanent
- Couverture : 2015-2026 dans les fichiers bruts ; utiliser 2015-2024 pour l'analyse
- Utilisation principale : Q2 et Q3
- Fichiers bruts : `data/raw/canada/ircc_*.xlsx`
- Note de nettoyage : en-têtes multi-lignes, colonnes mensuelles/trimestrielles, hiérarchie de catégories et valeurs masquées `--`.

### USA DHS / Census

- Rôle : résidents permanents légaux aux États-Unis, arrivées de réfugiés et profil de la diaspora en 2024
- Couverture : LPR 2015-2022, réfugiés 2015-2024, ACS 2024
- Utilisation principale : Q1 et Q3
- Fichiers bruts : `data/raw/usa/*.xlsx`
- Note de nettoyage : DHS utilise des années fiscales ; ACS est une table de contexte ponctuelle avec des marges d'erreur.

### Base de données migration de l'OCDE

- Rôle : flux/stocks complémentaires de migration liés au Cameroun par origine ou nationalité
- Couverture : 1995-2022
- Utilisation principale : Q1 et vérifications croisées
- Fichier brut : `data/raw/global/oecd_migration_database_raw.csv`
- Note de nettoyage : fichier volumineux ; filtrer `CO2 == CMR` avant l'analyse.

## Jeux de données secondaires / contextuels

### UNHCR

- Rôle : demandeurs d'asile, réfugiés, réinstallation et personnes relevant de la compétence du HCR
- Couverture : principalement jusqu'en 2016 ou 2017 dans les fichiers bruts actuels
- Utilisation principale : historique/contexte uniquement sauf mise à jour
- Fichiers bruts : `data/raw/unhcr/*.csv`

### Japon

- Rôle : contexte migration/visa au Japon
- Couverture : lignes de visas pour le Cameroun 2009-2017 ; les fichiers inbound/outbound s'arrêtent en 2005
- Utilisation principale : usage historique/contextuel limité
- Fichiers bruts : `data/raw/japan/*.csv`
- Note de nettoyage : `japan_translation_mapping.csv` nécessite l'encodage CP932/Shift-JIS.

### Contexte démographique du Cameroun

- Rôle : dénominateurs démographiques et contexte migratoire
- Couverture : variable selon les fichiers, souvent jusqu'en 2017
- Utilisation principale : contextualisation et normalisation uniquement
- Fichiers bruts : `data/raw/context/*.csv`
