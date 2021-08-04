#!/usr/bin/node

exports.esrever = function (list) {
  const List = [];
  for (let x = list.length - 1; x >= 0; x--) {
    List.push(list[x]);
  }
  return List;
};
