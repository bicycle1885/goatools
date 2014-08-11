import os
import unittest
from goatools.obo_parser import (
    OBOReader,
    GOTerm,
    GODag
)


class TestOBOReader(unittest.TestCase):
    def test_iteration(self):
        reader = OBOReader(os.path.join(os.path.dirname(__file__), "data/mini_obo.obo"))
        n = 0

        for i, term in enumerate(reader, start=1):
            n += 1
            self.assertIsInstance(term, GOTerm)
            # the GO IDs are sequential in this case
            self.assertEqual(term.id, "GO:{:07d}".format(i))

        # contains 10 records
        self.assertEqual(n, 10)


class TestGOTerm(unittest.TestCase):
    pass


class TestGODag(unittest.TestCase):
    pass
