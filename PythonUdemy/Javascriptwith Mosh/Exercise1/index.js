// Divisible by 3 => Fizz
// Divisble by 5 => Buzz
// Divisble by both 3 and 5 => FizzBuzz
// Not divisible by both => input
// Not a number => "Not a number"
const output = fizzbuzz(15);
console.log(output)
function fizzbuzz(input) {
    if (typeof (input) !== "number")
        return "Input is not number"
    if ((input % 3 == 0) && (input % 5 == 0))
        return "FizzBuzz";
    if (input % 3 == 0)
        return "Fizz";
    if (input % 5 == 0)
        return "Buzz";
    if (input % 3 !== 0 && input % 5 !== 0)
        return input;


}