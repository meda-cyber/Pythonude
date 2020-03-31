// Divisible by 3 => Fizz
// Divisble by 5 => Buzz
// Divisble by both 3 and 5 => FizzBuzz
// Not divisible by both => input
// Not a number => "Not a number"
const output = fizzbuzz();
console.log(output)
function fizzbuzz(input) {
    if input % 3 == 0 && input % 5 == 0 return FizzBuzz
    else if input % 3 == 0 return "Fizz"
    else if input % 5 == 0 return "Buzz"
    else if input % 3 !== 0 && input % 5 !== 0 return input
    else return "Not a NUmber"


}