# 📘 Guia de Modelagem Astah (Fiel à v10.x): Desbloquear Fases e Módulos

## 🎯 Objetivo
Progressão condicionada.

> [!IMPORTANT]
> Dica Astah: Use Dependência para mostrar verificação de progresso.

## 🚀 Tutorial Passo a Passo Detalhado (Interface Astah)

### 1️⃣ Diagrama de Classe (Estrutura)
   - [ ] 1. **Crie 'Modulo' com '+ bloqueada : bool'.**
   - [ ] 2. **Crie 'GerenciadorProgresso' (<<Controle>>).**
   - [ ] 3. **Dependência do Gerenciador para Alunos e Fases.**

**Como configurar no Astah:** Para adicionar o Estereótipo (ex: <<Entidade>>), selecione a classe, vá na aba **Stereotype** (na base da tela) e clique em **Add**.

### 2️⃣ Diagrama de Sequência (Processo)
   - [ ] 1. **Gerenciador pede progresso ao Aluno.**
   - [ ] 2. **Se ok, chama 'desbloquear()' na :Modulo.**
   - [ ] 3. **Fase muda estado para liberada.**

**Dica de Notação:** Note que os nomes das Linhas de Vida agora começam com dois pontos (ex: `:Controlador`), indicando que são instâncias anônimas da classe.


---

## 🛠️ Artefatos de Alta Fidelidade (PlantUML)

### Diagrama de Classe (Premium)
![UC13_Classe](./UC13_Classe.png)

### Diagrama de Sequência (Premium)
![UC13_Sequencia](./UC13_Sequencia.png)

---

## 📊 Referência Visual (Estilo Astah UML)
### Diagrama de Classe
```mermaid
classDiagram
    class Modulo {
        <<Entidade>>
        +bloqueada : bool
        +desbloquear()
    }
    class Aluno {
        <<Entidade>>
        +progresso : float
    }
    Modulo ..> Aluno : verifica
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant M as :GerenciadorProgresso
    participant A as :Aluno
    participant F as :Modulo
    M->>A: obterProgresso()
    M->>F: desbloquear()
    F-->>M: Sucesso
```

---
*Este manual foi otimizado para a versão 10.1.0 do Astah UML.*
---

## 🏛️ Contexto Arquitetural
Este Caso de Uso integra a arquitetura modular do sistema Nex_TI. Para uma visão das relações entre todas as classes, consulte o [Diagrama de Classes Global](./Diagrama_Classes_Global.png).

---

[⬅️ Voltar para o Dashboard Visual](../../01_Relatorios_e_Dashboard/DASHBOARD_VISUAL.md)
