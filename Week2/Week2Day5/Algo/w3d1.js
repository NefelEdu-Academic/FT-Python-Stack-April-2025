/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid

Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.
const str5 = "a)b((c))";
const expected5 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

function parensValid(str = "") {
    // We need to declare  a variable to check the number of open and closed parenthesis
    let result = 0;
    for(let i=0; i<str.length; i++){
        if(str[i] == "("){
            result++

        }
        else if(str[i] == ")"){
            result--

        }
        if(result <0){
            return false ;

        }
    }
    // if(result == 0){
    //     return true;

    // }
    // else{
    //     return false ;
    // }
    return result == 0
}


console.log(parensValid(str1))
console.log(parensValid(str2))
console.log(parensValid(str3))
console.log(parensValid(str4))

