#!/usr/bin/node
// Prints x times “C is fun”.
// Where x is the first argument of the script.

const x = process.argv[2];

if (x === undefined) {
  console.log('Missing number of occurrences');
}

for (let step = 0; step < x; step++) {
  console.log('C is fun');
}
