import pytest
import bowl


@pytest.mark.parametrize("expected,frames", (
    (5, [(2,3)]),
    (6, [(3,3)]),
    (10, [(10,None)]),
    (0, []),
    (4, [(1,1), (1,1)]),
    (14, [(10,None), (1,1)]),
    (13, [(4,6), (1,1)]),
    (19, [(1, 1), (6, 4), (2, 3)]),
    (30, [(10, None), (10, None)])
))
def test_sum_score(expected,frames):
    assert bowl.score(frames) == expected
