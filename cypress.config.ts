import { defineConfig } from 'cypress';

export default defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    specPattern: 'cypress/integration/**/*.spec.ts',
    supportFile: false,
    fixturesFolder: 'cypress/fixtures',
    screenshotsFolder: 'cypress/screenshots',
    videosFolder: 'cypress/videos',
    // pluginsFile: 'cypress/plugins/index.js', // assurez-vous que cette ligne est présente ou laissez par défaut
  },
});
