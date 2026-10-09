# SIA / SIAgro — projetos de negócio, módulos e origem das competências

Experiência profissional na Agrodan. As entradas são partes do mesmo ecossistema, não produtos independentes.

94 módulos/submódulos de negócio identificados nas referências Git locais e 48 fluxos do checkout/ETL/mobile. Há sobreposição entre camadas; não somar como produtos únicos.

A notação `Agrodan@origin/development:caminho` aponta para um arquivo na referência Git; use `git show origin/development:caminho` dentro do repositório. `Agrodan/etl@...` aponta para o repositório backend aninhado.

## Abastecimento da frota

**Domínio:** Frota e custos.

**Finalidade:** Acompanhar abastecimentos e sua leitura gerencial.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/AbastecimentoFrota/AbastecimentoFrota.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Absenteísmo

**Domínio:** Pessoas e operação.

**Finalidade:** Disponibilizar acompanhamento de absenteísmo.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/Absenteismo/Absenteismo.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Acompanhamentos operacionais

**Domínio:** Gestão.

**Finalidade:** Compor cartões, filtros, gráficos e tabelas de acompanhamento.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Referências a sincronização; Estado por hooks; Efeitos e carregamento por hooks.

**Stack:** @material-ui/core, @material-ui/icons, @material-ui/lab, @nivo/bar, @nivo/pie, color-interpolate, dexie, react, react-csv, react-custom-scrollbars, react-redux, thenby.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Referências a sincronização; Estado por hooks; Efeitos e carregamento por hooks.

**Fontes:** `Agrodan@origin/development:src/pages/Acompanhamentos/Dash_Orcamento.js:1`, `Agrodan@origin/development:src/pages/Acompanhamentos/MainData.js:1`, `Agrodan@origin/development:src/pages/Acompanhamentos/indicadores.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Áreas de campo e packing

**Domínio:** Navegação operacional.

**Finalidade:** Organizar acesso a informações de campo, packing e qualidade.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Estado por hooks.

**Stack:** @material-ui/core, @nivo/bar, moment, react, react-router-dom.

**Sinais da implementação:** Estado por hooks.

**Fontes:** `Agrodan@origin/development:src/pages/Areas/Campo.js:1`, `Agrodan@origin/development:src/pages/Areas/GestaoQualidadeLinks.js:1`, `Agrodan@origin/development:src/pages/Areas/Monitoramento.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Monitoramento Atel Escola

**Domínio:** Monitoramento ambiental.

**Finalidade:** Representar dados e leituras de monitoramento de umidade no contexto do módulo.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, react-router-dom, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/AtelEscola/AtelEscola.js:1`, `Agrodan@origin/development:src/pages/AtelEscola/LegendMUS.js:1`, `Agrodan@origin/development:src/pages/AtelEscola/MonitoramentoUmidadeSolo.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Auditoria de pulverização

**Domínio:** Operações agrícolas e geoinformação.

**Finalidade:** Relacionar trajeto, velocidade, talhões e serviços para avaliar a execução da pulverização.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Mapas e informação espacial; Mapas Leaflet; Rotas backend correspondentes localizadas.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, @use-it/event-listener, crypto-js, leaflet, moment, react, react-bootstrap, react-dom, react-leaflet, react-leaflet-canvas-layer, react-leaflet-multi-options-polyline, react-router-dom, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/AuditoriaPulverizacao/AuditoriaPulverizacao.js:1`, `Agrodan@origin/development:src/pages/AuditoriaPulverizacao/DataMap.js:1`, `Agrodan@origin/development:src/pages/AuditoriaPulverizacao/LegendMiam.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-miam.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Auditoria SGA

**Domínio:** Auditoria operacional.

**Finalidade:** Disponibilizar a visão de auditoria relacionada ao SGA.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/AuditoriaSGA/AuditoriaSGA.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Auditoria SIA

**Domínio:** Governança de dados.

**Finalidade:** Disponibilizar a visão de auditoria no SIA.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, moment-duration-format, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/AuditoriaSIA/AuditoriaSIA.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Avaliação de equipes

**Domínio:** RH e desempenho.

**Finalidade:** Organizar respostas, avaliação, qualidade e resumo de equipes.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Stack:** @material-ui/core, @material-ui/icons, dexie, react, react-select.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/AvaliacaoEquipe/Avaliacao.js:1`, `Agrodan@origin/development:src/pages/AvaliacaoEquipe/Qualidade.js:1`, `Agrodan@origin/development:src/pages/AvaliacaoEquipe/Resumo.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-avaliacao-equipe.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Avaliação de equipes administrativas

**Domínio:** RH e desempenho.

**Finalidade:** Representar o processo de avaliação de equipes administrativas.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Stack:** @material-ui/core, @material-ui/icons, dexie, react, react-select.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Fontes:** `Agrodan@origin/development:src/pages/AvaliacaoEquipeADM_OFC/Avaliacao.js:1`, `Agrodan@origin/development:src/pages/AvaliacaoEquipeADM_OFC/Qualidade.js:1`, `Agrodan@origin/development:src/pages/AvaliacaoEquipeADM_OFC/Resumo.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Avaliação aluno–professor

**Domínio:** Educação e avaliação.

**Finalidade:** Modelar a avaliação entre alunos e professores.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Stack:** @material-ui/core, @material-ui/icons, dexie, react, react-select.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Fontes:** `Agrodan@origin/development:src/pages/AvaliacaoEscolaAlunoProfessor/Avaliacao.js:1`, `Agrodan@origin/development:src/pages/AvaliacaoEscolaAlunoProfessor/Qualidade.js:1`, `Agrodan@origin/development:src/pages/AvaliacaoEscolaAlunoProfessor/Resumo.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Avaliação gestor–gestor

**Domínio:** Educação e avaliação.

**Finalidade:** Modelar avaliação entre gestores no contexto escolar.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Stack:** @material-ui/core, @material-ui/icons, dexie, react, react-select.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Fontes:** `Agrodan@origin/development:src/pages/AvaliacaoEscolaGestorGestor/Avaliacao.js:1`, `Agrodan@origin/development:src/pages/AvaliacaoEscolaGestorGestor/Qualidade.js:1`, `Agrodan@origin/development:src/pages/AvaliacaoEscolaGestorGestor/Resumo.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Avaliação professor–gestor

**Domínio:** Educação e avaliação.

**Finalidade:** Modelar o processo de avaliação de gestores por professores.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Stack:** @material-ui/core, @material-ui/icons, dexie, react, react-select.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Fontes:** `Agrodan@origin/development:src/pages/AvaliacaoEscolaProfessorGestor/Avaliacao.js:1`, `Agrodan@origin/development:src/pages/AvaliacaoEscolaProfessorGestor/Qualidade.js:1`, `Agrodan@origin/development:src/pages/AvaliacaoEscolaProfessorGestor/Resumo.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Avaliação professor–professor

**Domínio:** Educação e avaliação.

