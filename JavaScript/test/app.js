cToF = function(celsius) {
  if(!Number.isInteger(celsius)) return undefined;
  return celsius * 9 / 5 + 32;
}

fToC = function(fahrenheit) {
  if(!Number.isInteger(fahrenheit)) return undefined;
  return (fahrenheit - 32) * 5 / 9;
}