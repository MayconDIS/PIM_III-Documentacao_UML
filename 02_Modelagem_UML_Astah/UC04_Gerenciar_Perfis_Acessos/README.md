# 📘 Guia de Modelagem Astah (Fiel à v10.x): Gerenciar Perfis e Acessos

## 🎯 Objetivo
Administração de papéis e permissões.

> [!IMPORTANT]
> Dica Astah: O GerenciadorAcesso é um <<Controle>>.

## 🚀 Tutorial Passo a Passo Detalhado (Interface Astah)

### 1️⃣ Diagrama de Classe (Estrutura)
   - [ ] 1. **Crie 'Administrador' e 'Usuario'.**
   - [ ] 2. **Em 'Usuario', adicione '+ papel : string'.**
   - [ ] 3. **Crie 'GerenciadorAcesso' (<<Controle>>).**
   - [ ] 4. **Desenhe uma 'Associação' simples de Admin para Usuarios.**

**Como configurar no Astah:** Para adicionar o Estereótipo (ex: <<Entidade>>), selecione a classe, vá na aba **Stereotype** (na base da tela) e clique em **Add**.

### 2️⃣ Diagrama de Sequência (Processo)
   - [ ] 1. **O Admin solicita 'alterarPapel()' ao GerenciadorAcesso.**
   - [ ] 2. **O GerenciadorAcesso chama 'setPapel()' no Usuario alvo.**
   - [ ] 3. **Retorno de confirmação para o Admin.**

**Dica de Notação:** Note que os nomes das Linhas de Vida agora começam com dois pontos (ex: `:Controlador`), indicando que são instâncias anônimas da classe.


---

## 🛠️ Artefatos de Alta Fidelidade (PlantUML)

### Diagrama de Classe (Premium)
![UC04_Classe](./UC04_Classe.png)

### Diagrama de Sequência (Premium)
![UC04_Sequencia](./UC04_Sequencia.png)

---

## 📊 Referência Visual (Estilo Astah UML)
### Diagrama de Classe
```mermaid
classDiagram
    class Administrador {
        +gerenciarAcesso()
    }
    class Usuario {
        <<Entidade>>
        +papel : string
    }
    Administrador --> Usuario : administra
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant A as :Admin
    participant M as :GerenciadorAcesso
    participant U as :Usuario
    A->>M: alterarPapel(id, papel)
    activate M
    M->>U: setPapel(papel)
    U-->>M: ok
    M-->>A: Sucesso
    deactivate M
```

---
*Este manual foi otimizado para a versão 10.1.0 do Astah UML.*
---

## 🏛️ Contexto Arquitetural
Este Caso de Uso integra a arquitetura modular do sistema Nex_TI. Para uma visão das relações entre todas as classes, consulte o [Diagrama de Classes Global](./Diagrama_Classes_Global.png).

---

[⬅️ Voltar para o Dashboard Visual](../../01_Relatorios_e_Dashboard/DASHBOARD_VISUAL.md)
