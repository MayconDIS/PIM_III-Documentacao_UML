# 📘 Guia de Modelagem: Teste de Nivelamento

## 🎯 Objetivo do Caso de Uso
Avaliação diagnóstica para posicionamento do aluno no mapa de conhecimento.

> [!TIP]
> Dica Astah: No diagrama de classe, use 'Agregação' para mostrar que um Simulado contém questões.

## 🚀 Tutorial de Criação Passo a Passo (Astah)

### 1️⃣ Criando o Diagrama de Classe
1. No Menu Superior, vá em **Projeto** > **Árvore de Estrutura**.
2. Clique com o botão direito e selecione **Adicionar Diagrama** > **Diagrama de Classe**.
3. Arraste as classes para a área de desenho:
   - [ ] Criar **MD_Alunos**.
   - [ ] Criar **MD_Simulado**.
   - [ ] Criar **Método: definirFaseInicial(nota)**.
   - [ ] Criar **Atributo: complexidade: texto**.
4. Adicione os **Atributos** e **Métodos** clicando com o botão direito na classe.
5. Use as ferramentas de **Associação, Dependência ou Herança** para ligar as classes conforme a referência abaixo.

### 2️⃣ Criando o Diagrama de Sequência
1. Clique com o botão direito no Caso de Uso (na Árvore) e selecione **Adicionar Diagrama** > **Diagrama de Sequência**.
2. Adicione os **Participantes** (Linhas de Vida) no topo da tela.
3. Desenhe as setas de mensagem seguindo rigorosamente esta ordem:
   - [ ] 1. **Aluno -> MD_Simulado: iniciarTeste()**
   - [ ] 2. **MD_Simulado -->> Aluno: listaQuestoes[]**
   - [ ] 3. **Aluno -> MD_Simulado: enviarRespostas()**
   - [ ] 4. **Aluno -> Aluno: definirFaseInicial(nota)**
4. Lembre-se de adicionar as **Barras de Ativação** clicando sobre a linha de vida onde houver processamento.

---

## 📊 Referência Visual (Padrão PT-BR)
### Diagrama de Classe
```mermaid
classDiagram
    class MD_Alunos {
        +definirFaseInicial(nota)
    }
    class MD_Simulado {
        +float nota
        +iniciarTeste()
    }
    MD_Alunos --> MD_Simulado : realiza
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant A as Aluno
    participant S as MD_Simulado
    A->>S: iniciarTeste()
    activate S
    S-->>A: Lista de Questões
    A->>S: enviarRespostas()
    S-->>A: notaFinal
    deactivate S
    A->>A: definirFaseInicial(nota)
```

---
*Manual técnico gerado em Português para conformidade com o PIM III.*