 //sentence is a string of single-space separated words where each word consists only of lowercase letters.

//A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

//Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

//Example 1:

//Input: s1 = "this apple is sweet", s2 = "this apple is sour"

//Output: ["sweet","sour"]

//Explanation:

//The word "sweet" appears only in s1, while the word "sour" appears only in s2.

//Example 2:

//Input: s1 = "apple apple", s2 = "banana"

//Output: ["banana"]


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define the hash map entry structure
typedef struct HashEntry {
    char* word;
    int count;
    struct HashEntry* next;
} HashEntry;

// Define the hash map structure
typedef struct {
    HashEntry** table;
    int size;
} HashMap;

// Hash function
unsigned int hash(char* str, int size) {
    unsigned long hash = 5381;
    int c;
    while ((c = *str++)) {
        hash = ((hash << 5) + hash) + c;
    }
    return hash % size;
}

// Create a new hash map
HashMap* createHashMap(int size) {
    HashMap* map = (HashMap*)malloc(sizeof(HashMap));
    map->table = (HashEntry**)calloc(size, sizeof(HashEntry*));
    map->size = size;
    return map;
}

// Add or update a word in the hash map
void addWord(HashMap* map, char* word) {
    unsigned int index = hash(word, map->size);
    HashEntry* entry = map->table[index];
    while (entry != NULL) {
        if (strcmp(entry->word, word) == 0) {
            entry->count++;
            return;
        }
        entry = entry->next;
    }
    entry = (HashEntry*)malloc(sizeof(HashEntry));
    entry->word = strdup(word);
    entry->count = 1;
    entry->next = map->table[index];
    map->table[index] = entry;
}

// Get the count of a word from the hash map
int getWordCount(HashMap* map, char* word) {
    unsigned int index = hash(word, map->size);
    HashEntry* entry = map->table[index];
    while (entry != NULL) {
        if (strcmp(entry->word, word) == 0) {
            return entry->count;
        }
        entry = entry->next;
    }
    return 0;
}

// Free the hash map
void freeHashMap(HashMap* map) {
    for (int i = 0; i < map->size; i++) {
        HashEntry* entry = map->table[i];
        while (entry != NULL) {
            HashEntry* temp = entry;
            entry = entry->next;
            free(temp->word);
            free(temp);
        }
    }
    free(map->table);
    free(map);
}

// Tokenize the sentence and add words to the hash map
void tokenizeAndAddWords(char* sentence, HashMap* map) {
    char* token = strtok(sentence, " ");
    while (token != NULL) {
        addWord(map, token);
        token = strtok(NULL, " ");
    }
}

// Find uncommon words between two sentences
char** uncommonFromSentences(char* s1, char* s2, int* returnSize) {
    HashMap* map1 = createHashMap(1000);
    HashMap* map2 = createHashMap(1000);
    
    // Duplicate strings for tokenization
    char* s1_copy = strdup(s1);
    char* s2_copy = strdup(s2);

    // Tokenize and add words to hash maps
    tokenizeAndAddWords(s1_copy, map1);
    tokenizeAndAddWords(s2_copy, map2);

    free(s1_copy);
    free(s2_copy);

    // Find uncommon words
    char** result = (char**)malloc(1000 * sizeof(char*));
    int resultIndex = 0;

    // Check for uncommon words in s1
    char* token = strtok(s1, " ");
    while (token != NULL) {
        if (getWordCount(map1, token) == 1 && getWordCount(map2, token) == 0) {
            result[resultIndex++] = strdup(token);
        }
        token = strtok(NULL, " ");
    }

    // Check for uncommon words in s2
    token = strtok(s2, " ");
    while (token != NULL) {
        if (getWordCount(map2, token) == 1 && getWordCount(map1, token) == 0) {
            result[resultIndex++] = strdup(token);
        }
        token = strtok(NULL, " ");
    }

    *returnSize = resultIndex;

    // Free hash maps
    freeHashMap(map1);
    freeHashMap(map2);

    return result;
}

// Main function for testing
int main() {
    char s1[] = "this apple is sweet";
    char s2[] = "this apple is sour";
    int returnSize;

    char** uncommonWords = uncommonFromSentences(s1, s2, &returnSize);

    printf("Uncommon Words:\n");
    for (int i = 0; i < returnSize; i++) {
        printf("%s\n", uncommonWords[i]);
        free(uncommonWords[i]);  // Free each word
    }
    free(uncommonWords);  // Free the result array

    return 0;
}