**Finalidade:** Modelar avaliação entre professores.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Stack:** @material-ui/core, @material-ui/icons, dexie, react, react-select.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Fontes:** `Agrodan@origin/development:src/pages/AvaliacaoEscolaProfessorProfessor/Avaliacao.js:1`, `Agrodan@origin/development:src/pages/AvaliacaoEscolaProfessorProfessor/Qualidade.js:1`, `Agrodan@origin/development:src/pages/AvaliacaoEscolaProfessorProfessor/Resumo.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Avaliação invertida

**Domínio:** RH e avaliação.

**Finalidade:** Representar uma perspectiva invertida no processo de avaliação.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Stack:** @material-ui/core, @material-ui/icons, dexie, react, react-select.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/AvaliacaoInvertida/Avaliacao.js:1`, `Agrodan@origin/development:src/pages/AvaliacaoInvertida/Qualidade.js:1`, `Agrodan@origin/development:src/pages/AvaliacaoInvertida/Resumo.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-avaliacao-invertida.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Avaliação por pares

**Domínio:** RH e avaliação.

**Finalidade:** Modelar avaliações entre pares e seus resumos.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Stack:** @material-ui/core, @material-ui/icons, dexie, react, react-select.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/AvaliacaoPares/Avaliacao.js:1`, `Agrodan@origin/development:src/pages/AvaliacaoPares/Qualidade.js:1`, `Agrodan@origin/development:src/pages/AvaliacaoPares/Resumo.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-avaliacao-pares.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Batidas de ponto

**Domínio:** RH e jornadas.

**Finalidade:** Disponibilizar leitura de registros de ponto.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/BatidaPonto/BatidaPonto.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Visão CFO

**Domínio:** Gestão financeira.

**Finalidade:** Disponibilizar a visão gerencial identificada como CFO.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/CFO/CFO.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Resultados comerciais

**Domínio:** Comercial.

**Finalidade:** Organizar lançamentos, resultados, auditorias e visão gerencial comercial.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Stack:** @material-ui/core, @material-ui/icons, dexie, fs, moment, pdfreader, react, react-file-base64, react-select.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks; Efeitos e carregamento por hooks; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/COMERCIAL/Resultados/Auditorias.js:1`, `Agrodan@origin/development:src/pages/COMERCIAL/Resultados/Config.js:1`, `Agrodan@origin/development:src/pages/COMERCIAL/Resultados/CriarLancamento.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/comercial/rotas-comercial.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Contas a pagar

**Domínio:** Finanças.

**Finalidade:** Disponibilizar acompanhamento de contas a pagar.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/CONTAS_PAGAR/CONTAS_PAGAR.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Cadastro de talhões

**Domínio:** Gestão agrícola.

**Finalidade:** Disponibilizar consulta/gestão do cadastro de talhões.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/CadastroTalhoes/CadastroTalhoes.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Caderno de campo

**Domínio:** Coleta agrícola.

**Finalidade:** Organizar apontamentos, seleção de equipe, atividade e qualidade, com armazenamento local e sincronização no código.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Stack:** @material-ui/core, @material-ui/icons, @mui/material, dexie, moment, react, react-chartjs-2, react-select, uuidv4.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks; Efeitos e carregamento por hooks; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/CadernoCampo/Apontamentos.js:1`, `Agrodan@origin/development:src/pages/CadernoCampo/Config.js:1`, `Agrodan@origin/development:src/pages/CadernoCampo/MeusApontamentos.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-caderno-campo.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Caixas embaladas

**Domínio:** Packing.

**Finalidade:** Disponibilizar acompanhamento de caixas embaladas.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/CaixasEmbaladas/CaixasEmbaladas.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Caixas embaladas por UGB

**Domínio:** Packing e unidades de gestão.

**Finalidade:** Relacionar a leitura de embalagem às unidades de gestão.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/CaixasEmbaladasUgb/CaixasEmbaladasUgb.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Conferência de insumos

**Domínio:** Suprimentos e operação.

**Finalidade:** Disponibilizar informações para conferência de insumos.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/ConferenciaInsumos/ConferenciaInsumos.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Controle de pallets

**Domínio:** Packing e rastreabilidade.

**Finalidade:** Disponibilizar leitura de controle dos pallets.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/ControlePallets/ControlePallets.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Controle de qualidade

**Domínio:** Qualidade.

**Finalidade:** Disponibilizar acompanhamento de controle de qualidade.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/ControleQualidade/ControleQualidade.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Controle de recebimento

**Domínio:** Packing e suprimentos.

**Finalidade:** Disponibilizar a leitura do recebimento operacional.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Estado por hooks; Efeitos e carregamento por hooks; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Estado por hooks; Efeitos e carregamento por hooks; Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/ControleRecebimento/ControleRecebimento.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Cronograma de safra

**Domínio:** Planejamento agrícola.

**Finalidade:** Organizar cronograma, colheita e edição da programação.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, react-touch-screen-keyboard, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/CronogramaSafra/CronogramaSafra.js:1`, `Agrodan@origin/development:src/pages/CronogramaSafra/Colheita.js:1`, `Agrodan@origin/development:src/pages/CronogramaSafra/CronogramaSafraApp.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Formulário do cronograma de safra

**Domínio:** Coleta e planejamento.

**Finalidade:** Representar a entrada/edição de cronograma e talhões.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Referências a sincronização.

**Stack:** @material-ui/core, @material-ui/icons, dexie, moment, react, react-touch-screen-keyboard.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Referências a sincronização.

**Fontes:** `Agrodan@origin/development:src/pages/CronogramaSafraForm/CronogramaSafraForm.js:1`, `Agrodan@origin/development:src/pages/CronogramaSafraForm/Colheita.js:1`, `Agrodan@origin/development:src/pages/CronogramaSafraForm/CronogramaSafraEdit.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Cronograma de safra integrado ao SIA

**Domínio:** Planejamento e sincronização.

**Finalidade:** Relacionar edição, visualização e sincronização da programação de safra.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Referências a sincronização; Estado por hooks; Efeitos e carregamento por hooks.

**Stack:** @material-ui/core, @material-ui/icons, dexie, moment, react.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Referências a sincronização; Estado por hooks; Efeitos e carregamento por hooks; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/CronogramaSafraSIA/Config.js:1`, `Agrodan@origin/development:src/pages/CronogramaSafraSIA/Edicao.js:1`, `Agrodan@origin/development:src/pages/CronogramaSafraSIA/Sincronizacao.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-cronograma-safra.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Croquis

**Domínio:** Informação espacial.

**Finalidade:** Disponibilizar representação de croquis.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados.

**Stack:** @material-ui/core, @nivo/pie, moment, react.

**Sinais da implementação:** .

**Fontes:** `Agrodan@origin/development:src/pages/Croquis/Croquis.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Custos

**Domínio:** Controladoria.

**Finalidade:** Disponibilizar acompanhamento dos custos operacionais.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/Custos/Custos.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Dashboard de satisfação

**Domínio:** Qualidade de serviço.

**Finalidade:** Disponibilizar visão consolidada de satisfação.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/DashSatisfacao/DashSatisfacao.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Embalagem

**Domínio:** Packing.

**Finalidade:** Disponibilizar indicadores da operação de embalagem.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados.

**Stack:** @material-ui/core, @nivo/bar, moment, react.

**Sinais da implementação:** .

**Fontes:** `Agrodan@origin/development:src/pages/Embalagem/Embalagem.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Estoque virtual

**Domínio:** Estoques.

**Finalidade:** Integrar a consulta ao dashboard de estoque virtual.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/EstoqueVirtual/EstoqueVirtual.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Faturamento

**Domínio:** Comercial e finanças.

**Finalidade:** Disponibilizar acompanhamento de faturamento.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/Faturamento/Faturamento.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Fechamento de talhões

**Domínio:** Planejamento agrícola.

**Finalidade:** Disponibilizar acompanhamento de fechamento dos talhões.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/FechamentoTalhoes/FechamentoTalhoes.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Flutuação de preços

**Domínio:** Comercial.

**Finalidade:** Disponibilizar leitura da variação de preços.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/FlutuacaoPreco/FlutuacaoPreco.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Folha de pagamento

**Domínio:** RH e finanças.

**Finalidade:** Disponibilizar acompanhamento da folha de pagamento.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/FolhaPagamento/FolhaPagamento.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Gestão de estoque

**Domínio:** Supply chain.

**Finalidade:** Disponibilizar a visão de gestão de estoque.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/GestaoEstoque/GestaoEstoque.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Gestão de unidades de negócio

**Domínio:** Gestão organizacional.

**Finalidade:** Articular UGBs, colaboradores, avaliações, planos e melhorias em uma estrutura modular.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Referências a sincronização; Estado por hooks; Efeitos e carregamento por hooks; Planilhas; Integração HTTP.

