text=input("Input a text: ").lower()
letter_1=input("#1 Input a letter: ").lower()
letter_2=input("#2 Input a letter: ").lower()
letter_3=input("#3 Input a letter: ").lower()
print("\nThe text \n"+text)
print(f"\nLetter 1: {letter_1} {text.count(letter_1)}")
print(f"\nLetter 2: {letter_2} {text.count(letter_2)}")
print(f"\nLetter 3: {letter_3} {text.count(letter_3)}")

my_list=text.split(" ")
total_words=len(my_list)
print(f"\nTotal words in the text: {total_words}")

print(f"First word: {my_list[0]} \nLast word: {my_list[-1]}")
my_list.reverse()
reverse=" ".join(my_list)
print(f"\nReversed text: \n{reverse} ")
bool="python" in text
my_dict={False:"No",True:"Yes"}
print(f"\nIs python in the text: {my_dict[bool]}")