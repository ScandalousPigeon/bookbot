def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(file_contents)

    def word_count(string):
        count = 0
        for word in string.split():
            count += 1
        return count

    print(word_count(file_contents))

    def character_occurrences(string):
        final_dict = {}
        for char in string.lower():
            if char not in final_dict.keys():
                final_dict[char] = 1
            else:
                final_dict[char] += 1
        return final_dict
    
    print(character_occurrences(file_contents))




if __name__ == "__main__":
    main()
