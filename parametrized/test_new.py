import pytest

from pytest_demo.utils import booleanify, make_hashable


booleanify_test_data = [
    ('false', False),
    (False, True),
    ('FaLse', False),
    ('0', False),
    ('true', True),
    ('tRuE', True),
    ('1', True),
    ('cat', True),
    (True, True),
]

booleanify_ids = [
    'false_string',
    'false_boolean',
    'false_camelcase_string',
    'zero_string',
    'true_string',
    'true_camlecase_string',
    'one_string',
    'random_string',
    'true_boolean'
]


@pytest.mark.parametrize('value, expected_result',
                         booleanify_test_data,
                         ids=booleanify_ids)
def test_booleanify(value, expected_result):
    assert booleanify(value) == expected_result


hashable_test_data = [
    (
        [1, 2, 3],
        (1, 2, 3)
    ),
    (
        {1, 2, 3},
        (1, 2, 3)
    ),
    (
        frozenset([1, 2, 3]),
        frozenset([1, 2, 3])
    ),
    (
        tuple([1, 2, 3]),
        (1, 2, 3)
    ),
    (
        [[1, 2], (3, 4), dict(a=True, b=False)],
        ((1, 2), (3, 4), (('a', True), ('b', False))),
    ),
    (
        tuple([[1, 2], (3, 4), dict(a=True, b=False)]),
        ([1, 2], (3, 4), {'a': True, 'b': False}),
    ),
    (
        dict(
            a='hello',
            b='test'
        ),
        (
            ('a', 'hello'),
            ('b', 'test')
        )
    ),
    (
        dict(
                a='hello',
                b=dict(a='hello', b='test'),
                c=[1, 2, 3],
                d=[[1, 2], (3, 4), dict(a=True, b=False)]
            ),
        (
            ('a', 'hello'),
            ('b', (('a', 'hello'), ('b', 'test'))),
            ('c', (1, 2, 3)),
            ('d', ((1, 2), (3, 4), (('a', True), ('b', False))))
        )
    ),
]

hashable_ids = [
    'list',
    'set',
    'frozenset',
    'tuple',
    'mixed_objects_list',
    'mixed_objects_tuple',
    'dict',
    'nested_dict'
]


@pytest.mark.parametrize('value, expected_result',
                         hashable_test_data,
                         ids=hashable_ids)
def test_make_hashable(value, expected_result):
    assert make_hashable(value) == expected_result
