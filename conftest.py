import os
from hypothesis import settings

settings.register_profile("1k", max_examples=1000)
settings.register_profile("10k", max_examples=10000)
settings.load_profile(os.getenv("HYPOTHESIS_PROFILE", "default"))
