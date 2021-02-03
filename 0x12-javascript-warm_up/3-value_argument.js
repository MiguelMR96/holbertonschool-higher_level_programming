#!/usr/bin/node

// Print the argument passed when program run. Using ternary
// expression. Info about ternary structure:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator

console.log(process.argv[2] === undefined ? 'No argument' : process.argv[2]);
