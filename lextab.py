# lextab.py. This file automatically created by PLY (version 3.10). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('BEGINNING-OF-PROGRAM', 'BEGINNING-OF-EXECUTION', 'END-OF-EXECUTION', 'IF', 'ID', 'END-OF-PROGRAM', 'THEN', 'WHILE', 'NUMBER', 'AS', 'ELSE', 'DO', 'DEFINE-NEW-INSTRUCTION', 'CONDITION', 'BEGIN', 'ITERATE', 'END', 'TIMES'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_INSTRUCTION>MOVE|TURNLEFT|PICKBEEPER|PUTBEEPER|TURNOFF)|(?P<t_CONDITION>FRONT-IS-CLEAR|FRONT-IS-BLOCKED|LEFT-IS-CLEAR|LEFT-IS-BLOCKED|RIGHT-IS-CLEAR|RIGHT-IS-BLOCKED|BACK-IS-CLEAR|BACK-IS-BLOCKED|NEXT-TO-A-BEEPER|NOT-NEXT-TO-A-BEEPER|BEEPER-IN-BEEPER-BAG|NO-BEEPERS-IN-BEEPER-BAG|FACING-NORTH|NOT-FACING-NORTH|FACING-SOUTH|NOT-FACING-SOUTH|FACING-EAST|NOT-FACING-EAST|FACING-WEST|NOT-FACING-WEST)|(?P<t_ID>[a-zA-Z_][a-zA-Z0-9_-]*)|(?P<t_NUMBER>\\d+)|(?P<t_newline>\\n+)', [None, ('t_INSTRUCTION', 'INSTRUCTION'), ('t_CONDITION', 'CONDITION'), ('t_ID', 'ID'), ('t_NUMBER', 'NUMBER'), ('t_newline', 'newline')])]}
_lexstateignore = {'INITIAL': ' \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
