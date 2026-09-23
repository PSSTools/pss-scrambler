#****************************************************************************
#* __version__.py
#*
#* Copyright 2026 Matthew Ballance and Contributors
#*
#* Licensed under the Apache License, Version 2.0 (the "License"); you may
#* not use this file except in compliance with the License.
#* You may obtain a copy of the License at:
#*
#*   http://www.apache.org/licenses/LICENSE-2.0
#*
#* Unless required by applicable law or agreed to in writing, software
#* distributed under the License is distributed on an "AS IS" BASIS,
#* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#* See the License for the specific language governing permissions and
#* limitations under the License.
#****************************************************************************

# THE TAG IS THE VERSION. CI substitutes the tag into the line below on a `v*`
# build, so a release is a tag and nothing else -- there is no version to bump
# here before tagging, and editing this value does not change what gets
# released. This replaced a hand-maintained `version="0.0.2"` in setup.py plus
# a CI step that compared the two and failed the release when they disagreed;
# the thing that check guarded against was forgetting to hand-edit a file,
# which is a step that should not exist.
#
# 0.0.0 is deliberately not a plausible release. It is the baseline for dev
# artifacts, which CI stamps as 0.0.0.dev<run-id>+gh -- lower than every real
# release under PEP 440, and carrying a LOCAL VERSION SEGMENT (the part after
# the '+') that PyPI rejects outright at the tool. Dev builds are therefore
# unpublishable rather than merely unpublished: the tag gate on the publish
# step is the control, and this is the backstop for the day someone edits that
# gate. PyPI holds 0.0.2.4632135087 from before that was true.
#
# ONE LITERAL ASSIGNMENT, ON ONE LINE, and that shape is load-bearing.
# pyproject.toml reads this through `[tool.setuptools.dynamic] version =
# {attr = ...}`, which parses the file statically when the value is a literal
# and otherwise falls back to IMPORTING it. There is no `__init__.py` in this
# package (it has always been an implicit namespace package), so the import
# path is the one to stay off. pssparser splits this into BASE + SUFFIX
# because its setup.py exec'd the file; nothing here execs anything, so the
# simpler form is both sufficient and safer.
__version__ = "0.0.0"
