import flet as ft
from calculator_logic import CalculatorLogic
from components import GlassButton, CalculatorDisplay

class CalculatorApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.logic = CalculatorLogic()
        
        # Configurações da Página
        self.page.fonts = {
            "Segoe UI": "fonts/SegoeUI.ttf",
            "Consolas": "fonts/Consolas.ttf" 
        }
        
        self.page.title = "Calculadora"
        self.page.window_width = 340
        self.page.window_height = 560
        self.page.window_resizable = False
        self.page.padding = 0 
        self.page.bgcolor = "#d9e4f1" 
        
        # Evento de teclado (Fase 4)
        self.page.on_keyboard_event = self.handle_keyboard
        
        self.display = CalculatorDisplay()
        
        self.build_menu()
        self.build_ui()

    def handle_keyboard(self, e: ft.KeyboardEvent):
        # Mapeamento de teclas físicas para as funções da calculadora
        key = e.key
        
        # Números
        if key in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.button_clicked(key)
        
        # Operadores
        elif key == "+": self.button_clicked("+")
        elif key == "-": self.button_clicked("-")
        elif key == "*": self.button_clicked("*")
        elif key == "/": self.button_clicked("/")
        
        # Ações especiais
        elif key == "Enter" or key == "=": self.button_clicked("=")
        elif key == "Backspace": self.button_clicked("←")
        elif key == "Escape" or key == "Delete": self.button_clicked("C")
        elif key == "," or key == ".": self.button_clicked(",")
        elif key == "%": self.button_clicked("%")

    def build_menu(self):
        menu_exibir = ft.SubmenuButton(
            content=ft.Text("Exibir"),
            controls=[
                ft.MenuItemButton(content=ft.Text("Padrão"), leading=ft.Icon(ft.Icons.CHECK)),
                ft.MenuItemButton(content=ft.Text("Científica")),
                ft.MenuItemButton(content=ft.Text("Programador")),
                ft.MenuItemButton(content=ft.Text("Estatística")),
                ft.Divider(),
                ft.MenuItemButton(content=ft.Text("Histórico")),
                ft.MenuItemButton(content=ft.Text("Agrupamento de dígitos"), leading=ft.Icon(ft.Icons.CHECK)),
            ]
        )

        menu_editar = ft.SubmenuButton(
            content=ft.Text("Editar"),
            controls=[
                ft.MenuItemButton(
                    content=ft.Text("Copiar (Ctrl+C)"),
                    on_click=lambda _: self.page.set_clipboard(self.logic.expression)
                ),
                ft.MenuItemButton(
                    content=ft.Text("Colar (Ctrl+V)"),
                    on_click=lambda _: self.paste_from_clipboard()
                ),
            ]
        )

        menu_ajuda = ft.SubmenuButton(
            content=ft.Text("Ajuda"),
            controls=[
                ft.MenuItemButton(content=ft.Text("Exibir Ajuda")),
                ft.Divider(),
                ft.MenuItemButton(
                    content=ft.Text("Sobre a Calculadora"),
                    on_click=self.show_about
                ),
            ]
        )

        self.page.menu_bar = ft.MenuBar(
            expand=True,
            style=ft.MenuStyle(
                bgcolor=ft.Colors.WHITE,
            ),
            controls=[menu_exibir, menu_editar, menu_ajuda]
        )

    def paste_from_clipboard(self):
        content = self.page.get_clipboard()
        if content:
            clean_content = "".join([c for c in content if c.isdigit() or c in ",."])
            if clean_content:
                self.logic.expression = clean_content.replace(".", ",")
                self.display.update_display(self.logic.expression, self.logic.memory_active)

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
            actions=[
                ft.TextButton("OK", on_click=close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.dialog.open = True
        self.page.update()

    def button_clicked(self, text):
        if text.isdigit():
            self.logic.add_digit(text)
        elif text == ",":
            self.logic.add_decimal()
        elif text == "C":
            self.logic.clear()
        elif text == "CE":
            self.logic.clear_entry()
        elif text == "←":
            self.logic.backspace()
        elif text in ["+", "-", "*", "/"]:
            self.logic.set_operator(text)
        elif text == "=":
            self.logic.calculate()
        elif text == "%":
            self.logic.percentage()
        elif text == "±":
            self.logic.negate()
        elif text == "√":
            self.logic.sqrt()
        elif text == "1/x":
            self.logic.reciprocal()
        elif text == "MC":
            self.logic.memory_clear()
        elif text == "MR":
            self.logic.memory_recall()
        elif text == "MS":
            self.logic.memory_store()
        elif text == "M+":
            self.logic.memory_add()
        elif text == "M-":
            self.logic.memory_subtract()
            
        self.display.update_display(
            self.logic.expression, 
            memory_active=self.logic.memory_active
        )

    def build_ui(self):
        layout = ft.Container(
            content=ft.Column(
                expand=True,
                spacing=6,
                controls=[
                    self.display,
                    ft.Row([
                        GlassButton("MC", self.button_clicked, btn_type="operator"), 
                        GlassButton("MR", self.button_clicked, btn_type="operator"), 
                        GlassButton("MS", self.button_clicked, btn_type="operator"), 
                        GlassButton("M+", self.button_clicked, btn_type="operator"), 
                        GlassButton("M-", self.button_clicked, btn_type="operator")
                    ], expand=1, spacing=6),
                    ft.Row([
                        GlassButton("←", self.button_clicked, btn_type="operator"), 
                        GlassButton("CE", self.button_clicked, btn_type="operator"), 
                        GlassButton("C", self.button_clicked, btn_type="operator"), 
                        GlassButton("±", self.button_clicked, btn_type="operator"), 
                        GlassButton("√", self.button_clicked, btn_type="operator")
                    ], expand=1, spacing=6),
                    ft.Row([
                        GlassButton("7", self.button_clicked), 
                        GlassButton("8", self.button_clicked), 
                        GlassButton("9", self.button_clicked), 
                        GlassButton("/", self.button_clicked, btn_type="operator"), 
                        GlassButton("%", self.button_clicked, btn_type="operator")
                    ], expand=1, spacing=6),
                    ft.Row([
                        GlassButton("4", self.button_clicked), 
                        GlassButton("5", self.button_clicked), 
                        GlassButton("6", self.button_clicked), 
                        GlassButton("*", self.button_clicked, btn_type="operator"), 
                        GlassButton("1/x", self.button_clicked, btn_type="operator")
                    ], expand=1, spacing=6),
                    ft.Row(
                        expand=2, 
                        spacing=6,
                        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                        controls=[
                            ft.Column(
                                expand=4,
                                spacing=6,
                                controls=[
                                    ft.Row([
                                        GlassButton("1", self.button_clicked), 
                                        GlassButton("2", self.button_clicked), 
                                        GlassButton("3", self.button_clicked), 
                                        GlassButton("-", self.button_clicked, btn_type="operator")
                                    ], expand=1, spacing=6),
                                    ft.Row([
                                        GlassButton("0", self.button_clicked, expand=2), 
                                        GlassButton(",", self.button_clicked), 
                                        GlassButton("+", self.button_clicked, btn_type="operator")
                                    ], expand=1, spacing=6),
                                ]
                            ),
                            GlassButton("=", self.button_clicked, expand=1, btn_type="operator")
                        ]
                    )
                ]
            ),
            padding=15,
            expand=True
        )

        self.page.add(layout)

def main(page: ft.Page):
    CalculatorApp(page)

if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
