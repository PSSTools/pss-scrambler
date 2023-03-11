#****************************************************************************
#* TestTranslator.py
#*
#* Copyright 2023 Matthew Ballance and Contributors
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
#*
#* Created on:
#*     Author: 
#****************************************************************************
import unittest
from io import StringIO
from pss_scrambler.translator import Translator
from pss_scrambler.dictionary import dictionary

class TestTranslator(unittest.TestCase):

    def test_smoke(self):
        text = """
        component my_c {
            action my_a {

            }
        }
        """

        t = Translator({}, dictionary, {})
        out = StringIO()
        t.translate(StringIO(text), out)

        print("Result:\n%s\n" % out.getvalue())

    def test_smoke_reference(self):
        text = """
        component my_c {
            action my_a {

            }
            
            action entry_a {
                activity {
                    do my_c::my_a;
                }
            }
        }
        """

        t = Translator({}, dictionary, {})
        out = StringIO()
        t.translate(StringIO(text), out)

        print("Result:\n%s\n" % out.getvalue())

    def test_smoke_retain_entry(self):
        text = """
        component my_c {
            action my_a {

            }
            
            action entry_a {
                activity {
                    do my_c::my_a;
                }
            }
        }
        """

        t = Translator({}, dictionary, {"entry_a"})
        out = StringIO()
        t.translate(StringIO(text), out)

        print("Result:\n%s\n" % out.getvalue())
    pass