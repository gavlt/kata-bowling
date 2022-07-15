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


@pytest.mark.parametrize("expected,frames,darts_goal", (
    (5, [(2,3)], 15),
    (1, [(9,0),(5,0),(1,1)], 15),
    (5, [(10,None),(10,None)], 5),
    (0, [(0, 0)], 15),
    (1, [(5,4),(4,0),(3,0)], 5),
))
def test_house_rules_darts(expected,frames,darts_goal):
    score = bowl.house_rules(bowl.HouseRulesSpec(darts_goal))
    assert score(frames) == expected