import os
import unittest
from goatools.obo_parser import (
    OBOReader,
    GOTerm,
    GODag
)

mini_obo = os.path.join(os.path.dirname(__file__), "data/mini_obo.obo")


class TestOBOReader(unittest.TestCase):
    def test_iteration(self):
        reader = OBOReader(mini_obo)
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
    def setUp(self):
        self.dag = GODag(mini_obo)

    def test_query_term(self):
        term = self.dag.query_term("GO:0000006")
        self.assertEqual(term.id, "GO:0000006")

        term = self.dag.query_term("GO:1234567")
        self.assertIsNone(term)

    def test_paths_to_top(self):
        paths = self.dag.paths_to_top("GO:0000006")
        self.assertEqual(
            str(paths),
            "[[GOTerm('GO:0000001'), "
            "GOTerm('GO:0000003'), "
            "GOTerm('GO:0000006')]]"
        )
