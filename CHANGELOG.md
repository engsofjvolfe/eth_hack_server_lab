📘 CHANGELOG — eth_hack_server_lab  
Este changelog registra a evolução técnica do projeto, com foco em rastreabilidade clara entre TODOs, commits e progresso real. Cada entrada pode ser referenciada no Git, no TODO.md, ou nos documentos reflexivos.

---

📅 2025-06-12 — Estrutura inicial do servidor Flask vulnerável  
🔁 Commit: feat: estrutura inicial do servidor com falhas intencionais

Cria estrutura principal do projeto Flask:
- `app.py` para execução local com `flask run`
- `main.py` com função `create_app()` e registro explícito de blueprints

Adiciona rotas vulneráveis:
- `/login`: aceita GET e POST com formulário simples e autenticação hardcoded (sem hash ou banco de dados)
- `/admin`: acessível diretamente, sem qualquer verificação ou autenticação
- Redirecionamento de `/` para `/login`

Organiza serviços e lógica separada:
- `auth_service.py` e `admin_service.py` separados do roteador
- Sem uso de sessão, cookies ou JWT (comportamento intencional nesta fase)

Documenta vulnerabilidades:
- Comentários explicativos destacam falhas propositalmente mantidas para estudo
- Nenhuma proteção real implementada — serve como base para testes ofensivos

✍️ Observações:
- Essa primeira entrega foi feita diretamente na branch `main` para facilitar testes locais e ajustes iniciais.
- Próximos recursos e ajustes serão feitos via branches atômicas e commits rastreáveis.
