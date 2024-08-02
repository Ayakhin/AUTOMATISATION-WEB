/// <reference types="cypress" />

declare namespace Cypress {
    interface Chainable<Subject = any> {
      xpath<E extends Node = HTMLElement>(selector: string, options?: Partial<Loggable & Timeoutable & Withinable & Shadow>): Chainable<JQuery<E>>;
    }
  }
  