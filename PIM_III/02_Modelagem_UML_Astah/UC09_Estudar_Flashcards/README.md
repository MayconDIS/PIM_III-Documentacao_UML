# 📘 Guia de Modelagem: Estudar Flashcards (SM-2)

## 🎯 Objetivo do Caso de Uso
Ciclo de estudo principal utilizando o algoritmo de repetição espaçada.

> [!TIP]
> Dica Astah: No diagrama de sequência, use um 'Fragmento de Loop' para indicar a revisão de múltiplos cartões.

## 🚀 Tutorial de Criação Passo a Passo (Astah)

### 1️⃣ Criando o Diagrama de Classe
1. No Menu Superior, vá em **Projeto** > **Árvore de Estrutura**.
2. Clique com o botão direito e selecione **Adicionar Diagrama** > **Diagrama de Classe**.
3. Arraste as classes para a área de desenho:
   - [ ] Criar **MD_MotorSM2**.
   - [ ] Criar **MD_Flashcards**.
   - [ ] Criar **Atributos: intervalo: int, facilidade: decimal**.
4. Adicione os **Atributos** e **Métodos** clicando com o botão direito na classe.
5. Use as ferramentas de **Associação, Dependência ou Herança** para ligar as classes conforme a referência abaixo.

### 2️⃣ Criando o Diagrama de Sequência
1. Clique com o botão direito no Caso de Uso (na Árvore) e selecione **Adicionar Diagrama** > **Diagrama de Sequência**.
2. Adicione os **Participantes** (Linhas de Vida) no topo da tela.
3. Desenhe as setas de mensagem seguindo rigorosamente esta ordem:
   - [ ] 1. **Aluno -> MD_Flashcards: lerPergunta()**
   - [ ] 2. **Aluno -> MD_MotorSM2: calcularIntervalo(feedback)**
   - [ ] 3. **MD_MotorSM2 -> MD_Flashcards: atualizar()**
4. Lembre-se de adicionar as **Barras de Ativação** clicando sobre a linha de vida onde houver processamento.

---

## 📊 Referência Visual (Padrão PT-BR)
### Diagrama de Classe
```mermaid
classDiagram
    class MD_MotorSM2 {
        +aplicarSM2(feedback)
    }
    class MD_Flashcards {
        +date proximaRevisao
    }
    MD_MotorSM2 --> MD_Flashcards : atualiza
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant A as Aluno
    participant M as MD_MotorSM2
    participant F as MD_Flashcards
    A->>F: lerPergunta()
    A->>F: verResposta()
    A->>M: informarDificuldade(1-5)
    M->>M: aplicarSM2()
    M->>F: setProximaRevisao(data)
    F-->>A: Carta Agendada
```

---
*Manual técnico gerado em Português para conformidade com o PIM III.*