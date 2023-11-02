#!/usr/bin/node
// updates the text color of the <header> element to red (#FF0000):
// use document.querySelector to select the HTML tag
// can’t use the jQuery API
// script imported from the <head> tag, not at the end of the HTML

document.addEventListener('DOMContentLoaded', (event) => {
  const element = document.querySelector('header');
  if (element) {
    element.style.color = '#FF0000';
  }
});
