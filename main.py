import time

def read_words(file_path):
    """Reads words from a .txt file and returns them as a sorted list."""
    with open(file_path, 'r') as file:
        return sorted(file.read().splitlines(), key=len)

def can_form_word(word, word_set, is_original_word):
    """Checks if a word can be formed by other words in the set."""
    if word in word_set and not is_original_word:
        return True
    
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]
        if prefix in word_set and can_form_word(suffix, word_set, False):
            return True
    return False

def find_longest_compounded_words(file_path):
    """Finds the longest and second-longest compounded words in the file."""
    start_time = time.time()
    words = read_words(file_path)
    word_set = set(words)
    compounded_words = []

    for word in words:
        if can_form_word(word, word_set, True):
            compounded_words.append(word)

    compounded_words.sort(key=len, reverse=True)
    longest = compounded_words[0] if compounded_words else None
    second_longest = compounded_words[1] if len(compounded_words) > 1 else None
    time_taken = int((time.time() - start_time) * 1000)  # Convert into milliseconds
    
    return longest, second_longest, time_taken

if __name__ == "__main__":
    # Process file Input_01.txt
    longest, second_longest, time_taken = find_longest_compounded_words('Input_01.txt')
    print("For Input_01.txt:")
    print(f"Longest Compound Word: {longest}")
    print(f"Second Longest Compound Word: {second_longest}")
    print(f"Time taken to process file: {time_taken} ms")
    
    # Process file Input_02.txt
    longest, second_longest, time_taken = find_longest_compounded_words('Input_02.txt')
    print("\nFor Input_02.txt:")
    print(f"Longest Compound Word: {longest}")
    print(f"Second Longest Compound Word: {second_longest}")
    print(f"Time taken to process file: {time_taken} ms")
