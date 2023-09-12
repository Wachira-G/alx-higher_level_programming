#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

const fileA = args[2];
const fileB = args[3];
const fileC = args[4];

fs.readFile(fileA, 'utf8', (err, fileAData) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.readFile(fileB, 'utf8', (err, fileBData) => {
    if (err) {
      console.error(err);
      return;
    }
    const fileCData = fileAData + fileBData;
    fs.writeFile(fileC, fileCData, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
});
