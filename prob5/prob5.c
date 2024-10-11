int minAddToMakeValid(char* s) {
    int count1 = 0;  // Tracks unmatched open parentheses '('
    int count2 = 0;  // Tracks unmatched close parentheses ')'
    
    // Iterate over the string
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] == '(') {
            count1++;  // Expecting a closing parenthesis
        } else if (s[i] == ')') {
            if (count1 > 0) {
                count1--;  // Matched one open parenthesis
            } else {
                count2++;  // Unmatched closing parenthesis, need to add an opening one
            }
        }
    }
    
    // The total steps will be unmatched opening (count1) + unmatched closing (count2)
    return count1 + count2;
}