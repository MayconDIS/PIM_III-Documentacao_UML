# 📘 Guia de Modelagem Astah (Fiel à v10.x): Realizar Simulado ENADE

## 🎯 Objetivo
Treinamento intensivo.

> [!IMPORTANT]
> Dica Astah: Questao é uma <<Entidade>>.

## 🚀 Tutorial Passo a Passo Detalhado (Interface Astah)

### 1️⃣ Diagrama de Classe (Estrutura)
   - [ ] 1. **Crie 'MD_Simulado' e 'Questao'.**
   - [ ] 2. **Composição (losango preto).**
   - [ ] 3. **Simulado: '+ tempoRestante : int'.**

**Como configurar no Astah:** Para adicionar o Estereótipo (ex: <<Entidade>>), selecione a classe, vá na aba **Stereotype** (na base da tela) e clique em **Add**.

### 2️⃣ Diagrama de Sequência (Processo)
   - [ ] 1. **Aluno inicia Simulado.**
   - [ ] 2. **Simulado liga o :Temporizador.**
   - [ ] 3. **Após responder tudo, Simulado desliga e dá a nota.**

**Dica de Notação:** Note que os nomes das Linhas de Vida agora começam com dois pontos (ex: `:Controlador`), indicando que são instâncias anônimas da classe.

---

## 📊 Referência Visual (Estilo Astah UML)
### Diagrama de Classe
```mermaid
classDiagram
    class MD_Simulado {
        <<Entidade>>
        +tempoRestante : int
        +iniciarTeste()
    }
    class Questao {
        <<Entidade>>
        +texto : string
    }
    MD_Simulado "1" *-- "*" Questao
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant A as :Aluno
    participant S as :MD_Simulado
    participant T as :Temporizador
    A->>S: iniciarTeste()
    S->>T: iniciar()
    A->>S: responder()
    S-->>A: Nota Final
```

---
*Este manual foi otimizado para a versão 10.1.0 do Astah UML.*