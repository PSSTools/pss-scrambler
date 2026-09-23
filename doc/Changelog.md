
# Unreleased

- Packaging moved entirely to `pyproject.toml`; `setup.py` is removed. The wheel now
  carries `License-Expression: Apache-2.0` (PEP 639) instead of the legacy `License:`
  field, and declares `Requires-Python: >=3.9`, which it never did before.
- The version now lives in `src/pss_scrambler/__version__.py` and is stamped by CI from
  the git tag. **The tag is the version** — there is nothing to bump before tagging, and
  the CI step that compared the tag against a hand-edited `setup.py` is gone with it.
- `--preserve-comments` now works. It was accepted on the command line and never reached
  the translator, so comments were dropped whether or not it was passed.
- `return` and `instance_id` are no longer scrambled. A missing comma in the protected-word
  list silently fused them into one entry that matched nothing, so both were renamed as if
  they were user identifiers — which produced output that was not valid PSS.

# 0.0.2 - 20230406
- Add 'this' as a protected keyword
- Gracefully handle very long identifiers (longer than dictionary entry words)
- Replicate upper-case identifiers in the scrambled output

# 0.0.1
- Initial release