"""Group the complete case inventory into bilingual capability narratives."""
import html

# Title, narrative and concrete capabilities in Portuguese and English.
GROUPS=[
 ('agentic','Agentic AI, sistemas multiagentes e governança','Agentic AI, multiagent systems and governance',
  'Arquitetura de soluções com papéis especializados, coordenação de agentes, contexto compartilhado e controle das decisões. Planejamento Xavier traz coordenação por regras; Globalcom amplia o repertório com uma arquitetura entregue para certificação e compliance, atualmente em implementação.',
  'Solution architecture with specialized roles, agent coordination, shared context and decision controls. Planejamento Xavier provides rule-based coordination; Globalcom extends this experience through a delivered certification and compliance architecture, currently being implemented.',
  ['Decomposição de responsabilidades, orquestração e resolução de conflitos','RAG, recuperação documental, MCP e integração de sistemas no desenho Globalcom','Workflows persistentes, auditoria independente, permissões e aprovação humana'],
  ['Responsibility decomposition, orchestration and conflict resolution','RAG, document retrieval, MCP and system integration in the Globalcom design','Persistent workflows, independent audit, permissions and human approval'],
  ['case-agentes-1','case-globalcom-']),
 ('llm','LLMs, aplicações de IA e automação conversacional','LLMs, AI applications and conversational automation',
  'Integração de modelos de linguagem em produtos de planejamento, educação e relacionamento comercial. O trabalho conecta respostas de IA ao domínio da aplicação, com estruturas de dados, validação e tratamento de falhas para transformar a saída do modelo em ações utilizáveis.',
  'Language-model integration in planning, education and customer relationship products. This work connects AI responses to application domains through data structures, validation and failure handling, turning model output into usable actions.',
  ['Integração de provedores, seleção de modelos e fallback','Saídas estruturadas, contratos de operações e validação referencial','Contexto conversacional e revisão de planos com apoio de IA'],
  ['Provider integration, model selection and fallback','Structured outputs, operation contracts and reference validation','Conversation context and AI-assisted plan review'],['case-ia-']),
 ('ml','Machine Learning, pesquisa quantitativa e experimentação','Machine Learning, quantitative research and experimentation',
  'Pesquisa aplicada que combina preparação de dados, seleção de atributos, algoritmos evolutivos, modelos preditivos e avaliação experimental. EFS-AHP pertence ao doutorado; TraderMind explora séries temporais e ensembles de sinais em pesquisa quantitativa, sem presumir retorno financeiro validado.',
  'Applied research combining data preparation, feature selection, evolutionary algorithms, predictive models and experimental evaluation. EFS-AHP belongs to doctoral research; TraderMind explores time series and signal ensembles in quantitative research, without implying verified financial returns.',
  ['Seleção de atributos, AHP, baselines e comparação de modelos','Algoritmos evolutivos, ensembles e combinação de sinais','Engenharia de atributos, avaliação temporal e prevenção de vazamento de dados'],
  ['Feature selection, AHP, baselines and model comparison','Evolutionary algorithms, ensembles and signal combination','Feature engineering, temporal evaluation and data leakage prevention'],['case-ml-','case-agentes-2']),
 ('mlops','MLOps, pipelines e ciclo de vida de modelos','MLOps, pipelines and model lifecycle',
  'No TraderMind, a experiência se concentra na engenharia que conecta dados, treinamento, validação, artefatos, inferência e acompanhamento dos modelos. A integração MetaTrader5 é uma parte desse fluxo; os cases detalham pesquisa e operação demo, com responsabilidades separadas entre experimentação, API e execução.',
  'TraderMind centers on the engineering connecting data, training, validation, artifacts, inference and model monitoring. MetaTrader5 integration is one component of this workflow; the cases describe research and demo operation, separating experimentation, API and execution responsibilities.',
  ['Contratos de dados, preparação de features e validação fora da amostra','Checkpoints, persistência de artefatos e serving de modelos','Supervisão de processos, retreino, atualização e observabilidade'],
  ['Data contracts, feature preparation and out-of-sample validation','Checkpoints, artifact persistence and model serving','Process supervision, retraining, updates and observability'],['case-mlops-','case-infra-2']),
 ('vision','Visão computacional e integração industrial','Computer vision and industrial integration',
  'Aplicações de visão que vão de detecção e notificações em vídeo à estimação de pose no navegador e contagem de frutas na indústria. Na Agrodan/Agritech.NE, a participação como desenvolvedor conecta a plataforma aos dados do ERP, classificadora, lotes e indicadores operacionais; os resultados industriais são os registrados para o projeto.',
  'Vision applications range from video detection and notifications to browser pose estimation and industrial fruit counting. At Agrodan/Agritech.NE, the developer contribution connects the platform to ERP, sorting-machine, batch and operational indicator data; industrial outcomes are those reported for the project.',
  ['Inferência em vídeo, datasets de feedback e treinamento de classificadores','Estimação de pose, processamento no cliente e visualização','Contagem, rastreabilidade, reconciliação de volumes e alertas industriais'],
  ['Video inference, feedback datasets and classifier training','Pose estimation, client-side processing and visualization','Counting, traceability, volume reconciliation and industrial alerts'],['case-visao-','case-agritech-']),
 ('data','Engenharia de dados, ETL e integração ERP','Data engineering, ETL and ERP integration',
  'Integração de dados operacionais para sustentar indicadores e processos corporativos na Agrodan. A engenharia envolve importação em lotes, persistência, APIs e rotinas de atualização, aproximando os registros do ERP das aplicações web, análises e decisões de gestão.',
  'Operational data integration supporting corporate indicators and workflows at Agrodan. The engineering covers batch imports, persistence, APIs and update routines, connecting ERP records to web applications, analytics and management decisions.',
  ['Modelagem de dados e consultas SQL','ETLs modulares, ingestão em lotes e qualidade de dados','Integração ERP, rastreabilidade de erros e atualização operacional'],
  ['Data modeling and SQL queries','Modular ETL, batch ingestion and data quality','ERP integration, error traceability and operational updates'],['case-dados-']),
 ('software','Engenharia de software web, mobile e produtos','Web and mobile software engineering and products',
  'Desenvolvimento de sistemas com regras de domínio, interfaces, APIs e persistência em contextos corporativos, hospitalares, acadêmicos e empreendedores. SIAgro amplia essa experiência para coleta mobile; os produtos independentes agregam modelagem de entidades, autenticação, serviços e integrações comerciais.',
  'Development of systems with domain rules, interfaces, APIs and persistence across corporate, hospital, academic and entrepreneurial contexts. SIAgro extends this experience to mobile collection; independent products add entity modeling, authentication, services and commercial integrations.',
  ['Aplicações web, arquitetura de APIs e persistência relacional','React Native, navegação, coleta operacional e armazenamento local','Sistemas Java EE, gestão de indicadores, gamificação e produtos digitais'],
  ['Web applications, API architecture and relational persistence','React Native, navigation, operational collection and local storage','Java EE systems, indicator management, gamification and digital products'],['case-mobile-','case-produto-2']),
 ('agro','Agronegócio, gestão operacional e sistemas corporativos','Agriculture, operational management and enterprise systems',
  'No SIA/SIAgro, a tecnologia atende planejamento agrícola, irrigação, pulverização, compras, pessoas, qualidade e packing. Os cases mostram a tradução de regras do negócio em módulos, dados e interfaces, conectando desenvolvimento de software à experiência profissional de transformação digital e gestão na Agrodan.',
  'Within SIA/SIAgro, technology supports agricultural planning, irrigation, spraying, purchasing, people, quality and packing. The cases show business rules translated into modules, data and interfaces, connecting software development to professional digital transformation and management experience at Agrodan.',
  ['Regras agronômicas, modelagem de irrigação e previsão de colheita','Coleta offline, sincronização, auditoria de campo e dados geoespaciais','Compras, avaliações, UGB, indicadores comerciais e gestão da qualidade'],
  ['Agronomic rules, irrigation modeling and harvest forecasting','Offline collection, synchronization, field audits and geospatial data','Purchasing, assessments, business units, commercial indicators and quality management'],['case-sia-cases-','destaque-sia-']),
 ('decision','Decisão multicritério, otimização e pesquisa operacional','Multicriteria decisions, optimization and operations research',
  'Métodos analíticos transformados em ferramentas para comparar alternativas, dimensionar capacidade e decidir sob restrições. Utilibox reúne aplicações de AHP, TOPSIS, PROMETHEE e filas; Cartola e logística ampliam o repertório para decisões quantitativas e otimização aplicada.',
  'Analytical methods translated into tools for comparing alternatives, sizing capacity and making constrained decisions. Utilibox provides AHP, TOPSIS, PROMETHEE and queueing applications; Cartola and logistics extend this experience to quantitative decisions and applied optimization.',
  ['Pesos, consistência, rankings e análise de sensibilidade','Teoria das filas, capacidade e dimensionamento de serviços','Otimização com restrições, análise probabilística e roteamento'],
  ['Weights, consistency, rankings and sensitivity analysis','Queueing theory, capacity and service sizing','Constrained optimization, probabilistic analysis and routing'],['case-decisao-','destaque-utilibox-ahp','destaque-utilibox-topsis-promethee','destaque-utilibox-filas']),
 ('lean','Lean, melhoria contínua e análise econômica','Lean, continuous improvement and economic analysis',
  'Aplicação de métodos de engenharia de produção e gestão em ferramentas digitais do Utilibox. O repertório relaciona fluxo de valor, redução de setup, resolução estruturada de problemas, priorização e avaliação econômica; as ferramentas Lean também se conectam ao MBA Operational Excellence em andamento.',
  'Production engineering and management methods implemented in Utilibox digital tools. This experience connects value streams, setup reduction, structured problem solving, prioritization and economic evaluation; the Lean tools also relate to the ongoing Operational Excellence MBA.',
  ['VSM, SMED, PDSA e A3 para análise e melhoria de processos','Pareto, GUT e SWOT para priorização e diagnóstico','VPL, TIR, payback e cenários para avaliação de investimentos'],
  ['VSM, SMED, PDSA and A3 for process analysis and improvement','Pareto, GUT and SWOT for prioritization and diagnosis','NPV, IRR, payback and scenarios for investment evaluation'],['destaque-utilibox-lean','destaque-utilibox-financeiro','destaque-utilibox-priorizacao']),
 ('knowledge','Gestão do conhecimento, aprendizagem e modelagem de domínio','Knowledge management, learning and domain modeling',
  'Produtos que organizam conhecimento, relações e rotinas de aprendizagem. Narra, UtiliNotas e flashcards evidenciam modelagem de entidades, contexto e persistência, além de métodos de estudo, revisão espaçada e exportação de conteúdos.',
  'Products organizing knowledge, relationships and learning routines. Narra, UtiliNotas and flashcards demonstrate entity modeling, context and persistence alongside study methods, spaced review and content export.',
  ['Entidades, relações, contexto e organização de conhecimento','Persistência de conteúdo, Markdown e exportação','Repetição espaçada, planejamento de revisão e acompanhamento de estudo'],
  ['Entities, relationships, context and knowledge organization','Content persistence, Markdown and export','Spaced repetition, review planning and study tracking'],['case-produto-1','destaque-utilibox-conhecimento','destaque-utilibox-aprendizagem']),
 ('infra','Infraestrutura, segurança e liderança de tecnologia','Infrastructure, security and technology leadership',
  'Experiência de gestão de TIC na Agrodan com ambientes corporativos, suporte, servidores, redes e continuidade operacional. Esse repertório complementa a atuação como líder de tecnologia e integra operação, equipe técnica, sistemas empresariais e necessidades do negócio.',
  'ICT management experience at Agrodan covers enterprise environments, support, servers, networks and operational continuity. This experience complements technology leadership, connecting operations, technical teams, enterprise systems and business needs.',
  ['Windows/Linux, Active Directory, redes e administração de servidores','Monitoramento, service desk, backup, recuperação e disponibilidade','Gestão de equipe, priorização e integração entre tecnologia e operação'],
  ['Windows/Linux, Active Directory, networks and server administration','Monitoring, service desk, backup, recovery and availability','Team management, prioritization and technology–operations integration'],['case-infra-1']),
 ('spatial','Interfaces 3D, mapas e experiências interativas','3D interfaces, maps and interactive experiences',
  'Exploração de interfaces espaciais, mapas, modelos e mundos interativos em projetos independentes. O trabalho combina renderização no navegador, interação, física e visualização geográfica; os cases mantêm o contexto de protótipos e estudos.',
  'Exploration of spatial interfaces, maps, models and interactive worlds in independent projects. This work combines browser rendering, interaction, physics and geographic visualization; the cases retain their prototype and study context.',
  ['Cenas 3D, componentes de interação e estado da aplicação','Modelos, animação, física e renderização WebGL','Mapas, rotas e visualização geoespacial'],
  ['3D scenes, interaction components and application state','Models, animation, physics and WebGL rendering','Maps, routes and geospatial visualization'],['case-grafica-']),
]

