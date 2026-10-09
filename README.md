# CV digital — Danillo Xavier

Projeto do currículo digital, com versões em português, inglês e alemão e recursos de impressão do CV e da carta de apresentação.

## Arquivos principais

- `index.html`: interface, estilos e lógica de apresentação e impressão.
- `cv-data.json`: conteúdo do currículo e configurações por idioma.
- Imagens na raiz: avatar e elementos gráficos utilizados pelo currículo.
- `exports/`: PDFs e capturas previamente exportados.
- Arquivos `validation-*` e `visual-validation-*`: registros visuais anteriores, não resultados de uma nova validação.
- Arquivos `before-live-import` e variantes `index.*`: versões e materiais históricos.

## Desenvolvimento

Com as dependências instaladas, execute `npm run dev`. O projeto mantém a configuração Vercel existente em `vercel.json`.

## CV experimental ampliado

Abra `cv-experimental.html` diretamente no navegador. A versão experimental usa o motor do CV completo de `index.html`: mesmo tema, renderizadores, controles de idiomas, alternância compacto/completo, cartas e modos de impressão/PDF. Abre por padrão em português e no modo completo. Os dados são incorporados para permitir abertura local; as novas seções e os blocos do CV completo também têm conteúdo estático no HTML. Os controles continuam dependendo de JavaScript.

- Conteúdo original preservado: título, perfil, contato, cargos, períodos, resultados, reconhecimentos, formação, síntese da experiência e cartas de apresentação.
- Habilidades, ferramentas e stack reorganizadas somente na versão experimental.
- Novas seções: contextos e vínculos, onze especialidades, 28 cases técnicos, catálogo dos 36 projetos/pastas, módulos SIA, fluxos de dados/mobile, ferramentas Utilibox e matriz de competências por case.
- `cv-experimental-data.json`: dados originais com os ajustes autorizados e extensões estruturadas, incluindo vínculos e evidências. Os idiomas originais EN/DE permanecem preservados.
- `cv-experimental.md`: versão textual para leitura e processamento.

O CV atual em `index.html` e `cv-data.json` continua disponível. O estado anterior à experiência foi salvo no commit `648d76f`. Para regenerar a versão experimental, execute `python scripts/build-experimental-cv.py`; o gerador preserva os blocos originais e exige que os vínculos internos tenham destino no HTML.

A expansão está inicialmente em português e aparece no modo completo em PT. Os idiomas EN/DE mantêm o conteúdo original, sem tradução automática da expansão. As novas seções vêm depois das páginas originais, com índice e vínculos para os cargos e a formação. Cartas e síntese compacta permanecem acessíveis pelos controles existentes; a versão textual também as conserva. O gerador reutiliza `index.html` por meio de `scripts/experimental-engine.py`; `scripts/experimental-engine.css` adapta o tema para conteúdos extensos e permite que as páginas fluam na impressão, sem altura fixa ou corte do texto. O catálogo contém módulos, submódulos, fluxos e versões do mesmo ecossistema; seus totais não representam produtos independentes ou comprovação de implantação.

### Apresentação como currículo

A versão ampliada usa apresentação clara em fundo branco, tipografia legível, experiências em sequência e seções de perfil, áreas de atuação, reconhecimentos, resultados, formação, competências e tecnologias. As habilidades estão agrupadas com os projetos e experiências de origem; a stack principal contém tecnologias representativas, com o repertório ampliado nas categorias e anexos.

Os 28 cases recebem uma apresentação breve no corpo do CV, organizados em quatro contextos: Agrodan; pesquisa e formação; IA, multiagentes e ML; produtos, decisão e computação visual. Cada entrada apresenta contribuição, mecanismos de implementação, tecnologias e links para contexto e fontes. As métricas continuam sendo aquelas já declaradas no CV; não são atribuídas a módulos individuais sem correspondência documentada.

O acervo completo permanece no HTML em **Acervo técnico completo**, inicialmente recolhido. Links para fontes abrem o anexo correspondente. Para incluir esse material na impressão, marque **Incluir acervo técnico no PDF**; a impressão padrão contém o currículo e os resumos dos cases. As regras de paginação foram adaptadas no CSS, mas a paginação final depende do navegador e ainda precisa de revisão visual.

`scripts/cv-editorial.py` organiza as competências, tecnologias e resumos. O original em `index.html` permanece preservado, e o motor existente continua responsável por idiomas, alternância de versões, cartas e impressão.

## Proposta de evolução do currículo

Abra `proposta-cv.html` diretamente no navegador. A página é autônoma e contém:

- Comparação do conteúdo atual com a proposta em 13 blocos.
- Onze seções extensas, com textos de experiência, arquitetura, métodos e cases de agentes, IA, ML, visão, SIA, mobile, dados, produção, produtos, infraestrutura e gráficos.
- Catálogo de 94 módulos/submódulos de negócio do SIA em 23 referências Git locais, com distinção entre implementação e integração de conteúdo incorporado.
- Detalhamento adicional de 48 fluxos ETL/indicadores/mobile, com sobreposição entre camadas explicitada.
- Tabela pesquisável de associações entre habilidade, case e fonte.
- Catálogo pesquisável das 36 pastas levantadas, com contexto, métodos, stack e evidências.
- Pontos específicos para revisar antes de aplicar as alterações.

O EFS-AHP é apresentado como pesquisa vinculada ao doutorado, conforme confirmado por Danillo. Os textos propostos não foram aplicados a `index.html` ou `cv-data.json`.

Para atualizar o HTML a partir do CV atual e dos dados locais de pesquisa, execute `python scripts/build-cv-proposal.py`. O gerador lê `../../doutorado/portfolio-research` a partir da raiz do repositório (caminho resolvido automaticamente pelo script) e incorpora os dados ao HTML; esse diretório não é necessário para abrir a página gerada.

`scripts/audit-sia-branches.py` atualiza `sia-branch-cases.json` a partir das referências Git já disponíveis localmente em Agrodan e Agrodan/etl, sem trocar a branch, baixar dados ou executar o código dos projetos. Execute-o antes do gerador para atualizar esse catálogo. `scripts/proposal-details.py` contém as narrativas e os cases aprofundados.

`cv-proposta-detalhada.json` guarda a proposta estruturada e `SIA_MODULOS_E_COMPETENCIAS.md` apresenta o catálogo SIA em texto. Fontes no formato `Agrodan@origin/development:caminho` referem-se a arquivos daquela branch; podem ser lidas com `git show origin/development:caminho` no repositório correspondente. São evidências históricas locais, não confirmação de implantação ou do estado remoto atual.

## Transferência

Em 08/10/2026, os arquivos locais de `C:\Users\Danillo\Documents\doutorado\CV` foram copiados para a raiz deste repositório, incluindo conteúdo atualizado, assets, versões anteriores, exports e capturas. A origem foi preservada.

O link para `competencias.html` foi retirado da interface transferida porque essa página não está na pasta de origem. O mapa de projetos e competências continua separado em `C:\Users\Danillo\Documents\doutorado\portfolio-research`; suas propostas ainda não foram incorporadas ao currículo.

O arquivo preexistente `api/pdf.js` está vazio; não há geração de PDF no servidor implementada nesse endpoint. A impressão do currículo é feita pela interface web.
