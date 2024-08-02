describe('Form Authentication', () => {
  it('should successfully log in', () => {
    cy.visit('https://the-internet.herokuapp.com/');
    
    // Utilisation d'un sélecteur CSS pour trouver et cliquer sur le lien
    cy.contains('Form Authentication').click();
    cy.url().should('include', '/login');
    
    // Utilisation d'un sélecteur CSS pour trouver le champ de saisie
    cy.get('#username').type('tomsmith');
    
    // Utilisation d'un sélecteur XPath pour trouver le champ de saisie du mot de passe
    cy.xpath('//input[@id="password"]').type('SuperSecretPassword!');
    
    // Utilisation d'un sélecteur CSS pour trouver et cliquer sur le bouton de soumission
    cy.get('button[type="submit"]').click();
    
    // Utilisation d'un sélecteur XPath pour vérifier le message de succès
    cy.xpath('//div[contains(@class, "flash success")]').should('contain', 'You logged into a secure area!');
  });
});
