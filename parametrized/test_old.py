from unittest import TestCase
from pytest_demo.utils import booleanify, make_hashable


class BooleanifyTestCase(TestCase):

    def test_false_string(self):
        self.assertFalse(booleanify('false'))

    def test_false_boolean(self):
        self.assertFalse(booleanify(False))

    def test_false_camelcase_string(self):
        self.assertFalse(booleanify('FaLse'))

    def test_zero_string(self):
        self.assertFalse(booleanify('0'))

    def test_true_string(self):
        self.assertTrue(booleanify('true'))

    def test_true_camelcase_string(self):
        self.assertTrue(booleanify('tRuE'))

    def test_one_string(self):
        self.assertTrue(booleanify('1'))

    def test_random_string(self):
        self.assertTrue(booleanify('cat'))

    def test_true_boolean(self):
        self.assertTrue(booleanify(True))


class MakeHashableTestCase(TestCase):

    def test_list(self):
        self.assertEqual(
            (1, 2, 3),
            make_hashable([1, 2, 3])
        )

    def test_set(self):
        self.assertEqual(
            (1, 2, 3),
            make_hashable({1, 2, 3})
        )

    def test_frozenset(self):
        self.assertEqual(
            frozenset([1, 2, 3]),
            make_hashable(frozenset([1, 2, 3]))
        )

    def test_tuple(self):
        self.assertEqual(
            (1, 2, 3),
            make_hashable(tuple([1, 2, 3]))
        )

    def test_mixed_objects_list(self):
        self.assertEqual(
            ((1, 2), (3, 4), (('a', True), ('b', False))),
            make_hashable([[1, 2], (3, 4), dict(a=True, b=False)])
        )

    def test_mixed_objects_tuple(self):
        self.assertEqual(
            ([1, 2], (3, 4), {'a': True, 'b': False}),
            make_hashable(tuple([[1, 2], (3, 4), dict(a=True, b=False)]))
        )

    def test_dict(self):
        self.assertEqual(
            (
                ('a', 'hello'),
                ('b', 'test')
            ),
            make_hashable(
                dict(
                    a='hello',
                    b='test'
                )
            )
        )

    def test_nested_dict(self):
        self.assertEqual(
            (
                ('a', 'hello'),
                ('b', (('a', 'hello'), ('b', 'test'))),
                ('c', (1, 2, 3)),
                ('d', ((1, 2), (3, 4), (('a', True), ('b', False))))
            ),
            make_hashable(
                dict(
                    a='hello',
                    b=dict(a='hello', b='test'),
                    c=[1, 2, 3],
                    d=[[1, 2], (3, 4), dict(a=True, b=False)]
                )
            )
        )
