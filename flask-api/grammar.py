import json

from lark import Lark, Transformer, v_args
from lark.lexer import Token


parser = Lark(r"""
        start: _NL? production+
        production: VAR "->" value_list _NL
        value_list: value+ | value+ "|" value_list
        value: VAR | VALUE | COORD
        VAR: /[A-Z]/
        VALUE: /[\w.?!\'-]{2,}|[a-z.?\'-]{1,}/+
        COORD: /\([0-9], [0-9]\)/
        %import common.NEWLINE -> _NL
        %import common.WS_INLINE
        %import common.LETTER
        %ignore WS_INLINE
    """)

@v_args(inline=True)
class CFGTokenTransformer(Transformer):

    def value(self, value_token):
        return value_token

    def value_list(self, *value_list):
        newList = []
        strs = []
        for value in value_list:
            if(type(value) == Token):
                strs.append(value)
            if(type(value) == list):
                newList.extend(value)
        newList.append(strs)
        return newList

    def production(self, key, value):
        return (key, value)

    def start(self, *sections):
        return {name: data for name, data in sections}
    

@v_args(inline=True)
class CFGStringTransformer(Transformer):

    def value(self, value_token):
        return value_token

    def value_list(self, *value_list):
        newList = []
        strs = []
        for value in value_list:
            if(type(value) == Token):
                strs.append(value)
            if(type(value) == list):
                newList.extend(value)
        newList.append(strs)
        return newList

    def production(self, key, value):
        value_out = []
        for lst in value:
            proc = processOneValueList(lst)
            value_out.append(proc)
        return (key, value_out)

    def start(self, *sections):
        return {name.value: data for name, data in sections}
    
def processOneValueList(value_list):
    value_var_list = []
    value = ''
    for token in value_list:
        if token.type == 'VALUE':
            value+= token.value + ' '
        elif token.type == 'VAR' or token.type == 'COORD':
            if len(value)!=0:
                value_var_list.append(value)
                value = ''
            value_var_list.append(token.value)
    if len(value)!=0:
        value_var_list.append(value)
    value_var_list = [i.strip() for i in value_var_list]
    return value_var_list


def parseGrammar(grammar):
	return parser.parse(grammar)

def parseGrammarToString(grammar):
	r = parseGrammar(grammar)
	return CFGStringTransformer().transform(r)

def parseGrammarToTokens(grammar):
	r = parseGrammar(grammar)
	return CFGTokenTransformer().transform(r)


'''
	For example we might just want to pass a single 'S' tag, up to 3 'Q' tags or just give more information about the productions and rules
'''
def custom_rules(rules):
	return None


def getGrammarJSON(grammar):
	grammarString = parseGrammarToString(grammar)
	return json.dumps(grammarString)

if __name__ == "__main__":
	grammar = '''S -> is this C ? Y | how is C different from C ? C specializes C because A | how is C different from C ? C is like C except that A | if not C what is it ? C | i don't know what P is ? P is located at L in I | i don't know what R is ? R is M in I than I | i don't know what B is ? B is H in I .
		C -> deer | bear | dog | cat | panda .
		A -> Q and A | Q .
		Q -> it is M R | it is B | it has N O | its P is M R | its P is B .
		M -> more | less .
		R -> small | furry | long | thin | chubby .
		B -> black | brown | red | white .
		N -> no | .
		O -> Ps | P .
		P -> eye | leg | horn | snout | eye-spot .
		Y -> yes | no .
		L -> (0, 0) .
		I -> imagejpeg | image2jpeg .
		H -> present | absent .
	'''

	print(getGrammarJSON(grammar))


# REGEX: [\w|.!?'-]{2,}|\.|\?|[a-z]{1}|\([0-9], [0-9]\)