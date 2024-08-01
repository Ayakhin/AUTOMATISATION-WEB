describe('Form Authentication', () => {
    it('should successfully log in', () => {
      cy.visit('https://the-internet.herokuapp.com/');
  
      cy.contains('Form Authentication').click();
      cy.url().should('include', '/login');
  
      cy.get('#username').type('tomsmith');
      cy.get('#password').type('SuperSecretPassword!');
      cy.get('button[type="submit"]').click();
  
      cy.get('.flash.success').should('contain', 'You logged into a secure area!');
    });
  });
  