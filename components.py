import flet as ft

class GlassButton(ft.Container):
    """Botão com proporção dinâmica e visual Aero ajustado para o layout padrão."""
    def __init__(self, text, on_click, expand=1, btn_type="number"):
        super().__init__()
        self.text = text
        self.on_click_action = on_click
        self.expand = expand
        
        # Fonte Segoe UI para os botões
        self.content = ft.Text(
            text, 
            size=16, 
            color=ft.Colors.BLACK_87, 
            font_family="Segoe UI",
            weight=ft.FontWeight.W_400
        )
        self.alignment = ft.Alignment(0, 0)
        self.border_radius = 4 # Bordas levemente arredondadas do Win7
        
        # O gradiente varia se é número (branco) ou operador/memória (azulado)
        if btn_type == "operator":
            self.gradient = ft.LinearGradient(
                begin=ft.Alignment(0, -1),
                end=ft.Alignment(0, 1),
                colors=["#eaf0f7", "#d3def0"], # Azulado
            )
        else:
            self.gradient = ft.LinearGradient(
                begin=ft.Alignment(0, -1),
                end=ft.Alignment(0, 1),
                colors=["#f8fafd", "#e6ecf5"], # Branco
            )
            
        self.border = ft.Border.all(1, "#b5c4df")
        self.on_hover = self.handle_hover
        self.on_click = self._handle_click
        
        # Animação mais rápida para feedback instantâneo (Fase 4)
        self.animate = ft.Animation(100, ft.AnimationCurve.EASE_OUT)

    def handle_hover(self, e):
        # Escurece levemente a borda ao passar o mouse para dar feedback
        self.border = ft.Border.all(1, "#8ea5c8" if e.data == "true" else "#b5c4df")
        self.update()

    def _handle_click(self, e):
        # Visual feedback instantâneo no clique
        old_border = self.border
        self.border = ft.Border.all(2, "#3c7fb1") # Borda de foco do Windows
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
            size=14, 
            weight=ft.FontWeight.BOLD, 
            color=ft.Colors.BLACK54, 
            visible=False,
            font_family="Segoe UI"
        )
        
        self.display_text = ft.Text(
            value="0", 
            size=38, 
            color=ft.Colors.BLACK_87, 
            font_family="Consolas",
            text_align=ft.TextAlign.RIGHT
        )
        
        self.content = ft.Stack([
            ft.Container(
                content=self.memory_indicator,
                left=10,
                top=10
            ),
            ft.Container(
                content=self.display_text,
                alignment=ft.Alignment(1, 0), # Center Right
                padding=ft.Padding(0, 15, 10, 0)
            )
        ])
        
        self.padding = 0
        self.bgcolor = ft.Colors.with_opacity(0.4, ft.Colors.WHITE)
        self.border = ft.Border.all(1, "#a0b5d0")
        self.border_radius = 5
        self.margin = ft.margin.only(bottom=15)
        self.height = 80

    def update_display(self, value, memory_active=False):
        self.display_text.value = value
        self.memory_indicator.visible = memory_active
        self.update()
