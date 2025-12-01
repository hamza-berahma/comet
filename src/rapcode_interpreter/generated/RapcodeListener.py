# Generated from Rapcode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RapcodeParser import RapcodeParser
else:
    from RapcodeParser import RapcodeParser

# This class defines a complete listener for a parse tree produced by RapcodeParser.
class RapcodeListener(ParseTreeListener):

    # Enter a parse tree produced by RapcodeParser#program.
    def enterProgram(self, ctx:RapcodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by RapcodeParser#program.
    def exitProgram(self, ctx:RapcodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by RapcodeParser#AssignStmt.
    def enterAssignStmt(self, ctx:RapcodeParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by RapcodeParser#AssignStmt.
    def exitAssignStmt(self, ctx:RapcodeParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by RapcodeParser#OutputStmt.
    def enterOutputStmt(self, ctx:RapcodeParser.OutputStmtContext):
        pass

    # Exit a parse tree produced by RapcodeParser#OutputStmt.
    def exitOutputStmt(self, ctx:RapcodeParser.OutputStmtContext):
        pass


    # Enter a parse tree produced by RapcodeParser#IfStmt.
    def enterIfStmt(self, ctx:RapcodeParser.IfStmtContext):
        pass

    # Exit a parse tree produced by RapcodeParser#IfStmt.
    def exitIfStmt(self, ctx:RapcodeParser.IfStmtContext):
        pass


    # Enter a parse tree produced by RapcodeParser#LoopStmt.
    def enterLoopStmt(self, ctx:RapcodeParser.LoopStmtContext):
        pass

    # Exit a parse tree produced by RapcodeParser#LoopStmt.
    def exitLoopStmt(self, ctx:RapcodeParser.LoopStmtContext):
        pass


    # Enter a parse tree produced by RapcodeParser#BreakStmt.
    def enterBreakStmt(self, ctx:RapcodeParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by RapcodeParser#BreakStmt.
    def exitBreakStmt(self, ctx:RapcodeParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by RapcodeParser#assignment.
    def enterAssignment(self, ctx:RapcodeParser.AssignmentContext):
        pass

    # Exit a parse tree produced by RapcodeParser#assignment.
    def exitAssignment(self, ctx:RapcodeParser.AssignmentContext):
        pass


    # Enter a parse tree produced by RapcodeParser#output.
    def enterOutput(self, ctx:RapcodeParser.OutputContext):
        pass

    # Exit a parse tree produced by RapcodeParser#output.
    def exitOutput(self, ctx:RapcodeParser.OutputContext):
        pass


    # Enter a parse tree produced by RapcodeParser#breakStatement.
    def enterBreakStatement(self, ctx:RapcodeParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by RapcodeParser#breakStatement.
    def exitBreakStatement(self, ctx:RapcodeParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by RapcodeParser#ifStatement.
    def enterIfStatement(self, ctx:RapcodeParser.IfStatementContext):
        pass

    # Exit a parse tree produced by RapcodeParser#ifStatement.
    def exitIfStatement(self, ctx:RapcodeParser.IfStatementContext):
        pass


    # Enter a parse tree produced by RapcodeParser#loop.
    def enterLoop(self, ctx:RapcodeParser.LoopContext):
        pass

    # Exit a parse tree produced by RapcodeParser#loop.
    def exitLoop(self, ctx:RapcodeParser.LoopContext):
        pass


    # Enter a parse tree produced by RapcodeParser#EqualityExpr.
    def enterEqualityExpr(self, ctx:RapcodeParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by RapcodeParser#EqualityExpr.
    def exitEqualityExpr(self, ctx:RapcodeParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by RapcodeParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:RapcodeParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by RapcodeParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:RapcodeParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by RapcodeParser#RelationalExpr.
    def enterRelationalExpr(self, ctx:RapcodeParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by RapcodeParser#RelationalExpr.
    def exitRelationalExpr(self, ctx:RapcodeParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by RapcodeParser#AtomExpr.
    def enterAtomExpr(self, ctx:RapcodeParser.AtomExprContext):
        pass

    # Exit a parse tree produced by RapcodeParser#AtomExpr.
    def exitAtomExpr(self, ctx:RapcodeParser.AtomExprContext):
        pass


    # Enter a parse tree produced by RapcodeParser#ParenExpr.
    def enterParenExpr(self, ctx:RapcodeParser.ParenExprContext):
        pass

    # Exit a parse tree produced by RapcodeParser#ParenExpr.
    def exitParenExpr(self, ctx:RapcodeParser.ParenExprContext):
        pass


    # Enter a parse tree produced by RapcodeParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:RapcodeParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by RapcodeParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:RapcodeParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by RapcodeParser#UnaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:RapcodeParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by RapcodeParser#UnaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:RapcodeParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by RapcodeParser#IdAtom.
    def enterIdAtom(self, ctx:RapcodeParser.IdAtomContext):
        pass

    # Exit a parse tree produced by RapcodeParser#IdAtom.
    def exitIdAtom(self, ctx:RapcodeParser.IdAtomContext):
        pass


    # Enter a parse tree produced by RapcodeParser#StringAtom.
    def enterStringAtom(self, ctx:RapcodeParser.StringAtomContext):
        pass

    # Exit a parse tree produced by RapcodeParser#StringAtom.
    def exitStringAtom(self, ctx:RapcodeParser.StringAtomContext):
        pass


    # Enter a parse tree produced by RapcodeParser#NumberAtom.
    def enterNumberAtom(self, ctx:RapcodeParser.NumberAtomContext):
        pass

    # Exit a parse tree produced by RapcodeParser#NumberAtom.
    def exitNumberAtom(self, ctx:RapcodeParser.NumberAtomContext):
        pass


    # Enter a parse tree produced by RapcodeParser#BooleanAtom.
    def enterBooleanAtom(self, ctx:RapcodeParser.BooleanAtomContext):
        pass

    # Exit a parse tree produced by RapcodeParser#BooleanAtom.
    def exitBooleanAtom(self, ctx:RapcodeParser.BooleanAtomContext):
        pass


    # Enter a parse tree produced by RapcodeParser#InputCallAtom.
    def enterInputCallAtom(self, ctx:RapcodeParser.InputCallAtomContext):
        pass

    # Exit a parse tree produced by RapcodeParser#InputCallAtom.
    def exitInputCallAtom(self, ctx:RapcodeParser.InputCallAtomContext):
        pass


    # Enter a parse tree produced by RapcodeParser#boolean.
    def enterBoolean(self, ctx:RapcodeParser.BooleanContext):
        pass

    # Exit a parse tree produced by RapcodeParser#boolean.
    def exitBoolean(self, ctx:RapcodeParser.BooleanContext):
        pass


    # Enter a parse tree produced by RapcodeParser#inputCall.
    def enterInputCall(self, ctx:RapcodeParser.InputCallContext):
        pass

    # Exit a parse tree produced by RapcodeParser#inputCall.
    def exitInputCall(self, ctx:RapcodeParser.InputCallContext):
        pass



del RapcodeParser