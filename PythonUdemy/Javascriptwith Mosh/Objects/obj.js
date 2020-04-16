// Object-Oriented Programming(OOP)
const circle = {
    radius: 1,
    location: {
        x: 1,
        y: 1
    },
    isVisible: true,
    draw: function () {
        console.log("draw")
    }
}
circle.draw();// function inside object is a Method

// Factory Function
function createCircle(radius) {
    return {
        radius,
        draw() {
            console.log("draw");
        }
    };
}

const circle1 = createCircle(1);
console.log(circle1);

const circle2 = createCircle(2);
console.log(circle2)

// Constructor Function use also pascal conven

function Circle(radius) {
    this.radius = radius;
    this.draw = function () {
        console.log("draw");
    }
}
const circle3 = new Circle(1)

// Daynamic nature of Object
// const circle4 = {
//     radius: 1
// };
// circle = {};
// circle4.color = "yellow";
// circle4.draw = function () { }

// // delete circle.color;
// // delete circle.draw;

// console.log(circle4)

// value and reference type
// let x = 10
// let y = x
// x = 20;
// console.log(x)
// console.log(y)
// second example will be the same bcs both are stored on memory 

let x = { value: 10 };
let y = x
x.value = 20
console.log(x)
console.log(y)

let number = 10
function increase(number) {
    number++
    console.log(number)
}
increase(number)
console.log(number)
// second exaple
let obj = { value: 10 };
function inc(obj) {
    obj.value++;
}
inc(obj);
console.log(obj)
// definition of Primitive: are copied by their value
// definition of Objects: are copied by their reference

// Enumerating Properties of Object
const triangle = {
    base: 1,
    draw() {
        console.log("draw")
    }
}
for (let key in triangle)
    console.log(key, triangle[key]);

for (let key of Object.keys(triangle))
    console.log(key);

for (let entry of Object.entries(triangle))
    console.log(entry)

if ("base" in triangle) console.log("yes")

// Cloning an Object
// const another = {};

// for (let key in circle)
//     another[key] = triangle[key]
// console.log(another)
// we can do the above with same processe in modern js
const another = Object.assign({
    color: "yellow"
}, circle);
console.log(another)

// Exercise 1
// street
// city
// zipcode
// showAdress(address)
let address = {
    street: "Gummenholzweg 7",
    city: "Bern",
    zipcode: "3173"
}
function showAdress(address) {
    for (let key in address)
        console.log(key, address[key])
}
showAdress(address)

// Exercise 2
// Factory function
let loc = createAddress("Laupenstrasse 21", "Neuenegg", 3317)
console.log(loc)
function createAddress(street, city, zipcode) {
    return {
        street,
        city,
        zipcode
    };
}
// Constructor function
let place = new Address("Dorfstrasse 15", "Hinterkappelen", 3070)
console.log(place)
function Address(street, city, zipcode) {
    this.street = street;
    this.city = city;
    this.zipcode = zipcode;
}

// Sring primitive
const message = "hi"
console.log(typeof (message))

// Sring Object
const second = new String("hi");
console.log(typeof (second))

// Exercise
let address1 = new Address("Morillionstrasse 19", "Bern", 3012)
let address2 = new Address("Gümiligenstrasse 19", "Bern", 3015)
let address3 = address1
console.log(areEqual(address1, address2));
console.log(areSame(address1, address2));
console.log(areSame(address1, address3));

//  Constructor Function
function Address(street, city, zipcode) {
    this.street = street;
    this.city = city;
    this.zipcode = zipcode;
}
function areEqual(address1, address2) {
    return address1.street === address2.street &&
        address1.city === address2.city &&
        address1.zipcode === address2.zipcode;

}

function areSame(address1, address2) {
    return address1 === address2

}

// Sring primitive
mess =
    "This is my\n " +
    "\"first\" message";

// Litral
// object litral {}
// Boolean litral true,false
// Sring litral "",''
// Template litral `` back tick good for mailing 


const name = "Michaele";


const ano =
    `Hi ${name},
Thank you for joining my mailing list.
Regards ,
Medhanie Desale
`;
console.log(mess)
console.log(ano)