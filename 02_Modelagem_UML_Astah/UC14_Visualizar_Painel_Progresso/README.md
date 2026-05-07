# 📘 Guia de Modelagem Astah (Fiel à v10.x): Visualizar Painel de Progresso

## 🎯 Objetivo
Hub central.

> [!IMPORTANT]
> Dica Astah: PainelVisual é uma <<Fronteira>>.

## 🚀 Tutorial Passo a Passo Detalhado (Interface Astah)

### 1️⃣ Diagrama de Classe (Estrutura)
   - [ ] 1. **Crie 'PainelVisual' (<<Fronteira>>) e 'Aluno'.**
   - [ ] 2. **PainelVisual: '+ renderizar()'.**
   - [ ] 3. **Dependência para leitura de dados.**

**Como configurar no Astah:** Para adicionar o Estereótipo (ex: <<Entidade>>), selecione a classe, vá na aba **Stereotype** (na base da tela) e clique em **Add**.

### 2️⃣ Diagrama de Sequência (Processo)
   - [ ] 1. **Aluno abre início.**
   - [ ] 2. **Painel pede dados de progresso ao Aluno.**
   - [ ] 3. **Painel exibe informações.**

**Dica de Notação:** Note que os nomes das Linhas de Vida agora começam com dois pontos (ex: `:Controlador`), indicando que são instâncias anônimas da classe.


---

## 🛠️ Artefatos de Alta Fidelidade (PlantUML)

### Diagrama de Classe (Premium)
![UC14_Classe](./UC14_Classe.png)

### Diagrama de Sequência (Premium)
![UC14_Sequencia](./UC14_Sequencia.png)

---

## 📊 Referência Visual (Estilo Astah UML)
### Diagrama de Classe
```mermaid
classDiagram
    class PainelVisual {
        <<Fronteira>>
        +renderizar()
    }
    class Aluno {
        <<Entidade>>
        +obterProgresso()
    }
    PainelVisual ..> Aluno : lê
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant Al as :Aluno
    participant D as :PainelVisual
    Al->>D: abrirHome()
    D->>D: renderizar()
    D-->>Al: Ok
```

---
*Este manual foi otimizado para a versão 10.1.0 do Astah UML.*
---

## 🏛️ Contexto Arquitetural
Este Caso de Uso integra a arquitetura modular do sistema Nex_TI. Para uma visão das relações entre todas as classes, consulte o [Diagrama de Classes Global](./Diagrama_Classes_Global.png).

---

[⬅️ Voltar para o Dashboard Visual](../../01_Relatorios_e_Dashboard/DASHBOARD_VISUAL.md)
