# run the tests:
pytest .

# run with verbosity and stdout
pytest . -v --capture=no

# unit test with coverage:
pytest --cov-report=term-missing --cov=bowl --cov-branch

# auto-generate a hypothesis test for bowl.score:
hypothesis write bowl.score

# run the tests, with hypothesis stats:
pytest . --hypothesis-show-statistics

# run with more examples:
pytest . --hypothesis-show-statistics --hypothesis-profile=1k
pytest . --hypothesis-show-statistics --hypothesis-profile=10k

# run with verbose hypothesis (--capture=no aka -s is a pytest arg to print stdout):
pytest . --hypothesis-show-statistics --hypothesis-verbosity=verbose --capture=no
