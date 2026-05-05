# 📘 Guia de Modelagem: Consultar Agente IA

## 🎯 Objetivo do Caso de Uso
Interação instantânea com o especialista virtual para dúvidas pontuais.

> [!TIP]
> Dica Astah: Represente a 'MD_Duvidas' como um objeto persistente (Store/Entity).

## 🚀 Tutorial de Criação Passo a Passo (Astah)

### 1️⃣ Criando o Diagrama de Classe
1. No Menu Superior, vá em **Projeto** > **Árvore de Estrutura**.
2. Clique com o botão direito e selecione **Adicionar Diagrama** > **Diagrama de Classe**.
3. Arraste as classes para a área de desenho:
   - [ ] Criar **AgenteIA**.
   - [ ] Criar **MD_Duvidas**.
   - [ ] Criar **Método: responder(pergunta)**.
4. Adicione os **Atributos** e **Métodos** clicando com o botão direito na classe.
5. Use as ferramentas de **Associação, Dependência ou Herança** para ligar as classes conforme a referência abaixo.

### 2️⃣ Criando o Diagrama de Sequência
1. Clique com o botão direito no Caso de Uso (na Árvore) e selecione **Adicionar Diagrama** > **Diagrama de Sequência**.
2. Adicione os **Participantes** (Linhas de Vida) no topo da tela.
3. Desenhe as setas de mensagem seguindo rigorosamente esta ordem:
   - [ ] 1. **Aluno -> AgenteIA: perguntar()**
   - [ ] 2. **AgenteIA -> MD_Duvidas: salvar()**
   - [ ] 3. **AgenteIA -->> Aluno: resposta_formatada**
4. Lembre-se de adicionar as **Barras de Ativação** clicando sobre a linha de vida onde houver processamento.

---

## 📊 Referência Visual (Padrão PT-BR)
### Diagrama de Classe
```mermaid
classDiagram
    class AgenteIA {
        +responder(pergunta)
    }
    class MD_Duvidas {
        +string pergunta
        +string resposta
    }
    AgenteIA ..> MD_Duvidas : consulta
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant A as Aluno
    participant IA as AgenteIA
    A->>IA: enviarDuvida(texto)
    activate IA
    IA->>IA: processarLinguagemNatural()
    IA-->>A: Resposta Sugerida
    deactivate IA
```

---
*Manual técnico gerado em Português para conformidade com o PIM III.*