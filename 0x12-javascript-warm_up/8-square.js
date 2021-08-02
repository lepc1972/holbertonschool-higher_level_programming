#!/usr/bin/node

const number = process.argv[2];

if (isNaN(number)) console.log('Missing size');
else {
  for (let x = 0; x < number; x++) {
    let spc = '';
    for (let y = 0; y < number; y++) {
      spc = spc + 'X';
    }
    console.log(spc);
  }
}
