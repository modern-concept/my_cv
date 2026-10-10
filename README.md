# CV digital — Danillo Xavier

## CV principal

### PDF abaixo de 2 MB

Use **Baixar PDF leve** no HTML para gerar e baixar o arquivo diretamente. O botão respeita o idioma PT/EN, o modo completo/compacto, CV/Carta/CV+Carta, a variante da carta e a opção de incluir o acervo. A exportação é uma diagramação de texto com fundo branco, títulos, colunas, tabelas, gráficos vetoriais e links; a paginação é própria desse gerador e pode diferir da impressão do navegador. Nenhuma parte do conteúdo selecionado é cortada para reduzir o arquivo. O tamanho gerado é informado ao final.

Funciona também ao abrir `index.html` diretamente, sem Python, servidor ou internet. Mantenha a pasta `vendor/pdfmake` junto ao HTML: ela contém a biblioteca e as fontes. O código de exportação fica em `scripts/cv-pdf-export.js` e é incorporado ao HTML na regeneração. Os arquivos locais da biblioteca também estão incluídos na configuração de hospedagem existente. O botão **Imprimir / PDF** continua usando a diagramação de impressão do navegador.

Mantenha o modo completo e **Incluir acervo técnico no PDF** marcado para preservar todas as páginas adicionais. Essa opção fica marcada por padrão. A impressão usa fundos escuros sólidos e cores opacas para reduzir a complexidade do PDF, mantendo a diagramação; o visual na tela continua igual.

Depois de salvar pelo navegador, comprima a estrutura do PDF e a foto. O texto, os gráficos vetoriais, os links e todas as páginas são preservados:

```powershell
python scripts/compress-cv-pdf.py "C:\caminho\CV.pdf"
```

O comando cria `CV-compact.pdf`, preservando o original. Requer PyMuPDF (`python -m pip install PyMuPDF`). A foto é recomprimida em JPEG com qualidade 85 e sua máscara de transparência é mantida. O tamanho final depende da exportação do navegador; o script informa quando o resultado permanece acima de 2 MB e nunca remove páginas para atingir esse limite. Na exportação integral verificada, PT tinha 120 páginas/1,86 MB e EN 88 páginas/1,18 MB.

Abra **`index.html`**. O currículo completo está em um único HTML, com português e inglês, experiência profissional, formação, competências, projetos, cartas e anexos técnicos. O botão de idioma troca todo o conteúdo na própria página. A opção em alemão foi removida.

- `index.html`: página principal com o motor existente, dados incorporados e as duas versões das novas seções.
- `cv-data.json`: dados canônicos PT/EN com cases, vínculos e fontes. `extensions.locales.en` guarda a redação editorial em inglês.
- `cv-experimental.md` e `cv-experimental-en.md`: exportações textuais auxiliares; a apresentação do CV usa apenas o HTML principal.
- Imagens na raiz: avatar e elementos gráficos existentes.

O HTML pode ser aberto diretamente no navegador. Para desenvolvimento, execute `npm run dev` com as dependências instaladas. A configuração Vercel existente publica `index.html`, `cv-data.json` e imagens; não houve publicação nesta alteração.

## Conteúdo e apresentação

A seção Utilibox apresenta 11 áreas de aplicação, com objetivos, métodos, habilidades e três ferramentas representativas por grupo. O inventário completo permanece nos dados canônicos; os links internos existentes apontam para os respectivos grupos. O texto PT/EN é gerado por `scripts/cv-utilibox-domains.py`.

A matriz de habilidades agrupa os 45 cases e os 11 destaques em 13 especialidades, com narrativas, competências aplicadas, contexto, tecnologias e links para as entregas correspondentes. Um grupo adicional descreve a prática de algoritmos e estruturas de dados. A organização é compartilhada entre PT/EN e gerada em `scripts/cv-skill-matrix.py`; cada case pertence a um grupo, mantendo seu contexto de implementação, pesquisa ou proposta.

