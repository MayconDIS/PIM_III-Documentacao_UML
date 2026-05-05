# 📘 Guia de Modelagem Astah (Fiel à v10.x): Visualizar Painel de Progresso

## 🎯 Objetivo
Hub central.

> [!IMPORTANT]
> Dica Astah: PainelVisual é uma <<Fronteira>>.

## 🚀 Tutorial Passo a Passo Detalhado (Interface Astah)

### 1️⃣ Diagrama de Classe (Estrutura)
   - [ ] 1. **Crie 'PainelVisual' (<<Fronteira>>) e 'MD_Alunos'.**
   - [ ] 2. **PainelVisual: '+ renderizar()'.**
   - [ ] 3. **Dependência para leitura de dados.**

**Como configurar no Astah:** Para adicionar o Estereótipo (ex: <<Entidade>>), selecione a classe, vá na aba **Stereotype** (na base da tela) e clique em **Add**.

### 2️⃣ Diagrama de Sequência (Processo)
   - [ ] 1. **Aluno abre início.**
   - [ ] 2. **Painel pede dados de progresso ao Aluno.**
   - [ ] 3. **Painel exibe informações.**

**Dica de Notação:** Note que os nomes das Linhas de Vida agora começam com dois pontos (ex: `:Controlador`), indicando que são instâncias anônimas da classe.

---

## 📊 Referência Visual (Estilo Astah UML)
### Diagrama de Classe
```mermaid
classDiagram
    class PainelVisual {
        <<Fronteira>>
        +renderizar()
    }
    class MD_Alunos {
        <<Entidade>>
        +obterProgresso()
    }
    PainelVisual ..> MD_Alunos : lê
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