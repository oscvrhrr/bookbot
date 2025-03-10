from stats import count_words, count_chars, sorted_list
import sys


def main ():
  if len(sys.argv) < 2:
    print("Usage : python3 main.py <path_to_book>")
    sys.exit(1)

  arg1_path = sys.argv[1]
  
  def get_book_text(path):
    with open(path) as f:
      contents = f.read()
      return contents
    
  text = get_book_text(arg1_path)



  sorted_dic_chars = sorted_list(count_chars(text))

  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {count_words(text)} total words")
  print("--------- Character Count -------")
  for char_dic in sorted_dic_chars:
    char = char_dic["char"]
    count = char_dic["count"]
    print(f"{char}: {count}")
  print("============= END ===============")

main()