**Stack:** @material-ui/core, @material-ui/icons, @material-ui/styles, @react-pdf/renderer, axios, dexie, file-saver, moment, prop-types, react, react-icons, react-pdf, react-router-dom, react-select, react-to-pdf, xlsx.

**Sinais da implementação:** Referências a sincronização; Estado por hooks; Efeitos e carregamento por hooks; Planilhas; Integração HTTP; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/GestaoUGBs/Router.js:1`, `Agrodan@origin/development:src/pages/GestaoUGBs/env.js:1`, `Agrodan@origin/development:src/pages/GestaoUGBs/index.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-gestaoUGB.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Horímetro

**Domínio:** Frota e equipamentos.

**Finalidade:** Disponibilizar acompanhamento de horas dos equipamentos.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/Horimetro/Horimetro.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Indicadores e satisfação BPM

**Domínio:** Gestão de processos.

**Finalidade:** Organizar indicadores e registros de satisfação do serviço.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Referências a sincronização; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, dexie, leaflet, moment, prop-types, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf, uuidv4.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Referências a sincronização; Mapas e informação espacial; Mapas Leaflet; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/IndicadorBPM/IndicadorBPM.js:1`, `Agrodan@origin/development:src/pages/IndicadorBPM/SatisfacaoBPM.js:1`, `Agrodan@origin/development:src/pages/IndicadorBPM/utils/downloadData.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-satisfacao-bpm.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Satisfação da logística

**Domínio:** Logística e qualidade de serviço.

**Finalidade:** Representar satisfação relacionada à logística.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, moment, react.

**Sinais da implementação:** .

**Fontes:** `Agrodan@origin/development:src/pages/IndicadorLogistica/SatisfacaoLogistica.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Indicadores de TI e fila de chamados

**Domínio:** Gestão de TIC.

**Finalidade:** Relacionar indicadores, satisfação e fila de chamados.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Mapas e informação espacial; Mapas Leaflet; Rotas backend correspondentes localizadas.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/IndicadorTI/IndicadorTI.js:1`, `Agrodan@origin/development:src/pages/IndicadorTI/FilaChamados.js:1`, `Agrodan@origin/development:src/pages/IndicadorTI/SatisfacaoTI.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-ti.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Monitoramento de irrigação

**Domínio:** Irrigação agrícola.

**Finalidade:** Organizar monitoramento e entrada de dados relacionados à irrigação.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Mapas e informação espacial; Mapas Leaflet; Rotas backend correspondentes localizadas.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, moment-duration-format, react, react-csv-reader, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/Irrigacao/Irrigacao.js:1`, `Agrodan@origin/development:src/pages/Irrigacao/MonitoramentoIrrigacao/Enviando.js:1`, `Agrodan@origin/development:src/pages/Irrigacao/MonitoramentoIrrigacao/InputPhytech.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-irrigacao.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Visão Irrigas

**Domínio:** Irrigação.

**Finalidade:** Disponibilizar a visão identificada como Irrigas.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/Irrigas/Irrigas.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Lean Packing Game

**Domínio:** Produção e aprendizagem.

**Finalidade:** Integrar acesso ao simulador de operações Lean Packing Game.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/LeanPackingGame/LeanPackingGame.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Registro de horas

**Domínio:** Operação e jornadas.

**Finalidade:** Organizar o registro e a leitura de horas.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Rotas backend correspondentes localizadas.

**Stack:** @material-ui/core, @material-ui/icons, moment, react, react-chartjs-2, trabalho-eficiente.jpg.

**Sinais da implementação:** Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/Log Horas/LogHoras.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-log-horas.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Monitoramento MAD

**Domínio:** Monitoramento agrícola.

**Finalidade:** Representar dados de umidade/monitoramento presentes neste módulo.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Camada de dados local; Mapas e informação espacial; Mapas Leaflet; Rotas backend correspondentes localizadas.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, react-router-dom, turf.

**Sinais da implementação:** Camada de dados local; Mapas e informação espacial; Mapas Leaflet; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/MAD/MAD.js:1`, `Agrodan@origin/development:src/pages/MAD/LegendMUS.js:1`, `Agrodan@origin/development:src/pages/MAD/MonitoramentoUmidadeSolo.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-mad.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Monitoramento MAF e manga

**Domínio:** Qualidade do fruto.

**Finalidade:** Representar manga, posições de linhas e dados do monitoramento MAF.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Estado por hooks; Efeitos e carregamento por hooks; Eventos via socket; Rotas backend correspondentes localizadas.

**Stack:** @material-ui/core, @nivo/bar, moment, react, socket.io-client.

**Sinais da implementação:** Estado por hooks; Efeitos e carregamento por hooks; Eventos via socket; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/MAF/Maf.js:1`, `Agrodan@origin/development:src/pages/MAF/MangaCanvas.js:1`, `Agrodan@origin/development:src/pages/MAF/PosicaoLinhas.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/maf/rotas-maf.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Monitoramento integrado de pragas

**Domínio:** Agricultura e geoinformação.

**Finalidade:** Representar dados de pragas no módulo MIP.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Camada de dados local; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Camada de dados local; Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/MIP/MIP.js:1`, `Agrodan@origin/development:src/pages/MIP/LegendMIP.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Matéria seca e previsão de colheita

**Domínio:** Qualidade e maturação.

**Finalidade:** Relacionar leituras, variedades e equações para explorar previsão e ponto de colheita.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Função de previsão; Regra de ponto de colheita; Rotas backend correspondentes localizadas.

**Stack:** @material-ui/core, @nivo/pie, moment, react.

**Sinais da implementação:** Função de previsão; Regra de ponto de colheita; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/MateriaSeca/MateriaSeca.js:1`, `Agrodan@origin/development:src/pages/MateriaSeca/variaveis.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-materia-seca.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Materiais

**Domínio:** Suprimentos.

**Finalidade:** Disponibilizar informações de materiais.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Rotas backend correspondentes localizadas.

**Stack:** @material-ui/core, @nivo/pie, moment, react.

**Sinais da implementação:** Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/Materiais/Materiais.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-materiais.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Movimentação de materiais

**Domínio:** Suprimentos e rastreabilidade.

**Finalidade:** Disponibilizar informações de movimentação de materiais.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Rotas backend correspondentes localizadas.

**Stack:** @material-ui/core, @nivo/pie, moment, react.

**Sinais da implementação:** Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/MovimentacaoMateriais/MovimentacaoMateriais.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-movimentacao-materiais.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Movimentação de pallets e containers

**Domínio:** Packing e logística.

**Finalidade:** Organizar movimentações, dados de container e conferências.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Referências a sincronização; Estado por hooks; Rotas backend correspondentes localizadas.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, dexie, moment, react, react-touch-screen-keyboard.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Referências a sincronização; Estado por hooks; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/MovimentacaoPallet/MovimentacaoPallet.js:1`, `Agrodan@origin/development:src/pages/MovimentacaoPallet/ConferenciaCameras.js:1`, `Agrodan@origin/development:src/pages/MovimentacaoPallet/DadosContainer.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-containers.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Orçamento

**Domínio:** Controladoria.

**Finalidade:** Disponibilizar acompanhamento do orçamento.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet; Rotas backend correspondentes localizadas.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/Orcamento/Orcamento.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-orcamento.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Organograma e áreas

**Domínio:** RH e estrutura organizacional.

**Finalidade:** Representar áreas, indicadores e organização das fazendas.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Referências a sincronização; Estado por hooks.

**Stack:** @material-ui/core, @material-ui/icons, dexie, react.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Referências a sincronização; Estado por hooks.

**Fontes:** `Agrodan@origin/development:src/pages/Organograma/Areas.js:1`, `Agrodan@origin/development:src/pages/Organograma/Indicadores.js:1`, `Agrodan@origin/development:src/pages/Organograma/index.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## PDCA de mão de obra

**Domínio:** Gestão e melhoria contínua.

**Finalidade:** Organizar planos, auditorias e acompanhamento gerencial de mão de obra.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Stack:** @material-ui/core, @material-ui/icons, dexie, moment, react, react-file-base64, react-select.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks; Efeitos e carregamento por hooks.

