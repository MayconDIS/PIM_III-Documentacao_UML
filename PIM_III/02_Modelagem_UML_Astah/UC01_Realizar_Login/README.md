# 📘 Guia de Modelagem: Realizar Login

## 🎯 Objetivo do Caso de Uso
Acesso seguro do usuário ao sistema através de validação de credenciais.

> [!TIP]
> Dica Astah: No Diagrama de Sequência, utilize 'Barras de Ativação' para mostrar o tempo de vida do processamento no Controlador.

## 🚀 Tutorial de Criação Passo a Passo (Astah)

### 1️⃣ Criando o Diagrama de Classe
1. No Menu Superior, vá em **Projeto** > **Árvore de Estrutura**.
2. Clique com o botão direito e selecione **Adicionar Diagrama** > **Diagrama de Classe**.
3. Arraste as classes para a área de desenho:
   - [ ] Criar **Classe MD_Usuarios (Entidade)**.
   - [ ] Criar **Classe ControladorAutenticacao (Controle)**.
   - [ ] Criar **Atributos: email: texto, senha: hash**.
   - [ ] Criar **Método: autenticar()**.
4. Adicione os **Atributos** e **Métodos** clicando com o botão direito na classe.
5. Use as ferramentas de **Associação, Dependência ou Herança** para ligar as classes conforme a referência abaixo.

### 2️⃣ Criando o Diagrama de Sequência
1. Clique com o botão direito no Caso de Uso (na Árvore) e selecione **Adicionar Diagrama** > **Diagrama de Sequência**.
2. Adicione os **Participantes** (Linhas de Vida) no topo da tela.
3. Desenhe as setas de mensagem seguindo rigorosamente esta ordem:
   - [ ] 1. **Usuario -> ControladorAutenticacao: login()**
   - [ ] 2. **ControladorAutenticacao -> ControladorAutenticacao: validarCredenciais()**
   - [ ] 3. **Retorno: Token de Acesso ou Erro**
4. Lembre-se de adicionar as **Barras de Ativação** clicando sobre a linha de vida onde houver processamento.

---

## 📊 Referência Visual (Padrão PT-BR)
### Diagrama de Classe
```mermaid
classDiagram
    class MD_Usuarios {
        +string email
        +string senha
    }
    class ControladorAutenticacao {
        +autenticar(email, senha)
    }
    ControladorAutenticacao ..> MD_Usuarios : consulta
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant U as Usuario
    participant C as ControladorAutenticacao
    U->>C: login(email, senha)
    activate C
    C->>C: validarCredenciais()
    C-->>U: Retorno (Sucesso/Erro)
    deactivate C
```

---
*Manual técnico gerado em Português para conformidade com o PIM III.*