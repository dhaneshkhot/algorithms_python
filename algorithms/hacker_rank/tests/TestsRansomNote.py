import unittest
from algorithms.hacker_rank.RansomNote import RansomNote

class TestsRansomNote(unittest.TestCase):

    def test_can_note_be_made_from_magazine_negative(self):
        magazine = "ive got a lovely bunch of coconuts"
        note = "ive got some coconuts"

        ransom_note = RansomNote()

        self.assertEqual("No", ransom_note.can_note_be_made_from_magazine(magazine, note))

    def test_can_note_be_made_from_magazine_positive(self):
        magazine = "give me one grand today night"
        note = "give one grand today"

        ransom_note = RansomNote()

        self.assertEqual("Yes", ransom_note.can_note_be_made_from_magazine(magazine, note))