**Fontes:** `Agrodan@origin/development:src/pages/PDCA/MO/Auditorias.js:1`, `Agrodan@origin/development:src/pages/PDCA/MO/Config.js:1`, `Agrodan@origin/development:src/pages/PDCA/MO/CriarPlano.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Packing e caixaria

**Domínio:** Produção e embalagem.

**Finalidade:** Organizar acesso à operação de packing e caixaria.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Eventos via socket.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/bar, audio-loader, audio-play, moment, play-sound, react, react-router-dom, socket.io-client.

**Sinais da implementação:** Eventos via socket.

**Fontes:** `Agrodan@origin/development:src/pages/Packing/Packing.js:1`, `Agrodan@origin/development:src/pages/Packing/Caixaria/Caixaria.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## PLANAGRO — planejamento e regras agrícolas

**Domínio:** Planejamento agronômico e governança.

**Finalidade:** Relacionar atividades, insumos, orçamento e verificações de aplicação, carência, dosagem e deriva.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Referências a sincronização; Estado por hooks; Efeitos e carregamento por hooks.

**Stack:** @material-ui/core, @material-ui/icons, dexie, leaflet, moment, path, prop-types, react, react-custom-scrollbars, react-data-table-component, react-leaflet, react-leaflet-canvas-layer, react-leaflet-control, react-select, react-to-pdf, react-to-print, recharts, turf, uuidv4, xlsx.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Referências a sincronização; Estado por hooks; Efeitos e carregamento por hooks; Mapas e informação espacial; Mapas Leaflet; Planilhas; Impressão; Regra de carência; Regra de dosagem; Regra de deriva; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/PlanejamentoAgro/Legend.js:1`, `Agrodan@origin/development:src/pages/PlanejamentoAgro/Legenda_new.js:1`, `Agrodan@origin/development:src/pages/PlanejamentoAgro/PLANAGRO.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-planagro.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Previsão de resultados e câmbio

**Domínio:** Planejamento comercial.

**Finalidade:** Organizar previsões, acompanhamento de resultados e contexto de câmbio.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Referências a sincronização; Estado por hooks; Planilhas.

**Stack:** @material-ui/core, @material-ui/icons, dexie, moment, prop-types, react, react-select, uuidv4, xlsx.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Referências a sincronização; Estado por hooks; Planilhas; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/PrevisaoResultados/index.js:1`, `Agrodan@origin/development:src/pages/PrevisaoResultados/pages/Acompanhamento.js:1`, `Agrodan@origin/development:src/pages/PrevisaoResultados/pages/Cambio.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-previsao-resultados.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Programação de processamento

**Domínio:** Packing e capacidade.

**Finalidade:** Disponibilizar a programação de processamento.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/ProgramacaoProcessamento/ProgramacaoProcessamento.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Projetos

**Domínio:** Gestão de projetos.

**Finalidade:** Disponibilizar informações de projetos.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/Projetos/Projetos.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Quantidade de funcionários

**Domínio:** RH e operação.

**Finalidade:** Disponibilizar indicadores de quantidade de colaboradores.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/QtdFuncionarios/QtdFuncionarios.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Qualidade de campo e checklists

**Domínio:** Qualidade agrícola.

**Finalidade:** Organizar checklists, respostas e avaliação de qualidade de campo.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Referências a sincronização; Estado por hooks; Rotas backend correspondentes localizadas.

**Stack:** @material-ui/core, dexie, react, react-select.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Referências a sincronização; Estado por hooks; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/QualidadeCampo/Qualidade.js:1`, `Agrodan@origin/development:src/pages/QualidadeCampo/Respostas.js:1`, `Agrodan@origin/development:src/pages/QualidadeCampo/index.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-qualidade-campo.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Visão de RH

**Domínio:** Gestão de pessoas.

**Finalidade:** Disponibilizar acesso às informações de recursos humanos.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/RH/RH.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Riscos de segurança do trabalho

**Domínio:** SST e geoinformação.

**Finalidade:** Representar riscos de segurança do trabalho no contexto agrícola.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/RISCO_SST/Legenda.js:1`, `Agrodan@origin/development:src/pages/RISCO_SST/Legenda_new.js:1`, `Agrodan@origin/development:src/pages/RISCO_SST/RiscoSST.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Ramais

**Domínio:** Serviços corporativos.

**Finalidade:** Disponibilizar consulta aos ramais corporativos.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/Ramais/Ramais.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Refugo

**Domínio:** Packing e qualidade.

**Finalidade:** Disponibilizar leitura de refugo na operação.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/Refugo/Refugo.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Relatórios BI

**Domínio:** Analytics.

**Finalidade:** Integrar o acesso a relatórios de BI.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, react-router-dom, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/RelatoriosBI/index.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Resumo de mão de obra

**Domínio:** RH e operação.

**Finalidade:** Disponibilizar leitura consolidada de mão de obra.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/ResumoMO/ResumoMO.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Ritual gerencial

**Domínio:** Gestão.

**Finalidade:** Disponibilizar informações para acompanhamento gerencial.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/RitualGerencial/RitualGerencial.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Sistema de gestão da qualidade

**Domínio:** Auditoria e qualidade.

**Finalidade:** Organizar auditorias, registros, papéis e acompanhamento da qualidade.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Stack:** @material-ui/core, @material-ui/icons, dexie, moment, react, react-file-base64, react-select.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks; Efeitos e carregamento por hooks.

**Fontes:** `Agrodan@origin/development:src/pages/SGQ/Auditorias.js:1`, `Agrodan@origin/development:src/pages/SGQ/Config.js:1`, `Agrodan@origin/development:src/pages/SGQ/CriarAuditoria.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Relatórios de qualidade

**Domínio:** Qualidade e analytics.

**Finalidade:** Organizar relatórios vinculados ao SGQ.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Referências a sincronização; Estado por hooks; Efeitos e carregamento por hooks.

**Stack:** @material-ui/core, @material-ui/icons, dexie, react, react-file-base64, react-select.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Referências a sincronização; Estado por hooks; Efeitos e carregamento por hooks.

**Fontes:** `Agrodan@origin/qualiex:src/pages/SgqRelatorios/RelatorioAuditoria.js:1`, `Agrodan@origin/qualiex:src/pages/SgqRelatorios/ResumoAuditorias.js:1`, `Agrodan@origin/qualiex:src/pages/SgqRelatorios/index.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Saldo de banco de horas

**Domínio:** RH e jornadas.

**Finalidade:** Disponibilizar o acompanhamento do saldo de horas.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/SaldoBH/SaldoBH.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Satisfação

**Domínio:** Qualidade de serviço.

**Finalidade:** Disponibilizar informações de satisfação.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, moment, react.

**Sinais da implementação:** .

**Fontes:** `Agrodan@origin/development:src/pages/Satisfacao/Satisfacao.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Segurança

**Domínio:** Segurança e gestão.

**Finalidade:** Disponibilizar informações do módulo identificado como Segurança.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados.

**Stack:** @material-ui/core, @nivo/bar, moment, react.

**Sinais da implementação:** .

**Fontes:** `Agrodan@origin/development:src/pages/Seguranca/Seguranca.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Solicitações de compras

**Domínio:** Compras e orçamento.

**Finalidade:** Organizar itens, centros e solicitações, com contexto local e sincronização no código.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks.

**Stack:** @material-ui/core, @material-ui/icons, dexie, moment, react, react-select.

**Sinais da implementação:** Persistência IndexedDB via Dexie; Camada de dados local; Handlers de sincronização; Referências a sincronização; Estado por hooks; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/SolicitacaoCompras/Solicitacao.js:1`, `Agrodan@origin/development:src/pages/SolicitacaoCompras/index.js:1`, `Agrodan@origin/development:src/pages/SolicitacaoCompras/pages/EstoqueRepo.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-solicitacao-compras.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Sugestões de melhoria

