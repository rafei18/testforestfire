# **Prédiction des Incendies de Forêts en Algérie**  
_(Algerian Forest Fires Prediction)_

## **Description**
Ce projet utilise des techniques de Data Science et de Machine Learning pour prédire la probabilité d'incendies de forêts en Algérie, basé sur des données météorologiques et des indices du système Fire Weather Index (FWI). L'objectif est de développer un modèle performant et une application Flask déployée avec AWS Elastic Beanstalk pour des prédictions en temps réel.

---

## **Pipeline du Projet**
### 1. **Collecte des Données**
- **Dataset** : *Algerian Forest Fires Dataset (2012)*, contenant des observations météorologiques pour les régions de Béjaïa et Sidi Bel-Abbès.
- **Sources** :
  - Données météo (Température, Humidité, Vent, etc.).
  - Indices FWI : FFMC, DMC, DC, ISI, BUI, FWI.
- **Classes** : `Fire` (Incendie) et `Not Fire` (Pas d'Incendie).

### 2. **Exploratory Data Analysis (EDA) et Préparation des Données**
- Nettoyage des données : gestion des valeurs manquantes et des outliers.
- Analyse exploratoire : 
  - Analyse des distributions et relations entre variables.
  - Heatmap de corrélation pour identifier les liens entre les variables.
- **Feature Engineering** : création de nouvelles variables basées sur les données météorologiques et FWI.

### 3. **Modélisation Machine Learning**
- **Modèles testés** :
  - Régression linéaire.
  - Ridge Regression.
  - Lasso Regression.
  - Elastic Net.
- **Tuning des hyperparamètres** avec validation croisée.
- **Évaluation des performances** avec des métriques comme :
  - **R² Score** : mesurer la variance expliquée par le modèle.
  - **MAE** : Erreur Absolue Moyenne.
  - **MSE** : Erreur Quadratique Moyenne.

### 4. **Création d'une Application Flask**
- Développement d'une interface utilisateur pour permettre :
  - Chargement des données.
  - Entrée des valeurs météo pour prédire l'occurrence d'un incendie.
- Déploiement de l'application sur **AWS Elastic Beanstalk**.

---

## **Technologies Utilisées**
### **Langages et Frameworks**
- **Python** : Pandas, NumPy, Matplotlib, Scikit-learn.
- **Flask** : Framework pour l'application web.
- **AWS Elastic Beanstalk** : Déploiement de l'application.

### **Outils**
- Jupyter Notebooks : pour l'EDA et la modélisation.
- Pickle : pour la sauvegarde des modèles.
- Git/GitHub : gestion du code.
- VS Code : IDE.

---

## **Comment Exécuter le Projet ?**
### **1. Cloner le dépôt**
```bash
git clone https://github.com/votre-nom-utilisateur/nom-du-repo.git
cd nom-du-repo
