# 📘 Guia de Modelagem: Atribuir XP e Moedas

## 🎯 Objetivo do Caso de Uso
Motor de recompensas automático baseado na conclusão de atividades.

> [!TIP]
> Dica Astah: No diagrama de classe, use uma 'Dependência' (seta tracejada) entre Sistema e Gamificação.

## 🚀 Tutorial de Criação Passo a Passo (Astah)

### 1️⃣ Criando o Diagrama de Classe
1. No Menu Superior, vá em **Projeto** > **Árvore de Estrutura**.
2. Clique com o botão direito e selecione **Adicionar Diagrama** > **Diagrama de Classe**.
3. Arraste as classes para a área de desenho:
   - [ ] Criar **MD_Gamificacao**.
   - [ ] Criar **MD_Alunos**.
   - [ ] Criar **Método: creditarXP(valor)**.
4. Adicione os **Atributos** e **Métodos** clicando com o botão direito na classe.
5. Use as ferramentas de **Associação, Dependência ou Herança** para ligar as classes conforme a referência abaixo.

### 2️⃣ Criando o Diagrama de Sequência
1. Clique com o botão direito no Caso de Uso (na Árvore) e selecione **Adicionar Diagrama** > **Diagrama de Sequência**.
2. Adicione os **Participantes** (Linhas de Vida) no topo da tela.
3. Desenhe as setas de mensagem seguindo rigorosamente esta ordem:
   - [ ] 1. **Sistema -> MD_Gamificacao: calcularBonus()**
   - [ ] 2. **MD_Gamificacao -> MD_Alunos: creditarXP()**
4. Lembre-se de adicionar as **Barras de Ativação** clicando sobre a linha de vida onde houver processamento.

---

## 📊 Referência Visual (Padrão PT-BR)
### Diagrama de Classe
```mermaid
classDiagram
    class MD_Gamificacao {
        +calcularBonus()
        +creditarXP(id, valor)
    }
    class MD_Alunos {
        +int pontos
        +int moedas
    }
    MD_Gamificacao ..> MD_Alunos : credita
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant S as Sistema
    participant G as MD_Gamificacao
    participant A as MD_Alunos
    S->>G: notificarConclusao()
    activate G
    G->>G: calcularBonus()
    G->>A: creditarXP(id, 100)
    G-->>S: Atualizado
    deactivate G
```

---
*Manual técnico gerado em Português para conformidade com o PIM III.*