def character_count(word):
    """
    This function aims to count characters of words.
    """
    character_statistic = {}

    for char in word:
        if char in character_statistic:
            character_statistic[char] += 1
        else:
            character_statistic[char] = 1
    return character_statistic


# Testcases:
if __name__ == "__main__":
    assert character_count("Baby") == {"B": 1, "a": 1, "b": 1, "y": 1}
    print(character_count("Happiness"))
    print(character_count("smiles"))
