from antlr4.Token import CommonToken

from .generated.RapcodeLexer import RapcodeLexer
from .generated.RapcodeParser import RapcodeParser
from .generated.RapcodeVisitor import RapcodeVisitor

# --- Custom Exceptions for Clean Error Reporting & Control Flow ---

class RapcodeError(Exception):
    """
    Base class for all user-facing errors in the interpreter.
    Captures the context (line/column) to provide helpful messages.
    """
    def __init__(self, message, ctx):
        # When ctx is a token, not a rule context
        if isinstance(ctx, CommonToken):
            line = ctx.line
            col = ctx.column
        # When ctx is a rule context
        else:
            line = ctx.start.line
            col = ctx.start.column
        super().__init__(f"[Runtime Error] line {line}:{col}: {message}")

class BreakException(Exception):
    """Custom exception for the BREAK statement (for control flow, not an error)."""
    pass

# --- The Main Interpreter Class (Version 2.0) ---

class RapcodeInterpreter(RapcodeVisitor):
    def __init__(self, input_func=None, output_func=None):
        self.memory = {}
        self._input_func = input_func or input
        self._output_func = output_func or print

    # --- Helper Methods for Type & Logic Checking ---

    def _is_truthy(self, value):
        """Defines what is considered 'true' in Rapcode's logic."""
        if isinstance(value, bool):
            return value
        if isinstance(value, (int, float)):
            return value != 0
        if isinstance(value, str):
            return value != ""
        return False

    def _check_numeric_operands(self, ctx, left, right, op):
        """A centralized guard to ensure math operations are safe."""
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            raise RapcodeError(f"Cannot apply operator '{op}' to non-numeric types ('{type(left).__name__}' and '{type(right).__name__}').", ctx)

    # --- Statement Visitors ---

    def visitAssignStmt(self, ctx: RapcodeParser.AssignStmtContext):
        assign_ctx = ctx.assignment()
        var_name = assign_ctx.IDENTIFIER().getText()
        value = self.visit(assign_ctx.expr())
        self.memory[var_name] = value

    def visitOutputStmt(self, ctx: RapcodeParser.OutputStmtContext):
        value = self.visit(ctx.output().expr())
        self._output_func(value)

    def visitIfStmt(self, ctx: RapcodeParser.IfStmtContext):
        if_ctx = ctx.ifStatement()
        condition = self.visit(if_ctx.expr())

        if if_ctx.NOT():
            condition = not self._is_truthy(condition)

        if self._is_truthy(condition):
            # Execute the 'consequent' block (statements before ELSE)
            for stmt in if_ctx.statement():
                if if_ctx.ELSE() and stmt.getSourceInterval()[0] > if_ctx.ELSE().getSymbol().tokenIndex:
                    break # Stop if we reach the ELSE clause
                self.visit(stmt)
        elif if_ctx.ELSE():
            # Execute the 'alternate' block (statements after ELSE)
            for stmt in if_ctx.statement():
                if stmt.getSourceInterval()[0] > if_ctx.ELSE().getSymbol().tokenIndex:
                    self.visit(stmt)

    def visitLoopStmt(self, ctx: RapcodeParser.LoopStmtContext):
        loop_ctx = ctx.loop()
        while True:
            try:
                for stmt in loop_ctx.statement():
                    self.visit(stmt)
            except BreakException:
                break # Gracefully exit the while loop

    def visitBreakStmt(self, ctx: RapcodeParser.BreakStmtContext):
        raise BreakException()

    # --- Expression and Atom Visitors ---

    def visitParenExpr(self, ctx: RapcodeParser.ParenExprContext):
        return self.visit(ctx.expr())
        
    def visitUnaryMinusExpr(self, ctx: RapcodeParser.UnaryMinusExprContext):
        """Handles negative numbers."""
        value = self.visit(ctx.expr())
        if not isinstance(value, (int, float)):
            raise RapcodeError(f"Cannot apply unary minus '-' to non-numeric type '{type(value).__name__}'.", ctx)
        return -value

    def visitAddSubExpr(self, ctx: RapcodeParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if ctx.op.type == RapcodeParser.ADD:
            # Smart addition: concatenates if either operand is a string
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            self._check_numeric_operands(ctx, left, right, '+')
            return left + right

        # Subtraction is strictly numeric
        self._check_numeric_operands(ctx, left, right, '-')
        return left - right

    def visitMulDivExpr(self, ctx: RapcodeParser.MulDivExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op_text = ctx.op.text
        self._check_numeric_operands(ctx, left, right, op_text)

        if right == 0 and op_text in ['/', '%']:
            raise RapcodeError(f"Division by zero.", ctx.expr(1))

        if op_text == '*': return left * right
        if op_text == '/': return left / right
        if op_text == '%': return left % right

    def visitRelationalExpr(self, ctx: RapcodeParser.RelationalExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        self._check_numeric_operands(ctx, left, right, ctx.op.text)

        op = ctx.op.type
        if op == RapcodeParser.LT: return left < right
        if op == RapcodeParser.LTE: return left <= right
        if op == RapcodeParser.GT: return left > right
        if op == RapcodeParser.GTE: return left >= right

    def visitEqualityExpr(self, ctx: RapcodeParser.EqualityExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.type
        # Works on any two types
        if op == RapcodeParser.EQ: return left == right
        if op == RapcodeParser.NEQ: return left != right

    def visitAtomExpr(self, ctx: RapcodeParser.AtomExprContext):
        return self.visit(ctx.atom())

    def visitIdAtom(self, ctx: RapcodeParser.IdAtomContext):
        var_name = ctx.getText()
        if var_name in self.memory:
            return self.memory[var_name]
        raise RapcodeError(f"Variable '{var_name}' is not defined.", ctx)

    def visitStringAtom(self, ctx: RapcodeParser.StringAtomContext):
        return ctx.getText()[1:-1]

    def visitNumberAtom(self, ctx: RapcodeParser.NumberAtomContext):
        val = float(ctx.getText())
        return int(val) if val.is_integer() else val

    def visitBooleanAtom(self, ctx: RapcodeParser.BooleanAtomContext):
        return ctx.getText() == "TRUE"

    def visitInputCallAtom(self, ctx: RapcodeParser.InputCallAtomContext):
        prompt_val = self.visit(ctx.inputCall().expr())
        prompt = str(prompt_val)

        user_input = self._input_func(prompt + " ") # Add a space for better UX

        try:
            val = float(user_input)
            return int(val) if val.is_integer() else val
        except ValueError:
            return user_input # Keep as string if conversion fails

