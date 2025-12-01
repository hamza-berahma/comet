# Generated from Rapcode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,32,135,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,3,1,33,8,1,1,1,1,1,3,1,37,8,1,1,1,1,1,3,1,41,
        8,1,1,1,1,1,3,1,45,8,1,1,1,1,1,3,1,49,8,1,3,1,51,8,1,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,4,1,4,1,5,1,5,3,5,64,8,5,1,5,1,5,1,5,5,5,69,8,
        5,10,5,12,5,72,9,5,1,5,1,5,5,5,76,8,5,10,5,12,5,79,9,5,3,5,81,8,
        5,1,5,1,5,1,6,1,6,5,6,87,8,6,10,6,12,6,90,9,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,3,7,102,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,5,7,116,8,7,10,7,12,7,119,9,7,1,8,1,8,1,8,1,8,
        1,8,3,8,126,8,8,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,0,1,14,11,
        0,2,4,6,8,10,12,14,16,18,20,0,5,1,0,21,22,1,0,23,26,1,0,16,17,1,
        0,18,20,1,0,13,14,148,0,25,1,0,0,0,2,50,1,0,0,0,4,52,1,0,0,0,6,56,
        1,0,0,0,8,59,1,0,0,0,10,61,1,0,0,0,12,84,1,0,0,0,14,101,1,0,0,0,
        16,125,1,0,0,0,18,127,1,0,0,0,20,129,1,0,0,0,22,24,3,2,1,0,23,22,
        1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,
        27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,32,3,4,2,0,31,33,5,32,
        0,0,32,31,1,0,0,0,32,33,1,0,0,0,33,51,1,0,0,0,34,36,3,6,3,0,35,37,
        5,32,0,0,36,35,1,0,0,0,36,37,1,0,0,0,37,51,1,0,0,0,38,40,3,10,5,
        0,39,41,5,32,0,0,40,39,1,0,0,0,40,41,1,0,0,0,41,51,1,0,0,0,42,44,
        3,12,6,0,43,45,5,32,0,0,44,43,1,0,0,0,44,45,1,0,0,0,45,51,1,0,0,
        0,46,48,3,8,4,0,47,49,5,32,0,0,48,47,1,0,0,0,48,49,1,0,0,0,49,51,
        1,0,0,0,50,30,1,0,0,0,50,34,1,0,0,0,50,38,1,0,0,0,50,42,1,0,0,0,
        50,46,1,0,0,0,51,3,1,0,0,0,52,53,5,27,0,0,53,54,5,15,0,0,54,55,3,
        14,7,0,55,5,1,0,0,0,56,57,5,10,0,0,57,58,3,14,7,0,58,7,1,0,0,0,59,
        60,5,9,0,0,60,9,1,0,0,0,61,63,5,3,0,0,62,64,5,12,0,0,63,62,1,0,0,
        0,63,64,1,0,0,0,64,65,1,0,0,0,65,66,3,14,7,0,66,70,5,4,0,0,67,69,
        3,2,1,0,68,67,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,
        71,80,1,0,0,0,72,70,1,0,0,0,73,77,5,5,0,0,74,76,3,2,1,0,75,74,1,
        0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,81,1,0,0,0,79,
        77,1,0,0,0,80,73,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,83,5,6,0,
        0,83,11,1,0,0,0,84,88,5,7,0,0,85,87,3,2,1,0,86,85,1,0,0,0,87,90,
        1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,90,88,1,0,0,0,
        91,92,5,8,0,0,92,13,1,0,0,0,93,94,6,7,-1,0,94,95,5,17,0,0,95,102,
        3,14,7,3,96,102,3,16,8,0,97,98,5,1,0,0,98,99,3,14,7,0,99,100,5,2,
        0,0,100,102,1,0,0,0,101,93,1,0,0,0,101,96,1,0,0,0,101,97,1,0,0,0,
        102,117,1,0,0,0,103,104,10,7,0,0,104,105,7,0,0,0,105,116,3,14,7,
        8,106,107,10,6,0,0,107,108,7,1,0,0,108,116,3,14,7,7,109,110,10,5,
        0,0,110,111,7,2,0,0,111,116,3,14,7,6,112,113,10,4,0,0,113,114,7,
        3,0,0,114,116,3,14,7,5,115,103,1,0,0,0,115,106,1,0,0,0,115,109,1,
        0,0,0,115,112,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,
        0,0,0,118,15,1,0,0,0,119,117,1,0,0,0,120,126,5,27,0,0,121,126,5,
        29,0,0,122,126,5,28,0,0,123,126,3,18,9,0,124,126,3,20,10,0,125,120,
        1,0,0,0,125,121,1,0,0,0,125,122,1,0,0,0,125,123,1,0,0,0,125,124,
        1,0,0,0,126,17,1,0,0,0,127,128,7,4,0,0,128,19,1,0,0,0,129,130,5,
        11,0,0,130,131,5,1,0,0,131,132,3,14,7,0,132,133,5,2,0,0,133,21,1,
        0,0,0,16,25,32,36,40,44,48,50,63,70,77,80,88,101,115,117,125
    ]

