#!/usr/bin/node
// Print square of X's
// The first argument is the size of the square

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let step = 0; step < x; step++) {
    let string = '';
    for (let inStep = 0; inStep < x; inStep++) {
      string += 'X';
    }
    console.log(string);
  }
}
