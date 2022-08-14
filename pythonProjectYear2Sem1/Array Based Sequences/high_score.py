# Represents one entry of a list of high scores.
class GameEntry:

    # Create an entry with given name and score.
    def __init__(self, name, score):
        self._name = name
        self._score = score

    # Return the name of the person for this entry.
    def get_name(self):
        return self._name

    # Return the score of this entry.
    def get_score(self):
        return self._score

    # Return string representation of the entry.
    def __str__(self):
    # e.g., '(Bob, 98)'
        return '({0}, {1})'.format(self._name, self._score)