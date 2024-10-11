//You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

//Return the number of consistent strings in the array words.

 

//Example 1:
//Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
//Output: 2
//Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
//Example 2:

//Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
//Output: 7
//Explanation: All strings are consistent.
//Example 3:

//Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
//Output: 4
//Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
 //
#include <stdio.h>
#include <stdbool.h>

 bool isconsistent(char *word  , bool allowedchars[]){
    for(int i =0 ; word[i] !='\0'; i++ ){
        if(allowedchars[word[i] - 'a' ] == false){
            return false;
        }
    }
        return true;
    }



int countConsistentStrings(char * allowed, char ** words, int wordsSize){
    int count =0 ;
    bool allowedchars[26] = {false} ;

    for(int i =0 ; allowed[i] != '\0' ; i++){
        allowedchars[allowed[i]- 'a'] = true;
        
        
    }
    for(int i =0 ; i<wordsSize  ;i++){
        if(isconsistent(words[i] , allowedchars)){
            count++;
        }
    }
    return count;

}





//or



#include <stdio.h>
#include <stdbool.h>

// Function to check if a word is consistent
bool isconsistent(char *word, bool allowedchars[]) {
    for (int i = 0; word[i] != '\0'; i++) {
        if (allowedchars[word[i] - 'a'] == false) {
            return false;
        }
    }
    return true;
}

// Function to count the number of consistent strings
int countConsistentStrings(char *allowed, char **words, int wordsSize) {
    int count = 0;
    bool allowedchars[26] = {false}; // Boolean array to store allowed characters

    // Mark the characters in the allowed string
    for (int i = 0; allowed[i] != '\0'; i++) {
        allowedchars[allowed[i] - 'a'] = true; // Mark as allowed
    }

    // Check each word in the words array
    for (int i = 0; i < wordsSize; i++) {
        if (isconsistent(words[i], allowedchars)) {
            count++; // Increment count if word is consistent
        }
    }

    return count; // Return the number of consistent words
}

int main() {
    // Example input
    char *allowed = "ab";
    char *words[] = {"ad", "bd", "aaab", "baa", "badab"};
    int wordsSize = sizeof(words) / sizeof(words[0]);

    int result = countConsistentStrings(allowed, words, wordsSize);
    printf("Output: %d\n", result); // Should print 2

    return 0;
}
