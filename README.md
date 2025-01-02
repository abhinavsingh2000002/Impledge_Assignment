# Longest Compounded Words Finder

## Overview
This program identifies the longest and second-longest compounded words from a given text file. A compounded word is defined as a word that can be formed entirely by concatenating other words from the same file. The implementation reads a list of words, processes them to check for compounded words, and outputs the results. The program also reports the time taken to process each file.

### Key Features:
- **Input Flexibility**: Reads words from any `.txt` file.
- **Efficient Search**: Uses sorting and recursion to determine compounded words.
- **Performance Metrics**: Tracks and displays execution time in milliseconds.

## Design Decisions
1. **Sorting by Length**: Words are sorted by length to ensure smaller words are processed first, which aids in forming larger compounded words efficiently.
2. **Recursive Checking**: A helper function recursively determines if a word can be formed using other words.
3. **Optimized Data Structures**: A `set` is used for quick membership testing during word checks.

## Approach
1. **Read and Sort Words**: The input words are read from the file and sorted by length.
2. **Recursive Validation**: Each word is checked to see if it can be formed by other words.
3. **Result Compilation**: Compounded words are stored, sorted by length, and the two longest ones are identified.
4. **Performance Tracking**: Execution time is measured from start to finish for each file.

## Prerequisites
- Python 3.6 or higher
- Input files in `.txt` format, with one word per line.

## How to Run
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. **Prepare Input Files**:
   Ensure your input files (e.g., `Input_01.txt`, `Input_02.txt`) are in the same directory as the script.

3. **Run the Script**:
   ```bash
   python3 compounded_words.py
   ```

4. **View Results**:
   The program will display the following for each input file:
   - Longest compounded word
   - Second longest compounded word
   - Time taken to process the file

### Example Output
```plaintext
For Input_01.txt:
Longest Compound Word: concatenation
Second Longest Compound Word: subconcatenation
Time taken to process file: 120 ms

For Input_02.txt:
Longest Compound Word: interconnection
Second Longest Compound Word: disconnection
Time taken to process file: 150 ms
```

## Notes
- Ensure the input files contain valid words, one per line.
- For large files, processing time may increase due to the recursive nature of the checks.

