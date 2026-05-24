# 📘 Guia de Modelagem Astah (Fiel à v10.x): Consultar Agente IA

## 🎯 Objetivo
Interação instantânea.

## 🌊 Fluxos (Normal e Alternativo)
- **Fluxo Normal:** O aluno solicita ajuda à IA no chat. A IA (Agente Especialista) recebe a dúvida, identifica o contexto do flashcard atual através de Processamento de Linguagem Natural (NLP) e retorna uma explicação detalhada e pedagógica.
- **Fluxo Alternativo:** A IA não consegue interpretar a pergunta ou o aluno faz uma pergunta muito fora de contexto. A IA solicita reformulação ou sugere automaticamente "Escalar a dúvida para o Tutor humano".

> [!IMPORTANT]
> Dica Astah: Represente Duvida como <<Entidade>>.

## 🚀 Tutorial Passo a Passo Detalhado (Interface Astah)

### 1️⃣ Diagrama de Classe (Estrutura)
   - [ ] 1. **Crie 'Agente_IA' com '+ responderDuvida()'.**
   - [ ] 2. **Crie 'Duvida' com '- descricao : string'.**
   - [ ] 3. **Dependência da IA para Duvida.**

**Como configurar no Astah:** Para adicionar o Estereótipo (ex: <<Entidade>>), selecione a classe, vá na aba **Stereotype** (na base da tela) e clique em **Add**.

### 2️⃣ Diagrama de Sequência (Processo)
   - [ ] 1. **Aluno envia dúvida para :Agente_IA.**
   - [ ] 2. **Agente_IA processa linguagem natural.**
   - [ ] 3. **Agente_IA retorna resposta ao Aluno.**

**Dica de Notação:** Note que os nomes das Linhas de Vida agora começam com dois pontos (ex: `:Controlador`), indicando que são instâncias anônimas da classe.

---

## 📊 Referência Visual (Estilo Astah UML)
### Diagrama de Classe
```mermaid
classDiagram
    class Agente_IA {
        <<Controle>>
        +responderDuvida(duvida)
    }
    class Duvida {
        <<Entidade>>
        -descricao : string
    }
    Agente_IA ..> Duvida : consulta
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant A as :Aluno
    participant IA as :Agente_IA
    A->>IA: enviarDuvida(texto)
    IA->>IA: processarLinguagem()
    IA-->>A: Resposta
```

---
*Este manual foi otimizado para a versão 10.1.0 do Astah UML.*