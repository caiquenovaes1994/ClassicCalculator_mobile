<p align="center">
  <img src="assets/icon.png" alt="Classic Calculator" width="80" />
</p>

<h1 align="center">Classic Calculator — Windows 7 Aero Glass</h1>

<p align="center">
  <strong>Réplica fiel da Calculadora do Windows 7 construída com Python + Flet</strong><br/>
  Efeito visual Aero Glass · Fontes originais · Multiplataforma
</p>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12+"/></a>&nbsp;
  <a href="https://flet.dev/"><img src="https://img.shields.io/badge/Flet-0.84%2B-02569B?style=for-the-badge&logo=flutter&logoColor=white" alt="Flet 0.84+"/></a>&nbsp;
  <img src="https://img.shields.io/badge/Plataformas-Android%20%7C%20Desktop-34A853?style=for-the-badge&logo=android&logoColor=white" alt="Plataformas"/>&nbsp;
  <a href="https://github.com/caiquenovaes1994/ClassicCalculator_mobile"><img src="https://img.shields.io/badge/Licença-Pessoal%20%2F%20Educacional-lightgrey?style=for-the-badge" alt="Licença"/></a>
</p>

---

## 📖 Sobre o Projeto

Este projeto é uma **réplica pixel-perfect** da Calculadora clássica do Windows 7, reconstruída do zero para rodar nativamente em **Android** e **Desktop**.

O objetivo é preservar a estética **Aero Glass** — com seus gradientes azul-acinzentados, bordas sutis e fontes originais (`Segoe UI` e `Consolas`) — enquanto moderniza a base de código com uma arquitetura limpa e modular baseada no padrão MVC.

### Destaques

| Característica | Descrição |
| :--- | :--- |
| 🎨 **Aero Glass Fidelity** | Gradientes, bordas e sombras fiéis ao tema original do Windows 7 |
| 📱 **Mobile-First** | Layout otimizado para dispositivos Android com suporte a notch |
| 📳 **Haptic Feedback** | Vibração tátil em cada pressionamento de botão |
| 🧮 **Visor Duplo** | Exibe a equação em andamento e o resultado simultaneamente |
| 🌎 **Formatação BR** | Números exibidos no padrão brasileiro (`1.234,56`) |
| 🧠 **Memória Completa** | `MC` · `MR` · `MS` · `M+` · `M-` com indicador visual |

---

## ✨ Preview

```text
┌─────────────────────────────────┐
│                           Sobre │  ← Top bar
├─────────────────────────────────┤
│                             12+ │  ← Equation Preview
│                        1.234,56 │  ← Display (Consolas)
├────┬────┬────┬────┬─────────────┤
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

## ✅ Funcionalidades

### 🔢 Operações Matemáticas

| Operação | Botão | Teclado |
| :--- | :---: | :---: |
| Adição | `+` | `+` |
| Subtração | `-` | `-` |
| Multiplicação | `*` | `*` |
| Divisão | `/` | `/` |
| Igualdade | `=` | `Enter` |
| Porcentagem | `%` | `%` |
| Raiz Quadrada | `√` | — |
| Inverso (1/x) | `1/x` | — |
| Inversão de Sinal | `±` | — |
| Separador Decimal | `,` | `,` ou `.` |

### 🧠 Gerenciamento de Memória

| Função | Descrição |
| :---: | :--- |
| `MC` | Limpa o valor salvo na memória |
| `MR` | Recupera o valor da memória para o display |
| `MS` | Salva o valor atual do display na memória |
| `M+` | Adiciona o valor atual ao valor salvo |
| `M-` | Subtrai o valor atual do valor salvo |
| **Indicador `M`** | Exibido no display quando a memória está em uso |

### ⌨️ Controles de Tela

| Botão | Teclado | Descrição |
| :---: | :---: | :--- |
| `←` | `Backspace` | Apaga o último dígito |
| `CE` | — | Limpa apenas a entrada atual |
| `C` | `Esc` / `Delete` | Limpa tudo e reinicia a calculadora |

### 🖥️ Interface e Experiência

- **Visor Duplo** — Equação em andamento (ex: `12 +`) na linha superior, valor atual na linha inferior.
- **Haptic Feedback** — Vibração tátil em dispositivos móveis, simulando o clique físico de botões reais.
- **Diálogo Sobre** — Popup com informações do desenvolvedor e link de contato via e-mail.

---

## 🏗️ Arquitetura

O projeto segue uma arquitetura **MVC simplificada**, garantindo separação clara de responsabilidades:

```mermaid
graph TD
    subgraph View
        A[main.py — UI & Eventos]
        C[GlassButton — Componente Visual]
        D[Visor Duplo — Equation + Display]
    end

    subgraph Model
        B[CalculatorState — Motor Matemático]
    end

    A -->|instancia| B
    A -->|renderiza| C
    A -->|renderiza| D
    C -->|on_click| A
    A -->|chama métodos| B
    B -->|retorna estado| A
    A -->|update_ui| D

    style A fill:#e6eff9,stroke:#8e9cbc,color:#1e395b
    style B fill:#d4dfef,stroke:#8797b2,color:#1e395b
    style C fill:#f0f4f9,stroke:#8797b2,color:#1e395b
    style D fill:#f0f4f9,stroke:#8797b2,color:#1e395b
