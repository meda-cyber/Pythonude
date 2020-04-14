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