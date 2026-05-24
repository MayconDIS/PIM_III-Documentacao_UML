# 📘 Guia de Modelagem Astah (Fiel à v10.x): Atribuir XP e Moedas

## 🎯 Objetivo
Motor de recompensas.

## 🌊 Fluxos (Normal e Alternativo)
- **Fluxo Normal:** Ao final de um evento de aprendizagem validado (simulado ou sessão de flashcards), a rotina de gamificação é acionada invisivelmente no backend. O sistema soma os XP ao histórico do aluno, verifica se ele subiu de nível, e deposita o valor equivalente em moedas virtuais.
- **Fluxo Alternativo:** O sistema detecta que o aluno passou rápido demais pelas cartas (indício de burla/click spam). O sistema reduz drasticamente o multiplicador de XP para desestimular esse comportamento.

> [!IMPORTANT]
> Dica Astah: Gamificacao é um <<Controle>>.

## 🚀 Tutorial Passo a Passo Detalhado (Interface Astah)

### 1️⃣ Diagrama de Classe (Estrutura)
   - [ ] 1. **Crie 'Gamificacao' (<<Controle>>) e 'Aluno'.**
   - [ ] 2. **Aluno: '- pontos : int', '- moedas : int'.**
   - [ ] 3. **Dependência de Gamificação para Aluno.**

**Como configurar no Astah:** Para adicionar o Estereótipo (ex: <<Entidade>>), selecione a classe, vá na aba **Stereotype** (na base da tela) e clique em **Add**.

### 2️⃣ Diagrama de Sequência (Processo)
   - [ ] 1. **Sistema notifica :Gamificacao.**
   - [ ] 2. **Gamificação calcula bônus.**
   - [ ] 3. **Gamificação chama 'creditarXP()' no Aluno.**

**Dica de Notação:** Note que os nomes das Linhas de Vida agora começam com dois pontos (ex: `:Controlador`), indicando que são instâncias anônimas da classe.

---

## 📊 Referência Visual (Estilo Astah UML)
### Diagrama de Classe
```mermaid
classDiagram
    class Gamificacao {
        <<Controle>>
        +calcularBonus()
    }
    class Aluno {
        <<Entidade>>
        -pontos : int
        -moedas : int
    }
    Gamificacao ..> Aluno : credita
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant S as :Sistema
    participant G as :Gamificacao
    participant A as :Aluno
    S->>G: concluirTarefa()
    G->>G: calcular()
    G->>A: creditarXP(100)
    G-->>S: Ok
```

---
*Este manual foi otimizado para a versão 10.1.0 do Astah UML.*