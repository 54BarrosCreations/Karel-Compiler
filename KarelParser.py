from builtins import RuntimeError
import lexer as rules
import ply.lex as lex


class KarelParser:

    def __init__(self,lexer):
        self.lexer = lexer

    def parse(self):
        self._program()
        print("Todo bien")

    def _program(self):
        if self._demand('BEGINNING-OF-PROGRAM'):
            self._definition_many()
            if self._demand('BEGINNING-OF-EXECUTION'):
                self._statement_many()
                if self._demand('END-OF-EXECUTION'):
                    if not self._demand('END-OF-PROGRAM'):
                        error = 'Expected END-OF-PROGRAM in line {}'.format(lexer.lineno)
                        raise RuntimeError(error)
                else:
                    error = 'Expected END-OF-EXECUTION in line {}'.format(lexer.lineno)
                    raise RuntimeError(error)
            else:
                error = 'Expected BEGINNING-OF-EXECUTION in line {}'.format(lexer.lineno)
                raise RuntimeError(error)
        else:
            error = 'Expected BEGINNING-OF-PROGRAM in line {}'.format(lexer.lineno)
            raise RuntimeError(error)


    def _definition_many(self):
        if self._verify('DEFINE-NEW-INSTRUCTION'):
            self._definition()
            self._definition_prima()

    def _definition_prima(self):
        if self._verify('DEFINE-NEW-INSTRUCTION'):
            self._definition()
            self._definition_prima()

    def _definition(self):
        if self._demand('DEFINE-NEW-INSTRUCTION'):
            if self._demand('ID'):
                if self._demand('AS'):
                    self._statement()
                else:
                    error = 'Expected AS in line {}'.format(lexer.lineno)
                    raise RuntimeError(error)
            else:
                error = 'Expected ID in line {}'.format(lexer.lineno)
                raise RuntimeError(error)
        else:
            error = 'Expected DEFINE-NEW-INSTRUCTION in line {}'.format(lexer.lineno)
            raise RuntimeError(error)

    def _statement_many(self):
        if self._verify('BEGIN'):
            self._statement()
        elif self._verify('ITERATE'):
            self._statement()
        elif self._verify('WHILE'):
            self._statement()
        elif self._verify('IF'):
            self._statement()
        elif self._verify('INSTRUCTION'):
            self._statement()
        elif self._verify('ID'):
            error = 'Expected a STATEMENT in line {}'.format(lexer.lineno)
            raise RuntimeError(error)

    def _statement(self):
        if self._verify('BEGIN'):
            self._block()
        elif self._verify('ITERATE'):
            self._iteration()
        elif self._verify('WHILE'):
            self._loop()
        elif self._verify('IF'):
            self._conditional()
        elif self._verify('INSTRUCTION'):
            self._instruction()
        else:
            error = 'Expected a STATEMENT in line {}'.format(lexer.lineno)
            raise RuntimeError(error)
        self._statement_prima()

    def _statement_prima(self):
        if self._verify('BEGIN'):
            self._statement()
        elif self._verify('ITERATE'):
            self._statement()
        elif self._verify('WHILE'):
            self._statement()
        elif self._verify('IF'):
            self._statement()
        elif self._verify('INSTRUCTION'):
            self._statement()
        elif self._verify('ID'):
            error = 'Expected a STATEMENT in line {}'.format(lexer.lineno)
            raise RuntimeError(error)

    def _block(self):
        if self._demand('BEGIN'):
            self._statement_many()
            if not self._demand('END'):
                error = 'Expected END in line {}'.format(lexer.lineno)
                raise RuntimeError(error)
        else:
            error = 'Expected a BEGIN in line {}'.format(lexer.lineno)
            raise RuntimeError(error)

    def _iteration(self):
        if self._demand('ITERATE'):
            if self._demand('NUMBER'):
                if self._demand('TIMES'):
                    self._statement()
                else:
                    error = 'Expected a TIMES in line {}'.format(lexer.lineno)
                    raise RuntimeError(error)
            else:
                error = 'Expected a NUMBER in line {}'.format(lexer.lineno)
                raise RuntimeError(error)
        else:
            error = 'Expected a ITERATE in line {}'.format(lexer.lineno)
            raise RuntimeError(error)

    def _loop(self):
        if self._demand('WHILE'):
            if self._demand('CONDITION'):
                if self._demand('DO'):
                    self._statement()
                else:
                    error = 'Expected a DO in line {}'.format(lexer.lineno)
                    raise RuntimeError(error)
            else:
                error = 'Expected a CONDITION in line {}'.format(lexer.lineno)
                raise RuntimeError(error)
        else:
            error = 'Expected a WHILE in line {}'.format(lexer.lineno)
            raise RuntimeError(error)

    def _conditional(self):
        if self._demand('IF'):
            if self._demand('CONDITION'):
                if self._demand('THEN'):
                    self._statement()
                else:
                    error = 'Expected a THEN in line {}'.format(lexer.lineno)
                    raise RuntimeError(error)
            else:
                error = 'Expected a CONDITION in line {}'.format(lexer.lineno)
                raise RuntimeError(error)
            if self._verify('ELSE'):
                self._else_conditional()
        else:
            error = 'Expected a IF line {}'.format(lexer.lineno)
            raise RuntimeError(error)

    def _else_conditional(self):
        if self._demand('ELSE'):
            self._statement()
        else:
            error = 'Expected ELSE in line {}'.format(lexer.lineno)
            raise RuntimeError(error)


    def _instruction(self):
        if not self._demand('INSTRUCTION'):
            error = 'Expected a INSTRUCTION in line {}'.format(lexer.lineno)
            raise RuntimeError(error)

    def _demand(self,token):
        try:
            if token == self.lexer.token().__getattribute__('type'):
                return True
            else:
                return False
        except:
            return False
    def _verify(self, token):
        clone = self.lexer.clone()
        try:
            if token == clone.token().__getattribute__('type'):
                return True
            else:
                return False
        except:
            return False

lexer = lex.lex(module=rules, optimize=1)

data= """
BEGINNING-OF-PROGRAM
    DEFINE-NEW-INSTRUCTION turnright AS
        ITERATE 3 TIMES
            TURNLEFT

    BEGINNING-OF-EXECUTION
        WHILE NOT-NEXT-TO-A-BEEPER DO
            BEGIN
                IF RIGHT-IS-CLEAR
                THEN TURNLEFT
                ELSE
                    WHILE FRONT-IS-BLOCKED DO
                        TURNLEFT
                MOVE
            END
        TURNOFF
    END-OF-EXECUTION
END-OF-PROGRAM
      """
lexer.input(data)

k = KarelParser(lexer)
k.parse()

#
#
#
#