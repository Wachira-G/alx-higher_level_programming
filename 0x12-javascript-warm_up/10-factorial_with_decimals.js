#!/usr/bin/node

let num = Number(process.argv[2]);

if (isNaN(num)) {
  num = 1;
}

function factorial (num) {
  let flag = 1;
  if (num === 0) {
    return 1;
  }

  if (num < 0) {
    flag = -1;
    num = Math.abs(num);
  }

  const integerPart = Math.floor(num);
  const fractionalPart = num - integerPart;

  let result = flag * calculateFactorial(integerPart);

  if (fractionalPart !== 0) {
    result *= calculateGamma(fractionalPart);
  }

  return result;
}

function calculateFactorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  }

  return num * calculateFactorial(num - 1);
}

function calculateGamma (x) {
  // implement gamma function calculation -- THIS IS FAR FAR FROM ACCURATE.
  return Math.sqrt(2 * Math.PI / x) * Math.pow((x / Math.E), x);
}

console.log(factorial(num));

//  we are trying to handle non-integer inputs for calculating the factorial. When we have a non-integer input, we split it into two parts: the integer part and the decimal (or fractional) part.

// The integer part is straightforward. We calculate the factorial of the integer part using a recursive function called calculateFactorial. This function multiplies all the numbers from 1 up to the given integer.

// The tricky part is handling the decimal (or fractional) part. Since factorials are defined only for non-negative integers, we cannot directly calculate the factorial of a decimal number. Instead, we use an approximation technique called the gamma function.

// The gamma function is a mathematical concept that extends factorials to real and complex numbers. It is used to approximate factorials of non-integer values. In our code, we use a simplified approximation of the gamma function for simplicity.

// To calculate the gamma function approximation, we use Math.sqrt(2 * Math.PI / x) to calculate a constant value based on x, which represents our fractional part. This constant value is then multiplied by Math.pow((x / Math.E), x), where Math.pow() raises x to the power of x. These calculations help us approximate the factorial value for our decimal input.

// Please note that this simplified approximation may not be accurate for all cases, especially when dealing with large or complex decimal inputs. For precise calculations involving factorials of non-integer values, more advanced mathematical techniques and libraries are usually required.
