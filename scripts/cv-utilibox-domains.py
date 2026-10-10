"""Present Utilibox by application domain, with representative tools."""
import html
import runpy
from pathlib import Path

GROUPS=[
 ('decisao','Decisão multicritério e gestão','Multicriteria decisions and management', ['Gestão'],
  'Ferramentas para estruturar problemas, comparar alternativas e priorizar ações. A ideia central é tornar métodos de decisão utilizáveis em interfaces com critérios, pesos, rankings e visualizações, aproximando análise quantitativa e decisões de gestão.',
  'Tools for structuring problems, comparing alternatives and prioritizing actions. The central idea is to make decision methods usable through interfaces with criteria, weights, rankings and visualizations, connecting quantitative analysis to management decisions.',
  'AHP, TOPSIS e PROMETHEE; Pareto, GUT, SWOT e valor monetário esperado.',
  'AHP, TOPSIS and PROMETHEE; Pareto, GUT, SWOT and expected monetary value.',
  'Modelagem de critérios, consistência, sensibilidade e apresentação de resultados.',
  'Criteria modeling, consistency, sensitivity and result presentation.', ['ahp-online','topsis','promethee']),
 ('producao','Engenharia de produção, Lean e melhoria contínua','Production engineering, Lean and continuous improvement', ['Engenheiro de Produção 5.0'],
  'Aplicações para compreender o fluxo de trabalho, identificar gargalos, reduzir setup e acompanhar melhorias. O conjunto conecta ferramentas Lean a métricas de processo, dimensionamento de capacidade e aprendizagem estruturada, com relação ao MBA Operational Excellence em andamento.',
  'Applications for understanding workflows, identifying bottlenecks, reducing setup and tracking improvements. This group connects Lean tools to process metrics, capacity sizing and structured learning, relating to the ongoing Operational Excellence MBA.',
  'VSM, SMED, PDSA, A3, estudo de tempos e teoria das filas.',
  'VSM, SMED, PDSA, A3, time study and queueing theory.',
  'Tradução de métodos industriais em cálculos, modelos visuais e acompanhamento de ações.',
  'Translating industrial methods into calculations, visual models and action tracking.', ['vsm','smed','pdsa-manager']),
 ('financas','Finanças, investimentos e análise econômica','Finance, investments and economic analysis', ['Finanças & Juros'],
  'Simuladores que transformam fluxos de caixa, taxas, custos e prazos em indicadores comparáveis. A aplicação vai da avaliação de projetos e viabilidade econômica ao planejamento financeiro, crédito e comparação de cenários.',
  'Simulators translating cash flows, rates, costs and periods into comparable indicators. Applications range from project appraisal and economic feasibility to financial planning, credit and scenario comparison.',
  'VPL, TIR, payback, WACC, ponto de equilíbrio, juros e amortização.',
  'NPV, IRR, payback, WACC, break-even, interest and amortization.',
  'Matemática financeira, modelagem de cenários e explicação de indicadores ao usuário.',
  'Financial mathematics, scenario modeling and explaining indicators to users.', ['calculadora-payback-vpl-tir','calculadora-wacc','simulador-ponto-de-equilibrio']),
 ('trabalho','Pessoas, remuneração e regras de cálculo','People, compensation and calculation rules', ['Salário & Trabalho','Jurídico (Básico)'],
  'Ferramentas para explorar remuneração, descontos, benefícios e cálculos de trabalho. O domínio evidencia a transformação de regras e parâmetros em simuladores com entradas verificáveis e resultados compreensíveis.',
  'Tools for exploring compensation, deductions, benefits and employment calculations. This domain demonstrates translating rules and parameters into simulators with checkable inputs and understandable results.',
  'Salário líquido, horas extras, férias, rescisão e estimativas de tributos e benefícios.',
  'Net salary, overtime, vacation pay, termination and tax and benefit estimates.',
  'Regras parametrizadas, cálculos condicionais, datas e organização de informações.',
  'Parameterized rules, conditional calculations, dates and information organization.', ['calculadora-salario-liquido-br','calculadora-horas-extras','calculadora-fgts-rescisao-multa-40']),
 ('conhecimento','Conhecimento, escrita e aprendizagem','Knowledge, writing and learning', ['Escrita','Tools Premium'],
  'Produtos para organizar ideias, conteúdos e relações, mantendo contexto ao longo da escrita e do estudo. Narra e UtiliNotas trabalham a organização do conhecimento; flashcards acrescentam planejamento de revisões e repetição espaçada.',
  'Products organizing ideas, content and relationships while retaining context throughout writing and study. Narra and UtiliNotas support knowledge organization; flashcards add review planning and spaced repetition.',
  'Entidades e relações, Markdown, notas conectadas, SM-2 e exportação de conteúdos.',
  'Entities and relationships, Markdown, connected notes, SM-2 and content export.',
  'Modelagem de domínio, persistência local, edição e experiências de aprendizagem.',
  'Domain modeling, local persistence, editing and learning experiences.', ['narra','utilinotas','anki-flashcards']),
 ('criacao','Criação visual, IA aplicada e marketing','Visual creation, applied AI and marketing', ['Design & Arte','Marketing & Growth'],
  'Ferramentas que conectam criação de conteúdo, edição visual e análise comercial. O repertório combina interação gráfica no navegador, geração de conteúdo com IA e indicadores para compreender aquisição de clientes e valor econômico.',
  'Tools connecting content creation, visual editing and commercial analysis. This experience combines browser graphics interaction, AI content generation and indicators for understanding customer acquisition and economic value.',
  'Edição vetorial e 3D, carrosséis com IA, LTV e CAC.',
  'Vector and 3D editing, AI-generated carousels, LTV and CAC.',
  'Interfaces criativas, integração de IA e tradução de métricas de growth em ferramentas.',
  'Creative interfaces, AI integration and translating growth metrics into tools.', ['editor-3d','gerador-carrossel-instagram','calculadora-ltv-cac-ads']),
 ('documentos','Documentos, arquivos e produtividade digital','Documents, files and digital productivity', ['PDF & Produtividade','Conversores & Utilidades'],
  'Utilitários que simplificam tarefas recorrentes com documentos, imagens e formatos. A ideia central é reduzir etapas de trabalho por meio de interfaces diretas para manipular arquivos e produzir saídas reutilizáveis.',
  'Utilities simplifying recurring tasks with documents, images and formats. The central idea is to reduce workflow steps through direct interfaces for manipulating files and producing reusable outputs.',
  'Conversão, compressão, divisão e união de PDFs, imagens e geração de QR codes.',
  'Conversion, compression, PDF splitting and merging, images and QR-code generation.',
  'Processamento de arquivos, formatos, exportação e desenho de fluxos de interação.',
  'File processing, formats, export and interaction workflow design.', ['unir-pdf','compressor-de-imagem','gerador-qr-code']),
 ('saude','Bem-estar, corpo e informação gestacional','Wellbeing, body metrics and pregnancy information', ['Saúde & Corpo','Saúde Feminina'],
  'Calculadoras informativas para explorar medidas corporais, atividade física, ciclos e cronogramas gestacionais. Esse conjunto amplia a experiência de desenvolvimento para domínios com unidades, faixas de referência e relações temporais.',
  'Informational calculators for exploring body metrics, physical activity, cycles and pregnancy timelines. This group extends development experience into domains with units, reference ranges and temporal relationships.',
  'IMC, gasto energético, pace, idade gestacional e cronogramas por semana.',
  'BMI, energy expenditure, running pace, gestational age and weekly timelines.',
  'Cálculos parametrizados, conversão de unidades e apresentação de estimativas informativas.',
  'Parameterized calculations, unit conversion and presentation of informational estimates.', ['calculadora-imc','calculadora-pace-corrida','calculadora-tempo-gestacao']),
 ('beleza','Beleza, formulação e planejamento de consumo','Beauty, formulation and consumption planning', ['Beleza Feminina'],
  'Simuladores voltados a proporções, consumo e planejamento de procedimentos de beleza. O tema mostra a aplicação de lógica de cálculo e modelagem de parâmetros a situações práticas de serviços e uso de materiais.',
  'Simulators focused on proportions, consumption and beauty-service planning. This domain demonstrates calculation logic and parameter modeling applied to practical service and material-use situations.',
  'Proporções de mistura, quantidade de produto, colorimetria e cronograma capilar.',
  'Mixing ratios, product quantities, colorimetry and hair-care schedules.',
  'Modelagem de parâmetros, estimativas de consumo e interfaces orientadas ao contexto de uso.',
  'Parameter modeling, consumption estimates and context-oriented interfaces.', ['calculadora-mistura-tinta-oxidante','calculadora-quantidade-tinta-cabelo','calculadora-cronograma-capilar']),
 ('casa','Construção, recursos e planejamento cotidiano','Construction, resources and everyday planning', ['Casa & Construção','Lazer & Família'],
  'Aplicações para estimar materiais, custos, consumo e quantidades em tarefas domésticas e planejamento cotidiano. A engenharia conecta unidades, perdas, medidas e preços a resultados que ajudam o usuário a planejar recursos.',
  'Applications estimating materials, costs, consumption and quantities in household tasks and everyday planning. The engineering connects units, waste allowances, measurements and prices to outputs helping users plan resources.',
  'Área, preço por m², materiais, consumo elétrico e dimensionamento de quantidades.',
  'Area, price per square meter, materials, electricity use and quantity sizing.',
  'Estimativa quantitativa, conversões, regras de consumo e comparação de custos.',
  'Quantitative estimation, conversions, consumption rules and cost comparison.', ['calculadora-piso-azulejo','calculadora-de-tinta','calculadora-consumo-energia-eletrica']),
 ('tempo','Tempo, organização e foco','Time, organization and focus', ['Tempo & Datas'],
  'Ferramentas para organizar duração, datas, prazos e ciclos de trabalho. O conjunto traduz operações temporais e métodos de foco em interações simples para planejamento pessoal e produtividade.',
  'Tools organizing duration, dates, deadlines and work cycles. This group translates time operations and focus methods into simple interactions for personal planning and productivity.',
  'Dias úteis, intervalos, cronômetro, contagem regressiva e Pomodoro.',
  'Business days, intervals, stopwatch, countdown and Pomodoro.',
  'Lógica temporal, estado de interface, eventos e desenho de rotinas de produtividade.',
  'Temporal logic, interface state, events and productivity routine design.', ['pomodoro','calculadora-dias-uteis','relogio-cronometro-contador']),
]

