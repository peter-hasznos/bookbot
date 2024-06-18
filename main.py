def main():
    url = "./books/frankenstein.txt"
    text = get_book_text(url)
    counts = count_words(text)
    character_counts = count_characters(text)
    character_list = convert_dict_to_list(character_counts)
    print(f"--- Begin report of {url} ---")
    print(f"{counts} words found in the document")
    for item in character_list:
         print(f"The {item["name"]} character was found {item["num"]} times")
    print("--- End Report ---")
    

def get_book_text(book_url):
        with open(book_url) as b:
            return b.read();

def sort_on(dict):
    return dict["num"]

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    words = text.split()
    for word in words:
        word = word.lower()
        for char in word:
            if char not in characters:
                  characters[char] = 1
            else:
                 characters[char] += 1
    return characters

def convert_dict_to_list(dict):
     character_list = []
     for char in dict:
            if char.isalpha():
                character_list.append({"name": char, "num": dict[char]})
     character_list.sort(reverse=True, key=sort_on)
     return character_list
             
      

main()






