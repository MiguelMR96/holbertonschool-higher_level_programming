#!/usr/bin/node
// Increments and calls a function

exports.addMeMaybe = function (num, theFunction) {
  theFunction(num + 1);
};
