import math

class CalculatorLogic:
    def __init__(self):
        self.reset()
        self.memory = 0
        self.memory_active = False

    def reset(self):
        self.expression = "0"
        self.operator = None
        self.operand1 = None
        self.new_operand = True
        self.error = False

    def clear(self):
        self.reset()

    def clear_entry(self):
        self.expression = "0"
        self.new_operand = True

    def backspace(self):
        if self.error:
            self.reset()
            return
        
        if len(self.expression) > 1:
            self.expression = self.expression[:-1]
        else:
            self.expression = "0"
            self.new_operand = True

    def add_digit(self, digit):
        if self.error:
            self.reset()
            
        if self.new_operand:
            self.expression = digit
            self.new_operand = False
        else:
            if self.expression == "0":
                self.expression = digit
            else:
                # Limite de 16 dígitos para fidelidade
                if len(self.expression.replace(",", "").replace(".", "").replace("-", "")) < 16:
                    self.expression += digit

    def add_decimal(self):
        if self.error:
            self.reset()
            
        if self.new_operand:
            self.expression = "0,"
            self.new_operand = False
        elif "," not in self.expression:
            self.expression += ","

    def set_operator(self, operator):
        if self.error:
            return
            
        if self.operator and not self.new_operand:
            self.calculate()
        
        self.operand1 = self._parse_val(self.expression)
        self.operator = operator
        self.new_operand = True

    def calculate(self):
        if self.error or self.operator is None:
            return

        try:
            operand2 = self._parse_val(self.expression)
            if self.operator == "+":
                result = self.operand1 + operand2
            elif self.operator == "-":
                result = self.operand1 - operand2
            elif self.operator == "*":
                result = self.operand1 * operand2
            elif self.operator == "/":
                if operand2 == 0:
                    raise ZeroDivisionError()
                result = self.operand1 / operand2
            
            self.expression = self._format_result(result)
            self.operator = None
            self.operand1 = None
            self.new_operand = True
        except ZeroDivisionError:
            self.expression = "Erro: Divisão por zero"
            self.error = True
        except Exception:
            self.expression = "Erro"
            self.error = True

    def percentage(self):
        if self.error:
            return
        try:
            val = self._parse_val(self.expression)
            if self.operand1 is not None:
                result = self.operand1 * (val / 100)
                self.expression = self._format_result(result)
            else:
                result = val / 100
                self.expression = self._format_result(result)
        except Exception:
            self.expression = "Erro"
            self.error = True

    def negate(self):
        if self.error or self.expression == "0":
            return
        if self.expression.startswith("-"):
            self.expression = self.expression[1:]
        else:
            self.expression = "-" + self.expression

    def sqrt(self):
        if self.error: return
        try:
            val = self._parse_val(self.expression)
            if val < 0: raise ValueError()
            result = math.sqrt(val)
            self.expression = self._format_result(result)
            self.new_operand = True
        except Exception:
            self.expression = "Entrada inválida"
            self.error = True

    def reciprocal(self):
        if self.error: return
        try:
            val = self._parse_val(self.expression)
            if val == 0: raise ZeroDivisionError()
            result = 1 / val
            self.expression = self._format_result(result)
            self.new_operand = True
        except Exception:
            self.expression = "Erro: Divisão por zero"
            self.error = True

    # Memory Functions
    def memory_clear(self):
        self.memory = 0
        self.memory_active = False

    def memory_recall(self):
        self.expression = self._format_result(self.memory)
        self.new_operand = True

    def memory_store(self):
        try:
            self.memory = self._parse_val(self.expression)
            self.memory_active = (self.memory != 0)
            self.new_operand = True
        except Exception:
            pass

    def memory_add(self):
        try:
            self.memory += self._parse_val(self.expression)
            self.memory_active = (self.memory != 0)
            self.new_operand = True
        except Exception:
            pass

    def memory_subtract(self):
        try:
            self.memory -= self._parse_val(self.expression)
            self.memory_active = (self.memory != 0)
            self.new_operand = True
        except Exception:
            pass

    # Helpers
    def _parse_val(self, val_str):
        try:
            # Remove pontos de milhar e troca vírgula por ponto
            clean_str = val_str.replace(".", "").replace(",", ".")
            return float(clean_str)
        except:
            return 0.0

    def _format_result(self, val):
        # Arredondamento para evitar problemas de precisão float
        if abs(val) < 1e-12: val = 0
        
        if val == 0: return "0"
        
        # Formatação base
        if val.is_integer():
            res = f"{int(val):,}"
        else:
            # Limite de 12 casas decimais ou notação científica se muito grande/pequeno
            if abs(val) >= 1e16 or (abs(val) < 1e-12 and val != 0):
                res = f"{val:.12g}"
            else:
                res = f"{val:,.12g}"
        
        # Converte formato americano (1,000.5) para brasileiro (1.000,5)
        # Usamos um placeholder para a troca segura
        res = res.replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")
        
        return res

    def get_display_text(self):
        # Retorna a expressão formatada com pontos de milhar se for apenas número
        if self.operator is None and not self.error and "," not in self.expression:
            try:
                val = self._parse_val(self.expression)
                return self._format_result(val)
            except:
                return self.expression
        return self.expression