**Domínio:** Inovação e melhoria contínua.

**Finalidade:** Organizar submissão, avaliação e tratamento de sugestões e registros associados.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Referências a sincronização; Estado por hooks; Efeitos e carregamento por hooks; Integração HTTP; Rotas backend correspondentes localizadas.

**Stack:** @material-ui/core, @material-ui/icons, axios, moment, react.

**Sinais da implementação:** Referências a sincronização; Estado por hooks; Efeitos e carregamento por hooks; Integração HTTP; Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/SugestaoMelhorias/index.js:1`, `Agrodan@origin/development:src/pages/SugestaoMelhorias/Components/index.js:1`, `Agrodan@origin/development:src/pages/SugestaoMelhorias/Screens/index.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-sugestao-melhorias.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## UGB Oficina

**Domínio:** Manutenção e gestão.

**Finalidade:** Disponibilizar a visão da unidade de oficina.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/UgbOficina/UgbOficina.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Validação de colheita

**Domínio:** Operação agrícola.

**Finalidade:** Disponibilizar a leitura de validação da colheita.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/ValidacaoColheita/ValidacaoColheita.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Validação MDO

**Domínio:** Pessoas e operação.

**Finalidade:** Disponibilizar validação de mão de obra no módulo MDO.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Rotas backend correspondentes localizadas.

**Stack:** @material-ui/core, @nivo/pie, moment, react.

**Sinais da implementação:** Rotas backend correspondentes localizadas.

**Fontes:** `Agrodan@origin/development:src/pages/ValidacaoMDO/ValidacaoMDO.js:1`, `Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-validacao-mdo.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Validação de mão de obra

**Domínio:** Pessoas e operação.

**Finalidade:** Disponibilizar a visão de validação de mão de obra.

**Habilidades:** Integração de informações; Interface React; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/ValidacaoMO/ValidacaoMO.js:1`.

**Estado e limite:** Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado.

## Monitoramento de vigias

**Domínio:** Operação e vigilância.

**Finalidade:** Representar acompanhamento de vigias e informação espacial.

**Habilidades:** Modelagem de processo; Engenharia frontend; Estado e interação; Integração de dados; Mapas e informação espacial; Mapas Leaflet.

**Stack:** @material-ui/core, @material-ui/icons, @nivo/pie, leaflet, moment, react, react-dom, react-leaflet, react-leaflet-canvas-layer, react-router-dom, turf.

**Sinais da implementação:** Mapas e informação espacial; Mapas Leaflet.

**Fontes:** `Agrodan@origin/development:src/pages/Vigias/Vigias.js:1`, `Agrodan@origin/development:src/pages/Vigias/LegendMUS.js:1`, `Agrodan@origin/development:src/pages/Vigias/MonitoramentoUmidadeSolo.js:1`.

**Estado e limite:** Código de módulo em referência Git local; uso e implantação a contextualizar.

## Gestão UGB — colaboradores e histórico

**Domínio:** Submódulo de Gestão UGB; relacionado ao case principal.

**Finalidade:** Representar colaboradores e histórico no fluxo de gestão das unidades.

**Habilidades:** Modelagem organizacional; Interfaces de gestão; Reuso de componentes.

**Stack:** React, JavaScript.

**Sinais da implementação:** Código do fluxo de gestão UGB.

**Fontes:** `Agrodan@origin/development:src/pages/GestaoUGBs/Modulos/Funcionarios/index.js:1`.

**Estado e limite:** Submódulo; não contar como produto independente.

## Gestão UGB — unidades e papéis

**Domínio:** Submódulo de Gestão UGB; relacionado ao case principal.

**Finalidade:** Representar unidades e papéis no fluxo de gestão das unidades.

**Habilidades:** Modelagem organizacional; Interfaces de gestão; Reuso de componentes.

**Stack:** React, JavaScript.

**Sinais da implementação:** Código do fluxo de gestão UGB.

**Fontes:** `Agrodan@origin/development:src/pages/GestaoUGBs/Modulos/UGBs/index.js:1`.

**Estado e limite:** Submódulo; não contar como produto independente.

## Gestão UGB — 5S

**Domínio:** Submódulo de Gestão UGB; relacionado ao case principal.

**Finalidade:** Representar 5S no fluxo de gestão das unidades.

**Habilidades:** Modelagem organizacional; Interfaces de gestão; Reuso de componentes.

**Stack:** React, JavaScript.

**Sinais da implementação:** Código do fluxo de gestão UGB.

**Fontes:** `Agrodan@origin/development:src/pages/GestaoUGBs/Modulos/5S/index.js:1`.

**Estado e limite:** Submódulo; não contar como produto independente.

## Gestão UGB — avaliação humana

**Domínio:** Submódulo de Gestão UGB; relacionado ao case principal.

**Finalidade:** Representar avaliação humana no fluxo de gestão das unidades.

**Habilidades:** Modelagem organizacional; Interfaces de gestão; Reuso de componentes.

**Stack:** React, JavaScript.

**Sinais da implementação:** Código do fluxo de gestão UGB.

**Fontes:** `Agrodan@origin/development:src/pages/GestaoUGBs/Modulos/Avaliacao_humana/index.js:1`.

**Estado e limite:** Submódulo; não contar como produto independente.

## Gestão UGB — plano de ação

**Domínio:** Submódulo de Gestão UGB; relacionado ao case principal.

**Finalidade:** Representar plano de ação no fluxo de gestão das unidades.

**Habilidades:** Modelagem organizacional; Interfaces de gestão; Reuso de componentes.

**Stack:** React, JavaScript.

**Sinais da implementação:** Código do fluxo de gestão UGB.

**Fontes:** `Agrodan@origin/development:src/pages/GestaoUGBs/Modulos/PlanoAcao/index.js:1`.

**Estado e limite:** Submódulo; não contar como produto independente.

## Gestão UGB — qualificação técnica

**Domínio:** Submódulo de Gestão UGB; relacionado ao case principal.

**Finalidade:** Representar qualificação técnica no fluxo de gestão das unidades.

**Habilidades:** Modelagem organizacional; Interfaces de gestão; Reuso de componentes.

**Stack:** React, JavaScript.

**Sinais da implementação:** Código do fluxo de gestão UGB.

**Fontes:** `Agrodan@origin/development:src/pages/GestaoUGBs/Modulos/QualificacaoTecnica/index.js:1`.

**Estado e limite:** Submódulo; não contar como produto independente.

## Gestão UGB — requalificação técnica

**Domínio:** Submódulo de Gestão UGB; relacionado ao case principal.

**Finalidade:** Representar requalificação técnica no fluxo de gestão das unidades.

**Habilidades:** Modelagem organizacional; Interfaces de gestão; Reuso de componentes.

**Stack:** React, JavaScript.

**Sinais da implementação:** Código do fluxo de gestão UGB.

**Fontes:** `Agrodan@origin/development:src/pages/GestaoUGBs/Modulos/RequalificacaoTecnica/index.js:1`.

**Estado e limite:** Submódulo; não contar como produto independente.

## Gestão UGB — sugestões de melhoria

**Domínio:** Submódulo de Gestão UGB; relacionado ao case principal.

**Finalidade:** Representar sugestões de melhoria no fluxo de gestão das unidades.

**Habilidades:** Modelagem organizacional; Interfaces de gestão; Reuso de componentes.

**Stack:** React, JavaScript.

**Sinais da implementação:** Código do fluxo de gestão UGB.

**Fontes:** `Agrodan@origin/development:src/pages/GestaoUGBs/Modulos/SugestaoMelhorias/index.js:1`.

**Estado e limite:** Submódulo; não contar como produto independente.

## Apontamentos de produção

**Domínio:** Produção agrícola.

**Finalidade:** Integrar registros de produção para análise operacional.

