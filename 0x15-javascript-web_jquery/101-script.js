#!/usr/bin/node
// adds, removes and clears LI elements from a list when the user clicks:
// The new element must be: <li>Item</li>
// The new element must be added to UL.my_list
// When the user clicks on DIV#add_item: a new element is added to the list
// When the user clicks on DIV#remove_item: the last element is removed from the list
// When the user clicks on DIV#clear_list: all elements of the list are removed
// You can’t use document.querySelector to select the HTML tag
// You must use the JQuery API
// You script must work when it imported from the HEAD tag

$(document).ready(function () {
  const addButton = $('div#add_item');
  const removeButton = $('div#remove_item');
  const clearListButton = $('div#clear_list');
  const ul = $('ul.my_list');

  addButton.on('click', function () {
    ul.append('<li>Item</li>');
  });

  removeButton.on('click', function () {
    ul.children('li:last').remove();
  });

  clearListButton.on('click', function () {
    ul.empty();
  });
});
