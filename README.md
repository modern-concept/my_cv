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

## Transferência

Em 08/10/2026, os arquivos locais de `C:\Users\Danillo\Documents\doutorado\CV` foram copiados para a raiz deste repositório, incluindo conteúdo atualizado, assets, versões anteriores, exports e capturas. A origem foi preservada.

O link para `competencias.html` foi retirado da interface transferida porque essa página não está na pasta de origem. O mapa de projetos e competências continua separado em `C:\Users\Danillo\Documents\doutorado\portfolio-research`; suas propostas ainda não foram incorporadas ao currículo.

O arquivo preexistente `api/pdf.js` está vazio; não há geração de PDF no servidor implementada nesse endpoint. A impressão do currículo é feita pela interface web.
