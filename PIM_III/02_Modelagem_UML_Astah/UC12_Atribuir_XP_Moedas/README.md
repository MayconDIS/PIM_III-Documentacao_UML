# 📘 Guia de Modelagem Astah (Fiel à v10.x): Atribuir XP e Moedas

## 🎯 Objetivo
Motor de recompensas.

> [!IMPORTANT]
> Dica Astah: Gamificacao é um <<Controle>>.

## 🚀 Tutorial Passo a Passo Detalhado (Interface Astah)

### 1️⃣ Diagrama de Classe (Estrutura)
   - [ ] 1. **Crie 'SistemaGamificacao' (<<Controle>>) e 'Aluno'.**
   - [ ] 2. **Alunos: '+ pontos : int', '+ moedas : int'.**
   - [ ] 3. **Dependência de Gamificação para Alunos.**

**Como configurar no Astah:** Para adicionar o Estereótipo (ex: <<Entidade>>), selecione a classe, vá na aba **Stereotype** (na base da tela) e clique em **Add**.

### 2️⃣ Diagrama de Sequência (Processo)
   - [ ] 1. **Sistema notifica :SistemaGamificacao.**
   - [ ] 2. **Gamificação calcula bônus.**
   - [ ] 3. **Gamificação chama 'creditarXP()' no Aluno.**

**Dica de Notação:** Note que os nomes das Linhas de Vida agora começam com dois pontos (ex: `:Controlador`), indicando que são instâncias anônimas da classe.


---

## 🛠️ Artefatos de Alta Fidelidade (PlantUML)

### Diagrama de Classe (Premium)
![UC12_Classe](./UC12_Classe.png)

### Diagrama de Sequência (Premium)
![UC12_Sequencia](./UC12_Sequencia.png)


---

## 🛠️ Artefatos de Alta Fidelidade (PlantUML)

### Diagrama de Classe (Premium)
![UC12_Classe](./UC12_Classe.png)

### Diagrama de Sequência (Premium)
![UC12_Sequencia](./UC12_Sequencia.png)

---

## 📊 Referência Visual (Estilo Astah UML)
### Diagrama de Classe
```mermaid
classDiagram
    class SistemaGamificacao {
        <<Controle>>
        +calcularBonus()
    }
    class Aluno {
        <<Entidade>>
        +pontos : int
        +moedas : int
    }
    SistemaGamificacao ..> Aluno : credita
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant S as :Sistema
    participant G as :SistemaGamificacao
    participant A as :Aluno
    S->>G: concluirTarefa()
    G->>G: calcular()
    G->>A: creditarXP(100)
    G-->>S: Ok
```

---
*Este manual foi otimizado para a versão 10.1.0 do Astah UML.*
---

## 🏛️ Contexto Arquitetural
Este Caso de Uso integra a arquitetura modular do sistema Nex_TI. Para uma visão das relações entre todas as classes, consulte o [Diagrama de Classes Global](./Diagrama_Classes_Global.png).

---

[⬅️ Voltar para o Dashboard Visual](../../01_Relatorios_e_Dashboard/DASHBOARD_VISUAL.md)