**Habilidades:** ETL SQL; persistência em lote; modelagem de apontamentos.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Relacionamento entre tabelas na consulta.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/apontamento-producao-importer.js:14`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/apontamento-producao-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Jornadas operacionais

**Domínio:** Pessoas e capacidade.

**Finalidade:** Consolidar jornadas para relacionar tempo e operação.

**Habilidades:** Integração de bases; jornadas; transformações SQL.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Relacionamento entre tabelas na consulta.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/jornada-importer.js:3`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/jornada-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Inspeções de UGB

**Domínio:** Qualidade.

**Finalidade:** Normalizar inspeções e evitar duplicação pelo identificador do registro.

**Habilidades:** Deduplicação; normalização; inspeções; ETL.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/inspecoes-ugb-importer.js:13`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/inspecoes-ugb-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Origem de pallets

**Domínio:** Packing e rastreabilidade.

**Finalidade:** Consolidar a origem de pallets para relacionar produção e inspeções.

**Habilidades:** Rastreabilidade de dados; integração SQL; persistência.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Agregação na consulta SQL.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/pallet-origem-importer.js:13`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/pallet-origem-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Metas de produção

**Domínio:** Gestão de produção.

**Finalidade:** Importar metas para comparar a operação com seus referenciais.

**Habilidades:** Modelagem de metas; SQL; integração de fontes.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Relacionamento entre tabelas na consulta.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/meta-producao-importer.js:3`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/meta-producao-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Percentuais de metas

**Domínio:** Gestão de desempenho.

**Finalidade:** Consolidar percentuais relacionados às metas de produção.

**Habilidades:** Indicadores; modelagem de dados; ETL.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Agregação na consulta SQL.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/percentuais-meta-importer.js:13`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/percentuais-meta-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Rendimento por ficha e dia

**Domínio:** Rendimento e packing.

**Finalidade:** Integrar rendimento diário por ficha.

**Habilidades:** Granularidade temporal; indicadores de rendimento; SQL.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/rendimento-ficha-dia-importer.js:13`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/rendimento-ficha-dia-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Atualização de rendimento

**Domínio:** Rendimento e packing.

**Finalidade:** Manter uma segunda leitura de rendimentos para cruzamentos posteriores.

**Habilidades:** Integração de versões de dados; persistência; modelagem temporal.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Agregação na consulta SQL.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/rendimento-ficha-dia-atualizado-importer.js:13`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/rendimento-ficha-dia-atualizado-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Total produzido

**Domínio:** Produção.

**Finalidade:** Disponibilizar totais produzidos no data warehouse.

**Habilidades:** Agregação SQL; carga de dados; análise operacional.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Agregação na consulta SQL.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/total-produzido-importer.js:13`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/total-produzido-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Produção por fazenda

**Domínio:** Gestão agrícola.

**Finalidade:** Separar os totais de produção pela dimensão fazenda.

**Habilidades:** Dimensões analíticas; agregação; integração SQL.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Agregação na consulta SQL; Relacionamento entre tabelas na consulta.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/total-produzido-fazenda-importer.js:3`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/total-produzido-fazenda-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## UGBs e fazendas

**Domínio:** Cadastros e organização.

**Finalidade:** Integrar a relação entre unidades de gestão e fazendas.

**Habilidades:** Modelagem organizacional; dados de referência; ETL.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Relacionamento entre tabelas na consulta.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/ugb-fazenda-importer.js:13`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/fazenda-ugb-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Embalagem por UGB

**Domínio:** Packing.

**Finalidade:** Consolidar registros de embalagem ligados à unidade de gestão.

**Habilidades:** ETL; períodos; embalagem; persistência relacional.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Leitura de coleções persistidas; Agregação na consulta SQL; Relacionamento entre tabelas na consulta.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/l-ugb-embalagem-importer.js:13`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/l-ugb-embalagem-query.js:11`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Embalagem diária

**Domínio:** Packing.

**Finalidade:** Disponibilizar a granularidade diária dos registros de embalagem.

**Habilidades:** Granularidade diária; normalização; indicadores operacionais.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Leitura de coleções persistidas; Agregação na consulta SQL; Relacionamento entre tabelas na consulta.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/l-ugb-embalagem-diario-importer.js:13`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/l-ugb-embalagem-diario-query.js:11`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Base de LUGB Campo

**Domínio:** Operações de campo.

**Finalidade:** Estruturar a base para análises das operações de campo.

**Habilidades:** Camada analítica; SQL; cargas reutilizáveis.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Agregação na consulta SQL.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/lugb_campo/lugb-campo-base-importer.js:3`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/lugb_campo/lugb-campo-base-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Vínculo funcionário–UGB

**Domínio:** Pessoas e campo.

**Finalidade:** Consolidar a relação entre colaboradores e unidades de gestão.

**Habilidades:** Modelagem de vínculos; parametrização semanal; SQL.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Leitura de coleções persistidas; Relacionamento entre tabelas na consulta.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/lugb_campo/lugb-campo-funcionario-ugb-importer.js:3`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/lugb_campo/lugb-campo-funcionario-ugb-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Metas de produção de campo

**Domínio:** Campo e produtividade.

**Finalidade:** Importar metas de produção para as operações de campo.

**Habilidades:** Metas operacionais; ETL; integração de domínios.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Leitura de coleções persistidas; Relacionamento entre tabelas na consulta.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/lugb_campo/lugb-campo-meta-producao-importer.js:3`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/lugb_campo/lugb-campo-meta-producao-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Meta de qualidade por UGB

**Domínio:** Campo e qualidade.

**Finalidade:** Estruturar referenciais de qualidade por unidade de gestão.

**Habilidades:** Qualidade; modelagem de metas; SQL.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Leitura de coleções persistidas; Agregação na consulta SQL; Relacionamento entre tabelas na consulta.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/lugb_campo/lugb-campo-meta-qualidade-ugb-importer.js:3`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/lugb_campo/lugb-campo-meta-qualidade-ugb-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Composição de metas de campo

**Domínio:** Planejamento de campo.

**Finalidade:** Relacionar jornadas, colaboradores e metas no processamento do campo.

**Habilidades:** Cruzamento de entidades; regra de negócio; períodos e metas.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Leitura de coleções persistidas; Agregação na consulta SQL; Relacionamento entre tabelas na consulta.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/lugb_campo/lugb-campo-metas-importer.js:3`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/lugb_campo/lugb-campo-metas-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## NUGB de campo

**Domínio:** Estrutura operacional de campo.

**Finalidade:** Importar a estrutura NUGB usada nas análises de campo.

**Habilidades:** Dados de referência; consultas parametrizadas; integração.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Leitura de coleções persistidas.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/lugb_campo/lugb-campo-nugb-importer.js:3`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/lugb_campo/lugb-campo-nugb-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Qualidade por funcionário e dia

**Domínio:** Campo e pessoas.

**Finalidade:** Disponibilizar a qualidade na granularidade colaborador/dia.

**Habilidades:** Granularidade analítica; qualidade; parametrização semanal.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Leitura de coleções persistidas; Agregação na consulta SQL; Relacionamento entre tabelas na consulta.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/lugb_campo/lugb-campo-qualidade-funcionario-dia-importer.js:3`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/lugb_campo/lugb-campo-qualidade-funcionario-dia-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Qualidade de campo

**Domínio:** Qualidade agrícola.

**Finalidade:** Consolidar os dados de qualidade das atividades de campo.

**Habilidades:** Qualidade operacional; SQL; integração de fontes.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Leitura de coleções persistidas; Agregação na consulta SQL; Relacionamento entre tabelas na consulta.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_queries/lugb_campo/lugb-campo-qualidade-importer.js:3`, `Agrodan/etl/servers/server-dataware-house/core/sequelize/queries/lugb_campo/lugb-campo-qualidade-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Desdobramento de qualidade

**Domínio:** Qualidade e gestão.

**Finalidade:** Relacionar metas de qualidade e resultados por funcionário/dia.

