#!/usr/bin/node

// Get the first argument
let arg = process.argv[2];

// Attempt to convert the argument to an integer
let num = parseInt(arg);

// Check if the conversion was successful and print the result
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
