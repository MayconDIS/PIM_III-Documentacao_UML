# 📘 Guia de Modelagem Astah (Fiel à v10.x): Consultar Agente IA

## 🎯 Objetivo
Interação instantânea.

> [!IMPORTANT]
> Dica Astah: Represente MD_Duvidas como <<Entidade>>.

## 🚀 Tutorial Passo a Passo Detalhado (Interface Astah)

### 1️⃣ Diagrama de Classe (Estrutura)
   - [ ] 1. **Crie 'AgenteIA' com '+ responder()'.**
   - [ ] 2. **Crie 'MD_Duvidas' com '+ pergunta : string' e '+ resposta : string'.**
   - [ ] 3. **Dependência da IA para MD_Duvidas.**

**Como configurar no Astah:** Para adicionar o Estereótipo (ex: <<Entidade>>), selecione a classe, vá na aba **Stereotype** (na base da tela) e clique em **Add**.

### 2️⃣ Diagrama de Sequência (Processo)
   - [ ] 1. **Aluno envia dúvida para :AgenteIA.**
   - [ ] 2. **AgenteIA processa linguagem natural.**
   - [ ] 3. **AgenteIA retorna resposta ao Aluno.**

**Dica de Notação:** Note que os nomes das Linhas de Vida agora começam com dois pontos (ex: `:Controlador`), indicando que são instâncias anônimas da classe.

---

## 📊 Referência Visual (Estilo Astah UML)
### Diagrama de Classe
```mermaid
classDiagram
    class AgenteIA {
        <<Controle>>
        +responder(pergunta)
    }
    class MD_Duvidas {
        <<Entidade>>
        +pergunta : string
        +resposta : string
    }
    AgenteIA ..> MD_Duvidas : consulta
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant A as :Aluno
    participant IA as :AgenteIA
    A->>IA: enviarDuvida(texto)
    IA->>IA: processarLinguagem()
    IA-->>A: Resposta
```

---
*Este manual foi otimizado para a versão 10.1.0 do Astah UML.*