from lark import Lark, Transformer

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
r = parser.parse(grammar + '\n')


@lark.v_args(inline=True)
class CFGTransformer(Transformer):

    def value(self, value_token):
        return value_token

    def value_list(self, *value_list):
        newList = []
        strs = []
        for value in value_list:
            if(type(value) == lark.lexer.Token):
                strs.append(value)
            if(type(value) == list):
                newList.extend(value)
        newList.append(strs)
        return newList

    def production(self, key, value):
        return (key, value)

    def start(self, *sections):
        return {name: data for name, data in sections}
    
transformer = CFGTransformer()
transOut = transformer.transform(r)


def parseGrammar(grammar):
	r = parser.parse(grammar)
	transformer = CFGTransformer()
	return transformer.transform(r)