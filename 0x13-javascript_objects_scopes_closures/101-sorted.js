#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};
const set = new Set(Object.values(dict));

for (const item of set) {
  newDict[item.toString()] = [];
  for (const key in dict) {
    if (dict[key] === item) {
      newDict[item].push(key);
    }
  }
}

console.log(newDict);
