#!/usr/bin/node

console.log(factorial(process.argv[2]));

function factorial (number) {
  if (number <= 1 || isNaN(number)) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}
