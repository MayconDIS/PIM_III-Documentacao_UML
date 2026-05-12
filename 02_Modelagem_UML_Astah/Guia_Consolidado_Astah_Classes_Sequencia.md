# 🚀 Guia Consolidado: Fluxos (Normal e Alternativo) para Astah

Este guia detalha como representar tanto o **Fluxo Normal** quanto o **Fluxo Alternativo** nos diagramas de Classe e Sequência dentro do Astah UML.

---

## 🛠️ Detalhamento por Caso de Uso

### UC01: Realizar Login
*   **Diagrama de Classe:** `Usuario` (Entidade), `ServicoAutenticacao` (Controle).
*   **Diagrama de Sequência:**
    *   **Fluxo Normal:** Usuario -> `login()` -> :ServicoAutenticacao -> `validar()` -> Sucesso (Redirecionar).
    *   **Fluxo Alternativo (Erro):** Usuario -> `login()` -> :ServicoAutenticacao -> `validar()` -> Retorno: "Credenciais Inválidas".

### UC02: Cadastrar Usuário
*   **Diagrama de Classe:** `Usuario` (Base), `Aluno` (Entidade).
*   **Diagrama de Sequência:**
    *   **Fluxo Normal:** Visitante -> `registrar()` -> :ServicoAutenticacao -> `<<create>>` Aluno -> `inicializarPerfil()`.
    *   **Fluxo Alternativo (Duplicado):** Visitante -> `registrar()` -> :ServicoAutenticacao -> Verifica DB -> Retorno: "E-mail já cadastrado".

### UC03: Realizar Teste de Nivelamento
*   **Diagrama de Classe:** `Aluno`, `Simulado` (Entidade).
*   **Diagrama de Sequência:**
    *   **Fluxo Normal:** Aluno -> `iniciarTeste()` -> :Simulado -> Devolve Questões -> Aluno -> `enviarRespostas()` -> `definirFaseInicial(nota)`.
    *   **Fluxo Alternativo (Pular):** Aluno -> `pularTeste()` -> :Simulado -> Retorno: Atribuir "Módulo Básico" (Nível 1) por padrão.

### UC04: Gerenciar Perfis e Acessos
*   **Diagrama de Classe:** `Administrador`, `Usuario`, `GerenciadorAcesso` (Controle).
*   **Diagrama de Sequência:**
    *   **Fluxo Normal:** Admin -> `alterarPapel(id, novoPapel)` -> :GerenciadorAcesso -> `setPapel()` no Usuario.
    *   **Fluxo Alternativo (Auto-Revogação):** Admin -> `alterarPapel(self, Aluno)` -> :GerenciadorAcesso -> Bloqueio -> Erro: "Não é possível remover o último admin".

### UC05: Gerenciar Conteúdo e Cartas
*   **Diagrama de Classe:** `Modulo`, `Flashcard_SM2` (Entidade) - Relacionamento de Composição.
*   **Diagrama de Sequência:**
    *   **Fluxo Normal:** Tutor -> `novoModulo()` -> :Sistema -> `<<create>>` Modulo -> `adicionarCarta()`.
    *   **Fluxo Alternativo (Exclusão com Dependência):** Tutor -> `excluirModulo()` -> :Sistema -> Verifica uso por Alunos -> Sugestão: "Arquivar ao invés de excluir".

### UC06: Acompanhar Desempenho
*   **Diagrama de Classe:** `Tutor`, `Aluno`, `PainelVisual` (Fronteira).
*   **Diagrama de Sequência:**
    *   **Fluxo Normal:** Tutor -> `visualizar(id)` -> :PainelVisual -> `obterMetricas()` -> :Aluno -> Renderizar Gráficos.
    *   **Fluxo Alternativo (Sem Dados):** Tutor -> `visualizar(id)` -> :PainelVisual -> `obterMetricas()` -> Retorno: "Dados insuficientes para gerar estatísticas".

### UC07: Escalar Dúvida para Tutor
*   **Diagrama de Classe:** `AgenteIA` (Controle), `Tutor` (Entidade), `Duvida`.
*   **Diagrama de Sequência:**
    *   **Fluxo Normal:** Aluno -> Enviar Dúvida -> :AgenteIA -> `escalar()` -> :Tutor -> Notificação enviada.
    *   **Fluxo Alternativo (SLA Estourado):** :Sistema -> Verifica tempo -> :Duvida -> `setPrioridadeAlta()` -> Disparar E-mail para Coordenação.

### UC08: Consultar Agente IA
*   **Diagrama de Classe:** `AgenteIA` (Controle), `Duvida`.
*   **Diagrama de Sequência:**
    *   **Fluxo Normal:** Aluno -> `enviarDuvida()` -> :AgenteIA -> `processarNLP()` -> Retorno: Explicação Pedagógica.
    *   **Fluxo Alternativo (Fora de Contexto):** Aluno -> `enviarDuvida()` -> :AgenteIA -> Falha na interpretação -> Sugestão: "Reformule a pergunta ou Escalar para Tutor".

