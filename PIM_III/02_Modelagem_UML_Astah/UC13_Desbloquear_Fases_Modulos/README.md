# 📘 Guia de Modelagem: Desbloquear Fases e Módulos

## 🎯 Objetivo do Caso de Uso
Progressão de conteúdo condicionada ao desempenho nas fases anteriores.

> [!TIP]
> Dica Astah: Represente o estado 'bloqueada' como um atributo booleano público (+).

## 🚀 Tutorial de Criação Passo a Passo (Astah)

### 1️⃣ Criando o Diagrama de Classe
1. No Menu Superior, vá em **Projeto** > **Árvore de Estrutura**.
2. Clique com o botão direito e selecione **Adicionar Diagrama** > **Diagrama de Classe**.
3. Arraste as classes para a área de desenho:
   - [ ] Criar **MD_Fases**.
   - [ ] Criar **MD_Alunos**.
   - [ ] Criar **Método: desbloquear()**.
4. Adicione os **Atributos** e **Métodos** clicando com o botão direito na classe.
5. Use as ferramentas de **Associação, Dependência ou Herança** para ligar as classes conforme a referência abaixo.

### 2️⃣ Criando o Diagrama de Sequência
1. Clique com o botão direito no Caso de Uso (na Árvore) e selecione **Adicionar Diagrama** > **Diagrama de Sequência**.
2. Adicione os **Participantes** (Linhas de Vida) no topo da tela.
3. Desenhe as setas de mensagem seguindo rigorosamente esta ordem:
   - [ ] 1. **GerenciadorProgresso -> MD_Alunos: obterProgressoTotal()**
   - [ ] 2. **GerenciadorProgresso -> MD_Fases: desbloquear()**
4. Lembre-se de adicionar as **Barras de Ativação** clicando sobre a linha de vida onde houver processamento.

---

## 📊 Referência Visual (Padrão PT-BR)
### Diagrama de Classe
```mermaid
classDiagram
    class MD_Fases {
        +bool bloqueada
        +desbloquear()
    }
    class MD_Alunos {
        +float progresso
    }
    MD_Fases ..> MD_Alunos : verifica
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant M as GerenciadorProgresso
    participant A as MD_Alunos
    participant F as MD_Fases
    M->>A: obterProgressoTotal()
    A-->>M: 0.85
    M->>F: desbloquear()
    F->>F: setBloqueada(false)
    F-->>M: Liberada
```

---
*Manual técnico gerado em Português para conformidade com o PIM III.*