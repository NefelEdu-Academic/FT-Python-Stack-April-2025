/* 
String Encode

You are given a string that may contain sequences of consecutive characters.
Create a function to shorten a string by including the character,
then the number of times it appears. 


If final result is not shorter (such as "bb" => "b2" ),
return the original string.
*/

var str1 = "aaaabbcddd";
var expected1 = "a4b2c1d3";

var str2 = "";
var expected2 = "";

var str3 = "a";
var expected3 = "a";

// ! Bonus
var str4 = "bbcc";
var expected4 = "bbcc";

var str5 = "bc";
var expected5 = "bc";


function encodeStr(str) {
  // If the input is empty, return it as-is
  // Initialize a result string to build the encoded version
  // Initialize a count for repeated characters
  // Loop through the string starting from index 1
    // If the current character is the same as the previous one, increase the count
    // Otherwise,
        // add the previous character and count to result
        // Reset the count for the next character
  // If the encoded version is shorter, return it
  // Otherwise return the original string
}

console.log(encodeStr(str1));
console.log(encodeStr(str2));
console.log(encodeStr(str3));
console.log(encodeStr(str4));
console.log(encodeStr(str5));
