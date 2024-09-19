def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    def word_count(string):
        count = 0
        for word in string.split():
            count += 1
        return count

    def character_occurrences(string):
        final_dict = {}
        for char in string.lower():
            if char not in final_dict.keys():
                final_dict[char] = 1
            else:
                final_dict[char] += 1
        return final_dict
    
    def report():
        print(f"--- Here is the report of books/frankenstein.txt ---")
        print(f"{word_count(file_contents)} words found in the document")
        raw_report = character_occurrences(file_contents)
        raw_report_keys = sorted(raw_report.keys())
        for ch in raw_report_keys:
            if ch == "\n":
                print(f"The '\\n' (newline) character was found {raw_report[ch]} times")
            else:
                print(f"The '{ch}' character was found {raw_report[ch]} times")
        print("--- End of report ---")

    report()






if __name__ == "__main__":
    main()
