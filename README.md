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
