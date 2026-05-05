# 📘 Guia de Modelagem: Criar Flashcards

## 🎯 Objetivo do Caso de Uso
Funcionalidade que permite ao aluno personalizar seu próprio deck de estudos.

> [!TIP]
> Dica Astah: Utilize a associação '1..*' para indicar que um aluno pode criar múltiplas cartas.

## 🚀 Tutorial de Criação Passo a Passo (Astah)

### 1️⃣ Criando o Diagrama de Classe
1. No Menu Superior, vá em **Projeto** > **Árvore de Estrutura**.
2. Clique com o botão direito e selecione **Adicionar Diagrama** > **Diagrama de Classe**.
3. Arraste as classes para a área de desenho:
   - [ ] Criar **MD_Alunos**.
   - [ ] Criar **MD_Flashcards**.
   - [ ] Criar **Método: criarCarta()**.
4. Adicione os **Atributos** e **Métodos** clicando com o botão direito na classe.
5. Use as ferramentas de **Associação, Dependência ou Herança** para ligar as classes conforme a referência abaixo.

### 2️⃣ Criando o Diagrama de Sequência
1. Clique com o botão direito no Caso de Uso (na Árvore) e selecione **Adicionar Diagrama** > **Diagrama de Sequência**.
2. Adicione os **Participantes** (Linhas de Vida) no topo da tela.
3. Desenhe as setas de mensagem seguindo rigorosamente esta ordem:
   - [ ] 1. **Aluno -> MD_Alunos: criarCarta()**
   - [ ] 2. **MD_Alunos -> MD_Flashcards: <<create>>**
4. Lembre-se de adicionar as **Barras de Ativação** clicando sobre a linha de vida onde houver processamento.

---

## 📊 Referência Visual (Padrão PT-BR)
### Diagrama de Classe
```mermaid
classDiagram
    class MD_Alunos {
        +criarCarta()
    }
    class MD_Flashcards {
        +string pergunta
        +string resposta
    }
    MD_Alunos "1" --> "*" MD_Flashcards : cria
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant A as Aluno
    participant E as Editor
    participant F as MD_Flashcards
    A->>E: entradaDados(p, r)
    E->>F: <<create>>(p, r, usuario_id)
    F-->>A: Carta Adicionada ao Deck
```

---
*Manual técnico gerado em Português para conformidade com o PIM III.*