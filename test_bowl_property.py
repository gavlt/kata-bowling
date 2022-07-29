import bowl
from hypothesis import example, given, strategies as st

throw = st.integers(min_value=0, max_value=10)
frame = (
    st.tuples(throw, st.one_of(st.none(), throw))
    .filter(lambda f: f[0] + (f[1] or 0) <= 10)
    .filter(lambda f: f[0] == 10 if f[1] is None else f[0] < 10)
)


@given(
    frames=st.lists(
        frame,
        max_size=10,
    )
)
@example(frames=[(10, None) for _ in range(10)])
@example(frames=[(0, 10) for _ in range(10)])
@example(frames=[(0, 10), (10, None)] * 5)
def test_fuzz_score(frames):
    result = bowl.score(frames=frames)
    assert isinstance(result, int)
    assert result >= 0
    assert result <= 190
