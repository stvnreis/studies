const value = 5

function factorial(value) {
  if (value === 1) return 1

  return value * factorial(value -1)
}

console.log(factorial(6))