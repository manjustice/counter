from collections import defaultdict


def word_frequency(text: list[str]) -> dict[str, int]:
    words = defaultdict(int)

    for sentence in text:
        word = ""

        for char in sentence:
            if char.isalpha():
                word += char.lower()

            elif word:
                words[word] += 1
                word = ""

        if word:
            words[word] += 1

    return words


if __name__ == "__main__":
    paragraph = []
    frequency = word_frequency(paragraph)

    print(frequency)
