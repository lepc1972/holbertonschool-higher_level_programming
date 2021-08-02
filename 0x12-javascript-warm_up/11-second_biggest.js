#!/usr/bin/node

const my_list = process.argv.slice(2);

if (my_list.length <= 1) {
  console.log('0');
} else {
  my_list.sort((a, b) => a - b);
  const len = my_list.length;
  console.log(my_list[len - 2]);
}
