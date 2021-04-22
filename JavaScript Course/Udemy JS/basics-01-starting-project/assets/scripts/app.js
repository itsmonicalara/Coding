//Logic front end behind the calculator.
//This value will never change
const defaultResult = 0;
let currentResult = defaultResult;
currentResult = currentResult + 10 * 3;
let calculationDescription = '(' +currentResult+ ')'
outputResult(currentResult, calculationDescription);