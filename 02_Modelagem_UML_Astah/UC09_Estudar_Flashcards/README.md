# 📘 Guia de Modelagem Astah (Fiel à v10.x): Estudar Flashcards (SM-2)

## 🎯 Objetivo
Repetição espaçada.

> [!IMPORTANT]
> Dica Astah: No Astah, use 'Self-Message' para o algoritmo SM-2.

## 🚀 Tutorial Passo a Passo Detalhado (Interface Astah)

### 1️⃣ Diagrama de Classe (Estrutura)
   - [ ] 1. **Crie 'MotorSM2' (<<Controle>>) e 'Flashcard_SM2'.**
   - [ ] 2. **Atributos no Flashcard: '+ proximaRevisao : date'.**
   - [ ] 3. **Associação do Motor para o Flashcard.**

**Como configurar no Astah:** Para adicionar o Estereótipo (ex: <<Entidade>>), selecione a classe, vá na aba **Stereotype** (na base da tela) e clique em **Add**.

### 2️⃣ Diagrama de Sequência (Processo)
   - [ ] 1. **Aluno lê pergunta.**
   - [ ] 2. **Aluno informa dificuldade (1-5) ao :MotorSM2.**
   - [ ] 3. **Motor aplica algoritmo e atualiza data no Flashcard.**

**Dica de Notação:** Note que os nomes das Linhas de Vida agora começam com dois pontos (ex: `:Controlador`), indicando que são instâncias anônimas da classe.


---

## 🛠️ Artefatos de Alta Fidelidade (PlantUML)

### Diagrama de Classe (Premium)
![UC09_Classe](./UC09_Classe.png)

### Diagrama de Sequência (Premium)
![UC09_Sequencia](./UC09_Sequencia.png)


---

## 🛠️ Artefatos de Alta Fidelidade (PlantUML)

### Diagrama de Classe (Premium)
![UC09_Classe](./UC09_Classe.png)

### Diagrama de Sequência (Premium)
![UC09_Sequencia](./UC09_Sequencia.png)

---

## 📊 Referência Visual (Estilo Astah UML)
### Diagrama de Classe
```mermaid
classDiagram
    class MotorSM2 {
        <<Controle>>
        +aplicarSM2(feedback)
    }
    class Flashcard_SM2 {
        <<Entidade>>
        +proximaRevisao : date
    }
    MotorSM2 --> Flashcard_SM2 : atualiza
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant A as :Aluno
    participant M as :MotorSM2
    participant F as :Flashcard_SM2
    A->>F: lerPergunta()
    A->>M: informarDificuldade(1-5)
    M->>M: aplicarSM2()
    M->>F: setProximaRevisao(data)
    F-->>A: Ok
```

---
*Este manual foi otimizado para a versão 10.1.0 do Astah UML.*
---

## 🏛️ Contexto Arquitetural
Este Caso de Uso integra a arquitetura modular do sistema Nex_TI. Para uma visão das relações entre todas as classes, consulte o [Diagrama de Classes Global](./Diagrama_Classes_Global.png).

---

[⬅️ Voltar para o Dashboard Visual](../../01_Relatorios_e_Dashboard/DASHBOARD_VISUAL.md)
