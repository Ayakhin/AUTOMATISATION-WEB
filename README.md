# AUTOMATISATION-WEB

Test d'authentification avec Cypress et Brave

Ce projet contient un test automatisé pour vérifier l'authentification sur le site The Internet en utilisant Cypress et le navigateur Brave.

## Prérequis

Avant de pouvoir exécuter ce test, vous devez installer les outils et bibliothèques suivants :

- Node.js (version 16 ou ultérieure recommandée)
- npm (généralement inclus avec Node.js)
- Brave Browser

## Installation

1. Cloner le dépôt :
    ```bash
    git clone https://github.com/Ayakhin/AUTOMATISATION-WEB.git
    cd AUTOMATISATION-WEB
    ```

2. Installer les dépendances :
    ```bash
    npm install
    ```

## Configuration

Assurez-vous que Brave est installé sur votre machine. Ensuite, vous pouvez configurer Cypress pour utiliser Brave en modifiant le fichier `cypress.config.ts` :

```typescript
import { defineConfig } from 'cypress';

export default defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // configure node event listeners here
    },
    specPattern: 'cypress/integration/**/*.spec.ts',
    supportFile: false,
    fixturesFolder: 'cypress/fixtures',
    screenshotsFolder: 'cypress/screenshots',
    videosFolder: 'cypress/videos',
    browser: 'brave',  // Assurez-vous que le navigateur Brave est configuré correctement
  },
});

Pour exécuter les tests avec Cypress, utilisez la commande suivante :
npx cypress open

Pour exécuter les tests en mode headless (sans interface graphique), utilisez :
npx cypress run


Ce README reflète l'utilisation de Cypress et fournit des instructions pour l'installation, la configuration, et l'exécution des tests. Assurez-vous que les chemins et les détails spécifiques à votre configuration sont corrects.

