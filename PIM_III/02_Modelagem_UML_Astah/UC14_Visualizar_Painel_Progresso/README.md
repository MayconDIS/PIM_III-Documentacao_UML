# 📘 Guia de Modelagem: Visualizar Painel de Progresso

## 🎯 Objetivo do Caso de Uso
Hub central onde o aluno acompanha sua jornada e conquistas.

> [!TIP]
> Dica Astah: No diagrama de classe, mostre que o Painel lê dados de Aluno.

## 🚀 Tutorial de Criação Passo a Passo (Astah)

### 1️⃣ Criando o Diagrama de Classe
1. No Menu Superior, vá em **Projeto** > **Árvore de Estrutura**.
2. Clique com o botão direito e selecione **Adicionar Diagrama** > **Diagrama de Classe**.
3. Arraste as classes para a área de desenho:
   - [ ] Criar **PainelVisual**.
   - [ ] Criar **MD_Alunos**.
   - [ ] Criar **Método: renderizarDados()**.
4. Adicione os **Atributos** e **Métodos** clicando com o botão direito na classe.
5. Use as ferramentas de **Associação, Dependência ou Herança** para ligar as classes conforme a referência abaixo.

### 2️⃣ Criando o Diagrama de Sequência
1. Clique com o botão direito no Caso de Uso (na Árvore) e selecione **Adicionar Diagrama** > **Diagrama de Sequência**.
2. Adicione os **Participantes** (Linhas de Vida) no topo da tela.
3. Desenhe as setas de mensagem seguindo rigorosamente esta ordem:
   - [ ] 1. **Aluno -> PainelVisual: renderizarDados()**
   - [ ] 2. **PainelVisual -> MD_Alunos: obterProgressoTotal()**
4. Lembre-se de adicionar as **Barras de Ativação** clicando sobre a linha de vida onde houver processamento.

---

## 📊 Referência Visual (Padrão PT-BR)
### Diagrama de Classe
```mermaid
classDiagram
    class PainelVisual {
        +renderizarDados()
    }
    class MD_Alunos {
        +obterProgressoTotal()
    }
    PainelVisual ..> MD_Alunos : lê
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant Al as Aluno
    participant D as PainelVisual
    Al->>D: abrirInicio()
    activate D
    D->>D: renderizarDados()
    D-->>Al: Visualização Completa
    deactivate D
```

---
*Manual técnico gerado em Português para conformidade com o PIM III.*