O radar usa um índice relativo de abrangência entre 6 e 10, calculado pela normalização das contagens de projetos: `6 + 4 × (contagem − mínimo) / (máximo − mínimo)`. Os gráficos de barras mantêm as contagens reais. Esse índice representa a abrangência do portfólio, sem equivaler a uma avaliação de proficiência.

A terceira página do modo completo reúne o panorama visual de habilidades, stacks e áreas de atuação, em PT/EN. Os gráficos usam contagens de projetos relacionados, sem notas de proficiência; a seleção exclui backups, referências de terceiros e propostas. Cada competência tem links para os projetos correspondentes. A experiência profissional ocupa a primeira página, perfil/formação e trajetória adicional ficam na segunda, e as habilidades, ferramentas e cases detalhados vêm depois do panorama. Essas três primeiras páginas usam quebras de impressão explícitas; o restante segue em fluxo contínuo. A seleção e os gráficos são gerados por `scripts/cv-capability-map.py`.

O motor conserva o tema escuro, cabeçalho, cartões, grade de experiências, colunas, alternância compacto/completo, cartas e modos de impressão. As novas seções aparecem no modo completo e respeitam o idioma selecionado. A altura acompanha o conteúdo, sem reservar uma folha A4 para cada seção. Na impressão, os blocos seguem em fluxo contínuo, sem quebras obrigatórias entre seções; cards e linhas extensas dos anexos podem ser divididos para aproveitar o espaço. A carta começa em uma página própria quando impressa junto ao CV. A paginação final depende do navegador e ainda precisa de revisão visual.

O corpo do CV prioriza **34 destaques**:

- SIA/Agrodan: 13 entradas profissionais de planejamento agrícola, irrigação, pulverização, compras, qualidade, packing, ETL e coleta mobile.
- Utilibox: oito entradas de decisão multicritério, filas, Lean, análise econômica, priorização, conhecimento e aprendizagem.
- Pesquisa e formação: doutorado EFS-AHP, estágio hospitalar e faculdade.
- IA, sistemas multiagentes e Machine Learning.
- Otimização e integração de sistemas.

Os anexos mantêm 28 cases aprofundados, 36 pastas, 94 módulos SIA, 48 fluxos técnicos e 136 ferramentas Utilibox. Podem ser abertos na página ou incluídos no PDF com **Incluir acervo técnico no PDF**. Protótipos como Dente de Leão permanecem nesse acervo.

As métricas são aquelas declaradas no CV. Módulos não recebem impacto financeiro individual sem correspondência documentada. O catálogo contém componentes e camadas sobrepostas, estudos, backups e referências; seus totais não representam produtos independentes nem comprovam implantação.

Em inglês, os anexos usam uma adaptação editorial mais sintética da aplicação e dos mecanismos observados. Nomes próprios, siglas de domínio, identificadores e caminhos de código permanecem preservados.

## Atualização

Os links públicos ficam em `cv-project-links.json`: sites publicados têm prioridade e repositórios são incluídos quando acessíveis sem autenticação. As ferramentas do Utilibox usam endereços do catálogo publicado. `scripts/cv-project-links.py` aplica esses destinos nos destaques e anexos PT/EN; as evidências de código permanecem nos dados de pesquisa. A conferência inicial foi feita em 09/10/2026.

O detalhamento do CV apresenta áreas de aplicação, público, objetivos, arquitetura, métodos e tecnologias. `scripts/cv-project-details.py` organiza essas descrições em português e inglês. Caminhos de arquivos, listas de fontes locais e notas da revisão não são exibidos ao recrutador; a pesquisa original permanece nos dados. Os perfis bilíngues dos 38 projetos ficam em `extensions.projectProfiles`.

`scripts/cv-globalcom.py` apresenta o Globalcom Certification OS como arquitetura funcional e técnica entregue, com implementação em andamento, conforme confirmação do usuário. O CV contém um resumo com links; o acervo concentra os detalhes em sete frentes: Agentic AI, RAG/documentos, workflow, governança/segurança, API/MCP/RPA, domínio/produto e consultoria/roadmap. A stack é a especificada na arquitetura; operação em produção e resultados operacionais não são declarados. O HTML de origem não é publicado junto ao CV.

