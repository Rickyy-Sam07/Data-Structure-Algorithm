long long minimumSteps(char* s) {
    // Initialize 'r' to store the total number of steps (result)
    double r = 0;
    
    // Initialize 'o' to count the number of '1's encountered
    double o = 0;
    
    // Iterate through the string character by character until we reach the null terminator ('\0')
    for (int i = 0; s[i] != '\0'; i++) {
        // If the current character is '1'
        if (s[i] == '1') {
            // Increment the count of '1's
            o++;
        }
        // If the current character is '0'
        else {
            // Add the count of '1's seen so far to the result 'r'
            // This represents the number of moves needed to move the '1's past this '0'
            r = r + o;
        }
    }
    
    // Return the total number of steps needed to make all '1's come before all '0's
    return r;
}
