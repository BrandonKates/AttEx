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
	return convertGrammarTokensToJSON(grammar)

def convertGrammarTokensToJSON(grammar):
	return None
