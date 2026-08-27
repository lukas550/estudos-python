# estudos-python

Repositório dedicado à minha jornada de aprendizado em Python — do zero à Engenharia de IA.

---

## Sobre mim

Sou Lukas, desenvolvedor em formação. Este repositório é o meu diário de estudos público: aqui documento cada etapa do meu aprendizado em Python, desde os fundamentos até projetos mais complexos.

O objetivo é evoluir de forma consistente e transparente — mostrando não só o código final, mas toda a progressão até chegar lá. Cada tópico concluído representa conceitos aplicados em código real, não apenas teoria lida.

---

## Objetivos de Aprendizado

Acompanhe minha trilha de estudos. Os tópicos marcados já foram concluídos:

### Controle de Versão
- [x] Git e GitHub — commits, branches, push/pull, repositórios remotos, README, licença e .gitignore

### Fundamentos de Python
- [x] Variáveis, tipos de dados e operadores
- [x] Estruturas condicionais e de repetição
- [x] Funções e escopo
- [x] Listas, tuplas, dicionários e conjuntos

### Tratamento de Erros
- [x] `try`, `except`, `finally`
- [x] Tipos de exceções e hierarquia de erros
- [x] Criação de exceções customizadas

### Manipulação de Arquivos
- [x] Leitura e escrita de arquivos `.txt`
- [x] Formato JSON — estrutura, tipos de dados e modelagem
- [ ] Biblioteca `json` do Python
- [ ] Manipulação de arquivos `.json`

### Módulos e Bibliotecas
- [x] Importação de módulos e uso da biblioteca padrão
- [x] Criação de módulos próprios
- [ ] Gerenciadores de pacotes (`pip`) e ambientes virtuais (`venv`)
- [ ] Bibliotecas de terceiros

### Orientação a Objetos (POO)
- [ ] Classes e objetos
- [ ] Herança e polimorfismo
- [ ] Encapsulamento e abstração
- [ ] Métodos especiais (dunder methods)

### Boas Práticas
- [ ] PEP 8 — guia de estilo Python
- [ ] Docstrings e documentação de código
- [ ] Organização de projetos e nomenclatura

---

## Próximas etapas — AI Engineering

Com a base de Python concluída, o foco passa a ser construir sistemas que utilizam modelos de IA:

### Python Avançado + Fundamentos de Sistemas
- [ ] Decorators, context managers, generators
- [ ] Type hints e dataclasses
- [ ] Concorrência com `asyncio` e `async/await`
- [ ] Consumo de APIs REST (`requests`, `httpx`)
- [ ] Variáveis de ambiente e segurança de credenciais (`python-dotenv`)

### LLMs na Prática
- [ ] APIs de LLMs — Anthropic (Claude) e OpenAI
- [ ] Prompt engineering — system prompts, few-shot, chain-of-thought
- [ ] Function calling / tool use
- [ ] Structured outputs
- [ ] Streaming de respostas
- [ ] Gerenciamento de contexto e histórico de conversa

### RAG (Retrieval-Augmented Generation)
- [ ] Embeddings — conceito e funcionamento
- [ ] Bancos vetoriais — Chroma (local) e Pinecone (cloud)
- [ ] Pipeline RAG completo: chunking → embedding → retrieval → geração

### Agentes
- [ ] Conceito de agente: raciocínio + ferramentas + memória
- [ ] Construção de agentes com tool use nativo
- [ ] Memória de curto e longo prazo
- [ ] Multi-agentes

### Deploy e Produção
- [ ] FastAPI — criar APIs para expor sistemas de IA
- [ ] Docker — containerizar aplicações
- [ ] Deploy em cloud (Railway, Render ou AWS)
- [ ] Observabilidade — logs e monitoramento de custos de LLM

---

## Mini Projetos e Exercícios

| Exercício | Tipo | Descrição | Tópicos abordados | Status |
|-----------|------|-----------|-------------------|--------|
| [Agenda de Contatos](exercicios-de-manipulacao-de-arquivos/ex001/ex001.py) | Mini-projeto | Agenda simples via terminal com leitura, escrita e remoção de contatos em arquivo `.txt` | Manipulação de arquivos, funções, loops, tratamento de erros | Concluído |
| [Exercícios de JSON](exercicios-de-manipulacao-de-arquivos/ex002/) | Exercício | Modelagem de dados em formato JSON — contatos, produtos, pedidos, configurações e boas práticas de estrutura | Formato JSON, tipos de dados, modelagem de arrays e objetos | Concluído |

---

## Projetos publicados

Além dos exercícios deste repositório, desenvolvi projetos separados durante os estudos, cada um aplicando os conceitos aprendidos até o momento:

- [jogo-de-adivinhacao](https://github.com/lukas550/jogo-de-adivinhacao) — Jogo de terminal com níveis de dificuldade, dicas e estatísticas de sessão
- [gerenciador-escolar](https://github.com/lukas550/gerenciador-escolar) — Sistema de cadastro, edição e relatório de alunos com cálculo automático de médias
- [sistema-gerenciador-de-estoque](https://github.com/lukas550/sistema-gerenciador-de-estoque) — CRUD de produtos em estoque com relatório financeiro (refatorado)
- [gerenciador-de-tarefas](https://github.com/lukas550/gerenciador-de-tarefas) — Sistema de gerenciamento de tarefas via terminal, com arquitetura modular (pacote `core`) e persistência em arquivo `.txt`

---

## Tecnologias Utilizadas

- Python 3
- Git e GitHub
- VS Code

---

Feito com dedicação por Lukas.