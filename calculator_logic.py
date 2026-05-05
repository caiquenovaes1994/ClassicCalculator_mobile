import math

class CalculatorState:
    def __init__(self):
        self.reset()
        self.memory = 0
        self.memory_active = False

    def reset(self):
        self.current_value = "0"
        self.equation_preview = "" # Novo campo para o preview
        self.operand_a = None
        self.operator = None
        self.new_operand = True

    def format_display(self, value=None):
        """Formata o valor para exibição brasileira."""
        val_str = value if value is not None else self.current_value
        if val_str == "Error": return "Error"
        try:
            val = float(val_str.replace(",", "."))
            # Formatação brasileira (1.234,56)
            return f"{val:,.10g}".replace(",", "X").replace(".", ",").replace("X", ".")
        except:
            return val_str

    def add_digit(self, digit: str):
        if self.new_operand:
            self.current_value = digit if digit != "," else "0,"
            self.new_operand = False
        else:
            if digit == "," and "," in self.current_value: return
            if len(self.current_value.replace(",", "")) < 16:
                self.current_value += digit

    def backspace(self):
        if not self.new_operand:
            self.current_value = self.current_value[:-1]
            if not self.current_value or self.current_value == "-": 
                self.current_value = "0"
                self.new_operand = True

    def set_operator(self, operator: str):
        try:
            # Se já houver um operador e um novo operando sendo digitado, apenas troca o operador
            if self.operator and self.new_operand:
                self.operator = operator
                self.equation_preview = f"{self.format_display(str(self.operand_a).replace('.', ','))} {operator}"
                return
                
            self.operand_a = float(self.current_value.replace(",", "."))
            self.operator = operator
            # Atualiza o preview com o valor atual e o operador
            self.equation_preview = f"{self.format_display()} {operator}"
            self.new_operand = True
        except:
            pass

    def calculate(self):
        if self.operator and self.operand_a is not None:
            try:
                b = float(self.current_value.replace(",", "."))
                res = 0
                if self.operator == "+": res = self.operand_a + b
                elif self.operator == "-": res = self.operand_a - b
                elif self.operator == "*": res = self.operand_a * b
                elif self.operator == "/":
                    if b == 0:
                        self.current_value = "Error"
                        self.equation_preview = ""
                        self.operator = None
                        self.operand_a = None
                        self.new_operand = True
                        return
                    res = self.operand_a / b
                
                self.current_value = str(res).replace(".", ",")
                self.equation_preview = "" # Limpa o preview após o resultado
                self.operand_a = None
                self.operator = None
                self.new_operand = True
            except:
                self.current_value = "Error"
                self.equation_preview = ""

    # Funções de Memória (mantidas)
    def memory_clear(self):
        self.memory = 0
        self.memory_active = False

    def memory_recall(self):
        self.current_value = str(self.memory).replace(".", ",")
        self.new_operand = True

    def memory_store(self):
        try:
            self.memory = float(self.current_value.replace(",", "."))
            self.memory_active = (self.memory != 0)
            self.new_operand = True
        except:
            pass

    def memory_add(self):
        try:
            self.memory += float(self.current_value.replace(",", "."))
            self.memory_active = (self.memory != 0)
            self.new_operand = True
        except:
            pass

    def memory_subtract(self):
        try:
            self.memory -= float(self.current_value.replace(",", "."))
            self.memory_active = (self.memory != 0)
            self.new_operand = True
        except:
            pass
            
    def negate(self):
        if self.current_value == "0": return
        if self.current_value.startswith("-"):
            self.current_value = self.current_value[1:]
        else:
            self.current_value = "-" + self.current_value

    def sqrt(self):
        try:
            val = float(self.current_value.replace(",", "."))
            if val < 0: raise ValueError
            self.current_value = str(math.sqrt(val)).replace(".", ",")
            self.new_operand = True
        except:
            self.current_value = "Error"

    def reciprocal(self):
        try:
            val = float(self.current_value.replace(",", "."))
            if val == 0: raise ZeroDivisionError
            self.current_value = str(1/val).replace(".", ",")
            self.new_operand = True
        except:
            self.current_value = "Error"

    def percentage(self):
        try:
            val = float(self.current_value.replace(",", "."))
            if self.operand_a is not None:
                res = self.operand_a * (val / 100)
            else:
                res = val / 100
            self.current_value = str(res).replace(".", ",")
            self.new_operand = True
        except:
            self.current_value = "Error"

    def clear(self):
        self.reset()

    def clear_entry(self):
        self.current_value = "0"
        self.new_operand = True