```

| Camada | Arquivo | Responsabilidade |
| :---: | :--- | :--- |
| **Model** | `calculator_logic.py` | Toda lógica matemática, formatação brasileira, gerenciamento de memória e preview de equação |
| **View** | `main.py` | Componentes visuais (`GlassButton`, Visor Duplo), gradientes Aero Glass e layout |
| **Controller** | `main.py` | Orquestração de eventos `on_click`, haptic feedback e atualização da UI |

---

## 📁 Estrutura do Projeto

```text
ClassicCalculator_mobile/
├── assets/
│   ├── icon.png                  # Ícone da aplicação
│   └── fonts/
│       ├── SegoeUI.ttf           # Fonte dos botões e menus
│       └── consola.ttf           # Fonte monoespaçada do display
├── calculator_logic.py           # Motor matemático (CalculatorState)
├── main.py                       # Ponto de entrada e interface de usuário
├── requirements.txt              # Dependências do projeto
└── README.md                     # Documentação
```

---

## 🛠️ Stack Tecnológica

| Tecnologia | Versão | Função |
| :--- | :---: | :--- |
| [**Python**](https://www.python.org/) | `3.12+` | Linguagem principal |
| [**Flet**](https://flet.dev/) | `0.84+` | Framework UI multiplataforma (Flutter) |
| **Segoe UI** | — | Tipografia de botões, menus e diálogos |
| **Consolas** | — | Tipografia monoespaçada do display numérico |

---

## 🚀 Instalação e Execução

### Pré-requisitos

- [Python 3.12+](https://www.python.org/downloads/) instalado
- `pip` atualizado (`python -m pip install --upgrade pip`)

### 1. Clone o repositório

```bash
git clone https://github.com/caiquenovaes1994/ClassicCalculator_mobile.git
cd ClassicCalculator_mobile
```

### 2. Instale as dependências

```bash
pip install flet
```

### 3. Execute a aplicação

```bash
python main.py
```

> A calculadora abrirá em uma janela desktop de **340 × 560 px**.

---

## 📱 Build para Android (APK)

Para gerar o pacote `.apk` para dispositivos Android, utilize o **Flet CLI**:

```bash
flet build apk \
  --project "Calculadora Win7" \
  --org com.caiquenovaes.calc \
  --product "Calculadora Aero7"
```

> **Nota:** Certifique-se de ter o [Android SDK](https://developer.android.com/studio) e as dependências do Flet build configuradas corretamente.

---

## ⌨️ Atalhos de Teclado

| Tecla | Ação |
| :---: | :--- |
| `0` – `9` | Inserir dígito |
| `+` `-` `*` `/` | Operador matemático |
| `Enter` | Calcular resultado |
| `Backspace` | Apagar último dígito |
| `Esc` / `Delete` | Limpar tudo |
| `,` ou `.` | Separador decimal |
| `%` | Calcular porcentagem |

---

## 📄 Licença

Este projeto é de uso **pessoal e educacional**.  
Distribuição comercial não autorizada sem consentimento prévio do autor.

---

## 👨‍💻 Autor

<table>
  <tr>
    <td align="center">
      <strong>Caique Novaes</strong><br/>
      <a href="https://github.com/caiquenovaes1994">GitHub</a> · <a href="mailto:caiquenovaes1994@gmail.com">E-mail</a>
    </td>
  </tr>
</table>

---

<p align="center">
  Feito com 🐍 <strong>Python</strong> + ⚡ <strong>Flet</strong><br/>
  <sub>Inspirado no Windows 7 Aero Glass — © 2026</sub>
</p>
