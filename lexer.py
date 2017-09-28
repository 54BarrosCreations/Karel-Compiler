# ------------------------------------------------------------
# Lexer.py
#
# Lexer for the Karel language with support of &&, || and !
#
# Edgardo Gutierrez Trujillo
# Francisco Barros
# ------------------------------------------------------------
reserved = {
    'IF' : 'IF',
    'THEN' : 'THEN',
    'ELSE' : 'ELSE',
    'WHILE' : 'WHILE',
    'DO' : 'DO',
    'AS' : 'AS',
    'BEGINNING-OF-PROGRAM': 'BEGINNING-OF-PROGRAM',
    'BEGINNING-OF-EXECUTION' : 'BEGINNING-OF-EXECUTION',
    'END-OF-EXECUTION' : 'END-OF-EXECUTION',
    'END-OF-PROGRAM' : 'END-OF-PROGRAM',
    'DEFINE-NEW-INSTRUCTION' : 'DEFINE-NEW-INSTRUCTION',
    'BEGIN' : 'BEGIN',
    'END' : 'END',
    'ITERATE' : 'ITERATE',
    'TIMES' : 'TIMES',
}

tokens = [
    'NUMBER',
    'ID',
    'CONDITION'
] + list(reserved.values())

# t_CONDITION = r'FRONT-IS-CLEAR|FRONT-IS-BLOCKED|LEFT-IS-CLEAR|LEFT-IS-BLOCKED|' \
#                'RIGHT-IS-CLEAR|RIGHT-IS-BLOCKED|BACK-IS-CLEAR|BACK-IS-BLOCKED|' \
#                'NEXT-TO-A-BEEPER|NOT-NEXT-TO-A-BEEPER|BEEPER-IN-BEEPER-BAG|' \
#                'NO-BEEPERS-IN-BEEPER-BAG|FACING-NORTH|NOT-FACING-NORTH|' \
#                'FACING-SOUTH|NOT-FACING-SOUTH|FACING-EAST|NOT-FACING-EAST|' \
#                'FACING-WEST|NOT-FACING-WEST'


# A regular expression rule with some action code
def t_INSTRUCTION(t):
    r'MOVE|TURNLEFT|PICKBEEPER|PUTBEEPER|TURNOFF'
    return t

def t_CONDITION(t):
    r'FRONT-IS-CLEAR|FRONT-IS-BLOCKED|LEFT-IS-CLEAR|LEFT-IS-BLOCKED|' \
    'RIGHT-IS-CLEAR|RIGHT-IS-BLOCKED|BACK-IS-CLEAR|BACK-IS-BLOCKED|' \
    'NEXT-TO-A-BEEPER|NOT-NEXT-TO-A-BEEPER|BEEPER-IN-BEEPER-BAG|' \
    'NO-BEEPERS-IN-BEEPER-BAG|FACING-NORTH|NOT-FACING-NORTH|' \
    'FACING-SOUTH|NOT-FACING-SOUTH|FACING-EAST|NOT-FACING-EAST|' \
    'FACING-WEST|NOT-FACING-WEST'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_-]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
