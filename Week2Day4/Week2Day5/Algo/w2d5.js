/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";
const str2 = "   hello world from the other side     ";
const expected2 = "hello world from the other side";

function trim(str) {
    // create 2 variables the first one intialised to 0 and the second one to the str.length-1
    // loop through the given string using a while loop until a non-space character is found
        // increment the start varibale
    // loop through the given string using a while loop until a non-space character is found
        // decrement the end varibale

    //return the substring from start position to end position + 1
}
console.log(trim(str1));
// str.substring(start, end)