**Habilidades:** Cruzamento de dados; metas; processamento em lotes.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Leitura de coleções persistidas.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_dwh/lugb_campo/lugb-campo-desdobramento-qualidade.js:3`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Qualidade do packing

**Domínio:** Packing e qualidade.

**Finalidade:** Relacionar inspeções, origem de pallets e dados de qualidade.

**Habilidades:** Rastreabilidade; integração entre tabelas; regras de transformação.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Leitura de coleções persistidas; Cruzamento com registro específico.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_dwh/qualidade-packing-importer.js:3`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Qualidade NUGB no packing

**Domínio:** Packing e rendimento.

**Finalidade:** Cruzar dados de rendimento por ficha/dia para uma visão de qualidade.

**Habilidades:** Cruzamento temporal; indicadores de qualidade; modelos relacionais.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Leitura de coleções persistidas; Cruzamento com registro específico.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_dwh/qualidade-packing-nugb-importer.js:3`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Consolidação LUGB Packing

**Domínio:** Packing e gestão.

**Finalidade:** Reunir qualidade, metas, fazendas, produção e percentuais.

**Habilidades:** Integração de indicadores; camada analítica; múltiplos domínios.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Leitura de coleções persistidas; Cruzamento com registro específico.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_dwh/l-ugb-packing-importer.js:3`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Metas do packing

**Domínio:** Packing e capacidade.

**Finalidade:** Relacionar apontamentos, jornadas e metas da embalagem.

**Habilidades:** Metas; capacidade operacional; relacionamento de entidades.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Leitura de coleções persistidas.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/from_dwh/lugb-packing-metas-importer.js:13`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## APPT e integração Farmlog

**Domínio:** Integração corporativa.

**Finalidade:** Organizar apontamentos e vínculos com colaboradores Farmlog.

**Habilidades:** Oracle driver; integração entre sistemas; persistência em lotes.

**Stack:** Node.js, JavaScript, SQL, Sequelize.

**Sinais da implementação:** Persistência de registros em lote; Leitura de coleções persistidas; Relacionamento entre tabelas na consulta.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/importer/oracledb/ApptImporter.js:13`, `Agrodan/etl/servers/server-dataware-house/core/oracledb/queries/appt-query.js:1`.

**Estado e limite:** Importador/transformação implementado no material local; dependências históricas a contextualizar.

## Movimentação e sentido de acesso

**Domínio:** Catracas, pessoas e operação.

**Finalidade:** Relacionar entradas, saídas e sentido de circulação.

**Habilidades:** Modelagem de eventos; análise temporal.

**Stack:** Node.js, Moment.js, SQL Server, Oracle.

**Sinais da implementação:** Agrupamento de registros; Persistência de registros em lote.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/catracas/processamento/catraca.js:41`, `Agrodan/etl/servers/server-dataware-house/core/importer/from_catracas/CatracasImporter.js:15`, `Agrodan/etl/servers/server-dataware-house/core/catracas/queries/listaRegistros.js:1`.

**Estado e limite:** Indicadores do mesmo pipeline de catracas; não são seis produtos distintos.

## Distribuição horária de acessos

**Domínio:** Catracas, pessoas e operação.

**Finalidade:** Agregar entradas e saídas por faixas de horário.

**Habilidades:** Agregação temporal; distribuição de eventos.

**Stack:** Node.js, Moment.js, SQL Server, Oracle.

**Sinais da implementação:** Agrupamento de registros; Persistência de registros em lote.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/catracas/processamento/catraca.js:41`, `Agrodan/etl/servers/server-dataware-house/core/importer/from_catracas/CatracasImporter.js:15`, `Agrodan/etl/servers/server-dataware-house/core/catracas/queries/listaRegistros.js:1`.

**Estado e limite:** Indicadores do mesmo pipeline de catracas; não são seis produtos distintos.

## Disponibilidade operacional

**Domínio:** Catracas, pessoas e operação.

**Finalidade:** Calcular disponibilidade a partir dos eventos observados.

**Habilidades:** Indicadores de pessoas; regras temporais.

**Stack:** Node.js, Moment.js, SQL Server, Oracle.

**Sinais da implementação:** Agrupamento de registros; Persistência de registros em lote.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/catracas/processamento/catraca.js:41`, `Agrodan/etl/servers/server-dataware-house/core/importer/from_catracas/CatracasImporter.js:15`, `Agrodan/etl/servers/server-dataware-house/core/catracas/queries/listaRegistros.js:1`.

**Estado e limite:** Indicadores do mesmo pipeline de catracas; não são seis produtos distintos.

## Utilização das catracas

**Domínio:** Catracas, pessoas e operação.

**Finalidade:** Examinar utilização e caminhos de entrada e saída.

**Habilidades:** Indicadores de utilização; análise de fluxo.

**Stack:** Node.js, Moment.js, SQL Server, Oracle.

**Sinais da implementação:** Agrupamento de registros; Persistência de registros em lote.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/catracas/processamento/catraca.js:41`, `Agrodan/etl/servers/server-dataware-house/core/importer/from_catracas/CatracasImporter.js:15`, `Agrodan/etl/servers/server-dataware-house/core/catracas/queries/listaRegistros.js:1`.

**Estado e limite:** Indicadores do mesmo pipeline de catracas; não são seis produtos distintos.

## Visitantes e circulação por setor

**Domínio:** Catracas, pessoas e operação.

**Finalidade:** Relacionar acesso com setores e visitantes.

**Habilidades:** Segmentação; dimensões organizacionais.

**Stack:** Node.js, Moment.js, SQL Server, Oracle.

**Sinais da implementação:** Agrupamento de registros; Persistência de registros em lote.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/catracas/processamento/catraca.js:41`, `Agrodan/etl/servers/server-dataware-house/core/importer/from_catracas/CatracasImporter.js:15`, `Agrodan/etl/servers/server-dataware-house/core/catracas/queries/listaRegistros.js:1`.

**Estado e limite:** Indicadores do mesmo pipeline de catracas; não são seis produtos distintos.

## Frequência de pessoas

**Domínio:** Catracas, pessoas e operação.

**Finalidade:** Organizar frequência de visitas e recorrência.

**Habilidades:** Frequência; períodos; analytics operacional.

**Stack:** Node.js, Moment.js, SQL Server, Oracle.

**Sinais da implementação:** Agrupamento de registros; Persistência de registros em lote.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/catracas/processamento/catraca.js:41`, `Agrodan/etl/servers/server-dataware-house/core/importer/from_catracas/CatracasImporter.js:15`, `Agrodan/etl/servers/server-dataware-house/core/catracas/queries/listaRegistros.js:1`.

**Estado e limite:** Indicadores do mesmo pipeline de catracas; não são seis produtos distintos.

## Construtor dinâmico de formulários

**Domínio:** Coleta corporativa.

**Finalidade:** Compor páginas, painéis, linhas e componentes com estado Redux.

**Habilidades:** Modelagem de interfaces; reducers; composição de componentes.

**Stack:** React, Redux, Material UI.

**Sinais da implementação:** .

**Fontes:** `Agrodan/src/redux/reducers/FormBuilder.js:1`, `Agrodan/src/redux/components/FormContainer.js:44`.

**Estado e limite:** Artefatos localizados; extensão funcional e implantação a contextualizar.

## API de formulários e temas

**Domínio:** Coleta corporativa.

**Finalidade:** Organizar consultas e manutenção de formulários por temas.

**Habilidades:** APIs HTTP; DAO; regras de persistência.

**Stack:** Express, Sequelize, SQL.

**Sinais da implementação:** .

**Fontes:** `Agrodan/etl/servers/server-forms/router/rotas/rotas-tot-formulario.js:1`, `Agrodan/etl/servers/server-forms/DAO/TotFormulario.js:4`.

**Estado e limite:** Artefatos localizados; extensão funcional e implantação a contextualizar.

## Setores e subsetores

**Domínio:** Organização corporativa.

**Finalidade:** Modelar a organização da coleta por setor e subsetor.

