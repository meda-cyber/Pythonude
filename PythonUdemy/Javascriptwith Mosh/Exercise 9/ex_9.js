showPrimes(20);

function showPrimes(limit) {
    for (let i = 2; i < limit; i++) {

        let isPrime = true;
        for (let factor = 2; factor < i; factor++) {
            if (i % factor === 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) console.log(i)
    }
}