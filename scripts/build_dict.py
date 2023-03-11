#****************************************************************************
#* build_dict.py
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
import os
import sys

dictionary = []

scripts_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(scripts_dir, "google-10000-english-no-swears.txt"), "r") as fp:

    for line in fp.readlines():
        line = line.strip()

        while len(dictionary) < len(line):
            dictionary.append(None)
        
        if dictionary[len(line)-1] is None:
            dictionary[len(line)-1] = []
        
        dictionary[len(line)-1].append(line)

max_words = 6000
n_words = 0
print("dictionary = [")
for d in dictionary:
    if d is None:
        print("None,")
    else:
        d.sort()
        sys.stdout.write("[")
        n_words += len(d)
#        print("%d words up to length %d" % (n_words, len(d[0])))
        line_l = 1
        for w in d:
            if line_l > 76:
                sys.stdout.write("\n")
                line_l = 0
            sys.stdout.write("\"%s\", " % w)
            line_l += len(w) + 4
        sys.stdout.write("],\n")

    if n_words > max_words:
        break
print("]")

