# French Cooking Assistant

Un assistant IA spécialisé en cuisine française, développé en groupe 
dans le cadre du cours INF-2220 à l'UiT The Arctic University of Norway (novembre 2024).

## Description

Application web de type chatbot propulsée par l'API OpenAI, 
permettant d'obtenir des recettes françaises authentiques 
basées sur les ingrédients et préférences de l'utilisateur.

## Fonctionnalités

- Suggestions de recettes selon les ingrédients disponibles
- Adaptation aux préférences alimentaires (végétarien, low-calorie…)
- Inspiration par régions françaises
- Historique des conversations
- Interface style ChatGPT

## Architecture

- **Back-end** : Python / Flask
- **IA** : OpenAI Assistants API
- **Front-end** : HTML / CSS / JavaScript

## Installation

1. Cloner le repo
2. Installer les dépendances :
```bash
   pip install flask openai markdown
```
3. Ajouter votre clé OpenAI dans `app.py`
4. Lancer le serveur :
```bash
   python app.py
```
5. Ouvrir `http://localhost:4000`

## Équipe

Bastien Lambert, Camilia Haghighi, Francesco Orsi, Lilian Derain, Thomas Kaczmarek
