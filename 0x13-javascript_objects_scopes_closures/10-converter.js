#!/usr/bin/node

exports.converter = function (base) {
  if (base < 2 || base > 36) {
    throw new Error('Base must be between 2 and 36');
  }

  return function (num) {
    if (num === 0) {
      return '0';
    }

    const digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let result = '';

    while (num > 0) {
      const remainder = num % base;
      result = digits[remainder] + result;
      num = Math.floor(num / base);
    }

    return result;
  };
};
