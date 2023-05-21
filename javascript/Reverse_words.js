function reverseWords(str) {
    // * 1. reverse the whole string
    // * 2. check for each string with space and append to array
    // * 3. reverse the position of each value in array
    // * 4. return array to new string
    let index = [];
    let string = "";
    
    str = str.split(' ').reverse();
    return str;
}

console.log(reverseWords("This is an example!"));