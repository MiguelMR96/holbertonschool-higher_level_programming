#!/usr/bin/node

// Convert argument to integer
// Try it! ./5-to_integer.js <argument_to_convert>

console.log(isNaN(parseInt(process.argv[2])) ? 'Not a number' : 'My number: ' + parseInt(process.argv[2]));
