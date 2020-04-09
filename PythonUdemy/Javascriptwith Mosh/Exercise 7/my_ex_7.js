// calculating  the average and given grade based on average
// For example ave = 70
// 1-59:F
// 60-69:D
// 70-79:C
// 80-89:B
// 90-100:A
const marks = [87, 72, 80]
console.log(caluateGrade(marks));
function caluateGrade(array) {
    // let sum = 0
    // for (let mark of marks)
    //     sum += mark;
    // let average = sum / marks.length

    // if (average < 59)
    //     return "F"
    // else if (average > 60 && average < 69)
    //     return "D"
    // else if (average > 70 && average < 79)
    //     return "C";
    // else if (average > 80 && average < 89)
    //     return "B";
    // else
    //     return "A";
    // Second way 
    const average = calculatAverage(marks)
    if (average < 60) return "F";
    if (average < 70) return "D";
    if (average < 80) return "C";
    if (average < 90) return "B";
    return "A"


    // if we are working with bunch of number
    function calculatAverage(array) {
        let sum = 0
        for (let value of array)
            sum += value;
        return sum / array.length

    }

}