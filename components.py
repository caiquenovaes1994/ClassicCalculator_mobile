import flet as ft

class GlassButton(ft.Container):
    """Botão refinado com as proporções e cores exatas do Windows 7."""
    def __init__(self, text, on_click, expand=1, btn_type="number"):
        super().__init__()
        self.text = text
        self.on_click_action = on_click
        self.expand = expand
        
        # Fonte menor e mais delicada
        self.content = ft.Text(
            text, 
            size=14, 
            color=ft.Colors.BLACK_87, 
            font_family="Segoe UI",
            weight=ft.FontWeight.W_400
        )
        self.alignment = ft.Alignment(0, 0)
        self.border_radius = 2 # Quase quadrado, igual ao original
        
        # Cores extremamente claras, imitando o reflexo vítreo
        if btn_type == "operator":
            self.gradient = ft.LinearGradient(
                begin=ft.Alignment(0, -1),
                end=ft.Alignment(0, 1),
                colors=["#edf1f6", "#d4dfef"], # Azul muito pálido
            )
        else:
            self.gradient = ft.LinearGradient(
                begin=ft.Alignment(0, -1),
                end=ft.Alignment(0, 1),
                colors=["#fdfdfd", "#e3e8ee"], # Branco gelo
            )
            
        self.border = ft.Border.all(1, "#99a9c4") # Borda sutil
        self.on_hover = self.handle_hover
        self.on_click = self._handle_click

    def handle_hover(self, e):
        # Efeito de hover levemente amarelado/azulado característico do Win7
        self.border = ft.Border.all(1, "#ffd232" if e.data == "true" else "#99a9c4")
        self.bgcolor = ft.Colors.with_opacity(0.1, ft.Colors.YELLOW) if e.data == "true" else None
        self.update()

    def _handle_click(self, e):
        # Visual feedback instantâneo no clique
        old_border = self.border
        self.border = ft.Border.all(2, "#3c7fb1") 
        self.update()
        
        if self.on_click_action:
            self.on_click_action(self.text)
            
        self.border = old_border
        self.update()

class CalculatorDisplay(ft.Container):
    def __init__(self):
        super().__init__()
        # Indicador de Memória "M"
        self.memory_indicator = ft.Text(
            "M", 
            size=12, 
            weight=ft.FontWeight.BOLD, 
            color=ft.Colors.BLACK_54, 
            visible=False,
            font_family="Segoe UI"
        )
        
        self.display_text = ft.Text(
            value="0", 
            size=28, # Fonte reduzida
            color=ft.Colors.BLACK_87, 
            font_family="Consolas",
            text_align=ft.TextAlign.RIGHT
        )
        
        self.content = ft.Stack([
            ft.Container(
                content=self.memory_indicator,
                left=0,
                top=0
            ),
            ft.Container(
                content=self.display_text,
                alignment=ft.Alignment(1, 1), # Alinha o número na base inferior
            )
        ])
        
        self.height = 55 # Altura fixa para não ficar tão "gordo"
        self.padding = ft.padding.only(right=10, left=10, bottom=2, top=2)
        self.bgcolor = "#f4f7fc" # Fundo do visor quase branco
        self.border = ft.Border.all(1, "#8e9cbc")
        self.border_radius = 3
        self.margin = ft.margin.only(bottom=10)

    def update_display(self, value, memory_active=False):
        self.display_text.value = value
        self.memory_indicator.visible = memory_active
        self.update()
