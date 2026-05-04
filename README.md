<!-- markdownlint-disable MD051 -->
# 🖩 Classic Calculator — Windows 7 Aero Glass Clone

> Uma réplica fiel da Calculadora do **Windows 7** construída com **Python + Flet**, com efeito visual **Aero Glass**, fontes originais e funcionalidade completa.

---

## ✨ Demonstração

```text
┌─────────────────────────────────┐
│ Exibir  Editar  Ajuda           │  ← Menu nativo
├─────────────────────────────────┤
│ M                               │  ← Indicador de memória
│                        1.234,56 │  ← Display Consolas
├────┬────┬────┬────┬────────────-┤
│ MC │ MR │ MS │ M+ │ M-          │
├────┼────┼────┼────┼─────────────┤
│  ← │ CE │  C │  ± │  √          │
├────┼────┼────┼────┼─────────────┤
│  7 │  8 │  9 │  / │  %          │
├────┼────┼────┼────┼─────────────┤
│  4 │  5 │  6 │  * │  1/x        │
├────┼────┼────┼────┤             │
│  1 │  2 │  3 │  - │    =        │
├─────────┼────┼────┤             │
│    0    │  , │  + │             │
└─────────┴────┴────┴─────────────┘
```

---

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Como Executar](#como-executar)
- [Build Mobile](#build-mobile)
- [Atalhos de Teclado](#atalhos-de-teclado)
- [Arquitetura](#arquitetura)

---

## 📖 Sobre o Projeto

Este projeto é uma **réplica pixel-perfect** da Calculadora clássica do Windows 7, reconstruída do zero com **Python** e o framework **Flet** para rodar nativamente em **Android**, **iOS** e **Desktop**.

O objetivo é preservar a estética **Aero Glass** — com seus gradientes azul-acinzentados, bordas sutis e fontes originais (`Segoe UI` e `Consolas`) — enquanto moderniza a base de código com uma arquitetura limpa e modular.

---

## ✅ Funcionalidades

### 🔢 Operações Matemáticas

| Operação | Botão | Teclado |
| --- | --- | --- |
| Adição | `+` | `+` |
| Subtração | `-` | `-` |
| Multiplicação | `*` | `*` |
| Divisão | `/` | `/` |
| Igualdade | `=` | `Enter` |
| Porcentagem | `%` | `%` |
| Raiz Quadrada | `√` | — |
| Inverso | `1/x` | — |
| Inversão de Sinal | `±` | — |
| Decimal | `,` | `,` ou `.` |

### 🧠 Gerenciamento de Memória

| Função | Descrição |
| --- | --- |
| `MC` | Limpa o valor salvo na memória |
| `MR` | Recupera o valor da memória para o display |
| `MS` | Salva o valor atual do display na memória |
| `M+` | Adiciona o valor atual ao valor salvo |
| `M-` | Subtrai o valor atual do valor salvo |
| Indicador `M` | Aparece no display quando a memória está em uso |

### ⌨️ Controles de Tela

| Botão | Teclado | Descrição |
| --- | --- | --- |
| `←` | `Backspace` | Apaga o último dígito |
| `CE` | — | Limpa apenas a entrada atual |
| `C` | `Esc` / `Delete` | Limpa tudo e reinicia |

### 🖥️ Interface e Menus

- **Menu Exibir**: Seleção de modo (Padrão ativo, Científica, Programador, Estatística)
- **Menu Editar**: Copiar valor do display e Colar número da área de transferência
- **Menu Ajuda**: Diálogo "Sobre" com informações da versão

---

## 🛠️ Tecnologias

| Tecnologia | Versão | Função |
| --- | --- | --- |
| **Python** | 3.12+ | Linguagem principal |
| **Flet** | 0.84+ | Framework UI multiplataforma |
| **Segoe UI** | — | Fonte dos botões e menus |
| **Consolas** | — | Fonte monoespaçada do display |

---

## 📁 Estrutura do Projeto

```text
ClassicCalculator_mobile/
│
├── assets/
│   └── fonts/
│       ├── SegoeUI.ttf          # Fonte dos botões e menus
│       └── Consolas.ttf         # Fonte do display numérico
│
├── calculator_logic.py          # Motor matemático (CalculatorLogic)
├── components.py                # Componentes reutilizáveis (GlassButton, Display)
├── main.py                      # Ponto de entrada, layout e menus
│
├── ROADMAP_CLASSIC_CALCULATOR_MOBILE.md
└── README.md
```

### Descrição dos Módulos

#### `calculator_logic.py` — Motor Matemático

Classe `CalculatorLogic` totalmente desacoplada da UI:

- Gerencia o estado da operação em andamento
- Formata números no padrão brasileiro (`1.234.567,89`)
- Limite de 16 dígitos (fidelidade ao Windows 7)
- Tratamento de erros (divisão por zero, entradas inválidas)

#### `components.py` — Componentes de UI

- **`GlassButton`**: Botão com gradiente Aero, hover e feedback de clique
- **`CalculatorDisplay`**: Visor com fonte Consolas e indicador "M" de memória

#### `main.py` — Aplicação Principal

- Configuração da página e tema
- Barra de menus nativa (`ft.MenuBar`)
- Layout assimétrico (botão `0` duplo, botão `=` alto)
- Mapeamento de eventos de teclado

---

## 🚀 Instalação

### Pré-requisitos

- **Python 3.12+** instalado
- **pip** atualizado

### Passos

**1. Clone ou acesse a pasta do projeto:**

```bash
cd ClassicCalculator_mobile
```

**2. Crie e ative um ambiente virtual (recomendado):**

```bash
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

**3. Instale as dependências:**

```bash
pip install flet
```

---

## ▶️ Como Executar

```bash
python main.py
```

A calculadora abrirá em uma janela desktop de `340×560px`.

---

## 📱 Build Mobile

Para gerar o pacote para dispositivos móveis, utilize o **Flet CLI**:

```bash
# Android (.apk)
flet build apk

# iOS (requer macOS com Xcode)
flet build ios

# Web
flet build web
```

> **Nota**: Para build Android, é necessário ter o **Android SDK** configurado. Consulte a [documentação oficial do Flet](https://flet.dev/docs/publish).

---

## ⌨️ Atalhos de Teclado

| Tecla | Ação |
| --- | --- |
| `0` – `9` | Inserir dígito |
| `+` `-` `*` `/` | Operador matemático |
| `Enter` | Calcular resultado |
| `Backspace` | Apagar último dígito |
| `Esc` / `Delete` | Limpar tudo |
| `,` ou `.` | Inserir separador decimal |
| `%` | Calcular porcentagem |

---

## 🏗️ Arquitetura

```mermaid
graph TD
    A[main.py - CalculatorApp] -->|instancia| B[CalculatorLogic]
    A -->|renderiza| C[CalculatorDisplay]
    A -->|renderiza| D[GlassButton x N]
    D -->|on_click| A
    A -->|chama métodos| B
    B -->|retorna estado| A
    A -->|update_display| C
```

O padrão adotado segue uma arquitetura **MVC simplificada**:

- **Model**: `CalculatorLogic` — toda lógica matemática e de estado
- **View**: `GlassButton` + `CalculatorDisplay` — componentes visuais puros
- **Controller**: `CalculatorApp` em `main.py` — orquestra eventos e atualiza a UI

---

## 📄 Licença

Este projeto é de uso pessoal e educacional, desenvolvido como exercício de fidelidade de UI e arquitetura de aplicações Python com Flet.

---

## 👨‍💻 Autor

Desenvolvido por **Caique Novaes**.

- 🐙 GitHub: [caiquenovaes1994](https://github.com/caiquenovaes1994)
- ✉️ E-mail: <caiquenovaes1994@gmail.com>

Fique à vontade para contribuir, enviar sugestões ou reportar problemas!

---

Feito com 🐍 Python + ⚡ Flet | Inspirado no Windows 7 Aero Glass
