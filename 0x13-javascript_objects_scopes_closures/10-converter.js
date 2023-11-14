#!/usr/bin/node
exports.converter = function (base) {
  return function convert (number) {
    if (number === 0) {
      return '0';
    } else {
      const remainder = number % base;
      const quotient = Math.floor(number / base);
      const convertedDigit = remainder < 10 ? remainder : String.fromCharCode(87 + remainder);
      return convert(quotient) + convertedDigit;
    }
  };
};
