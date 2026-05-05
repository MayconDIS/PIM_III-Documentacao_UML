# 📘 Guia de Modelagem: Cadastrar Usuário

## 🎯 Objetivo do Caso de Uso
Registro de novos alunos com inicialização automática de perfil de gamificação.

> [!TIP]
> Dica Astah: Use a 'Generalização' (seta fechada) de MD_Alunos para MD_Usuarios para indicar herança.

## 🚀 Tutorial de Criação Passo a Passo (Astah)

### 1️⃣ Criando o Diagrama de Classe
1. No Menu Superior, vá em **Projeto** > **Árvore de Estrutura**.
2. Clique com o botão direito e selecione **Adicionar Diagrama** > **Diagrama de Classe**.
3. Arraste as classes para a área de desenho:
   - [ ] Criar **MD_Usuarios (Base)**.
   - [ ] Criar **MD_Alunos (Extensão)**.
   - [ ] Criar **Herança: MD_Alunos herda de MD_Usuarios**.
   - [ ] Criar **Atributos: pontos: int, moedas: int**.
4. Adicione os **Atributos** e **Métodos** clicando com o botão direito na classe.
5. Use as ferramentas de **Associação, Dependência ou Herança** para ligar as classes conforme a referência abaixo.

### 2️⃣ Criando o Diagrama de Sequência
1. Clique com o botão direito no Caso de Uso (na Árvore) e selecione **Adicionar Diagrama** > **Diagrama de Sequência**.
2. Adicione os **Participantes** (Linhas de Vida) no topo da tela.
3. Desenhe as setas de mensagem seguindo rigorosamente esta ordem:
   - [ ] 1. **Visitante -> ControladorAutenticacao: registrar()**
   - [ ] 2. **ControladorAutenticacao -> MD_Alunos: <<create>>**
   - [ ] 3. **MD_Alunos -> MD_Alunos: inicializarPerfil()**
4. Lembre-se de adicionar as **Barras de Ativação** clicando sobre a linha de vida onde houver processamento.

---

## 📊 Referência Visual (Padrão PT-BR)
### Diagrama de Classe
```mermaid
classDiagram
    MD_Usuarios <|-- MD_Alunos
    class MD_Usuarios {
        +string nome
        +string email
    }
    class MD_Alunos {
        +int pontos
        +int moedas
    }
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant V as Visitante
    participant C as ControladorAutenticacao
    participant A as MD_Alunos
    V->>C: registrar(dados)
    activate C
    C-->>A: <<create>>
    activate A
    A->>A: inicializarPerfil()
    deactivate A
    C-->>V: Cadastro Confirmado
    deactivate C
```

---
*Manual técnico gerado em Português para conformidade com o PIM III.*