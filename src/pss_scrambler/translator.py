
from .pss_keywords import pss_keywords

class Translator(object):

    def __init__(self,
                 defined_mappings,
                 new_mapping_dict,
                 ignore_words):
        self.defined_mappings = defined_mappings.copy()
        self.new_mapping_dict = new_mapping_dict
        self.ignore_words = pss_keywords.copy()
        # Suffixes are the markers that denote type
        # categories. Retaining these is helpful
        self.suffixes = {"_a", "_c", "_e", "_s", "_t"}
        for w in ignore_words:
            self.ignore_words.add(w)
        self._c = ""
        self.in_s = None
        self.out_s = None
        pass

    def translate(self, in_s, out_s):
        self.in_s = in_s
        self.out_s = out_s

        while True:
            c = self._getc()
            if c == "":
                break

            if c == "_" or c.isalpha():
                # Should be able to form a token
                token = c
                while True:
                    c = self._getc()
                    if c == "":
                        break
                    elif c.isalnum() or c == '_':
                        token += c
                    else:
                        self._ungetc(c)
                        break
                if token in self.ignore_words:
                    self.out_s.write(token)
                elif token in self.defined_mappings.keys():
                    self.out_s.write(self.defined_mappings[token])
                else:
                    # Need o form a new mapping
                    token_xl = self.map_token(token)
                    self.out_s.write(token_xl)
            else:
                self.out_s.write(c)

        pass

    def _getc(self):
        if self._c != "":
            ret = self._c
            self._c = ""
            return ret
        else:
            return self.in_s.read(1)
    
    def _ungetc(self, c):
        self._c = c

    def map_token(self, token):
        remap_i = len(token)-1

        while remap_i < len(self.new_mapping_dict) and len(self.new_mapping_dict[remap_i]) == 0:
            remap_i += 1

        token_xl_i = 0 # TODO: randomly select
        token_xl = self.new_mapping_dict[remap_i][token_xl_i]
        self.new_mapping_dict[remap_i].pop(token_xl_i)

        for s in self.suffixes:
            if token.endswith(s):
                token_xl += s
                break
        
        self.defined_mappings[token] = token_xl

        return token_xl
