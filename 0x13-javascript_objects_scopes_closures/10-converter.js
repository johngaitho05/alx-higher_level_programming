#!/usr/bin/node
exports.converter = function (base) {
  return function convert (number) {
    if (number === 0) {
      return '';
    } else {
      const remainder = number % base;
      const quotient = Math.floor(number / base);
      return convert(quotient) + remainder;
    }
  };
};
