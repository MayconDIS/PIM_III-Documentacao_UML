# Registro Scrum: Reunião 10 (24/05)

**Ritual**: Sprint Review & Retrospective (Refatoração SOLID no Backend C#)  
**Data**: 24 de Maio de 2026 (Domingo)  
**Facilitador (Scrum Master)**: Gabriel Alves Moreira  
**Participantes**: Gabriel, Maciel, Maycon, Miguel, Rafael  

---

### 1. O que foi feito (Progresso)

- **Refatoração SOLID do Backend**: Para cumprir as diretrizes técnicas do projeto e garantir uma arquitetura limpa e de fácil manutenção, refatoramos o backend C# (.NET 10):
  - **SRP e DIP**: Isolamos o algoritmo matemático de repetição espaçada SM-2 em um serviço dedicado (`Sm2Engine.cs`) que implementa a interface `ISm2Engine` em `backend/Services/`. Qualquer chamada de cálculo foi desacoplada dos controladores de rotas.
  - **Mapeamento Limpo (SRP)**: Retiramos todas as declarações e mapeamentos de Minimal APIs do arquivo principal `Program.cs` e as organizamos em extensões modulares (`EndpointExtensions.cs`), evitando inflar o arquivo de entrada do sistema.
- **Validação de Compilação**: A API compila com sucesso e as rotas HTTP de `/api/status`, `/api/usuarios/{username}` e `/api/fases/{codigo}/flashcards` respondem perfeitamente.

### 2. O que será feito (Próximos Passos)

- **Sincronização Final**: Executar a consolidação do ecossistema sincronizando os logs e atas do Scrum em todos os repositórios complementares.
- **Validação Final da Banca**: Testar a execução integrada do frontend com o backend compilado e banco SQL local.

### 3. Impedimentos e Resoluções

- **Impedimento**: Havia a preocupação de que o desacoplamento do cálculo matemático do SM-2 introduzisse bugs de arredondamento de dias (como float vs double) nos objetos de progresso.
- **Resolução**: Mantivemos a precisão idêntica ao modelo original, criando testes de unidade focados nos fatores de facilidade (`1.3` a `2.5`) e no agendamento de datas.

### 4. Backlog da Sprint (Status)

- [x] Isolar a lógica matemática do algoritmo SM-2 (SRP e DIP) em backend/Services/
- [x] Extrair o mapeamento de Minimal APIs do Program.cs para EndpointExtensions.cs
- [x] Limpar e reestruturar o arquivo de entrada Program.cs
- [x] Validar a compilação completa da API REST C#
- [x] Testar integração end-to-end com o frontend na porta 5001
