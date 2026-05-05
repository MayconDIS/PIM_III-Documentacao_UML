# 📘 Guia de Modelagem Astah (Fiel à v10.x): Escalar Dúvida para Tutor

## 🎯 Objetivo
Transferência IA -> Humano.

> [!IMPORTANT]
> Dica Astah: AgenteIA é um <<Controle>>.

## 🚀 Tutorial Passo a Passo Detalhado (Interface Astah)

### 1️⃣ Diagrama de Classe (Estrutura)
   - [ ] 1. **Crie 'AgenteIA' (<<Controle>>) com '+ analisar()' e '+ escalar()'.**
   - [ ] 2. **Crie 'MD_Tutor' com '+ responderDuvida()'.**
   - [ ] 3. **Associação simples entre os dois.**

**Como configurar no Astah:** Para adicionar o Estereótipo (ex: <<Entidade>>), selecione a classe, vá na aba **Stereotype** (na base da tela) e clique em **Add**.

### 2️⃣ Diagrama de Sequência (Processo)
   - [ ] 1. **AgenteIA detecta complexidade.**
   - [ ] 2. **AgenteIA envia 'escalar(duvida)' para :MD_Tutor.**
   - [ ] 3. **Tutor responde ao Aluno.**

**Dica de Notação:** Note que os nomes das Linhas de Vida agora começam com dois pontos (ex: `:Controlador`), indicando que são instâncias anônimas da classe.

---

## 📊 Referência Visual (Estilo Astah UML)
### Diagrama de Classe
```mermaid
classDiagram
    class AgenteIA {
        <<Controle>>
        +analisar()
        +escalar(duvida)
    }
    class MD_Tutor {
        <<Entidade>>
        +responderDuvida()
    }
    AgenteIA --> MD_Tutor : notifica
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant IA as :AgenteIA
    participant T as :MD_Tutor
    participant Al as :Aluno
    IA->>IA: detectarComplexidade()
    IA->>T: escalar(duvida, id)
    T-->>Al: Resposta
```

---
*Este manual foi otimizado para a versão 10.1.0 do Astah UML.*