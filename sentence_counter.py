import re

# function to split a paragraph into sentences
def get_sentences(paragraph):
    pattern = r'[A-Za-z0-9].*?[.!?](?=\s+[A-Za-z0-9]|\s*$)'
    sentences = re.findall(pattern, paragraph, flags=re.DOTALL)
    return [sentence.strip() for sentence in sentences]


# function to display each sentence and the total count
def display_sentences(sentences):
    print("\nIndividual sentences:")
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence}")

    print(f"\nTotal number of sentences: {len(sentences)}")


def main():
    paragraph = input("Enter a paragraph: ")
    sentences = get_sentences(paragraph)

    if len(sentences) == 0:
        print("\nNo complete sentences were found.")
    else:
        display_sentences(sentences)


main()
