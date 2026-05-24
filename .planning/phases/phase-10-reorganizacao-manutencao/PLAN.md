# Plano da Fase 10: Reorganização e Manutenção Geral do Repositório

## 🎯 Objetivos
1. Corrigir os caminhos de arquivos "hardcoded" nos scripts de automação Python em `04_Scripts/`.
2. Sincronizar e alinhar a nomenclatura de classes no script de automação com o modelo de classes definitivo (substituir prefixos `MD_` por classes reais).
3. Eliminar backups de imagens exportadas em `02_Modelagem_UML/`.
4. Mover a pasta legada de código C# `03_Codigo_Gerado/` para `05_Legacy/`.
5. Eliminar arquivos locais duplicados de casos de uso na pasta de exportações gerais `03_Artefatos_Gerados/`.
6. Regenerar e atualizar todos os manuais de casos de uso e o Dashboard centralizado usando o script atualizado.
7. Atualizar a documentação principal (`README.md`, `.planning/PROJECT.md` e `.planning/STATE.md`).
8. Limpar e estruturar a pasta `.planning/phases/`.

## 🛠️ Passos de Execução
- [x] Ajustar scripts em `04_Scripts/generate_docs_step_by_step.py` e `04_Scripts/update_all.py` para usar caminhos relativos.
- [x] Substituir o dicionário de dados no gerador de manuais pelas novas classes e propriedades.
- [x] Deletar arquivos `.png.bak` de backup em `02_Modelagem_UML/`.
- [x] Mover `03_Codigo_Gerado/` para `05_Legacy/Codigo_Gerado_Astah_Legado/`.
- [x] Remover arquivos locais de imagens de UCs em `03_Artefatos_Gerados/`.
- [x] Executar `generate_docs_step_by_step.py` e `update_all.py` para atualizar os manuais e Dashboard.
- [x] Limpar a pasta `.planning/phases/` deixando apenas as fases relevantes documentadas.
- [x] Atualizar referências no `README.md` principal.
