/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

/**
 * De-dupes the given string.
 */

function stringDedupe(str) {
    //create an empty string to store the result
    //create an empty object to store each character and the number of its occurence
    //loop through the given string that start from 0 to the end of the string and going step by step
        // check if the current charater exist in the created object
            // the value of the current charater should increment by 1
        //otherwise
            // the value of the current charater should be initialised to 1
    // loop through the created object 
        //concatenate the key to the result string
    // return result string
}
console.log(stringDedupe(str1));
console.log(stringDedupe(str2));
console.log(stringDedupe(str3));
console.log(stringDedupe(str4));

