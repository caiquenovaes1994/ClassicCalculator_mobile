# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

---

## [1.0.0] — 2026-05-12

> **Primeira versão estável do Classic Calculator — Windows 7 Aero Glass para Android.**

### ✨ Adicionado

- **Interface Aero Glass** — Gradientes azul-acinzentados, bordas sutis e bordas arredondadas que replicam fielmente o tema visual do Windows 7.
- **Visor Duplo** — Exibição simultânea da equação em andamento (`equation_preview`) e do valor atual no display principal.
- **Componente `GlassButton`** — Botão reutilizável com gradiente Aero Glass, suportando dois tipos visuais: numérico e operador.
- **Motor matemático (`CalculatorState`)** — Lógica completa isolada em `calculator_logic.py`, incluindo:
  - Operações básicas: adição, subtração, multiplicação e divisão.
  - Operações avançadas: porcentagem (`%`), raiz quadrada (`√`) e inverso (`1/x`).
  - Inversão de sinal (`±`) e separador decimal (`,`).
  - Backspace (`←`), limpar entrada (`CE`) e resetar tudo (`C`).
- **Gerenciamento completo de memória** — Funções `MC`, `MR`, `MS`, `M+` e `M-` com indicador visual `M` no display.
- **Formatação numérica brasileira** — Números exibidos no padrão `1.234,56` (ponto como separador de milhar, vírgula como decimal).
- **Haptic Feedback** — Vibração tátil a cada pressionamento de botão em dispositivos Android.
- **Barra de título minimalista** — Menu superior com acesso ao diálogo **Sobre**.
- **Diálogo "Sobre"** — Popup modal com nome do aplicativo, versão, autor e link de contato via e-mail.
- **Fontes customizadas** — Integração de `Segoe UI` (interface) e `Consolas` (display numérico) via assets locais.
- **Suporte a notch (Android)** — Padding superior dinâmico para evitar sobreposição do entalhe em dispositivos modernos.
- **Arquitetura MVC simplificada** — Separação clara entre `Model` (`calculator_logic.py`) e `View/Controller` (`main.py`).
- **Build para Android (APK)** — Suporte ao comando `flet build apk` com configurações de organização e produto definidas.
- **Atalhos de teclado** — Suporte a `0–9`, `+`, `-`, `*`, `/`, `Enter`, `Backspace`, `Esc`, `Delete`, `,` e `%`.
- **Configuração de ambiente** — Arquivos `requirements.txt`, `pyrightconfig.json` e `.markdownlint.json` para padronização do projeto.

### 🔧 Alterado

- N/A — versão inicial.

### 🗑️ Removido

- N/A — versão inicial.

### 🐛 Corrigido

- N/A — versão inicial.

---

## Convenções de Versionamento

Este projeto segue o padrão **Semantic Versioning (SemVer)**:

| Componente | Quando incrementar |
| :---: | :--- |
| **MAJOR** (`X`.0.0) | Mudanças incompatíveis com versões anteriores |
| **MINOR** (1.`X`.0) | Novas funcionalidades compatíveis com versões anteriores |
| **PATCH** (1.0.`X`) | Correções de bugs compatíveis com versões anteriores |

---

<p align="center">
  <sub>Classic Calculator — Windows 7 Aero Glass · © 2026 Caique Novaes</sub>
</p>
