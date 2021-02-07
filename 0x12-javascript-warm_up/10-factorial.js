#!/usr/bin/node
// Script that computes and prints a factorial
const num = process.argv[2];
function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}
console.log(factorial(num));
