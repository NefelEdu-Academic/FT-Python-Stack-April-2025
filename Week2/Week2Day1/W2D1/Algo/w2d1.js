/* 
  String: Is Palindrome

  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */

var str1 = "a x a";
var expected1 = true;

var str2 = "racecar";
var expected2 = true;

var str3 = "Dud";
var expected3 = false;

var str4 = "oho!";
var expected4 = false;

function isPalindrome(str) {
    //start looping through the given string starting from 0 to the middle of the string and incrementing by 1 each step
        // check if current character is different than the character at index srt.length-1-i
            // return false
    // after looping inside the given string if we didn't return false, we have to return true
}

console.log(isPalindrome(str1));
console.log(isPalindrome(str2));
console.log(isPalindrome(str3));
console.log(isPalindrome(str4));