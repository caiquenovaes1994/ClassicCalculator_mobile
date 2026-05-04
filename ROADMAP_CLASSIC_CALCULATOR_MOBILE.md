# Roadmap: Windows 7 Calculator (Flet Clone)

## Fase 1: Interface Gráfica (Concluído ✅)

- [x] Configuração base do aplicativo Flet (janela, fundo).
- [x] Carregamento de fontes originais (`Segoe UI` e `Consolas`).
- [x] Construção do visor do display simulando LCD/LED (com fundo branco translúcido).
- [x] Implementação da classe `GlassButton` para simular os botões nativos.
- [x] **Layout Exato (Standard Mode):**
  - [x] Grade de 5 colunas.
  - [x] Cores distintas para Números (brancos) e Operadores (azulados).
  - [x] Botão `0` com largura dupla (expand=2).
  - [x] Botão `=` com altura dupla estendida.

## Fase 2: Motor Lógico Matemático (Concluído ✅)

- [x] Definição inicial da classe `CalculatorState`.
- [x] **Operações Básicas:**
  - [x] Adição (`+`), Subtração (`-`), Multiplicação (`*`), Divisão (`/`).
  - [x] Igualdade (`=`) com repetição de operação se clicado múltiplas vezes.
- [x] **Operações Avançadas (Linha Direita/Topo):**
  - [x] Raiz Quadrada (`√`).
  - [x] Porcentagem (`%`).
  - [x] Fração (`1/x`).
  - [x] Alternância de Sinal (`±`).
  - [x] Decimal/Vírgula (`,`).
- [x] **Limpeza de Tela/Estado:**
  - [x] Apagar último dígito (`←` ou Backspace).
  - [x] Limpar Entrada atual (`CE`).
  - [x] Limpar tudo (`C`).
- [x] **Gerenciamento de Memória:**
  - [x] `M+` (Adicionar ao valor salvo).
  - [x] `M-` (Subtrair do valor salvo).
  - [x] `MS` (Salvar valor atual na memória).
  - [x] `MR` (Recuperar valor da memória).
  - [x] `MC` (Limpar memória).
  - [x] Indicador visual "M" no display quando a memória estiver em uso.
- [x] **Refinamento do Visor:**
  - [x] Limitação de caracteres (ex: 16 dígitos).
  - [x] Formatação de milhares (ex: `1.000.000` em vez de `1000000`).

## Fase 3: Menus Nativos (Concluído ✅)

- [x] Implementar `ft.MenuBar` no topo da janela.
- [x] **Menu 'Exibir':**
  - [x] Padrão, Científica, Programador, Estatística (apenas UI indicando "Padrão" ativo, resto opcional).
  - [x] Histórico.
- [x] **Menu 'Editar':**
  - [x] Copiar (Ctrl+C).
  - [x] Colar (Ctrl+V).
- [x] **Menu 'Ajuda':**
  - [x] Exibir Ajuda (F1).
  - [x] Sobre a Calculadora (Pop-up modal imitando a janela do Windows).

## Fase 4: Polimento e Fidelidade 100% (Concluído ✅)

- [x] Suporte a teclado físico (NumPad e atalhos de operações).
- [x] Efeito de clique mais rápido no `GlassButton` (feedback tátil/visual).
- [x] Validação final contra screenshots do Windows 7 para pixel-perfect accuracy.
- [x] Testes de build (Android/iOS/Desktop).