class RapcodeParser ( Parser ):

    grammarFileName = "Rapcode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'IF'", "'THEN'", "'ELSE'", 
                     "'ENDIF'", "'LOOP'", "'ENDLOOP'", "'BREAK'", "'OUTPUT'", 
                     "'INPUT'", "'NOT'", "'TRUE'", "'FALSE'", "':='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'='", "'!='", "'>'", "'>='", 
                     "'<'", "'<='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "IF", "THEN", 
                      "ELSE", "ENDIF", "LOOP", "ENDLOOP", "BREAK", "OUTPUT", 
                      "INPUT", "NOT", "TRUE", "FALSE", "ASSIGN", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", "GT", "GTE", 
                      "LT", "LTE", "IDENTIFIER", "NUMBER", "STRING", "COMMENT", 
                      "WS", "SEMI" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_output = 3
    RULE_breakStatement = 4
    RULE_ifStatement = 5
    RULE_loop = 6
    RULE_expr = 7
    RULE_atom = 8
    RULE_boolean = 9
    RULE_inputCall = 10

    ruleNames =  [ "program", "statement", "assignment", "output", "breakStatement", 
                   "ifStatement", "loop", "expr", "atom", "boolean", "inputCall" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    IF=3
    THEN=4
    ELSE=5
    ENDIF=6
    LOOP=7
    ENDLOOP=8
    BREAK=9
    OUTPUT=10
    INPUT=11
    NOT=12
    TRUE=13
    FALSE=14
    ASSIGN=15
    ADD=16
    SUB=17
    MUL=18
    DIV=19
    MOD=20
    EQ=21
    NEQ=22
    GT=23
    GTE=24
    LT=25
    LTE=26
    IDENTIFIER=27
    NUMBER=28
    STRING=29
    COMMENT=30
    WS=31
    SEMI=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(RapcodeParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RapcodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(RapcodeParser.StatementContext,i)


        def getRuleIndex(self):
            return RapcodeParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = RapcodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134219400) != 0):
                self.state = 22
                self.statement()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(RapcodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RapcodeParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifStatement(self):
            return self.getTypedRuleContext(RapcodeParser.IfStatementContext,0)

        def SEMI(self):
            return self.getToken(RapcodeParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)


    class LoopStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def loop(self):
            return self.getTypedRuleContext(RapcodeParser.LoopContext,0)

        def SEMI(self):
            return self.getToken(RapcodeParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStmt" ):
                listener.enterLoopStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStmt" ):
                listener.exitLoopStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStmt" ):
                return visitor.visitLoopStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignment(self):
            return self.getTypedRuleContext(RapcodeParser.AssignmentContext,0)

        def SEMI(self):
            return self.getToken(RapcodeParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)


    class BreakStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def breakStatement(self):
            return self.getTypedRuleContext(RapcodeParser.BreakStatementContext,0)

        def SEMI(self):
            return self.getToken(RapcodeParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStmt" ):
                listener.enterBreakStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStmt" ):
                listener.exitBreakStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)


    class OutputStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def output(self):
            return self.getTypedRuleContext(RapcodeParser.OutputContext,0)

        def SEMI(self):
            return self.getToken(RapcodeParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutputStmt" ):
                listener.enterOutputStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutputStmt" ):
                listener.exitOutputStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputStmt" ):
                return visitor.visitOutputStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = RapcodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                localctx = RapcodeParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.assignment()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 31
                    self.match(RapcodeParser.SEMI)


                pass
            elif token in [10]:
                localctx = RapcodeParser.OutputStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.output()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 35
                    self.match(RapcodeParser.SEMI)


                pass
            elif token in [3]:
                localctx = RapcodeParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.ifStatement()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 39
                    self.match(RapcodeParser.SEMI)


                pass
            elif token in [7]:
                localctx = RapcodeParser.LoopStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.loop()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 43
                    self.match(RapcodeParser.SEMI)


                pass
            elif token in [9]:
                localctx = RapcodeParser.BreakStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.breakStatement()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 47
                    self.match(RapcodeParser.SEMI)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(RapcodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(RapcodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(RapcodeParser.ExprContext,0)


        def getRuleIndex(self):
            return RapcodeParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = RapcodeParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(RapcodeParser.IDENTIFIER)
            self.state = 53
            self.match(RapcodeParser.ASSIGN)
            self.state = 54
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUTPUT(self):
            return self.getToken(RapcodeParser.OUTPUT, 0)

        def expr(self):
            return self.getTypedRuleContext(RapcodeParser.ExprContext,0)


        def getRuleIndex(self):
            return RapcodeParser.RULE_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput" ):
                return visitor.visitOutput(self)
            else:
                return visitor.visitChildren(self)




    def output(self):

        localctx = RapcodeParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_output)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(RapcodeParser.OUTPUT)
            self.state = 57
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(RapcodeParser.BREAK, 0)

        def getRuleIndex(self):
            return RapcodeParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = RapcodeParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(RapcodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(RapcodeParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(RapcodeParser.ExprContext,0)


        def THEN(self):
            return self.getToken(RapcodeParser.THEN, 0)

        def ENDIF(self):
            return self.getToken(RapcodeParser.ENDIF, 0)

        def NOT(self):
            return self.getToken(RapcodeParser.NOT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RapcodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(RapcodeParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(RapcodeParser.ELSE, 0)

        def getRuleIndex(self):
            return RapcodeParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = RapcodeParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(RapcodeParser.IF)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 62
                self.match(RapcodeParser.NOT)


            self.state = 65
            self.expr(0)
            self.state = 66
            self.match(RapcodeParser.THEN)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134219400) != 0):
                self.state = 67
                self.statement()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 73
                self.match(RapcodeParser.ELSE)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134219400) != 0):
                    self.state = 74
                    self.statement()
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 82
            self.match(RapcodeParser.ENDIF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOOP(self):
            return self.getToken(RapcodeParser.LOOP, 0)

        def ENDLOOP(self):
            return self.getToken(RapcodeParser.ENDLOOP, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RapcodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(RapcodeParser.StatementContext,i)


        def getRuleIndex(self):
            return RapcodeParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = RapcodeParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(RapcodeParser.LOOP)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 134219400) != 0):
                self.state = 85
                self.statement()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self.match(RapcodeParser.ENDLOOP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RapcodeParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class EqualityExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RapcodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(RapcodeParser.ExprContext,i)

        def EQ(self):
            return self.getToken(RapcodeParser.EQ, 0)
        def NEQ(self):
            return self.getToken(RapcodeParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpr" ):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpr" ):
                listener.exitEqualityExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RapcodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(RapcodeParser.ExprContext,i)

        def MUL(self):
            return self.getToken(RapcodeParser.MUL, 0)
        def DIV(self):
            return self.getToken(RapcodeParser.DIV, 0)
        def MOD(self):
            return self.getToken(RapcodeParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelationalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RapcodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(RapcodeParser.ExprContext,i)

        def LT(self):
            return self.getToken(RapcodeParser.LT, 0)
        def LTE(self):
            return self.getToken(RapcodeParser.LTE, 0)
        def GT(self):
            return self.getToken(RapcodeParser.GT, 0)
        def GTE(self):
            return self.getToken(RapcodeParser.GTE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(RapcodeParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomExpr" ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomExpr" ):
                listener.exitAtomExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RapcodeParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RapcodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(RapcodeParser.ExprContext,i)

        def ADD(self):
            return self.getToken(RapcodeParser.ADD, 0)
        def SUB(self):
            return self.getToken(RapcodeParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(RapcodeParser.SUB, 0)
        def expr(self):
            return self.getTypedRuleContext(RapcodeParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusExpr" ):
                listener.enterUnaryMinusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusExpr" ):
                listener.exitUnaryMinusExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinusExpr" ):
                return visitor.visitUnaryMinusExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RapcodeParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                localctx = RapcodeParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 94
                self.match(RapcodeParser.SUB)
                self.state = 95
                self.expr(3)
                pass
            elif token in [11, 13, 14, 27, 28, 29]:
                localctx = RapcodeParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 96
                self.atom()
                pass
            elif token in [1]:
                localctx = RapcodeParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 97
                self.match(RapcodeParser.T__0)
                self.state = 98
                self.expr(0)
                self.state = 99
                self.match(RapcodeParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 117
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 115
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = RapcodeParser.EqualityExprContext(self, RapcodeParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 103
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 104
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 105
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = RapcodeParser.RelationalExprContext(self, RapcodeParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 106
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 107
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 108
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = RapcodeParser.AddSubExprContext(self, RapcodeParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 109
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 110
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 111
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = RapcodeParser.MulDivExprContext(self, RapcodeParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 112
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 113
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 114
                        self.expr(5)
                        pass

             
                self.state = 119
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RapcodeParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumberAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(RapcodeParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberAtom" ):
                listener.enterNumberAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberAtom" ):
                listener.exitNumberAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberAtom" ):
                return visitor.visitNumberAtom(self)
            else:
                return visitor.visitChildren(self)


    class InputCallAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def inputCall(self):
            return self.getTypedRuleContext(RapcodeParser.InputCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputCallAtom" ):
                listener.enterInputCallAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputCallAtom" ):
                listener.exitInputCallAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputCallAtom" ):
                return visitor.visitInputCallAtom(self)
            else:
                return visitor.visitChildren(self)


    class StringAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(RapcodeParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringAtom" ):
                listener.enterStringAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringAtom" ):
                listener.exitStringAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringAtom" ):
                return visitor.visitStringAtom(self)
            else:
                return visitor.visitChildren(self)


    class BooleanAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolean(self):
            return self.getTypedRuleContext(RapcodeParser.BooleanContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanAtom" ):
                listener.enterBooleanAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanAtom" ):
                listener.exitBooleanAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanAtom" ):
                return visitor.visitBooleanAtom(self)
            else:
                return visitor.visitChildren(self)


    class IdAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RapcodeParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(RapcodeParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdAtom" ):
                listener.enterIdAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdAtom" ):
                listener.exitIdAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdAtom" ):
                return visitor.visitIdAtom(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = RapcodeParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_atom)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                localctx = RapcodeParser.IdAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(RapcodeParser.IDENTIFIER)
                pass
            elif token in [29]:
                localctx = RapcodeParser.StringAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.match(RapcodeParser.STRING)
                pass
            elif token in [28]:
                localctx = RapcodeParser.NumberAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.match(RapcodeParser.NUMBER)
                pass
            elif token in [13, 14]:
                localctx = RapcodeParser.BooleanAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.boolean()
                pass
            elif token in [11]:
                localctx = RapcodeParser.InputCallAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 124
                self.inputCall()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(RapcodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(RapcodeParser.FALSE, 0)

        def getRuleIndex(self):
            return RapcodeParser.RULE_boolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)




    def boolean(self):

        localctx = RapcodeParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(RapcodeParser.INPUT, 0)

        def expr(self):
            return self.getTypedRuleContext(RapcodeParser.ExprContext,0)


        def getRuleIndex(self):
            return RapcodeParser.RULE_inputCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputCall" ):
                listener.enterInputCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputCall" ):
                listener.exitInputCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputCall" ):
                return visitor.visitInputCall(self)
            else:
                return visitor.visitChildren(self)




    def inputCall(self):

        localctx = RapcodeParser.InputCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_inputCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(RapcodeParser.INPUT)
            self.state = 130
            self.match(RapcodeParser.T__0)
            self.state = 131
            self.expr(0)
            self.state = 132
            self.match(RapcodeParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




