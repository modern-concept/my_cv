"""Specific case narratives and skill provenance for the extended CV draft."""
from pathlib import Path
import re

def build_details(root, projects, utilibox):
    import json
    branch_audit=json.loads((Path(__file__).resolve().parents[1]/'sia-branch-cases.json').read_text(encoding='utf-8'))
    agro=root/'Agrodan'
    core='etl/servers/server-dataware-house/core/'
    importer=core+'importer/'
    # Each row describes a module/flow of SIA, not an independent product.
    rows=[
      ('Apontamentos de produção','Produção agrícola','Integrar registros de produção para análise operacional','from_queries/apontamento-producao-importer.js','ETL SQL; persistência em lote; modelagem de apontamentos'),
      ('Jornadas operacionais','Pessoas e capacidade','Consolidar jornadas para relacionar tempo e operação','from_queries/jornada-importer.js','Integração de bases; jornadas; transformações SQL'),
      ('Inspeções de UGB','Qualidade','Normalizar inspeções e evitar duplicação pelo identificador do registro','from_queries/inspecoes-ugb-importer.js','Deduplicação; normalização; inspeções; ETL'),
      ('Origem de pallets','Packing e rastreabilidade','Consolidar a origem de pallets para relacionar produção e inspeções','from_queries/pallet-origem-importer.js','Rastreabilidade de dados; integração SQL; persistência'),
      ('Metas de produção','Gestão de produção','Importar metas para comparar a operação com seus referenciais','from_queries/meta-producao-importer.js','Modelagem de metas; SQL; integração de fontes'),
      ('Percentuais de metas','Gestão de desempenho','Consolidar percentuais relacionados às metas de produção','from_queries/percentuais-meta-importer.js','Indicadores; modelagem de dados; ETL'),
      ('Rendimento por ficha e dia','Rendimento e packing','Integrar rendimento diário por ficha','from_queries/rendimento-ficha-dia-importer.js','Granularidade temporal; indicadores de rendimento; SQL'),
      ('Atualização de rendimento','Rendimento e packing','Manter uma segunda leitura de rendimentos para cruzamentos posteriores','from_queries/rendimento-ficha-dia-atualizado-importer.js','Integração de versões de dados; persistência; modelagem temporal'),
      ('Total produzido','Produção','Disponibilizar totais produzidos no data warehouse','from_queries/total-produzido-importer.js','Agregação SQL; carga de dados; análise operacional'),
      ('Produção por fazenda','Gestão agrícola','Separar os totais de produção pela dimensão fazenda','from_queries/total-produzido-fazenda-importer.js','Dimensões analíticas; agregação; integração SQL'),
      ('UGBs e fazendas','Cadastros e organização','Integrar a relação entre unidades de gestão e fazendas','from_queries/ugb-fazenda-importer.js','Modelagem organizacional; dados de referência; ETL'),
      ('Embalagem por UGB','Packing','Consolidar registros de embalagem ligados à unidade de gestão','from_queries/l-ugb-embalagem-importer.js','ETL; períodos; embalagem; persistência relacional'),
      ('Embalagem diária','Packing','Disponibilizar a granularidade diária dos registros de embalagem','from_queries/l-ugb-embalagem-diario-importer.js','Granularidade diária; normalização; indicadores operacionais'),
      ('Base de LUGB Campo','Operações de campo','Estruturar a base para análises das operações de campo','from_queries/lugb_campo/lugb-campo-base-importer.js','Camada analítica; SQL; cargas reutilizáveis'),
      ('Vínculo funcionário–UGB','Pessoas e campo','Consolidar a relação entre colaboradores e unidades de gestão','from_queries/lugb_campo/lugb-campo-funcionario-ugb-importer.js','Modelagem de vínculos; parametrização semanal; SQL'),
      ('Metas de produção de campo','Campo e produtividade','Importar metas de produção para as operações de campo','from_queries/lugb_campo/lugb-campo-meta-producao-importer.js','Metas operacionais; ETL; integração de domínios'),
      ('Meta de qualidade por UGB','Campo e qualidade','Estruturar referenciais de qualidade por unidade de gestão','from_queries/lugb_campo/lugb-campo-meta-qualidade-ugb-importer.js','Qualidade; modelagem de metas; SQL'),
      ('Composição de metas de campo','Planejamento de campo','Relacionar jornadas, colaboradores e metas no processamento do campo','from_queries/lugb_campo/lugb-campo-metas-importer.js','Cruzamento de entidades; regra de negócio; períodos e metas'),
      ('NUGB de campo','Estrutura operacional de campo','Importar a estrutura NUGB usada nas análises de campo','from_queries/lugb_campo/lugb-campo-nugb-importer.js','Dados de referência; consultas parametrizadas; integração'),
      ('Qualidade por funcionário e dia','Campo e pessoas','Disponibilizar a qualidade na granularidade colaborador/dia','from_queries/lugb_campo/lugb-campo-qualidade-funcionario-dia-importer.js','Granularidade analítica; qualidade; parametrização semanal'),
      ('Qualidade de campo','Qualidade agrícola','Consolidar os dados de qualidade das atividades de campo','from_queries/lugb_campo/lugb-campo-qualidade-importer.js','Qualidade operacional; SQL; integração de fontes'),
      ('Desdobramento de qualidade','Qualidade e gestão','Relacionar metas de qualidade e resultados por funcionário/dia','from_dwh/lugb_campo/lugb-campo-desdobramento-qualidade.js','Cruzamento de dados; metas; processamento em lotes'),
      ('Qualidade do packing','Packing e qualidade','Relacionar inspeções, origem de pallets e dados de qualidade','from_dwh/qualidade-packing-importer.js','Rastreabilidade; integração entre tabelas; regras de transformação'),
      ('Qualidade NUGB no packing','Packing e rendimento','Cruzar dados de rendimento por ficha/dia para uma visão de qualidade','from_dwh/qualidade-packing-nugb-importer.js','Cruzamento temporal; indicadores de qualidade; modelos relacionais'),
      ('Consolidação LUGB Packing','Packing e gestão','Reunir qualidade, metas, fazendas, produção e percentuais','from_dwh/l-ugb-packing-importer.js','Integração de indicadores; camada analítica; múltiplos domínios'),
      ('Metas do packing','Packing e capacidade','Relacionar apontamentos, jornadas e metas da embalagem','from_dwh/lugb-packing-metas-importer.js','Metas; capacidade operacional; relacionamento de entidades'),
      ('APPT e integração Farmlog','Integração corporativa','Organizar apontamentos e vínculos com colaboradores Farmlog','oracledb/ApptImporter.js','Oracle driver; integração entre sistemas; persistência em lotes'),
    ]
    modules=[]
    def add(title,domain,goal,paths,skills,stack,status='Código de módulo localizado'):
        sources=[]
        signals=[]
        allpaths=list(paths)
        # Include directly required SQL query modules as concrete business evidence.
        for rel in paths:
            path=agro/rel
            text=path.read_text(encoding='utf-8',errors='replace')
            for required in re.findall(r"require\(['\"]([^'\"]*queries/[^'\"]+)['\"]\)",text):
                candidate=(path.parent/required).with_suffix('.js').resolve()
                if candidate.is_file() and candidate.is_relative_to(agro.resolve()):
                    reference=candidate.relative_to(agro.resolve()).as_posix()
                    if reference not in allpaths: allpaths.append(reference)
        for rel in allpaths:
            p=agro/rel
            if not p.is_file(): raise FileNotFoundError(p)
            text=p.read_text(encoding='utf-8',errors='replace')
            # Capture anchors and structural evidence, excluding connection values.
            match=re.search(r'(?m)^.*(?:class\s+\w+|export\s+(?:default|class|const|function)|const\s+\w+\s*=\s*\(|function\s+\w+).*$',text)
            line=text[:match.start()].count('\n')+1 if match else 1
            sources.append({'path':'Agrodan/'+rel,'line':line})
            active=re.sub(r'/\*[\s\S]*?\*/','',text)
            active=re.sub(r'(?m)^\s*//.*$','',active)
            markers={'bulkCreate':'Persistência de registros em lote','findAll':'Leitura de coleções persistidas','findOne':'Cruzamento com registro específico','groupBy':'Agrupamento de registros','GROUP BY':'Agregação na consulta SQL','JOIN':'Relacionamento entre tabelas na consulta','AsyncStorage':'Armazenamento local no aplicativo','createTable':'Definição de estrutura relacional','agenda.define':'Registro de tarefas agendadas','agenda.every':'Definição de periodicidade'}
            for token,description in markers.items():
                if token in active and description not in signals: signals.append(description)
        modules.append({'title':title,'domain':domain,'objective':goal,'sources':sources,'skills':skills.split('; '),'stack':stack,'status':status,
          'implementationSignals':signals,
          'cvText':f'{goal}. A frente evidencia {skills.lower()}.',
          'result':'Artefatos de implementação encontrados nos arquivos indicados; operação, cobertura e resultado medido a contextualizar.'})
    for title,domain,goal,path,skills in rows:
        add(title,domain,goal,[importer+path],skills,['Node.js','JavaScript','SQL','Sequelize'],'Importador/transformação implementado no material local; dependências históricas a contextualizar')
    cat=core+'catracas/processamento/catraca.js'
    catmodules=[('Movimentação e sentido de acesso','Relacionar entradas, saídas e sentido de circulação','Modelagem de eventos; análise temporal'),('Distribuição horária de acessos','Agregar entradas e saídas por faixas de horário','Agregação temporal; distribuição de eventos'),('Disponibilidade operacional','Calcular disponibilidade a partir dos eventos observados','Indicadores de pessoas; regras temporais'),('Utilização das catracas','Examinar utilização e caminhos de entrada e saída','Indicadores de utilização; análise de fluxo'),('Visitantes e circulação por setor','Relacionar acesso com setores e visitantes','Segmentação; dimensões organizacionais'),('Frequência de pessoas','Organizar frequência de visitas e recorrência','Frequência; períodos; analytics operacional')]
    for title,goal,skills in catmodules:
        add(title,'Catracas, pessoas e operação',goal,[cat,importer+'from_catracas/CatracasImporter.js'],skills,['Node.js','Moment.js','SQL Server','Oracle'],'Indicadores do mesmo pipeline de catracas; não são seis produtos distintos')
    extra=[
      ('Construtor dinâmico de formulários','Coleta corporativa','Compor páginas, painéis, linhas e componentes com estado Redux',['src/redux/reducers/FormBuilder.js','src/redux/components/FormContainer.js'],'Modelagem de interfaces; reducers; composição de componentes',['React','Redux','Material UI']),
      ('API de formulários e temas','Coleta corporativa','Organizar consultas e manutenção de formulários por temas',['etl/servers/server-forms/router/rotas/rotas-tot-formulario.js','etl/servers/server-forms/DAO/TotFormulario.js'],'APIs HTTP; DAO; regras de persistência',['Express','Sequelize','SQL']),
      ('Setores e subsetores','Organização corporativa','Modelar a organização da coleta por setor e subsetor',['etl/servers/server-forms/DAO/Setor.js','etl/servers/server-forms/DAO/SubSetor.js'],'Modelagem relacional; dados de referência; CRUD',['Node.js','Sequelize']),
      ('Ordens de preenchimento','Coleta corporativa','Representar ordens e estados de preenchimento',['etl/servers/server-forms/models/ordem_preenchimento.js','etl/servers/server-forms/models/estado_ordem_preenchimento.js'],'Modelagem de workflow; entidades; schemas',['Sequelize','SQL']),
      ('Ingestão meteorológica','Dados ambientais','Coletar e organizar dados de estações meteorológicas',['etl/servers/server-estacao-meteorologica/services/estacao-meteorologica.js','etl/servers/server-estacao-meteorologica/models/dados_meteorologicos.js'],'Ingestão HTTP; normalização JSON; observações temporais',['Node.js','Sequelize']),
      ('Agenda de rotinas operacionais','Operação de dados','Definir rotinas periódicas de importação e meteorologia',['etl/servers/server-agenda/index.js'],'Agendamento; orquestração; integração de jobs',['Agenda','MongoDB','Agendash']),
      ('Reestimativa e datas reais de colheita','Planejamento agrícola','Representar integração com reestimativas e datas de colheita',['etl/servers/server-agenda/tarefas/farmlog/reestimativa-ler-datas-reais-colheita.js','etl/servers/server-agenda/tarefas/farmlog/reestimativa-gravar-total-produzido.js'],'Integração de processos; planejamento; modelagem agrícola',['Node.js','SQL','Sequelize']),
      ('Validação e rastreabilidade de erros','Qualidade dos dados','Validar campos e organizar registros de erros na integração',['etl/servers/server-dataware-house/core/validation/core-validation.js','etl/servers/server-dataware-house/core/validation/validators/campo-obrigatorio-validator.js'],'Validação de dados; regras; rastreabilidade',['JavaScript','Sequelize']),
      ('Ordens de serviço mobile','Operações de campo','Organizar ordens de serviço e seus dados na aplicação SIAgro',['sia_app/Modulos/SIAgro/Telas/OrdemServico/OrdemServico.js','sia_app/Modulos/SIAgro/Objetos/OrdemServico.js'],'Desenvolvimento mobile; regras de negócio; interfaces operacionais',['React Native','Expo']),
      ('Apontamentos mobile','Operações de campo','Registrar apontamentos e dados da atividade no aplicativo',['sia_app/Modulos/SIAgro/Telas/Apontamento/Apontamento.js','sia_app/Modulos/SIAgro/Objetos/Apontamento.js'],'Coleta mobile; modelagem de registros; interação',['React Native','Expo']),
      ('Colaboradores nos apontamentos','Pessoas e campo','Associar colaboradores ao registro operacional',['sia_app/Modulos/SIAgro/Telas/Apontamento/AdicionarColaborador.js','sia_app/Modulos/SIAgro/Objetos/Funcionario.js'],'Modelagem de vínculos; componentes mobile; cadastros',['React Native']),
      ('Qualidade mobile','Qualidade agrícola','Capturar informações de qualidade no fluxo de apontamento',['sia_app/Modulos/SIAgro/Telas/Apontamento/Qualidade.js','sia_app/Modulos/SIAgro/Objetos/Qualidade.js'],'Captura de qualidade; modelagem de domínio; formulários mobile',['React Native','Expo']),
      ('Metas e UGBs nas ordens','Gestão de campo','Representar metas e unidades de gestão no fluxo de ordens de serviço',['sia_app/Modulos/SIAgro/Telas/OrdemServico/Metas.js','sia_app/Modulos/SIAgro/Telas/OrdemServico/Ugbs.js'],'Modelagem operacional; componentes; contexto da ordem',['React Native']),
      ('Dashboard operacional mobile','Indicadores','Apresentar indicadores e gráficos na aplicação mobile',['sia_app/Modulos/SIAgro/Telas/Dashboard/DashBoard.js','sia_app/Modulos/SIAgro/Telas/Graficos.js'],'Visualização de dados; gráficos; experiência mobile',['React Native','Victory Native']),
      ('Persistência local reutilizável','Engenharia mobile','Organizar operações de armazenamento local para objetos do aplicativo',['sia_app/Modulos/SIAgro/Objetos/ObjetoPadrao.js'],'Persistência local; abstração de CRUD; reuso',['React Native','AsyncStorage']),
    ]
    for title,domain,goal,paths,skills,stack in extra:
        status='Artefatos localizados; extensão funcional e implantação a contextualizar'
        if 'Reestimativa' in title: status='Rotinas e modelos presentes; ativação comentada na agenda'
        if 'Ordens de preenchimento' in title: status='Modelos presentes; fluxo completo ainda não comprovado'
        if 'Agenda' in title: status='Agendamentos definidos; montagem do serviço comentada no bootstrap consultado'
        add(title,domain,goal,paths,skills,stack,status)

    def case(title,context,problem,implementation,skills,sources,text,limit):
        return dict(title=title,context=context,problem=problem,implementation=implementation,skills=skills,sources=sources,text=text,limit=limit)
    def topic(id,title,intro,text,cases,flow): return dict(id=id,title=title,intro=intro,text=text,cases=cases,flow=flow)
    topics=[
      topic('agentes','Sistemas multiagentes, coordenação e decisões',
        'Dois tipos de arquitetura aparecem concretamente: um conselho de funções especializadas no planejamento e um ensemble de sinais com votação na pesquisa quantitativa. As integrações LLM do produto de planejamento acrescentam uma camada de geração e validação de propostas.',
        ['Trabalhei com decomposição de decisões em papéis especializados e mecanismos de coordenação. No Planejamento Xavier, um conselho de agentes examina estratégia, execução, risco, aprendizado, integridade e mentoria, produzindo manifestações com evidências, confiança, pesos e referências às entidades do plano.',
         'Explorei também políticas multiagentes para pesquisa quantitativa no TraderMind, combinando votos de indicadores e fontes externas. A seleção de agentes e de regras de concordância utiliza simulated annealing, com calibração e avaliação posterior em janelas separadas.',
         'Essa experiência envolve contratos de comunicação, tratamento de divergências, quórum, abstinência e rastreabilidade da decisão. No planejamento, propostas produzidas por IA são normalizadas e validadas contra as entidades reais antes de virar operações de replanejamento.'],
        [case('Conselho de seis agentes — Planejamento Xavier','Projeto independente; vínculo individual a contextualizar','Relacionar prioridades, capacidade, execução e consistência sem perder a origem de cada recomendação',
          ['Estratégico: identifica impacto sistêmico e áreas prioritárias sem objetivos.', 'Execução: observa tarefas atrasadas e tarefas sem vínculo com metas; considera capacidade semanal.', 'Risco: utiliza riscos cadastrados e sobrecarga; a concentração de alertas aparece como proxy documentado quando necessário.', 'Aprendizado: examina registros e pendências de aprendizagem/experimentos.', 'Integridade: identifica associações e dados incompletos, podendo sugerir patches.', 'Mentoria: contextualiza divergências e pontos de reflexão.', 'Cada manifestação carrega claim, evidence, confidence, polarity, weight, nodeIds e suggestedPatch opcional.', 'Conflitos são resolvidos por prioridade do agente, confiança, peso e desempate determinístico; ações têm vínculo com as manifestações de origem.'],
          ['Arquitetura por papéis','Contratos tipados','Coordenação de agentes','Resolução de conflitos','Explicabilidade e provenance'],
          ['planejamentoxavier/supabase/functions/_shared/brain/council.ts'],
          'Implementei um conselho de seis agentes especializados para apoiar planejamento e replanejamento, com evidências por recomendação, resolução determinística de conflitos e geração de ações rastreáveis.',
          'Os agentes deste arquivo são funções puras por regras sobre um snapshot. A integração LLM é outra camada; não chamar cada agente de LLM autônomo.'),
         case('Ensemble de agentes financeiros — TraderMind','Pesquisa quantitativa; ambiente demo documentado','Transformar sinais heterogêneos em uma política verificável',
          ['Sinais de RSI, CCI, Williams, Bollinger, posição de preço e médias são combinados com Nasdaq, ETH, MFI, MACD e funding.', 'A política BTC consultada tem doze sinais/agentes, votos ternários e regras de concordância e mínimo de agentes ativos.', 'A busca escolhe seguir, inverter ou ignorar cada sinal e ajusta quórum/concordância.', 'O campeão é escolhido antes do OOS final; a política registra sua origem e congelamento.', 'Fontes externas usam merge_asof backward, tolerância de atualização e atraso de publicação; indisponibilidade externa gera neutralidade no fluxo documentado.'],
          ['Ensembles','Votação e quórum','Simulated annealing','Validação temporal','Alinhamento de dados'],
          ['mt5/TraderMind/scripts/btc_multiagent_policy.py','mt5/TraderMind/scripts/experiment_btc_multiagent_sa.py','mt5/TraderMind/scripts/experiment_gold_multiagent_sa.py'],
          'Estruturei experimentos de políticas multiagentes com votação de sinais, quórum e otimização por simulated annealing, organizando calibração, validação temporal e teste fora da amostra.',
          'São agentes de sinais por regras, não LLMs negociando entre si. Resultados financeiros não foram verificados neste levantamento.')],
        ['Contexto e estado','Papéis/sinais especializados','Manifestações e evidências','Conflitos ou votação','Proposta/política','Validação e ação']),
      topic('ia','Engenharia de IA generativa e assistentes de domínio',
        'As evidências vão da composição do prompt à integração no fluxo do produto: contexto, contrato de resposta, validação, recuperação de falha e operação supervisionada.',
        ['Integrei modelos de linguagem a aplicações de educação, planejamento e relacionamento comercial, construindo contextos específicos do domínio e saídas estruturadas para uso pela aplicação.',
         'No planejamento, a camada de IA reúne seleção de provedores, limites de tempo, validação de respostas e sinais de saúde por provedor/tarefa. As propostas de revisão precisam respeitar a árvore real de objetivos, metas, estratégias e atividades.',
         'No CRM, combinei geração com um motor de regras e ações explícitas de resposta, esclarecimento, agendamento, encerramento e encaminhamento humano. O histórico e as perguntas anteriores alimentam o contexto para reduzir repetição e apoiar continuidade.'],
        [case('Motor compartilhado de IA — Planejamento Xavier','Projeto de planejamento','Manter chamadas de IA úteis quando há latência, erro ou resposta fora do contrato',
          ['Abstração de provedores e capacidades json, text e grounded_search.', 'Seleção de Gemini, DeepSeek, OpenAI e APIs compatíveis conforme configuração; presença de adaptador não prova uso de todos em produção.', 'Orçamento global de tempo e teto por tentativa; validação pode rejeitar JSON e permitir tentar outro provedor.', 'Saúde com sucesso, latência, falhas consecutivas, pausa temporária de provedor e qualidade por tarefa.', 'Para a busca fundamentada, preserva fontes e a ligação de trechos aos índices das fontes.'],
          ['Abstração de provedores','Resiliência de APIs','Validação de saída','Grounding com fontes','Telemetria de chamadas'],
          ['planejamentoxavier/supabase/functions/_shared/ai/engine.ts','planejamentoxavier/supabase/functions/_shared/llm_client.ts'],
          'Desenvolvi uma camada compartilhada de integração de IA com adaptação de provedores, respostas estruturadas, validação, orçamento de tempo e tratamento de falhas por tarefa.',
          'Código de roteamento não comprova SLA, custo otimizado ou operação em escala. Grounded search não equivale automaticamente a RAG vetorial.'),
         case('Revisão de planos com IA e regras','Planejamento Xavier','Converter sugestões em mudanças coerentes com um plano existente',
          ['Contexto autorizado contém IDs reais, fatos, capacidade, diagnóstico e decisões anteriores.', 'O contrato compara manter, simplificar, ajustar estratégia, pedir informação ou rodar experimento.', 'Normalização transforma o retorno em operações, dependências, ocorrências afetadas e acompanhamento.', 'Operações incluem expected_updated_at, fingerprints de contexto, preservação de objetivos e issues de validação.'],
          ['Context engineering','Modelagem de operações','Validação referencial','Gestão de contexto','Replanejamento'],
          ['planejamentoxavier/supabase/functions/_shared/brain/councilReviewProposal.ts'],
          'Modelei propostas de revisão assistidas por IA com validação de referências, alternativas, operações e acompanhamento, preservando o vínculo das mudanças com o plano real.',
          'Descrever o mecanismo presente; autonomia e eficácia comportamental não foram medidas.'),
         case('Planejamento pedagógico assistido — ClassPlanner','Educação','Transformar dados de aula em uma proposta pedagógica estruturada',
          ['Prompt combina turma, disciplina, contexto, duração, recursos, avaliação e habilidades BNCC.', 'Instrução de domínio pede objetivos, metodologia por etapas, recursos e avaliação em JSON.', 'Backend chama GoogleGenAI, extrai o texto e tenta converter a resposta para JSON.', 'Controllers e persistência integram a geração à aplicação web.'],
          ['Integração Gemini','Prompts de domínio','Saída estruturada','Backend de produto','Modelagem pedagógica'],
          ['ClassPlanner/backend/src/llm/gemini.js','ClassPlanner/backend/src/controllers/controller.plan.js'],
          'Integrei geração de planos de aula com Gemini a uma aplicação web, usando contexto pedagógico, referências BNCC e saída estruturada para objetivos, metodologia e avaliação.',
          'Parsing JSON não é validação completa de schema; existem demos e inconsistências no módulo. Não afirmar alinhamento pedagógico ou qualidade validada.'),
         case('CRM conversacional híbrido — Instagram Conversion CRM','Produto e vendas','Apoiar decisões conversacionais com histórico e alternativas de ação',
          ['Motor SPIN por regras calcula o fallback antes da chamada ao modelo.', 'Contexto inclui etapa atual, últimas mensagens e perguntas já feitas.', 'Retorno é normalizado para reply, schedule, handoff, exit ou clarify, com motivo e confiança.', 'Há até quatro tentativas com espera exponencial e retorno para regras quando falta chave ou a chamada falha.'],
          ['Stateful conversation','Fallback determinístico','Normalização de ações','Retries','Encaminhamento humano'],
          ['instagram-conversion-crm/src/gemini-spin.js','instagram-conversion-crm/src/spin-decision-engine.js'],
          'Construí um fluxo conversacional híbrido de IA e regras, com memória de interação, contrato de ações, tratamento de falhas e encaminhamento humano.',
          'SDK e configuração dependem de outro projeto local; ganho de conversão, modelo disponível e operação real não foram verificados.')],
        ['Entrada do usuário','Contexto autorizado','Modelo/provedor','Resposta estruturada','Validação e fallback','Operação do produto']),
      topic('ml','Machine Learning, seleção de atributos e pesquisa do doutorado',
        'O EFS-AHP constitui um case de pesquisa ligado ao doutorado. A trajetória inclui comparação de métodos, seleção de atributos e avaliação experimental, além de pesquisa de séries temporais no TraderMind.',
        ['Na pesquisa EFS-AHP vinculada ao doutorado profissional em Engenharia de Software, explorei seleção de atributos com algoritmos evolutivos e AHP, articulando qualidade preditiva, dimensionalidade e custo computacional.',
         'Organizei experimentos, métodos de comparação e análises estatísticas com Python, JavaScript e Jupyter. O acervo inclui Random Forest, LASSO, PCA, t-SNE e UMAP em papéis distintos de modelagem, seleção e representação de dados.',
         'Em pesquisa quantitativa, explorei classificadores e modelos com engenharia de atributos, pipelines de inferência e avaliação temporal. A descrição dos resultados deve identificar o experimento, a janela de dados e o critério de seleção correspondente.'],
        [case('EFS-AHP — framework de pesquisa','Doutorado confirmado por Danillo','Escolher subconjuntos de atributos e conciliar critérios de avaliação',
          ['Rotinas de busca evolutiva e avaliação de subconjuntos.', 'Julgamentos e pesos AHP para estruturar prioridades entre alternativas.', 'Três conjuntos de experimentos, scripts auxiliares e notebooks estatísticos.', 'Comparações com métodos de seleção/modelagem e redução dimensional.', 'Formação atual relaciona a tese a bases de irrigação/Kc, calibres de manga e produtividade; especificar quais aparecem em cada experimento.'],
          ['Feature selection','Computação evolutiva','AHP','Desenho experimental','Estatística e avaliação de modelos'],
          ['[EFS-AHP]/Experimento 1/[AG].js','[EFS-AHP]/Experimento 1/[AHP].js','[EFS-AHP]/Experimento 3/Arquivos/[EFS_AHP]random_forest.py','[EFS-AHP]/Estatísticas/[ESTATÍSTICA]EXPERIMENTO 1.ipynb'],
          'Desenvolvi a pesquisa EFS-AHP no doutorado, combinando seleção de atributos, algoritmos evolutivos e decisão multicritério, com comparação de alternativas de ML e análise experimental de desempenho, dimensionalidade e custo.',
          'Titulação, publicações, métricas e significância final precisam de confirmação. Métodos de redução dimensional não devem ser apresentados como todos equivalentes a seletores de atributos.'),
         case('TraderMind — do experimento à inferência','Pesquisa quantitativa','Organizar dados, modelos e políticas para avaliação e uso por API',
          ['Acervo de notebooks e scripts com pandas, NumPy, scikit-learn, boosting e bibliotecas de deep learning.', 'Features e dados históricos alimentam estudos e experimentos temporais.', 'API Flask e conector Python MetaTrader5 aproximam pesquisa, inferência e ambiente demo.', 'Scripts específicos controlam janela de calibração e avaliação fora da amostra; exemplos antigos de TPOT/PCA usam split aleatório.'],
          ['Engenharia de atributos','Modelos tabulares','Pipelines de pesquisa','Validação temporal','Inferência e integração'],
          ['mt5/TraderMind/serve.py','mt5/TraderMind/connector/bot.py','mt5/TraderMind/scripts/btc_multiagent_policy.py'],
          'Estruturei experimentos quantitativos e componentes de inferência, conectando preparação de dados, avaliação de modelos e políticas a uma API e ao terminal MetaTrader5.',
          'Não generalizar validação temporal para todo notebook nem afirmar retorno financeiro comprovado.')],
        ['Base e hipótese','Atributos e alternativas','Busca/modelagem','Critérios e baselines','Avaliação experimental','Resultados por experimento']),
      topic('visao','Visão computacional, treinamento e computação visual',
        'Há um ciclo mais amplo do que chamar um detector: eventos de vídeo, recortes, revisão de exemplos, preparação de dataset, treinamento de classificador e estabilização temporal; em outra frente, inferência de pose no browser e renderização.',
        ['Construí componentes de visão computacional para transformar vídeo em detecções, eventos e alertas, combinando inferência, tratamento temporal e persistência de estado.',
         'No DVR Person Alert, o material inclui coleta/revisão de exemplos e um fluxo de treinamento supervisionado de classificação a partir de um modelo pré-treinado. A estabilização entre frames e a fila persistente de notificações conectam o modelo a uma operação acompanhável.',
         'Em Mocap e protótipos de esqueleto, integrei modelos de estimação de pose no navegador à visualização de keypoints, suavização temporal e recursos 3D, explorando captura de movimento e interação.'],
        [case('DVR — feedback, dataset e treinamento','Projeto de monitoramento','Adaptar classificação ao contexto das câmeras e coletar exemplos revisados',
          ['Detecção produz candidatos e recortes; a revisão no dashboard/Telegram pode alimentar classes do dataset.', 'prepare_dataset separa treino/validação por classe com embaralhamento determinístico.', 'uvinha_training.py chama YOLO(args.base_model).train com pretrained=True, callbacks por época e parâmetros de treino.', 'O script registra status/métricas e copia o melhor checkpoint para o modelo de classificação.', 'TemporalIdentityTracker combina posição, IoU, observações e votação temporal; outbox persiste alertas pendentes.'],
          ['Coleta e rotulagem','Treinamento supervisionado','Transfer learning','Dataset split','Checkpoint e callbacks','Processamento temporal','Confiabilidade operacional'],
          ['DvrPersonAlert/uvinha_training.py','DvrPersonAlert/detection_reviews.py','DvrPersonAlert/temporal_identity.py','DvrPersonAlert/telegram_outbox.py','DvrPersonAlert/dvr_person_alert.py'],
          'Implementei um fluxo de visão computacional com detecção, revisão de exemplos e treinamento de classificador personalizado a partir de modelo pré-treinado, integrando acompanhamento de épocas, checkpoint, estabilização temporal e alertas persistentes.',
          'O código de treinamento foi localizado; não foi executado nesta revisão. Métricas, generalização entre câmeras e risco de imagens semelhantes nos splits precisam de análise.'),
         case('Mocap — ML no cliente e visualização','Protótipo de captura de movimento','Conectar vídeo, landmarks e interação visual no navegador',
          ['Alternativas MoveNet e BlazePose/MediaPipe no acervo.', 'Inferência TensorFlow.js/MediaPipe e coordenação do ciclo de vídeo/renderização.', 'Keypoints, esqueleto e suavização temporal para explorar estabilidade do movimento.', 'Three.js/VRM, p5 e WebGL no conjunto de implementações e recursos.'],
          ['Inferência no browser','Estimação de pose','Geometria e coordenadas','Suavização temporal','Renderização 3D'],
          ['mocap/src/main.js','mocap/docs/ARQUITETURA.md','skeleton from video/detectPoseMediaPipe.js'],
          'Desenvolvi protótipos de estimação de pose no navegador, integrando inferência, visualização de keypoints e suavização temporal para explorar captura de movimento e interação com recursos 3D.',
          'São modelos existentes integrados à aplicação; FPS, latência e qualidade de retargeting não foram medidos.')],
        ['Vídeo e candidatos','Inferência/classificação','Estado temporal','Revisão e exemplos','Treino/checkpoint','Visualização ou alerta']),
      topic('dados','Engenharia de dados e sistemas operacionais — Agrodan/SIA',
        'As capacidades de ETL e analytics vêm de fluxos identificáveis: apontamentos, jornadas, qualidade, packing, metas, catracas e meteorologia. O catálogo SIA abaixo abre esses fluxos em módulos, com suas fontes.',
        ['Na experiência profissional da Agrodan, trabalhei na integração de dados e processos do campo ao packing, articulando consultas SQL, importadores, transformações, modelos persistentes e visualização operacional.',
         'A arquitetura do material local separa cargas a partir de consultas e transformações a partir do próprio data warehouse. As especializações incluem produção por fazenda, origem de pallets, metas, qualidade por colaborador/dia, rendimento e consolidadores de packing.',
         'Também desenvolvi frentes de indicadores de pessoas a partir de eventos de catracas, dados meteorológicos e formulários corporativos. O valor técnico está na tradução de processos reais para granularidades, regras, vínculos e indicadores verificáveis.'],
        [case('ETL modular e qualidade de dados','Experiência profissional Agrodan','Reutilizar infraestrutura de carga sem perder regras específicas de cada domínio',
          ['Base de importação reutilizável com callbacks por lote.', 'Importadores from_queries obtêm dados em SQL; from_dwh cruza registros já disponíveis.', 'Persistência bulkCreate, normalização de propriedades e validações no acervo.', 'Migrations/Umzug e registro de erros apoiam evolução de schemas e rastreabilidade.'],
          ['ETL','Arquitetura reutilizável','SQL','Modelagem de granularidade','Persistência em lote','Qualidade de dados'],
          ['Agrodan/'+importer+'from_queries/core-importer-from-queries.js','Agrodan/'+importer+'from_dwh/core-importer-from-dwh.js','Agrodan/'+core+'validation/core-validation.js'],
          'Estruturei pipelines de integração com importadores reutilizáveis, processamento em lotes e regras específicas para produção, packing, qualidade e pessoas, organizando dados operacionais para análise e apoio à decisão.',
          'As rotinas têm dependências históricas e partes comentadas. Quantidade de módulos não é quantidade de produtos nem comprovação de todos em produção.')],
        ['Fontes operacionais','Consulta e normalização','Lotes e validação','Modelos e data warehouse','Cruzamentos e indicadores','Web/mobile e decisão']),
      topic('mobile','Desenvolvimento mobile, web corporativo e modelagem de processos',
        'SIAgro demonstra uma aplicação mobile de negócio. EBSERH e The Game Project acrescentam Java corporativo, persistência, regras e interfaces; os produtos mais recentes ampliam o repertório web.',
        ['Desenvolvi aplicações e interfaces que representam processos operacionais, combinando modelos de domínio, persistência e experiência do usuário. No SIAgro, a coleta mobile organiza ordens de serviço, apontamentos, colaboradores, metas e qualidade.',
         'A experiência web inclui aplicações React/Next/Astro e backend em Node/Python, além de sistemas Java EE com JSF, PrimeFaces, EJB e JPA/Hibernate. Trabalhei com diferentes formas de separar apresentação, regras e acesso a dados.',
         'Essa extensão permite apresentar decisões de engenharia concretas: armazenamento local no mobile, componentes reutilizáveis no frontend, rotas/DAOs no backend e esquemas/relacionamentos para manter consistência do domínio.'],
        [case('SIAgro — coleta operacional mobile','Agrodan','Representar registros e gestão de campo em um dispositivo móvel',
          ['React Native/Expo e React Navigation para as telas e navegação.', 'Objetos de ordem de serviço, apontamento, funcionário e qualidade.', 'ObjetoPadrao centraliza operações de persistência com AsyncStorage.', 'Componentes para metas, UGBs, período e colaboradores; dashboard com gráficos.', 'Recursos de arquivos e imagens constam na stack; configuração não comprova publicação em loja.'],
          ['React Native/Expo','Persistência local','Modelagem operacional','Componentes mobile','Visualização de indicadores'],
          ['Agrodan/sia_app/Modulos/SIAgro/Objetos/ObjetoPadrao.js','Agrodan/sia_app/Modulos/SIAgro/Telas/OrdemServico/OrdemServico.js','Agrodan/sia_app/Modulos/SIAgro/Telas/Apontamento/Apontamento.js'],
          'Desenvolvi módulos mobile do SIAgro para ordens de serviço, apontamentos e qualidade, combinando React Native/Expo, modelagem de objetos de negócio, persistência local e visualização de indicadores.',
          'Sincronização offline completa, GPS em operação e publicação dependem da confirmação da experiência; flags e bibliotecas não bastam para essas afirmações.'),
         case('Indicadores hospitalares e gamificação acadêmica','EBSERH: estágio; The Game Project: faculdade','Traduzir indicadores/avaliações e regras de progressão em sistemas persistentes',
          ['EBSERH separa módulo EJB de negócio e módulo WAR/JSF de apresentação.', 'Entidades e beans representam indicadores e avaliações.', 'The Game Project separa entidades, DAOs, managed beans, converters e regras de mundo.', 'A aplicação acadêmica relaciona aventuras, tarefas, personagens, histórico e progressão RPG.'],
          ['Java EE','JSF/PrimeFaces','EJB','JPA/Hibernate','DAO','Regras de negócio','Gamificação'],
          [e for p in projects if p['id'] in ['ebserh','The game project'] for e in [p['id']+'/'+p['evidence'][0]]],
          'No estágio hospitalar, desenvolvi sistema web de indicadores e avaliações com Java EE. Na faculdade, construí uma aplicação de gestão de projetos com gamificação e persistência, explorando regras de progressão e organização de tarefas.',
          'Manter os contextos separados. Não tratar reutilização de código EBSERH no projeto acadêmico como outra experiência hospitalar.')],
        ['Processo real','Entidades e regras','Persistência e APIs','Telas e componentes','Estado e interação','Acompanhamento operacional']),
      topic('decisao','Pesquisa operacional, finanças, produção e aprendizagem',
        'Utilibox revela uma extensão temática e metodológica: métodos multicritério, filas, Lean, matemática financeira, growth e repetição espaçada. Cartola e Logística trazem otimização em problemas específicos.',
        ['Transformei métodos quantitativos e regras de domínio em ferramentas de software para comparar alternativas, simular cenários e apoiar decisões. O repertório inclui AHP, TOPSIS, PROMETHEE, árvores de valor esperado, filas e otimização sob restrições.',
         'Em produção, explorei tempos padrão, SMED, VSM, takt time, capacidade, gargalos e ciclos PDSA. Em finanças e crescimento, modelei cálculos de WACC/CAPM, VPL/TIR, payback e LTV/CAC. Em aprendizagem, implementei regras de repetição espaçada SM-2.',
         'Esses cases mostram conexão entre engenharia de produção, análise e software. Cada método é apresentado com sua aplicação e fonte, sem transformar o tema da ferramenta em habilitação profissional.'],
        [case('Utilibox — multicritério, filas e métodos aplicados','Produto de ferramentas','Disponibilizar métodos especializados com entrada, cálculo e interpretação',
          ['AHP: pesos, consistência e julgamentos em grupo.', 'TOPSIS: normalização, pesos, ideais e proximidade relativa.', 'PROMETHEE: funções de preferência, fluxos e sensibilidade.', 'Filas: modelos analíticos, variabilidade, buffers e simulação.', 'SMED/VSM: setup, tempos de processo/espera, PCE, takt e cenários.', 'Anki: agendamento SM-2, intervalos e estatísticas do deck.'],
          ['Decisão multicritério','Simulação','Pesquisa operacional','Lean','Matemática financeira','Modelagem de aprendizagem'],
          ['utilibox/src/tools/ahp-online/domain/consistency.js','utilibox/src/tools/topsis/domain/topsis.js','utilibox/src/tools/promethee/domain/promethee.js','utilibox/src/tools/queueing-theory/logic.js','utilibox/src/tools/vsm/client.js','utilibox/src/tools/anki-flashcards/logic.js'],
          'Implementei ferramentas de apoio à decisão e aprendizagem com métodos multicritério, filas, simulação, matemática financeira e repetição espaçada, traduzindo modelos em interfaces e cálculos explicáveis.',
          'O catálogo tem 136 slugs únicos e categorias sobrepostas. Status live é declarado; acurácia, validação externa e uso real não foram verificados.'),
         case('Cartola e Logística — decisão com restrições','Projetos analíticos','Transformar estimativas e estruturas geográficas em escolhas executáveis',
          ['Cartola: ETL de históricos, representação probabilística por Markov e programação inteira OR-Tools/CBC para orçamento/formação.', 'Logística: mapas Leaflet, desenho de áreas e experimentos de roteamento/TSP com heurísticas e algoritmos genéticos.'],
          ['Modelagem probabilística','Programação inteira','Heurísticas','Geoinformação','Otimização com restrições'],
          ['cartola_oracle/cartola_markov_optimizer/src/cartola/models/markov.py','cartola_oracle/cartola_markov_optimizer/src/cartola/optimize/ilp_solver.py','Logistica/src/leaflet/Roteirizador.js'],
          'Desenvolvi pipelines que conectam dados e otimização à decisão, explorando escalações sob orçamento/formação e roteamento com visualização geográfica.',
          'Confirmar métricas e comparação de soluções; presença de NDVI não comprova pipeline completo de sensoriamento remoto.')],
        ['Problema e critérios','Modelo matemático','Cálculo/otimização','Sensibilidade e cenários','Interpretação','Escolha e acompanhamento']),
      topic('produto','Produtos, conhecimento, automação e computação gráfica',
        'Construção de produto aparece em módulos e fluxos: marketplace, conhecimento narrativo, notas, coleta comercial, finanças pessoais, carreira e experiências 3D. Esta seção amplia a narrativa de iniciativa e engenharia.',
        ['Desenvolvi e experimentei produtos em diferentes domínios, articulando catálogo, acesso, persistência, integrações e conteúdo. No Launch With Me, o modelo organiza campanhas, missões, evidências e papéis; na Utilibox, a base compartilhada reúne ferramentas e módulos de conhecimento.',
         'Narra e Utilinotas exploram organização de obras, personagens, cenas, notas e relações, com assistência contextual e referências de evidência. Scrapers, Job Assistant e Minhas Finanças conectam coleta e processamento de dados a fluxos de uso e revisão.',
         'Em computação gráfica, construí protótipos 3D com cena, câmera, personagem, física e interface. Esse repertório liga software, modelagem de domínio, interação e experimentação de produto.'],
        [case('Narra/Utilinotas — domínio e conhecimento','Utilibox','Organizar informação criativa e responder com referência ao estado do usuário',
          ['Narra modela obras, personagens, cenas, relações e cânone.', 'Writing companion encaminha intenções para funções do domínio.', 'Evidence engine apresenta fontes, confiança e sinalização de inferência.', 'Utilinotas trabalha vaults, Markdown/YAML, wikilinks/backlinks e importação/exportação.'],
          ['Modelagem de conhecimento','Assistência contextual','Evidence tracing','Interoperabilidade de notas','Engenharia de domínio'],
          ['utilibox/src/tools/narra/assistant/writing/writingCompanionEngine.js','utilibox/src/tools/narra/assistant/query/evidenceEngine.js','utilibox/src/tools/utilinotas/content.md'],
          'Construí módulos de organização narrativa e conhecimento, com relações entre entidades, assistência contextual, rastreabilidade de respostas e interoperabilidade de notas.',
          'Despacho por intenção não é sozinho arquitetura multiagente; não comprova banco vetorial/RAG/MCP implementado.'),
         case('Marketplace, automações e interação 3D','Vínculos individuais a contextualizar','Ligar regras de produto, fontes externas e interfaces a experiências completas',
          ['Launch With Me: rotas por papéis, schema, migrations, RLS/RPC e missões/evidências.', 'Scrapers: adaptadores por site, runner, supervisão e distribuição de ofertas.', 'Job Assistant: Playwright, ranking por regras, CLI e revisão humana.', 'Minhas Finanças: Pluggy, classificação por regras, agregações e SQLite.', 'Dente de Leão: React Three Fiber, Rapier, Zustand, câmera, interação e HUD.'],
          ['Product engineering','RLS e modelagem de acesso','Automação supervisionada','Open Finance','Computação gráfica','Física e estado de jogo'],
          [p['id']+'/'+p['evidence'][0] for p in projects if p['id'] in ['launch_with_me','Scrapers','linkedin-job-assistant','minhas-financas','dente_de_leao']],
          'Estruturei produtos e protótipos com regras de acesso, integrações e fluxos supervisionados, incluindo marketplace, coleta comercial, finanças pessoais e experiência narrativa 3D.',
          'Não atribuir faturamento, escala ou publicação sem dados; pagamentos e recursos planejados têm maturidade variável.')],
        ['Necessidade e domínio','Modelo e regras','Dados/integrações','Experiência de uso','Operação e revisão','Aprendizagem de produto'])
    ]
    topics.extend([
      topic('infra','Infraestrutura, integração desktop, IoT e operação de tecnologia',
        'A experiência em TIC registrada no CV complementa o código dos projetos: servidores, redes, suporte, continuidade, ERP, segurança e IoT. A integração com MetaTrader5 é um case local de conexão com software desktop.',
        ['Na gestão de TIC, atuei com rotinas de equipe, suporte, servidores, redes, backup/recovery, virtualização e iniciativas de disponibilidade. O currículo atual relaciona Windows/Linux, Active Directory, Zabbix/GLPI, Mikrotik, Unifi, ERP, Arduino e Raspberry Pi a essa experiência.',
         'Essa atuação conecta operação de tecnologia, integração e entrega de aplicações: acompanhar ambientes, organizar necessidades dos usuários e relacionar dados e serviços às operações do negócio.',
         'No TraderMind, desenvolvi componentes Python para integrar pesquisa e inferência ao terminal desktop MetaTrader5, conectando dados de mercado, contexto da conta e envio de ordens. Essa integração deve ser diferenciada de desenvolvimento de uma interface desktop nativa própria.'],
        [case('Gestão de TIC — Agrodan','Experiência já declarada no CV; contexto Agrodan confirmado','Sustentar ambiente e serviços de tecnologia utilizados pela operação',
          ['Rotinas de equipe, help desk e parque de dispositivos constam no cargo de Gerente de TIC.', 'Administração Windows/Linux, Active Directory e redes corporativas consta no relato profissional.', 'Backup/recovery, virtualização e alta disponibilidade fazem parte do escopo declarado.', 'Zabbix/GLPI, firewall, Mikrotik, Unifi, Arduino e Raspberry Pi estão relacionados à função no CV.'],
          ['Operação de TI','Redes e servidores','Gestão de suporte','Continuidade','Segurança','IoT'],
          ['my_ cv/cv-data.json'],
          'Gerenciei a operação de TIC, integrando suporte, servidores, redes, continuidade, ERP e iniciativas de IoT à entrega de serviços e soluções para a empresa.',
          'Fonte: relato profissional já existente, não código auditado nesta pesquisa. Detalhar os projetos de infraestrutura, escala, responsabilidades e resultados com Danillo.'),
         case('Conector desktop MetaTrader5 — TraderMind','Projeto de pesquisa quantitativa','Ligar a aplicação Python ao terminal de negociação instalado localmente',
          ['Conector utiliza o pacote MetaTrader5 oficial e depende do terminal aberto/autenticado.', 'Consulta conta e dados de candles; prepara o fluxo de operação ligado à política/inferência.', 'API/dashboard e bot têm responsabilidades separadas no acervo.', 'A política registra fonte e congelamento para relacionar pesquisa e execução documentada.'],
          ['Integração desktop','Python','Integração de APIs locais','Separação de serviços','Rastreabilidade de política'],
          ['mt5/TraderMind/connector/bot.py','mt5/TraderMind/serve.py','mt5/TraderMind/docs/SETUP_DASHBOARD_BOT.md'],
          'Construí um conector Python para o terminal desktop MetaTrader5, integrando dados de mercado e conta ao fluxo de pesquisa e operação documentado no projeto.',
          'Não equivale a aplicação GUI própria em Qt, Electron, WPF ou Swing. O F-AHP Java declarado no TCC precisa de seus próprios arquivos para detalhar plataforma e interface.')],
        ['Necessidade operacional','Ambiente e acesso','Serviços e integração','Monitoramento','Continuidade','Suporte e melhoria']),
      topic('grafica','Computação gráfica, experiência 3D e geoinformação',
        'O repertório visual inclui cena, câmera, física, interação e mapas. A origem das competências aparece nos protótipos 3D, no Mocap, na experiência narrativa e nos experimentos de logística.',
        ['Desenvolvi protótipos de interação e visualização no navegador, explorando cenas 3D, modelos, câmera, controle de personagem, física e interfaces de acompanhamento.',
         'No Dente de Leão, a organização separa input, mundo, personagem, câmera e HUD; React Three Fiber, Rapier e Zustand apoiam renderização, física e estado. Em outros estudos, Three.js e loaders FBX ampliam o repertório de modelos e visualização.',
         'Em geoinformação, utilizei Leaflet para representar áreas, desenho e roteamento, conectando visualização espacial a experimentos de planejamento logístico. No Mocap, a representação visual também é ligada à inferência de pose e ao movimento.'],
        [case('Dente de Leão — mundo e interação narrativa','Protótipo independente','Construir uma experiência de exploração e interação em ambiente 3D',
          ['src/core concentra entrada do usuário.', 'src/game organiza mundo, personagem, câmera e interação.', 'src/ui contém elementos de HUD.', 'React Three Fiber, Rapier e Zustand articulam renderização, física e estado.'],
          ['Renderização 3D','Input e câmera','Física','Estado de jogo','Interação narrativa','Arquitetura de protótipo'],
          [p['id']+'/'+e for p in projects if p['id']=='dente_de_leao' for e in p['evidence']],
          'Construí um protótipo narrativo 3D com controle de personagem, câmera, interação, física e HUD, organizando estado e renderização com React Three Fiber, Rapier e Zustand.',
          'É um protótipo no navegador; não afirmar lançamento comercial de jogo, engine própria ou desenvolvimento Unity a partir dele.'),
         case('Mapas, modelos e exploração espacial','Logística, Leaflet, threejs e movimento_3D','Representar informação e interação em espaços geográficos ou cenas',
          ['Logística reúne componentes de mapa, canvas, desenho e roteirização.', 'Leaflet inclui uma página própria e biblioteca de roteamento de terceiros.', 'threejs e movimento_3D contêm experiências de cenas, interação e carregamento de modelos.', 'Loaders/bibliotecas incluídos são componentes reutilizados; não autoria própria.'],
          ['Mapas interativos','Visualização geoespacial','Geometria','Carregamento de modelos','Three.js','Prototipação visual'],
          [p['id']+'/'+p['evidence'][0] for p in projects if p['id'] in ['Logistica','Leaflet','threejs','movimento_3D']],
          'Explorei visualização espacial e modelos 3D com Leaflet e Three.js, construindo interfaces de mapa, desenho, roteamento e interação com cenas.',
          'Não comprova especialização GIS completa, sensoriamento remoto operacional ou desenvolvimento de bibliotecas de renderização.')],
        ['Dados/recursos','Espaço e geometria','Cena ou mapa','Câmera e input','Estado/física','Interação e visualização'])
    ])
    topics.insert(4,topic('sia-cases','SIA — projetos de negócio, agricultura e gestão',
      'As branches locais revelam um sistema muito mais amplo do que o checkout master: 668 arquivos frontend na referência development, dezenas de módulos de negócio, backend por domínio e bibliotecas adicionais. Os cases abaixo mostram processos específicos e sua fonte.',
      ['Na Agrodan, desenvolvi e evoluí soluções ligadas a planejamento agrícola, irrigação, auditoria de pulverização, qualidade, colheita, packing, comercial, compras, pessoas e melhoria contínua. Essa amplitude envolve aplicações e modelos de domínio, além da integração de relatórios existentes.',
       'No PLANAGRO, o código relaciona insumos, aplicações, dosagem, carência, deriva e orçamento. Em irrigação, há programação por válvulas/cabeçais, experimentos evolutivos e um módulo de rede neural para sugestão de Kc. Em matéria seca, funções de previsão e ponto de colheita conectam leituras e variedades.',
       'Na gestão, o sistema reúne coleta local de campo, solicitações de compras, avaliações, unidades de negócio, sugestões de melhoria e acompanhamento comercial. Cada case deve ser atribuído à minha participação real, distinguindo implementação própria, integração de BI e recursos incorporados.'],
      [case('PLANAGRO — insumos, aplicações e regras agronômicas','Experiência profissional Agrodan','Apoiar planejamento e verificação de operações agrícolas com critérios de aplicação',
        ['PLANAGRO.js concentra uma interface de planejamento e funções especializadas.', 'Funções avisoAplicacoes, avisoCarencia, avisoDosagem, avisoDeriva, avisoInsumo e avisoOrcamento representam verificações do domínio.', 'Há componentes para representação de planos e informações geográficas no módulo.', 'A rota backend correspondente organiza acesso e operações de dados para o planejamento.'],
        ['Modelagem agronômica','Motores de regras','Planejamento','Validação de aplicação','Geoinformação','Full stack'],
        ['Agrodan@origin/development:src/pages/PlanejamentoAgro/PLANAGRO.js','Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-planagro.js'],
        'Desenvolvi componentes de planejamento agrícola no PLANAGRO, traduzindo aplicação de insumos, dosagem, carência, deriva e orçamento em regras e interfaces ligadas aos dados operacionais.',
        'Existência da regra não comprova sua validação agronômica ou ativação em todas as operações. Confirmar contribuição, implantação e quais verificações foram utilizadas.'),
       case('Irrigação — programação, algoritmos genéticos e rede neural para Kc','Agrodan — material em branch local','Explorar programação de irrigação e estimativa/sugestão do coeficiente de cultura',
        ['ProgIrrig recebe horários, limites de rega, intervalos e dados de válvulas; organiza programação por cabeçal.', 'indexIrrigacao contém população, estrutura de cromossomo, avaliação e evolução genética.', 'KcAutomatico utiliza a biblioteca nn, codificação de fazenda/fase/mês/solo e normalização de dados numéricos.', 'O módulo chama train, restaura rede de JSON e produz KC_SUGERIDO; rotas de irrigação instanciam ProgIrrig e KcAutomatico.', 'Camadas ocultas, ativação, learning rate, momentum e limite de erro aparecem como parâmetros explícitos.'],
        ['Programação de recursos','Algoritmos genéticos','Redes neurais','Feature engineering','Codificação categórica','Normalização','Serialização de modelo'],
        ['Agrodan/etl@origin/development:servers/server-backend/rotas/irrigacao/KcAutomatico.js','Agrodan/etl@origin/development:servers/server-backend/rotas/irrigacao/ProgIrrig.js','Agrodan/etl@origin/development:servers/server-backend/rotas/irrigacao/indexIrrigacao.js','Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-irrigacao.js'],
        'Explorei programação de irrigação, algoritmos genéticos e modelagem neural de Kc, trabalhando com codificação de variáveis, normalização, parâmetros de rede e integração ao backend operacional.',
        'A avaliação consultada reutiliza TRAINING_DATA; o Kc histórico aparece também na entrada/alvo e há ajustes heurísticos na saída. Não apresentar acurácia do arquivo como generalização validada nem afirmar otimização agronômica comprovada.'),
       case('Auditoria de pulverização — mapas e execução','Agrodan','Relacionar execução em campo com posição, velocidade, talhão e serviço',
        ['Interface utiliza dados e camadas cartográficas para analisar trajetos.', 'O arquivo contém Dist, cálculo de média/desvio, avaliar_pulv e velocidadeAcimaPorc.', 'Filtros por trator/data e contextualização por talhão/serviço compõem a investigação.', 'O backend tem rotas relacionadas ao monitoramento/auditoria.'],
        ['Analytics geoespacial','Auditoria operacional','Estatística descritiva','Mapas','Dados de execução','Indicadores de velocidade'],
        ['Agrodan@origin/development:src/pages/AuditoriaPulverizacao/AuditoriaPulverizacao.js','Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-miam.js'],
        'Construí componentes de auditoria da pulverização com dados espaciais e operacionais, relacionando trajetória, velocidade, talhões e serviços para apoiar investigação da execução em campo.',
        'A redução de problemas declarada no CV só será vinculada a este case após confirmar iniciativa, período e método de medição.'),
       case('Matéria seca — previsão e ponto de colheita','Agrodan','Transformar leituras do fruto em acompanhamento e estimativas por variedade',
        ['Funções calcular_previsao, calcular_alpha, equacoes e isPontoColheita aparecem na implementação.', 'Filtros por fazenda, semana/ano e variedades ligam resultado ao contexto da colheita.', 'Gráficos e resumos apresentam combinações e resultados previstos.', 'Rotas de matéria seca integram acesso aos dados; o frontend contém a lógica de cálculo observada.'],
        ['Modelagem de previsão','Regras por variedade','Equações e parâmetros','Analytics agrícola','Visualização'],
        ['Agrodan@origin/development:src/pages/MateriaSeca/MateriaSeca.js','Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-materia-seca.js'],
        'Implementei componentes de análise de matéria seca e previsão de colheita, relacionando leituras, variedades e parâmetros a gráficos e regras de acompanhamento.',
        'São equações/regras localizadas; não classificar automaticamente como modelo de Machine Learning treinado. Confirmar método, validação e uso.'),
       case('Caderno de campo e compras — dados locais e sincronização','Agrodan','Registrar operações e solicitações com continuidade no cliente',
        ['CadernoCampo/Apontamentos utiliza Dexie e módulos de localDb/downloadData.', 'Handlers tratam colaboradores, seleção, rateio, data, processo e serviços.', 'SolicitacaoCompras representa itens/centros e tem handlers de remoção e sincronização.', 'Rotas backend de caderno de campo e compras completam a evidência de integração por domínio.'],
        ['IndexedDB/Dexie','Coleta web','Modelagem de processo','Sincronização','Formulários','Compras e apontamentos'],
        ['Agrodan@origin/development:src/pages/CadernoCampo/Apontamentos.js','Agrodan@origin/development:src/pages/SolicitacaoCompras/Solicitacao.js','Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-caderno-campo.js','Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-solicitacao-compras.js'],
        'Desenvolvi fluxos de coleta de campo e solicitações de compras com dados locais, componentes de processo e rotinas de sincronização, integrados ao backend por domínio.',
        'Dexie e handlers sustentam o mecanismo de dados locais; comportamento offline completo, conflitos e taxa de sucesso não foram executados ou medidos nesta revisão.'),
       case('Gestão UGB, pessoas e sugestões de melhoria','Agrodan','Organizar unidades, colaboradores, avaliações e ciclos de melhoria',
        ['GestaoUGBs organiza módulos para unidades, funcionários, avaliação humana, 5S, planos, qualificação e sugestões.', 'Funcionários inclui componentes de histórico/cadastro/faltas e banco local no acervo.', 'Sugestões têm interfaces de submissão, administração e avaliação.', 'Backend de sugestões usa uploads, geração documental e rotas de pesquisa/filtros.'],
        ['Modelagem organizacional','Gestão de pessoas','Workflow de melhoria','Documentos e uploads','Reuso de componentes','Full stack corporativo'],
        ['Agrodan@origin/development:src/pages/GestaoUGBs/Modulos/Funcionarios/index.js','Agrodan@origin/development:src/pages/GestaoUGBs/Modulos/UGBs/index.js','Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-sugestao-melhorias.js'],
        'Modelei aplicações de gestão de unidades e pessoas e fluxos de sugestão de melhorias, articulando dados organizacionais, histórico, avaliações, papéis e documentos.',
        'Submódulos compartilham arquitetura e componentes; não apresentar como produtos independentes nem afirmar resultados de RH sem evidência.'),
       case('Comercial, previsão de resultados e movimentação de pallets','Agrodan','Relacionar lançamentos, previsões, câmbio e operação de logística/packing',
        ['COMERCIAL/Resultados contém lançamentos, auditorias e visão gerencial.', 'PrevisaoResultados compõe previsão, acompanhamento e câmbio em telas próprias.', 'MovimentacaoPallet organiza movimentação, dados de container e conferência.', 'Backend separado por comercial, previsão e containers representa operações correspondentes.'],
        ['Modelagem comercial','Planejamento de resultados','Fluxos de logística','Rastreabilidade','Interfaces e APIs'],
        ['Agrodan@origin/development:src/pages/PrevisaoResultados/index.js','Agrodan@origin/development:src/pages/MovimentacaoPallet/MovimentacaoPallet.js','Agrodan/etl@origin/development:servers/server-backend/rotas/comercial/rotas-comercial.js','Agrodan/etl@origin/development:servers/server-backend/rotas/rotas-containers.js'],
        'Desenvolvi componentes de acompanhamento comercial e logística, relacionando lançamentos e previsões a interfaces de gestão e dados operacionais de pallets e containers.',
        'Previsão no nome da tela não comprova algoritmo de ML; verificar método de cálculo. Implantação e ganhos serão ligados à participação real.')],
      ['Processo de negócio','Tela e modelo de domínio','Regras/cálculos','Dados locais ou API','Auditoria e acompanhamento','Resultado a contextualizar']))
    # Reference existence is a generation invariant, not runtime validation.
    for t in topics:
        for c in t['cases']:
            for ref in c['sources']:
                if '@origin/' in ref:
                    import subprocess
                    repo,qualified=ref.split('@',1)
                    subprocess.run(['git','cat-file','-e',qualified],cwd=root/repo,check=True,capture_output=True)
                    continue
                if not (root/ref).is_file():
                    raise FileNotFoundError(root/ref)
    skills=[]
    for t in topics:
        for c in t['cases']:
            for skill in c['skills']: skills.append({'skill':skill,'case':c['title'],'context':c['context'],'evidence':c['sources']})
    for m in modules:
        for skill in m['skills']: skills.append({'skill':skill,'case':'SIA · '+m['title'],'context':'Agrodan — experiência profissional','evidence':[s['path']+':'+str(s['line']) for s in m['sources']]})
    for m in branch_audit['modules']:
        for skill in m['skills']: skills.append({'skill':skill,'case':'SIA · '+m['title'],'context':'Agrodan — código em branches locais','evidence':[s['path']+':'+str(s['line']) for s in m['sources']]})
    return {'topics':topics,'agroModules':modules,'agroBusinessModules':branch_audit['modules'],'agroBranchAudit':{k:v for k,v in branch_audit.items() if k!='modules'},'skillProvenance':skills,'utiliboxTools':utilibox['tools']}
