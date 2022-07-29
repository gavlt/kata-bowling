import bowl
from hypothesis import example, given, strategies as st

throw = st.integers(min_value=0, max_value=10)


@given(
    frames=st.lists(
        st.tuples(throw, st.one_of(st.none(), throw)).filter(
            lambda f: f[0] + (f[1] or 0) <= 10
        ),
        max_size=10,
    )
)
@example(frames=[(10, None) for _ in range(10)])
def test_fuzz_score(frames):
    result = bowl.score(frames=frames)
    assert result <= 190
