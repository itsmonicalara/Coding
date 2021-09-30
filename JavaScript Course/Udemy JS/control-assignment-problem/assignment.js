const randomNumber = Math.random(); // produces random number between 0 (including) and 1 (excluding)
if (randomNumber > 0.7) {
    alert('The number is greater than 0.7');
}

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}

for (let elem in numbers) {
    console.log(numbers[elem]);
} 

for (let i = numbers.length - 1; i >= 0; i--) {
    console.log(numbers[i]);
}


const randomNumber2 = Math.random();

if ((randomNumber > 0.7 && randomNumber2 > 0.7) || (randomNumber <= 0.2 || randomNumber2 <= 0.2)) {
    alert('Successful');
}