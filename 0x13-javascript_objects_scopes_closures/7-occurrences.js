#!/usr/bin/node
// Return number of occurrencies in a list
exports.nbOccurences = function (list, searchElement) {
  let ocurrences = 0;
  for (const i of list) {
    if (i === searchElement) {
      ocurrences++;
    }
  }
  return ocurrences;
};
