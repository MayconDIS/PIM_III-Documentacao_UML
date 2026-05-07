# 📘 Guia de Modelagem Astah (Fiel à v10.x): Acompanhar Desempenho

## 🎯 Objetivo
Métricas de progresso.

> [!IMPORTANT]
> Dica Astah: PainelVisual deve usar o Estereótipo <<Fronteira>> (Boundary).

## 🚀 Tutorial Passo a Passo Detalhado (Interface Astah)

### 1️⃣ Diagrama de Classe (Estrutura)
   - [ ] 1. **Crie 'Tutor', 'Aluno' e 'PainelVisual' (<<Fronteira>>).**
   - [ ] 2. **Em Alunos: '+ progresso : float'.**
   - [ ] 3. **Ligue Tutor a Aluno via Dependência através do Painel.**

**Como configurar no Astah:** Para adicionar o Estereótipo (ex: <<Entidade>>), selecione a classe, vá na aba **Stereotype** (na base da tela) e clique em **Add**.

### 2️⃣ Diagrama de Sequência (Processo)
   - [ ] 1. **Tutor pede 'visualizar(id)' no PainelVisual.**
   - [ ] 2. **PainelVisual chama 'obterMetricas()' no objeto :Aluno.**
   - [ ] 3. **Painel renderiza o relatório final.**

**Dica de Notação:** Note que os nomes das Linhas de Vida agora começam com dois pontos (ex: `:Controlador`), indicando que são instâncias anônimas da classe.


---

## 🛠️ Artefatos de Alta Fidelidade (PlantUML)

### Diagrama de Classe (Premium)
![UC06_Classe](./UC06_Classe.png)

### Diagrama de Sequência (Premium)
![UC06_Sequencia](./UC06_Sequencia.png)

---

## 📊 Referência Visual (Estilo Astah UML)
### Diagrama de Classe
```mermaid
classDiagram
    class Tutor {
        +acompanharDesempenho()
    }
    class Aluno {
        <<Entidade>>
        +progresso : float
    }
    class PainelVisual {
        <<Fronteira>>
        +renderizar()
    }
    Tutor ..> Aluno : visualiza
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant T as :Tutor
    participant D as :PainelVisual
    participant A as :Aluno
    T->>D: visualizar(id)
    activate D
    D->>A: obterMetricas()
    A-->>D: dados
    D-->>T: Relatório Visual
    deactivate D
```

---
*Este manual foi otimizado para a versão 10.1.0 do Astah UML.*
---

## 🏛️ Contexto Arquitetural
Este Caso de Uso integra a arquitetura modular do sistema Nex_TI. Para uma visão das relações entre todas as classes, consulte o [Diagrama de Classes Global](./Diagrama_Classes_Global.png).

---

[⬅️ Voltar para o Dashboard Visual](../../01_Relatorios_e_Dashboard/DASHBOARD_VISUAL.md)