def render(cases, priorities, language='pt', stacks=None):
    en=language=='en';esc=lambda s:html.escape(str(s),quote=True)
    tr=lambda pt,eng:eng if en else pt
    all_cases=cases+priorities
    assigned=set();body=[];navigation=[]
    for key,pt_title,en_title,pt_text,en_text,pt_skills,en_skills,prefixes in GROUPS:
        selected=[c for c in all_cases if any(c['id'].startswith(p) for p in prefixes)]
        selected.sort(key=lambda c:next(i for i,p in enumerate(prefixes) if c['id'].startswith(p)))
        if not selected:continue
        overlap=assigned & {c['id'] for c in selected}
        if overlap:raise ValueError('Duplicate capability assignment: '+str(overlap))
        assigned.update(c['id'] for c in selected)
        title=en_title if en else pt_title;anchor='competencia-'+key
        navigation.append('<a href="#'+anchor+'">'+esc(title)+'</a>')
        content='<article class="skill-cluster" id="'+anchor+'"><h3>'+esc(title)+'</h3><p class="skill-cluster-summary">'+esc(en_text if en else pt_text)+'</p>'
        content+='<h4>'+tr('Competências aplicadas','Applied capabilities')+'</h4><ul class="skill-cluster-capabilities">'+''.join('<li>'+esc(s)+'</li>' for s in (en_skills if en else pt_skills))+'</ul>'
        technologies=[]
        content+='<h4>'+tr('Cases e contextos de origem','Source cases and contexts')+'</h4><ul class="skill-case-list">'
        for c in selected:
            destination=('resumo-' if c['id'].startswith('destaque-') else '')+c['id']
            if c['id'].startswith('case-globalcom-'):
                content+='<li><a href="#'+esc(destination)+'">Globalcom · '+esc(c['title'])+'</a></li>'
            else:
                content+='<li><a href="#'+esc(destination)+'">'+esc(c['title'])+'</a><span class="skill-case-context">'+esc(c['context'])+'</span><p>'+esc(c['text'])+'</p></li>'
            stack=c.get('stack') or (stacks or {}).get(c['id'].removeprefix('case-'),'')
            for token in stack.split(' · '):
                if token and token not in technologies:technologies.append(token)
        content+='</ul><p class="skill-cluster-stack"><strong>'+tr('Tecnologias e métodos: ','Technologies and methods: ')+'</strong>'+esc(' · '.join(technologies))+'</p></article>'
        body.append(content)
    missing={c['id'] for c in all_cases}-assigned
    if missing:raise ValueError('Ungrouped capability cases: '+str(missing))
    intro=tr('Competências organizadas por especialidade, com aplicações, métodos e projetos de origem. Cada grupo conecta o trabalho técnico ao seu contexto profissional, acadêmico ou independente; os links abrem os cases correspondentes.','Capabilities organized by specialty, with applications, methods and source projects. Each group connects technical work to its professional, academic or independent context; links open the corresponding cases.')
    practice='<article class="skill-cluster"><h3>'+tr('Algoritmos, estruturas de dados e resolução de problemas','Algorithms, data structures and problem solving')+'</h3><p>'+tr('Prática complementar de 120 horas de LeetCode: arrays, hashing, busca binária, árvores, grafos, heaps, programação dinâmica e backtracking. O repertório apoia a análise de complexidade e a escolha de estruturas e estratégias de solução.','120 hours of complementary LeetCode practice covering arrays, hashing, binary search, trees, graphs, heaps, dynamic programming and backtracking. This experience supports complexity analysis and the selection of data structures and solution strategies.')+'</p><a href="#leetcode-practice">'+tr('Ver experiência complementar e desafios de referência','See complementary experience and reference challenges')+'</a></article>'
    return '<p>'+intro+'</p><nav class="skill-cluster-nav" aria-label="'+tr('Especialidades','Specialties')+'">'+''.join(navigation)+'</nav><div class="skill-clusters">'+''.join(body)+practice+'</div>'
