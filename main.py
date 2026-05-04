import flet as ft
from calculator_logic import CalculatorLogic
from components import GlassButton, CalculatorDisplay

class CalculatorApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.logic = CalculatorLogic()
        
        self.page.fonts = {
            "Segoe UI": "fonts/SegoeUI.ttf",
            "Consolas": "fonts/Consolas.ttf" 
        }
        
        self.page.title = "Calculadora"
        self.page.window_width = 250 # Janela mais estreita
        self.page.window_height = 380 # Janela mais baixa
        self.page.window_resizable = False
        self.page.padding = 0 # Removido para o menu grudar no topo
        self.page.bgcolor = "#d9e4f1"
        
        self.page.on_keyboard_event = self.handle_keyboard
        
        self.display = CalculatorDisplay()
        
        self.build_ui()

    def handle_keyboard(self, e: ft.KeyboardEvent):
        key = e.key
        if key in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.button_clicked(key)
        elif key == "+": self.button_clicked("+")
        elif key == "-": self.button_clicked("-")
        elif key == "*": self.button_clicked("*")
        elif key == "/": self.button_clicked("/")
        elif key == "Enter" or key == "=": self.button_clicked("=")
        elif key == "Backspace": self.button_clicked("←")
        elif key == "Escape" or key == "Delete": self.button_clicked("C")
        elif key == "," or key == ".": self.button_clicked(",")
        elif key == "%": self.button_clicked("%")

    def show_about(self, e):
        def close_dlg(e):
            self.page.dialog.open = False
            self.page.update()

        self.page.dialog = ft.AlertDialog(
            title=ft.Text("Sobre a Calculadora"),
            content=ft.Column([
                ft.Image(src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Windows_7_logo.svg/1200px-Windows_7_logo.svg.png", width=50),
                ft.Text("Calculadora Classic (Flet Clone)", weight=ft.FontWeight.BOLD),
                ft.Text("Inspirado no design Aero Glass do Windows 7."),
                ft.Text("Versão 1.0.0"),
            ], tight=True, spacing=10),
            actions=[ft.TextButton("OK", on_click=close_dlg)],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.dialog.open = True
        self.page.update()

    def button_clicked(self, text):
        if text.isdigit(): self.logic.add_digit(text)
        elif text == ",": self.logic.add_decimal()
        elif text == "C": self.logic.clear()
        elif text == "CE": self.logic.clear_entry()
        elif text == "←": self.logic.backspace()
        elif text in ["+", "-", "*", "/"]: self.logic.set_operator(text)
        elif text == "=": self.logic.calculate()
        elif text == "%": self.logic.percentage()
        elif text == "±": self.logic.negate()
        elif text == "√": self.logic.sqrt()
        elif text == "1/x": self.logic.reciprocal()
        elif text == "MC": self.logic.memory_clear()
        elif text == "MR": self.logic.memory_recall()
        elif text == "MS": self.logic.memory_store()
        elif text == "M+": self.logic.memory_add()
        elif text == "M-": self.logic.memory_subtract()
            
        self.display.update_display(
            self.logic.expression, 
            memory_active=self.logic.memory_active
        )

    def build_ui(self):
        # --- 1. BARRA DE MENUS ---
        menu_bar = ft.Container(
            content=ft.Row([
                ft.Text("Exibir", size=12, color=ft.Colors.BLACK_87, font_family="Segoe UI"),
                ft.Text("Editar", size=12, color=ft.Colors.BLACK_87, font_family="Segoe UI"),
                ft.GestureDetector(
                    content=ft.Text("Ajuda", size=12, color=ft.Colors.BLACK_87, font_family="Segoe UI"),
                    on_tap=self.show_about
                ),
            ], spacing=15),
            bgcolor=ft.Colors.WHITE,
            padding=ft.padding.only(left=10, top=4, bottom=4),
            width=float('inf')
        )

        # --- 3. GRADE DE BOTÕES ---
        # Espaçamento (spacing) reduzido para 4 para deixar os botões mais próximos
        button_grid = ft.Column(
            expand=True,
            spacing=4,
            controls=[
                self.display,
                ft.Row([GlassButton("MC", self.button_clicked, btn_type="operator"), GlassButton("MR", self.button_clicked, btn_type="operator"), GlassButton("MS", self.button_clicked, btn_type="operator"), GlassButton("M+", self.button_clicked, btn_type="operator"), GlassButton("M-", self.button_clicked, btn_type="operator")], expand=1, spacing=4),
                ft.Row([GlassButton("←", self.button_clicked, btn_type="operator"), GlassButton("CE", self.button_clicked, btn_type="operator"), GlassButton("C", self.button_clicked, btn_type="operator"), GlassButton("±", self.button_clicked, btn_type="operator"), GlassButton("√", self.button_clicked, btn_type="operator")], expand=1, spacing=4),
                ft.Row([GlassButton("7", self.button_clicked), GlassButton("8", self.button_clicked), GlassButton("9", self.button_clicked), GlassButton("/", self.button_clicked, btn_type="operator"), GlassButton("%", self.button_clicked, btn_type="operator")], expand=1, spacing=4),
                ft.Row([GlassButton("4", self.button_clicked), GlassButton("5", self.button_clicked), GlassButton("6", self.button_clicked), GlassButton("*", self.button_clicked, btn_type="operator"), GlassButton("1/x", self.button_clicked, btn_type="operator")], expand=1, spacing=4),
                
                # Bloco assimétrico inferior
                ft.Row(
                    expand=2, 
                    spacing=4,
                    vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                    controls=[
                        ft.Column(
                            expand=4,
                            spacing=4,
                            controls=[
                                ft.Row([GlassButton("1", self.button_clicked), GlassButton("2", self.button_clicked), GlassButton("3", self.button_clicked), GlassButton("-", self.button_clicked, btn_type="operator")], expand=1, spacing=4),
                                ft.Row([GlassButton("0", self.button_clicked, expand=2), GlassButton(",", self.button_clicked), GlassButton("+", self.button_clicked, btn_type="operator")], expand=1, spacing=4),
                            ]
                        ),
                        GlassButton("=", self.button_clicked, expand=1, btn_type="operator")
                    ]
                )
            ]
        )

        # Container que segura a calculadora (dando o espaçamento da borda azul)
        calc_body = ft.Container(
            content=button_grid,
            padding=12,
            expand=True
        )

        # Adiciona primeiro o menu branco (topo) e depois o corpo da calculadora
        self.page.add(menu_bar, calc_body)

def main(page: ft.Page):
    CalculatorApp(page)

if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