**Habilidades:** Modelagem relacional; dados de referência; CRUD.

**Stack:** Node.js, Sequelize.

**Sinais da implementação:** .

**Fontes:** `Agrodan/etl/servers/server-forms/DAO/Setor.js:4`, `Agrodan/etl/servers/server-forms/DAO/SubSetor.js:4`.

**Estado e limite:** Artefatos localizados; extensão funcional e implantação a contextualizar.

## Ordens de preenchimento

**Domínio:** Coleta corporativa.

**Finalidade:** Representar ordens e estados de preenchimento.

**Habilidades:** Modelagem de workflow; entidades; schemas.

**Stack:** Sequelize, SQL.

**Sinais da implementação:** .

**Fontes:** `Agrodan/etl/servers/server-forms/models/ordem_preenchimento.js:1`, `Agrodan/etl/servers/server-forms/models/estado_ordem_preenchimento.js:1`.

**Estado e limite:** Modelos presentes; fluxo completo ainda não comprovado.

## Ingestão meteorológica

**Domínio:** Dados ambientais.

**Finalidade:** Coletar e organizar dados de estações meteorológicas.

**Habilidades:** Ingestão HTTP; normalização JSON; observações temporais.

**Stack:** Node.js, Sequelize.

**Sinais da implementação:** .

**Fontes:** `Agrodan/etl/servers/server-estacao-meteorologica/services/estacao-meteorologica.js:1`, `Agrodan/etl/servers/server-estacao-meteorologica/models/dados_meteorologicos.js:1`.

**Estado e limite:** Artefatos localizados; extensão funcional e implantação a contextualizar.

## Agenda de rotinas operacionais

**Domínio:** Operação de dados.

**Finalidade:** Definir rotinas periódicas de importação e meteorologia.

**Habilidades:** Agendamento; orquestração; integração de jobs.

**Stack:** Agenda, MongoDB, Agendash.

**Sinais da implementação:** Registro de tarefas agendadas; Definição de periodicidade.

**Fontes:** `Agrodan/etl/servers/server-agenda/index.js:1`.

**Estado e limite:** Agendamentos definidos; montagem do serviço comentada no bootstrap consultado.

## Reestimativa e datas reais de colheita

**Domínio:** Planejamento agrícola.

**Finalidade:** Representar integração com reestimativas e datas de colheita.

**Habilidades:** Integração de processos; planejamento; modelagem agrícola.

**Stack:** Node.js, SQL, Sequelize.

**Sinais da implementação:** .

**Fontes:** `Agrodan/etl/servers/server-agenda/tarefas/farmlog/reestimativa-ler-datas-reais-colheita.js:1`, `Agrodan/etl/servers/server-agenda/tarefas/farmlog/reestimativa-gravar-total-produzido.js:1`.

**Estado e limite:** Rotinas e modelos presentes; ativação comentada na agenda.

## Validação e rastreabilidade de erros

**Domínio:** Qualidade dos dados.

**Finalidade:** Validar campos e organizar registros de erros na integração.

**Habilidades:** Validação de dados; regras; rastreabilidade.

**Stack:** JavaScript, Sequelize.

**Sinais da implementação:** Persistência de registros em lote.

**Fontes:** `Agrodan/etl/servers/server-dataware-house/core/validation/core-validation.js:1`, `Agrodan/etl/servers/server-dataware-house/core/validation/validators/campo-obrigatorio-validator.js:3`.

**Estado e limite:** Artefatos localizados; extensão funcional e implantação a contextualizar.

## Ordens de serviço mobile

**Domínio:** Operações de campo.

**Finalidade:** Organizar ordens de serviço e seus dados na aplicação SIAgro.

**Habilidades:** Desenvolvimento mobile; regras de negócio; interfaces operacionais.

**Stack:** React Native, Expo.

**Sinais da implementação:** Relacionamento entre tabelas na consulta.

**Fontes:** `Agrodan/sia_app/Modulos/SIAgro/Telas/OrdemServico/OrdemServico.js:33`, `Agrodan/sia_app/Modulos/SIAgro/Objetos/OrdemServico.js:4`.

**Estado e limite:** Artefatos localizados; extensão funcional e implantação a contextualizar.

## Apontamentos mobile

**Domínio:** Operações de campo.

**Finalidade:** Registrar apontamentos e dados da atividade no aplicativo.

**Habilidades:** Coleta mobile; modelagem de registros; interação.

**Stack:** React Native, Expo.

**Sinais da implementação:** Armazenamento local no aplicativo.

**Fontes:** `Agrodan/sia_app/Modulos/SIAgro/Telas/Apontamento/Apontamento.js:27`, `Agrodan/sia_app/Modulos/SIAgro/Objetos/Apontamento.js:5`.

**Estado e limite:** Artefatos localizados; extensão funcional e implantação a contextualizar.

## Colaboradores nos apontamentos

**Domínio:** Pessoas e campo.

**Finalidade:** Associar colaboradores ao registro operacional.

**Habilidades:** Modelagem de vínculos; componentes mobile; cadastros.

**Stack:** React Native.

**Sinais da implementação:** Armazenamento local no aplicativo.

**Fontes:** `Agrodan/sia_app/Modulos/SIAgro/Telas/Apontamento/AdicionarColaborador.js:33`, `Agrodan/sia_app/Modulos/SIAgro/Objetos/Funcionario.js:8`.

**Estado e limite:** Artefatos localizados; extensão funcional e implantação a contextualizar.

## Qualidade mobile

**Domínio:** Qualidade agrícola.

**Finalidade:** Capturar informações de qualidade no fluxo de apontamento.

**Habilidades:** Captura de qualidade; modelagem de domínio; formulários mobile.

**Stack:** React Native, Expo.

**Sinais da implementação:** Armazenamento local no aplicativo.

**Fontes:** `Agrodan/sia_app/Modulos/SIAgro/Telas/Apontamento/Qualidade.js:33`, `Agrodan/sia_app/Modulos/SIAgro/Objetos/Qualidade.js:5`.

**Estado e limite:** Artefatos localizados; extensão funcional e implantação a contextualizar.

## Metas e UGBs nas ordens

**Domínio:** Gestão de campo.

**Finalidade:** Representar metas e unidades de gestão no fluxo de ordens de serviço.

**Habilidades:** Modelagem operacional; componentes; contexto da ordem.

**Stack:** React Native.

**Sinais da implementação:** Armazenamento local no aplicativo.

**Fontes:** `Agrodan/sia_app/Modulos/SIAgro/Telas/OrdemServico/Metas.js:25`, `Agrodan/sia_app/Modulos/SIAgro/Telas/OrdemServico/Ugbs.js:26`.

**Estado e limite:** Artefatos localizados; extensão funcional e implantação a contextualizar.

## Dashboard operacional mobile

**Domínio:** Indicadores.

**Finalidade:** Apresentar indicadores e gráficos na aplicação mobile.

**Habilidades:** Visualização de dados; gráficos; experiência mobile.

**Stack:** React Native, Victory Native.

**Sinais da implementação:** Armazenamento local no aplicativo.

**Fontes:** `Agrodan/sia_app/Modulos/SIAgro/Telas/Dashboard/DashBoard.js:23`, `Agrodan/sia_app/Modulos/SIAgro/Telas/Graficos.js:16`.

**Estado e limite:** Artefatos localizados; extensão funcional e implantação a contextualizar.

## Persistência local reutilizável

**Domínio:** Engenharia mobile.

**Finalidade:** Organizar operações de armazenamento local para objetos do aplicativo.

**Habilidades:** Persistência local; abstração de CRUD; reuso.

**Stack:** React Native, AsyncStorage.

**Sinais da implementação:** Armazenamento local no aplicativo.

**Fontes:** `Agrodan/sia_app/Modulos/SIAgro/Objetos/ObjetoPadrao.js:5`.

**Estado e limite:** Artefatos localizados; extensão funcional e implantação a contextualizar.
