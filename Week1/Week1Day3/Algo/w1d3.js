/**
 * Determines whether or not the strings are equal, ignoring case.
 * @param {string} strA
 * @param {string} strB
 * @returns {boolean} If the strings are equal or not.
 */

var strA1 = "ABC"; //A 502358
var strB1 = "abc"; //a 225588
var expected1 = true;

var strA2 = "ABC";
var strB2 = "abd";
var expected2 = false;

var strA3 = "ABC";
var strB3 = "bc";
var expected3 = false;

// ! BONUS
var strA4 = "Dad ";
var strB4 = " dAd";
var expected4 = true;
// You can use .trim() : a built-in string method that removes whitespace characters from the beginning and end of a string. 
function caseInsensitiveStringCompare(strA, strB) {
  // update given strings into upper case strings and removing whitespaces using .trim()
    // check if the length of the 2 strings is different, we return false
    // otherwise we have to loop through one of the given strings strating from 0 to the length-1 and going step by step
        // check if each current character in first string is different to the current character in the second, we return false
    // after looping through the strings, return true
}

console.log(caseInsensitiveStringCompare(strA1, strB1));
console.log(caseInsensitiveStringCompare(strA2, strB2));
console.log(caseInsensitiveStringCompare(strA3, strB3));
console.log(caseInsensitiveStringCompare(strA4, strB4));