### UC09: Estudar Flashcards (SM-2)
*   **Diagrama de Classe:** `MotorSM2` (Controle), `Flashcard_SM2`.
*   **Diagrama de Sequência:**
    *   **Fluxo Normal:** Aluno -> `informarDificuldade()` -> :MotorSM2 -> `recalcularSM2()` -> `setProximaRevisao()` no Flashcard.
    *   **Fluxo Alternativo (Concluído):** Aluno -> Abre Deck -> :Sistema -> Verifica agenda -> Mensagem: "Metas diárias cumpridas! Volte amanhã".

### UC10: Criar Flashcards
*   **Diagrama de Classe:** `Aluno`, `Flashcard_SM2`, `Editor` (Fronteira).
*   **Diagrama de Sequência:**
    *   **Fluxo Normal:** Aluno -> `salvar(p, r)` -> :Editor -> `<<create>>` Flashcard -> Persistência.
    *   **Fluxo Alternativo (Verso em Branco):** Aluno -> `salvar(p, "")` -> :Editor -> Validação falha -> Botão desabilitado + Alerta visual.

### UC11: Realizar Simulado ENADE
*   **Diagrama de Classe:** `Simulado`, `Questao`, `Temporizador`.
*   **Diagrama de Sequência:**
    *   **Fluxo Normal:** Aluno -> `iniciarTeste()` -> :Simulado -> `iniciar()` Temporizador -> Responder -> Corrigir.
    *   **Fluxo Alternativo (Queda de Conexão):** :Sistema -> Detectar Offline -> `salvarProgressoLocal()` -> Ao reconectar: `retomarDeOndeParou()`.

### UC12: Atribuir XP e Moedas
*   **Diagrama de Classe:** `SistemaGamificacao` (Controle), `Aluno`.
*   **Diagrama de Sequência:**
    *   **Fluxo Normal:** :Sistema -> `finalizarAtividade()` -> :SistemaGamificacao -> `creditarXP()` e `adicionarMoedas()` no Aluno.
    *   **Fluxo Alternativo (Burla/Spam):** :Sistema -> Detectar velocidade anormal -> :SistemaGamificacao -> Reduzir multiplicador de XP drasticamente.

### UC13: Desbloquear Fases e Módulos
*   **Diagrama de Classe:** `Modulo`, `Aluno`, `Loja` (Fronteira).
*   **Diagrama de Sequência:**
    *   **Fluxo Normal:** Aluno -> `comprar()` -> :Loja -> Verifica Moedas no Aluno -> `desbloquear()` Modulo.
    *   **Fluxo Alternativo (Saldo Insuficiente):** Aluno -> `comprar()` -> :Loja -> Verifica Moedas -> Bloqueio -> Mensagem: "Faltam X moedas".

### UC14: Visualizar Painel de Progresso
*   **Diagrama de Classe:** `PainelVisual` (Fronteira), `Aluno`.
*   **Diagrama de Sequência:**
    *   **Fluxo Normal:** Aluno -> `abrirHome()` -> :PainelVisual -> `obterProgresso()` -> Aluno -> Renderizar Heatmap e Nível.
    *   **Fluxo Alternativo (Primeiro Acesso):** Aluno -> `abrirHome()` -> :PainelVisual -> Dados vazios -> Exibir CTA: "Faça seu primeiro estudo!".

### UC15: Ajustar Acessibilidade
*   **Diagrama de Classe:** `Acessibilidade` (Entidade), `PainelConfiguracao` (Fronteira).
*   **Diagrama de Sequência:**
    *   **Fluxo Normal:** Usuario -> `ativarAltoContraste()` -> :PainelConfiguracao -> `salvar()` na Acessibilidade -> Injetar CSS.
    *   **Fluxo Alternativo (Conflito de Layout):** Usuario -> `restaurarPadroes()` -> :PainelConfiguracao -> Limpar configurações -> Retornar CSS original.

---

## 💡 Como modelar os fluxos alternativos no Astah?

1.  **Diagrama de Sequência:** Use o fragmento combinado **Combined Fragment** com o operador **Alt** (Alternative). No Astah, você desenha um quadro ao redor das mensagens e define as condições (ex: `[sucesso]` e `[erro]`).
2.  **Diagrama de Classe:** As classes permanecem as mesmas para ambos os fluxos, mas você deve garantir que os **Métodos** necessários para os fluxos alternativos (ex: `restaurarPadroes()`, `salvarProgressoLocal()`) estejam declarados na classe correta.

---
*Este manual foi atualizado para cobrir todos os cenários de modelagem do PIM III.*
