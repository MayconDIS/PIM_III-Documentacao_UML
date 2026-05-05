# 🎓 Guia Educativo: Modelagem UML Passo a Passo

Este guia ensina a lógica de construção dos diagramas para o sistema Nex_TI, focado na prática para o software Astah.

---

## 1. 🏗️ Diagrama de Classe: O "Quem" e o "O Que"
O objetivo aqui é descrever a **estrutura**. Imagine que você está definindo as peças de um tabuleiro de xadrez.

### Passo a Passo:
1.  **Identifique as Entidades (Models)**: São as classes que guardam dados. No Nex_TI, elas começam com `MD_` (ex: `MD_Usuarios`, `MD_Flashcards`).
    - *Pergunta:* "O que eu preciso salvar no banco de dados?"
2.  **Identifique os Controladores (Controle)**: São as classes que fazem o trabalho pesado e a lógica. (ex: `ControladorAutenticacao`, `GerenciadorProgresso`).
    - *Pergunta:* "Quem vai processar essa ação?"
3.  **Defina Atributos e Métodos**:
    - **Atributos (`+`)**: São as características (nome, email, nota).
    - **Métodos (`()`)**: São as ações (login, salvar, calcular).
4.  **Estabeleça Relacionamentos**:
    - **Associação (`-->`)**: Uma classe conhece a outra.
    - **Dependência (`..>`)**: Uma classe usa a outra temporariamente (ex: Controle consulta uma Entidade).
    - **Herança (`<|--`)**: Uma classe "é um tipo de" outra (ex: Aluno é um tipo de Usuário).

---

## 2. 🎬 Diagrama de Sequência: O "Como" e o "Quando"
O objetivo aqui é descrever o **processo**. Imagine que você é um diretor de cinema desenhando o roteiro de uma cena.

### Passo a Passo:
1.  **Identifique o Ator**: Quem inicia a ação? Geralmente é o `Usuario` ou `Aluno`.
2.  **Posicione os Participantes**: Coloque o Ator à esquerda e as classes que ele vai usar à direita (Controle, Entidade, Banco de Dados).
3.  **Desenhe as Linhas de Vida (Lifelines)**: São as linhas tracejadas que descem de cada participante.
4.  **Adicione as Mensagens (Setas)**:
    - **Seta Cheia (`->>`)**: Uma chamada de método (ação).
    - **Seta Tracejada (`-->>`)**: Um retorno de informação (resposta).
5.  **Use Barras de Ativação (Work Bars)**: No Astah, coloque retângulos sobre a linha de vida para mostrar que aquela classe está "trabalhando" naquele momento.
6.  **Autonumeração**: Sempre numere os passos (1, 2, 3...) para que qualquer pessoa consiga seguir o fluxo.

---
*Dica de Ouro: No Astah, mantenha os nomes exatamente iguais aos que estão nos guias que eu gerei para você. Isso garante que seu projeto seja consistente.*
