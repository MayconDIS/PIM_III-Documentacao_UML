# 📘 Guia de Modelagem: Acompanhar Desempenho

## 🎯 Objetivo do Caso de Uso
Visualização de métricas de progresso e engajamento dos alunos.

> [!TIP]
> Dica Astah: No diagrama de sequência, represente o 'Painel' como uma classe de 'Fronteira' (Boundary).

## 🚀 Tutorial de Criação Passo a Passo (Astah)

### 1️⃣ Criando o Diagrama de Classe
1. No Menu Superior, vá em **Projeto** > **Árvore de Estrutura**.
2. Clique com o botão direito e selecione **Adicionar Diagrama** > **Diagrama de Classe**.
3. Arraste as classes para a área de desenho:
   - [ ] Criar **MD_Tutor**.
   - [ ] Criar **MD_Alunos**.
   - [ ] Criar **PainelVisual**.
   - [ ] Criar **Atributo: progresso: decimal**.
4. Adicione os **Atributos** e **Métodos** clicando com o botão direito na classe.
5. Use as ferramentas de **Associação, Dependência ou Herança** para ligar as classes conforme a referência abaixo.

### 2️⃣ Criando o Diagrama de Sequência
1. Clique com o botão direito no Caso de Uso (na Árvore) e selecione **Adicionar Diagrama** > **Diagrama de Sequência**.
2. Adicione os **Participantes** (Linhas de Vida) no topo da tela.
3. Desenhe as setas de mensagem seguindo rigorosamente esta ordem:
   - [ ] 1. **Tutor -> PainelVisual: requisitarDados(aluno)**
   - [ ] 2. **PainelVisual -> MD_Alunos: obterMetricas()**
   - [ ] 3. **PainelVisual -->> Tutor: Renderiza Gráficos**
4. Lembre-se de adicionar as **Barras de Ativação** clicando sobre a linha de vida onde houver processamento.

---

## 📊 Referência Visual (Padrão PT-BR)
### Diagrama de Classe
```mermaid
classDiagram
    class MD_Tutor {
        +acompanharDesempenho()
    }
    class MD_Alunos {
        +float progresso
    }
    MD_Tutor ..> MD_Alunos : visualiza
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant T as Tutor
    participant D as PainelVisual
    participant A as MD_Alunos
    T->>D: visualizar(aluno_id)
    activate D
    D->>A: obterMetricas()
    A-->>D: dados_progresso
    D-->>T: Relatório Visual
    deactivate D
```

---
*Manual técnico gerado em Português para conformidade com o PIM III.*