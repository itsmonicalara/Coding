// Simple for loop
for (let i = 0; i < 3; i++)
{
    console.log(i);
}

// For-of loop to work w/ arrays
let fruits = ['Apple', 'Banana'];
for (const el of fruits)
{
    console.log(el);
}

// For-in loops to work w/ objects
// Object initializer
const myCar = {
    make: 'Ford',
    model: 'Mustang',
    year: 1969
};

for (const key in myCar)
{
    console.log(key, ':' , myCar[key]);
}

// While loop
let n = 0;

while (n < 3) {
    n++;
}
console.log(n);



let sum = 0;
for (let i = 0; i < 3; i++) {
    for (let j = 5; j > 2; j--) {
        sum = j + i;
    }
}
console.log(sum); // ???

const hobbies = ['Sports', 'Cooking', 'Coding'];
let favoriteHobby;
for (const hobby of hobbies) {
    favoriteHobby = hobby;
}
console.log(favoriteHobby);

