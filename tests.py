import pytest

from main import word_frequency
from collections import defaultdict


@pytest.mark.parametrize(
    "paragraph,frequency",
    [
        (
            [
                "The quick brown fox", "jumps over the lazy dog.",
                "The dog barks,", "and the fox runs away"
            ],
            {
                "the": 4, "quick": 1, "brown": 1, "fox": 2, "jumps": 1, "over": 1,
                "lazy": 1, "dog": 2, "barks": 1,"and": 1, "runs": 1, "away": 1
            }
        ),
        (
            [
                "Now is the winter of our          discontent",
                "Made glorious summer by this sun of York;"
            ],
            {
                'now': 1, 'is': 1, 'the': 1, 'winter': 1, 'of': 2, 'our': 1, "discontent": 1,
                'made': 1, 'glorious': 1, 'summer': 1, 'by': 1, 'this': 1, 'sun': 1, 'york': 1
            },
        ),
        (
            [], defaultdict(int)
        ),
        (
            ["    "], defaultdict(int)
        ),
        (
            ["!!    word!  !!"], {"word": 1}
        )
    ]
)
def test_word_frequency(paragraph: list[str], frequency: dict[str, int]) -> None:
    assert word_frequency(paragraph) == frequency
