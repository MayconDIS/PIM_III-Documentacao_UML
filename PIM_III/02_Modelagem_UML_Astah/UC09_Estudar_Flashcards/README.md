# 📘 Guia de Modelagem Astah (Fiel à v10.x): Estudar Flashcards (SM-2)

## 🎯 Objetivo
Repetição espaçada.

> [!IMPORTANT]
> Dica Astah: No Astah, use 'Self-Message' para o algoritmo SM-2.

## 🚀 Tutorial Passo a Passo Detalhado (Interface Astah)

### 1️⃣ Diagrama de Classe (Estrutura)
   - [ ] 1. **Crie 'MD_MotorSM2' (<<Controle>>) e 'MD_Flashcards'.**
   - [ ] 2. **Atributos no Flashcard: '+ proximaRevisao : date'.**
   - [ ] 3. **Associação do Motor para o Flashcard.**

**Como configurar no Astah:** Para adicionar o Estereótipo (ex: <<Entidade>>), selecione a classe, vá na aba **Stereotype** (na base da tela) e clique em **Add**.

### 2️⃣ Diagrama de Sequência (Processo)
   - [ ] 1. **Aluno lê pergunta.**
   - [ ] 2. **Aluno informa dificuldade (1-5) ao :MD_MotorSM2.**
   - [ ] 3. **Motor aplica algoritmo e atualiza data no Flashcard.**

**Dica de Notação:** Note que os nomes das Linhas de Vida agora começam com dois pontos (ex: `:Controlador`), indicando que são instâncias anônimas da classe.

---

## 📊 Referência Visual (Estilo Astah UML)
### Diagrama de Classe
```mermaid
classDiagram
    class MD_MotorSM2 {
        <<Controle>>
        +aplicarSM2(feedback)
    }
    class MD_Flashcards {
        <<Entidade>>
        +proximaRevisao : date
    }
    MD_MotorSM2 --> MD_Flashcards : atualiza
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant A as :Aluno
    participant M as :MD_MotorSM2
    participant F as :MD_Flashcards
    A->>F: lerPergunta()
    A->>M: informarDificuldade(1-5)
    M->>M: aplicarSM2()
    M->>F: setProximaRevisao(data)
    F-->>A: Ok
```

---
*Este manual foi otimizado para a versão 10.1.0 do Astah UML.*