O panorama da página 3 mostra contagens de projetos associados a competências, stacks e áreas de aplicação, com links para as evidências. O radar não usa notas de proficiência. Os resultados financeiros estão vinculados à atuação na Agrodan (jan/2019–abr/2024), mantendo as bases anuais/mensais sem total agregado. Head de Tecnologia e Gerente de TIC são funções simultâneas entre mar/2021 e nov/2023.

`scripts/cv-development.py` mantém o MBA Operational Excellence da FM2S em andamento (maio/2026 a março/2027 previsto), relaciona a formação às aplicações de Lean e melhoria contínua do Utilibox e acrescenta 120 horas de prática no LeetCode. Os desafios listados são referências temáticas, sem declaração de quantidade resolvida ou ranking. Também acrescenta seis frentes de MLOps do TraderMind: dados/qualidade, treinamento/artefatos, validação temporal, serving, supervisão/retreino e observabilidade. O MBA usa um identificador próprio e aparece primeiro na formação; os links do doutorado continuam preservados.

`scripts/cv-agritech.py` acrescenta a atuação de Danillo como desenvolvedor da plataforma de contagem e rastreabilidade de frutas na Agrodan/Agritech.NE, confirmada pelo usuário e contextualizada pelo relatório final de março/2024. Quatro frentes cobrem plataforma, integração ERP/classificadora, acompanhamento/alertas e resultados industriais. Os indicadores são atribuídos ao projeto/equipe. A produção é apresentada como 30 → 37,5 caixas/h, sem reproduzir o percentual inconsistente de 22,5% do documento. Não são inferidos frameworks de visão computacional, linguagens ou autoria individual do treinamento. O DOCX não é publicado no repositório do CV.

Execute `python scripts/build-experimental-cv.py` para regenerar **`index.html` e `cv-data.json`**, além das exportações textuais. O gerador exige destinos válidos para links internos de ambas as versões e preserva os relatos profissionais, salvo ajustes autorizados de competências e tecnologias.

- `scripts/experimental-engine.py`: template do motor original e integração PT/EN. O template fica no próprio script para permitir regeneração sem outro HTML.
- `scripts/experimental-engine.css`: estilos adicionais, visibilidade por idioma e impressão.
- `scripts/cv-editorial.py`: destaques e competências.
- `scripts/cv-priority-projects.py`: destaques SIA/Utilibox e correspondência com o inventário.
- `scripts/cv-english.py` e `scripts/cv-english-catalogs.py`: redação e catálogos em inglês.

O gerador usa o inventário salvo em `cv-proposta-detalhada.json`. Mudanças de layout regeneráveis devem ser feitas no template do motor ou nos estilos de extensão.

## Pesquisa e histórico

`proposta-cv.html` é o material de proposta e pesquisa anterior. `SIA_MODULOS_E_COMPETENCIAS.md` e `sia-branch-cases.json` guardam o detalhamento SIA. `scripts/audit-sia-branches.py` lê referências Git locais de Agrodan e Agrodan/etl. `scripts/build-cv-proposal.py` atualiza a proposta a partir de `../../doutorado/portfolio-research`.

Fontes como `Agrodan@origin/development:caminho` indicam arquivos em referências Git locais, consultáveis com `git show origin/development:caminho`. São evidências de implementação, sem afirmação automática de autoria exclusiva, disponibilidade pública ou impacto medido.

Os originais vieram de `C:\Users\Danillo\Documents\doutorado\CV`, com a origem preservada. A versão anterior à ampliação está no histórico Git. `cv-experimental.html`, `cv-experimental-en.html` e `cv-experimental-data.json` foram retirados após a integração no CV principal. `exports/`, capturas e variantes históricas de `index.*` preservam materiais anteriores.

O endpoint `api/pdf.js` está vazio; a geração pelo botão **Baixar PDF leve** acontece no navegador, usando pdfmake 0.2.20 e fontes locais. **Imprimir / PDF** usa a impressão nativa. O comando de compressão abaixo é uma alternativa para PDFs salvos pela impressão nativa.
