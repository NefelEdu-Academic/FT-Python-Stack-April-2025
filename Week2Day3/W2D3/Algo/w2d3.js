/* 
    Given a non-empty array of odd length containing ints where every int but one
    belongs to a pair (the int is duplicated once)
    return the only int that has no matching pair.
    Hint: You can use makeFrequencyTable(arr) developed in the previous Algorithm
*/

const nums1 = [1];
const expected1 = 1;

const nums2 = [5, 4, 5];
const expected2 = 4;

const nums3 = [5, 4, 3, 4, 3, 4, 5];
const nums3Sorted = [3, 3, 4, 4, 4, 5, 5];
const expected3 = 4; // there is a pair of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expected4 = 1;

function makeFrequencyTable(arr) {
    let expected = {};
    for (let i = 0; i < arr.length; i++) {
        if (expected[arr[i]]) {
        expected[arr[i]] += 1;
        } else {
        expected[arr[i]] = 1;
        }
    }
    return expected;
}

function oddOccurrencesInArray(nums) {
    // First, generate a frequency table of the numbers in the given array
    // create a variable that contain the result of makeFrequencyTable function with the given array in the paramters
    // loop through each key (element) in the result variable
        // check if the count of that key (element) is odd
            // return the key
}

console.log(oddOccurrencesInArray(nums1), "should equal", expected1);
console.log(oddOccurrencesInArray(nums2), "should equal", expected2);
console.log(oddOccurrencesInArray(nums3), "should equal", expected3);
console.log(oddOccurrencesInArray(nums4), "should equal", expected4);
