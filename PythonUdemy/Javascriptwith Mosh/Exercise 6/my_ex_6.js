// calculate the multiple of 3 and 5 less than 10 and sum up
console.log(sum(10))

function sum(limit) {
    sum = 0
    for (i = 0; i <= limit; i++) {
        if (i % 3 === 0 || i % 5 === 0)
            sum += i;

    }
    return sum;

}