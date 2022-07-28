import bowl
from hypothesis import given, strategies as st


@given(frames=st.lists(st.tuples(st.integers(), st.one_of(st.none(), st.integers()))))
def test_fuzz_score(frames):
    bowl.score(frames=frames)