def render(tools, language='pt'):
    en=language=='en';tr=lambda pt,eng:eng if en else pt;esc=lambda s:html.escape(str(s),quote=True)
    registry=runpy.run_path(str(Path(__file__).with_name('cv-project-links.py')))['REGISTRY']
    catalog=runpy.run_path(str(Path(__file__).with_name('cv-english-catalogs.py')))
    names={t['slug']:catalog['TOOL_TITLES'][i] if en else t['name'] for i,t in enumerate(tools)}
    aliases={g[0]:[] for g in GROUPS}
    example_groups={slug:g[0] for g in GROUPS for slug in g[-1]}
    method_groups={slug:'decisao' for slug in ['ahp-online-free','promethee-analysis','topsis-online','tomada-de-decisao','decision-maker','analise-pareto','matriz-gut','matriz-swot','matriz-eisenhower','arvore-decisao','arvore-decisao-ml']}
    method_groups.update({slug:'producao' for slug in ['folha-a3','estudo-de-tempos','teoria-das-filas','queueing-theory','arvore-ctc']})
    for tool in tools:
        categories={c['title'] for c in tool['categories']}
        # Put shared production/management methods with production engineering.
        group=next((g for g in GROUPS if g[0]=='producao' and categories.intersection(g[3])),None)
        group=group or next((g for g in GROUPS if categories.intersection(g[3])),GROUPS[0])
        key=example_groups.get(tool['slug'],method_groups.get(tool['slug'],group[0]))
        aliases[key].append(tool['slug'])
    navigation=[];cards=[]
    for key,pt_title,en_title,categories,pt_text,en_text,pt_methods,en_methods,pt_skill,en_skill,examples in GROUPS:
        title=en_title if en else pt_title
        navigation.append('<a href="#utilibox-area-'+key+'">'+esc(title)+'</a>')
        card='<article class="skill-cluster utilibox-domain" id="utilibox-area-'+key+'">'+''.join('<span class="tool-context-anchor" id="utilibox-tool-'+esc(slug)+'"></span>' for slug in aliases[key])+'<h3>'+esc(title)+'</h3><p>'+esc(en_text if en else pt_text)+'</p>'
        card+='<p><strong>'+tr('Métodos e temas: ','Methods and topics: ')+'</strong>'+esc(en_methods if en else pt_methods)+'</p><p><strong>'+tr('Habilidades demonstradas: ','Demonstrated capabilities: ')+'</strong>'+esc(en_skill if en else pt_skill)+'</p>'
        links=[]
        for slug in examples:
            name=names[slug];url=registry['utiliboxTools'].get(slug)
            links.append('<a href="'+esc(url)+'" target="_blank" rel="noopener noreferrer">'+esc(name)+'</a>' if url else esc(name))
        card+='<p class="utilibox-examples"><strong>'+tr('Exemplos: ','Examples: ')+'</strong>'+' · '.join(links)+'</p>'
        if key=='producao':card+='<p class="career-reference"><a href="#formacao-fm2s">'+tr('Formação relacionada: MBA Operational Excellence — em andamento','Related education: Operational Excellence MBA — in progress')+'</a></p>'
        cards.append(card+'</article>')
    intro=tr('Utilibox é um projeto independente que transforma métodos, cálculos e tarefas em ferramentas digitais. O repertório combina apoio à decisão, engenharia de produção, finanças, conhecimento, criação e utilidades do cotidiano. As áreas abaixo apresentam a ideia central e exemplos representativos de aplicação.','Utilibox is an independent project translating methods, calculations and tasks into digital tools. Its scope combines decision support, production engineering, finance, knowledge, creation and everyday utilities. The areas below present the central idea and representative application examples.')
    engineering=tr('A engenharia do produto combina Astro, JavaScript e TypeScript com interfaces interativas, modelagem de dados e lógica de cálculo. Nos módulos que exigem essas capacidades, o projeto utiliza persistência local com IndexedDB, serviços Supabase/PostgreSQL, integrações de IA com Gemini, edição de conteúdo e geração de documentos. Isso conecta conhecimento de domínio a desenvolvimento de software e experiência do usuário.','Product engineering combines Astro, JavaScript and TypeScript with interactive interfaces, data modeling and calculation logic. Modules requiring these capabilities use IndexedDB local persistence, Supabase/PostgreSQL services, Gemini AI integrations, content editing and document generation. This connects domain knowledge to software development and user experience.')
    return '<p>'+intro+'</p><nav class="skill-cluster-nav" aria-label="'+tr('Áreas do Utilibox','Utilibox domains')+'">'+''.join(navigation)+'</nav>'+''.join(cards)+'<article class="skill-cluster"><h3>'+tr('Engenharia transversal do produto','Shared product engineering')+'</h3><p>'+engineering+'</p><a href="#cv-utilibox">'+tr('Ver os cases de destaque do Utilibox','See the highlighted Utilibox cases')+'</a></article>'
