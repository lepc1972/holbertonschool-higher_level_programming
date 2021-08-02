#!/usr/bin/node

const lista = process.argv.slice(2);

if (lista.length <= 1) {
  console.log('0');
} else {
  lista.sort((a, b) => a - b);
  const len = lista.length;
  console.log(lista[len - 2]);
}
