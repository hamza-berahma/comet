# Generated from Rapcode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RapcodeParser import RapcodeParser
else:
    from RapcodeParser import RapcodeParser

# This class defines a complete generic visitor for a parse tree produced by RapcodeParser.

class RapcodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RapcodeParser#program.
    def visitProgram(self, ctx:RapcodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#AssignStmt.
    def visitAssignStmt(self, ctx:RapcodeParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#OutputStmt.
    def visitOutputStmt(self, ctx:RapcodeParser.OutputStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#IfStmt.
    def visitIfStmt(self, ctx:RapcodeParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#LoopStmt.
    def visitLoopStmt(self, ctx:RapcodeParser.LoopStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#BreakStmt.
    def visitBreakStmt(self, ctx:RapcodeParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#assignment.
    def visitAssignment(self, ctx:RapcodeParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#output.
    def visitOutput(self, ctx:RapcodeParser.OutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#breakStatement.
    def visitBreakStatement(self, ctx:RapcodeParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#ifStatement.
    def visitIfStatement(self, ctx:RapcodeParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#loop.
    def visitLoop(self, ctx:RapcodeParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#EqualityExpr.
    def visitEqualityExpr(self, ctx:RapcodeParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:RapcodeParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#RelationalExpr.
    def visitRelationalExpr(self, ctx:RapcodeParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#AtomExpr.
    def visitAtomExpr(self, ctx:RapcodeParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#ParenExpr.
    def visitParenExpr(self, ctx:RapcodeParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:RapcodeParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#UnaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:RapcodeParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#IdAtom.
    def visitIdAtom(self, ctx:RapcodeParser.IdAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#StringAtom.
    def visitStringAtom(self, ctx:RapcodeParser.StringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#NumberAtom.
    def visitNumberAtom(self, ctx:RapcodeParser.NumberAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#BooleanAtom.
    def visitBooleanAtom(self, ctx:RapcodeParser.BooleanAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#InputCallAtom.
    def visitInputCallAtom(self, ctx:RapcodeParser.InputCallAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#boolean.
    def visitBoolean(self, ctx:RapcodeParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RapcodeParser#inputCall.
    def visitInputCall(self, ctx:RapcodeParser.InputCallContext):
        return self.visitChildren(ctx)



del RapcodeParser