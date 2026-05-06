# 📘 Guia de Modelagem Astah (Fiel à v10.x): Criar Flashcards

## 🎯 Objetivo
Personalização de deck.

> [!IMPORTANT]
> Dica Astah: Editor é uma classe de <<Fronteira>>.

## 🚀 Tutorial Passo a Passo Detalhado (Interface Astah)

### 1️⃣ Diagrama de Classe (Estrutura)
   - [ ] 1. **Crie 'MD_Alunos' e 'MD_Flashcards'.**
   - [ ] 2. **Método em Aluno: '+ criarCarta()'.**
   - [ ] 3. **Associação 1..*.**

**Como configurar no Astah:** Para adicionar o Estereótipo (ex: <<Entidade>>), selecione a classe, vá na aba **Stereotype** (na base da tela) e clique em **Add**.

### 2️⃣ Diagrama de Sequência (Processo)
   - [ ] 1. **Aluno usa :Editor para digitar dados.**
   - [ ] 2. **Editor envia dados para criar :MD_Flashcards.**
   - [ ] 3. **Confirmação de salvamento.**

**Dica de Notação:** Note que os nomes das Linhas de Vida agora começam com dois pontos (ex: `:Controlador`), indicando que são instâncias anônimas da classe.


---

## 🛠️ Artefatos de Alta Fidelidade (PlantUML)

### Diagrama de Classe (Premium)
![UC10_Classe](../../03_Artefatos_Gerados/UC10_Classe.png)

### Diagrama de Sequência (Premium)
![UC10_Sequencia](../../03_Artefatos_Gerados/UC10_Sequencia.png)


---

## 🛠️ Artefatos de Alta Fidelidade (PlantUML)

### Diagrama de Classe (Premium)
![UC10_Classe](../../03_Artefatos_Gerados/UC10_Classe.png)

### Diagrama de Sequência (Premium)
![UC10_Sequencia](../../03_Artefatos_Gerados/UC10_Sequencia.png)

---

## 📊 Referência Visual (Estilo Astah UML)
### Diagrama de Classe
```mermaid
classDiagram
    class MD_Alunos {
        <<Entidade>>
        +criarCarta()
    }
    class MD_Flashcards {
        <<Entidade>>
        +pergunta : string
        +resposta : string
    }
    MD_Alunos "1" --> "*" MD_Flashcards : cria
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant A as :Aluno
    participant E as :Editor
    participant F as :MD_Flashcards
    A->>E: entrada(p, r)
    E->>F: <<create>>(p, r)
    F-->>A: Sucesso
```

---
*Este manual foi otimizado para a versão 10.1.0 do Astah UML.*