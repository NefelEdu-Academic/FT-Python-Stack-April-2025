/* 
Book Index

You are given an array of page numbers (as integers).
Your job is to return a string where:

* Single pages appear as they are (like 5).

* Consecutive pages are combined into a range (like 13-15 for 13, 14, 15).
*/

var nums1 = [1, 13, 14, 15, 37, 38, 70];
var expected1 = "1, 13-15, 37-38, 70";

var nums2 = [5, 6, 7, 8, 9];
var expected2 = "5-9";

var nums3 = [1, 2, 3, 7, 9, 15, 16, 17];
var expected3 = "1-3, 7, 9, 15-17";

function bookIndex(nums) {
    // Create an empty string variable to store the result (result)
    // create a variable representing the start potential range (start), start with value in first index
    // create a variable representing the end potential range (end), initialised to the first value of the given array
    // Start loopping through the given array stating from the second index to the length of the array going step by step
        // check if the current number is consecutive (current number is equal to end +1)
            // update the end value to the current number
        // otherwise, 
            // check if the start value is equal to end value
                // concatenate the value of start to result
            //  otherwise,
                // concatinate the start value with "-" and end value to the result
            // check if index is less than the length of the given array
                // concatenate ", " to the result
            // update start value to the current value (nums[i])
            // update end value to the current value (nums[i])
    // return the result variable

}
console.log(bookIndex(nums2));
