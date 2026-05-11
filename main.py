import flet as ft
from calculator_logic import CalculatorState

class GlassButton(ft.Container):
    def __init__(self, text, on_click, btn_type="number", expand=1):
        super().__init__()
        self.expand = expand
        self.on_click_action = on_click
        self.btn_text = text
        
        self.content = ft.Text(text, size=13, color="#1e395b", font_family="Segoe UI")
        self.alignment = ft.Alignment(0, 0)
        self.border_radius = 3
        self.border = ft.Border.all(1, "#8797b2")
        
        # Gradientes Aero Glass
        if btn_type == "operator":
            self.gradient = ft.LinearGradient(
                begin=ft.Alignment(0, -1), end=ft.Alignment(0, 1),
                colors=["#f2f5f9", "#d4dfef", "#c9d5e9"], stops=[0, 0.5, 1.0]
            )
        else:
            self.gradient = ft.LinearGradient(
                begin=ft.Alignment(0, -1), end=ft.Alignment(0, 1),
                colors=["#ffffff", "#f0f4f9", "#e1e9f3"], stops=[0, 0.5, 1.0]
            )
            
        self.on_click = self._handle_click

    def _handle_click(self, e):
        if self.on_click_action:
            self.on_click_action(self.btn_text)

def show_about_dialog(page: ft.Page):
    """Exibe o popup de informações do desenvolvedor."""
    async def send_email(e):
        await page.launch_url("mailto:caiquenovaes1994@gmail.com")

    about_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Sobre a Calculadora", size=16, font_family="Segoe UI"),
        content=ft.Column([
            ft.Text("Calculadora Windows 7 Aero (Android)", weight="bold"),
            ft.Row([
                ft.Text("Desenvolvido por: ", size=13),
                ft.GestureDetector(
                    content=ft.Text(
                        "Caique", 
                        size=13, 
                        color=ft.Colors.BLUE_700, 
                        weight="bold"
                    ),
                    on_tap=send_email,
                    mouse_cursor=ft.MouseCursor.CLICK
                ),
            ], spacing=0),
            ft.Text("Ano: 2026", size=13),
        ], tight=True, spacing=10),
        actions=[
            ft.TextButton("Fechar", on_click=lambda e: close_dialog(page, about_dialog))
        ],
    )
    
    page.dialog = about_dialog
    about_dialog.open = True
    page.update()

def close_dialog(page, dialog):
    dialog.open = False
    page.update()

def main(page: ft.Page):
    # Configurações de página e fontes (assets/fonts)
    page.fonts = {"Segoe UI": "/fonts/SegoeUI.ttf", "Consolas": "/fonts/consola.ttf"}
    page.window_width = 230
    page.window_height = 360
    page.window_resizable = False
    
    # AJUSTE AQUI: Adicionamos o padding superior para desviar do entalhe
    page.padding = ft.Padding.only(top=45, left=0, right=0, bottom=0) 
    
    page.bgcolor = "#d9e4f1"

    calc = CalculatorState()

    # Visor Duplo (Equation Preview + Current Value)
    equation_text = ft.Text(value="", size=12, color="#707070", font_family="Segoe UI", text_align=ft.TextAlign.RIGHT)
    display_text = ft.Text(value="0", size=28, font_family="Consolas", color="#000000", text_align=ft.TextAlign.RIGHT)
    
    def update_ui():
        display_text.value = calc.format_display()
        equation_text.value = calc.equation_preview
        page.update()

    def on_click(text):
        try:
            page.haptic_feedback.vibrate() 
        except:
            pass
            
        if text.isdigit() or text == ",": calc.add_digit(text)
        elif text == "←": calc.backspace()
        elif text == "C": calc.reset()
        elif text == "CE": calc.clear_entry()
        elif text in ["+", "-", "*", "/"]: calc.set_operator(text)
        elif text == "=": calc.calculate()
        elif text == "±": calc.negate()
        elif text == "√": calc.sqrt()
        elif text == "1/x": calc.reciprocal()
        elif text == "%": calc.percentage()
        elif text == "MC": calc.memory_clear()
        elif text == "MR": calc.memory_recall()
        elif text == "MS": calc.memory_store()
        elif text == "M+": calc.memory_add()
        elif text == "M-": calc.memory_subtract()
        
        update_ui()

    # Barra de topo minimalista ajustada para o Android
    top_bar = ft.Container(
        content=ft.Row([
            ft.TextButton(
                "Sobre", 
                on_click=lambda _: show_about_dialog(page),
                style=ft.ButtonStyle(
                    color="#1e395b", 
                    text_style=ft.TextStyle(size=12, font_family="Segoe UI")
                )
            )
        ], alignment=ft.MainAxisAlignment.END),
        padding=ft.Padding.only(right=15), # Afasta levemente da borda direita
        height=40 # Altura fixa para manter a proporção Aero
    )

    # Visor Container
    display_container = ft.Container(
        content=ft.Column([equation_text, display_text], spacing=0, horizontal_alignment=ft.CrossAxisAlignment.END),
        height=70,
        padding=ft.Padding(10, 5, 10, 5),
        gradient=ft.LinearGradient(begin=ft.Alignment(0, -1), end=ft.Alignment(0, 1), colors=["#e6eff9", "#ffffff"]),
        border=ft.Border.all(1, "#8e9cbc"),
        border_radius=2,
        alignment=ft.Alignment(1, 1),
        margin=ft.Margin(0, 0, 0, 10)
    )

    # Grade de Botões
    grid = ft.Column(expand=True, spacing=4, controls=[
        display_container,
        ft.Row([GlassButton("MC", on_click, "operator"), GlassButton("MR", on_click, "operator"), GlassButton("MS", on_click, "operator"), GlassButton("M+", on_click, "operator"), GlassButton("M-", on_click, "operator")], expand=1, spacing=4),
        ft.Row([GlassButton("←", on_click, "operator"), GlassButton("CE", on_click, "operator"), GlassButton("C", on_click, "operator"), GlassButton("±", on_click, "operator"), GlassButton("√", on_click, "operator")], expand=1, spacing=4),
        ft.Row([GlassButton("7", on_click), GlassButton("8", on_click), GlassButton("9", on_click), GlassButton("/", on_click, "operator"), GlassButton("%", on_click, "operator")], expand=1, spacing=4),
        ft.Row([GlassButton("4", on_click), GlassButton("5", on_click), GlassButton("6", on_click), GlassButton("*", on_click, "operator"), GlassButton("1/x", on_click, "operator")], expand=1, spacing=4),
        ft.Row(expand=2, spacing=4, controls=[
            ft.Column(expand=4, spacing=4, controls=[
                ft.Row([GlassButton("1", on_click), GlassButton("2", on_click), GlassButton("3", on_click), GlassButton("-", on_click, "operator")], expand=1, spacing=4),
                ft.Row([GlassButton("0", on_click, expand=2), GlassButton(",", on_click), GlassButton("+", on_click, "operator")], expand=1, spacing=4),
            ]),
            GlassButton("=", on_click, btn_type="operator", expand=1)
        ])
    ])

    page.add(
        top_bar,
        ft.Container(content=grid, padding=8, expand=True)
    )
    update_ui()

if __name__ == "__main__":
    # ft.run substitui o ft.app nas versões recentes
    ft.run(main)
