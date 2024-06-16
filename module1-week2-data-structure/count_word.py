import gdown


def count_word(file_path):
    """
    This function aims to count words of text.
    """
    # Read file
    with open(file_path, "r") as file:
        document = file.read()

        # Split and count words
        counter = {}
        words = document.lower().split()
        for word in words:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
        return counter


# Testcases:
if __name__ == "__main__":
    gdown.download(
        "https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko",
        "./module1-week2-data-structure/content/P1_data.txt",
        quiet=False,
    )
    file_path = "./module1-week2-data-structure/content/P1_data.txt"
    result = count_word(file_path)
    print(result)
