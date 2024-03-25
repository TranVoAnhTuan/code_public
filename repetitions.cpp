#include <iostream>
#include <string>

int longestRepetition(const std::string& dna) {
    int maxLength = 0;
    int currentLength = 1;  // Minimum length is 1
    char currentChar = dna[0];  // Start with the first character

    for (size_t i = 1; i < dna.size(); i++) {
        if (dna[i] == currentChar) {
            // Increment current length if the character repeats
            currentLength++;
        } else {
            // Update max length and reset current length if character changes
            maxLength = std::max(maxLength, currentLength);
            currentLength = 1;  // Reset length for new character
            currentChar = dna[i];  // Update current character
        }
    }

    // Check the last repetition if needed
    maxLength = std::max(maxLength, currentLength);

    return maxLength;
}

int main() {
    std::string dna;
    std::cin >> dna;

    int result = longestRepetition(dna);
    std::cout << result << std::endl;

    return 0;
}

