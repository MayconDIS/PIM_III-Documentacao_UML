# 📘 Guia de Modelagem: Gerenciar Perfis e Acessos

## 🎯 Objetivo do Caso de Uso
Administração de papéis (Admin, Tutor, Aluno) e permissões de sistema.

> [!TIP]
> Dica Astah: Use 'Notas' para descrever os tipos de 'papéis' (roles) suportados no sistema.

## 🚀 Tutorial de Criação Passo a Passo (Astah)

### 1️⃣ Criando o Diagrama de Classe
1. No Menu Superior, vá em **Projeto** > **Árvore de Estrutura**.
2. Clique com o botão direito e selecione **Adicionar Diagrama** > **Diagrama de Classe**.
3. Arraste as classes para a área de desenho:
   - [ ] Criar **MD_Admin**.
   - [ ] Criar **MD_Usuarios**.
   - [ ] Criar **GerenciadorAcesso (Controle)**.
   - [ ] Criar **Atributo: papel: texto**.
4. Adicione os **Atributos** e **Métodos** clicando com o botão direito na classe.
5. Use as ferramentas de **Associação, Dependência ou Herança** para ligar as classes conforme a referência abaixo.

### 2️⃣ Criando o Diagrama de Sequência
1. Clique com o botão direito no Caso de Uso (na Árvore) e selecione **Adicionar Diagrama** > **Diagrama de Sequência**.
2. Adicione os **Participantes** (Linhas de Vida) no topo da tela.
3. Desenhe as setas de mensagem seguindo rigorosamente esta ordem:
   - [ ] 1. **Admin -> GerenciadorAcesso: alterarPapel()**
   - [ ] 2. **GerenciadorAcesso -> MD_Usuarios: setPapel()**
   - [ ] 3. **Retorno: Confirmação**
4. Lembre-se de adicionar as **Barras de Ativação** clicando sobre a linha de vida onde houver processamento.

---

## 📊 Referência Visual (Padrão PT-BR)
### Diagrama de Classe
```mermaid
classDiagram
    class MD_Admin {
        +gerenciarAcesso()
    }
    class MD_Usuarios {
        +string papel
    }
    MD_Admin --> MD_Usuarios : administra
```

### Diagrama de Sequência
```mermaid
sequenceDiagram
    autonumber
    participant A as Admin
    participant M as GerenciadorAcesso
    participant U as MD_Usuarios
    A->>M: alterarPapel(usuario_id, papel)
    activate M
    M->>U: setPapel(papel)
    U-->>M: ok
    M-->>A: Alteração Concluída
    deactivate M
```

---
*Manual técnico gerado em Português para conformidade com o PIM III.*