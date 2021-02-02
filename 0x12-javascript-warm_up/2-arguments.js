#!/usr/bin/node

const args = process.argv.length;
// Just running the program without arguments returns
// args lenght = 2, so we start at 2 being no arguments passed

if (args === 2) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
