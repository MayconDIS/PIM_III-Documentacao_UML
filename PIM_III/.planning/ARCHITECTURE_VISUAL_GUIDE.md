# 🎨 Guia de Arquitetura Visual: Nex_TI UML (v1.0)

Este documento define os padrões técnicos e estéticos para toda a modelagem UML do ecossistema Nex_TI, garantindo consistência, profissionalismo e alta legibilidade.

## 🏁 1. Design System: Premium Clean Contrast

O projeto utiliza uma paleta de **Alto Contraste** focada em clareza técnica.

| Propriedade | Padrão | Justificativa |
| :--- | :--- | :--- |
| **Paleta** | Monochrome (Preto, Branco, Tons de Cinza) | Evita distrações e facilita a impressão. |
| **Tipografia** | Arial / Roboto / Sans-Serif | Facilita a leitura em telas de baixa resolução. |
| **Linhas** | Orthogonal (Ângulos retos) | Organização visual e limpeza. |
| **Sombreado** | Desativado | Reduz o ruído visual. |

---

## 📐 2. Padrões de Notação PlantUML

Todos os novos arquivos `.puml` devem iniciar com o seguinte bloco de configuração:

```puml
@startuml
' --- Configurações Premium ---
skinparam monochrome true
skinparam shadowing false
skinparam classAttributeIconSize 0
skinparam linetype ortho
skinparam nodesep 50
skinparam ranksep 50

' --- Estilos de Fonte ---
skinparam defaultFontName Arial
skinparam defaultFontSize 12
@enduml
```

### Regras de Estereótipos
- `<<Entidade>>`: Classes de domínio (dados persistentes).
- `<<Controle>>`: Classes de lógica de negócio e serviços.
- `<<Fronteira>>`: Interfaces e pontos de interação externa.

---

## 📁 3. Estrutura de Artefatos

Os diagramas devem ser organizados seguindo a convenção de nomenclatura rigorosa:

- **PUML:** `.agent/skills/uml-architect/artifacts/UCXX_Tipo.puml`
- **PNG:** `.agent/skills/uml-architect/artifacts/UCXX_Tipo.png`

*Exemplo: `UC01_Classe.puml`*

---

## 📝 4. Checklist de Qualidade Visual

Antes de considerar um diagrama concluído, verifique:
- [ ] As linhas de associação não se cruzam desnecessariamente.
- [ ] Os nomes das classes estão em **PascalCase**.
- [ ] Atributos e métodos possuem modificadores de acesso (`+`, `-`, `#`).
- [ ] O diagrama cabe em uma página A4 sem perda de nitidez.

---
*Este guia é a autoridade visual do projeto Nex_TI UML.*
