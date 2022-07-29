import pytest
import bowl


@pytest.mark.parametrize(
    "expected,frames",
    (
        (5, [(2, 3)]),
        (6, [(3, 3)]),
        (10, [(10, None)]),
        (0, []),
        (4, [(1, 1), (1, 1)]),
        (14, [(10, None), (1, 1)]),
        (13, [(4, 6), (1, 1)]),
        (19, [(1, 1), (6, 4), (2, 3)]),
        (30, [(10, None), (10, None)]),
        (100, [(0, 10) for _ in range(10)]),
        (190, [(10, None) for _ in range(10)]),
        (190, [(0, 10), (10, None)] * 5),
        (190, [(10, None), (0, 10)] * 5),
    ),
)
def test_sum_score(expected, frames):
    assert bowl.score(frames) == expected


@pytest.mark.parametrize(
    "expected,frames,darts_goal",
    (
        (5, [(2, 3)], 15),
        (1, [(9, 0), (5, 0), (1, 1)], 15),
        (5, [(10, None), (10, None)], 5),
        (0, [(0, 0)], 15),
        (1, [(5, 4), (4, 0), (3, 0)], 5),
    ),
)
@pytest.mark.parametrize("house_rules_fn", (bowl.house_rules_darts, bowl.house_rules))
def test_house_rules(expected, frames, darts_goal, house_rules_fn):
    score = house_rules_fn(bowl.HouseRulesSpec(darts_goal))
    assert score(frames) == expected
