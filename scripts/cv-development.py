"""Ongoing education, algorithm practice and TraderMind MLOps coverage."""
import copy
import html

EDUCATION={
 'pt':{'id':'formacao-fm2s','from':'MAIO 2026','to':'MARÇO 2027 (PREVISÃO)', 'school':'FM2S EDUCAÇÃO E CONSULTORIA',
 'degree':'MBA OPERATIONAL EXCELLENCE — EM ANDAMENTO',
 'details':['Administração, gestão e operações.','Formação relacionada aos projetos independentes de Lean e melhoria contínua do Utilibox: VSM, SMED, PDSA, A3, Pareto e cronoanálise.'], 'status':'in-progress'},
 'en':{'id':'formacao-fm2s','from':'MAY 2026','to':'MAR 2027 (EXPECTED)', 'school':'FM2S EDUCAÇÃO E CONSULTORIA',
 'degree':'MBA OPERATIONAL EXCELLENCE — IN PROGRESS',
 'details':['Business Administration, Management and Operations.','Related independent Utilibox projects: VSM, SMED, PDSA, A3, Pareto and time study.'],'status':'in-progress'}
}

def education(data):
    for language,item in EDUCATION.items():
        values=data['languages'][language]['education']
        values[:]=[entry for entry in values if entry.get('id')!='formacao-fm2s']
        # Existing anchors retain their indices; rendering places ongoing study first.
        values.append(copy.deepcopy(item))

MLOPS=[
 ('Pipeline de dados, features e contratos de qualidade','Data pipelines, features and quality contracts',
 'Integração de extração, atualização de dados, construção de datasets e seleção de atributos em fases operacionais do TraderMind.',
 'Integrated extraction, data updates, dataset construction and feature selection into operational TraderMind pipeline stages.',
 ['Dados de mercado e indicadores em múltiplos timeframes, datasets Parquet e seleção evolutiva de atributos com EFS-AHP.', 'Verificações por fase cobrem integridade temporal, disponibilidade e saúde de features, consistência de configuração e sincronização de artefatos.'],
 ['Market data and multitimeframe indicators, Parquet datasets and evolutionary feature selection with EFS-AHP.', 'Stage checks cover temporal integrity, feature availability and health, configuration consistency and artifact synchronization.'],
 'Python · pandas · NumPy · Parquet · DEAP · EFS-AHP'),
 ('Treinamento, checkpoints e gestão de artefatos','Training, checkpoints and artifact management',
 'Organização de experimentos, treinamento e recuperação de execução, preservando a relação entre modelo, features e parâmetros.',
 'Organized experiments, training and execution recovery while preserving the relationship between models, features and parameters.',
 ['Rotinas de treinamento e comparação de classificadores, seleção de atributos e modelos de entrada e saída antecipada.', 'Checkpoints permitem retomar a busca evolutiva; modelos serializados, listas de features, configurações e logs apoiam a reprodução do fluxo.'],
 ['Classifier training and comparison routines, feature selection and entry and early-exit models.', 'Checkpoints resume evolutionary search; serialized models, feature lists, configuration and logs support workflow reproduction.'],
 'Python · scikit-learn · XGBoost · LightGBM · CatBoost · joblib · checkpoints'),
 ('Validação temporal, leakage e avaliação fora da amostra','Temporal validation, leakage and out-of-sample evaluation',
 'Separação entre seleção, calibração e avaliação temporal para comparar modelos e políticas sem contaminar o período final.',
 'Separated selection, calibration and temporal evaluation to compare models and policies without contaminating the final evaluation period.',
 ['Walk-forward, holdouts temporais, backtests e auditorias de leakage complementam o treinamento; alinhamento causal das fontes externas evita usar informação futura.', 'Políticas são escolhidas antes do teste final OOS; comparação entre operação registrada e replay/backtest apoia a investigação de divergências.'],
 ['Walk-forward, temporal holdouts, backtests and leakage audits complement training; causal external-data alignment avoids future information.', 'Policies are selected before final OOS testing; comparisons between logged operation and replay/backtest help investigate discrepancies.'],
 'Python · validação temporal · walk-forward · OOS · backtesting'),
 ('Serving de modelos e integração com MetaTrader5','Model serving and MetaTrader5 integration',
 'Integração entre artefatos de ML, serviço de inferência e terminal desktop para conectar pesquisa e operação de demonstração.',
 'Connected ML artifacts, an inference service and the desktop terminal to bridge research and demonstration operation.',
 ['API Flask carrega modelos e respectivas features por par/direção, produz predições e probabilidades e atende verificações de saída.', 'Conector Python integra dados e execução ao MetaTrader5; o serviço expõe saúde, status, modelos carregados e uptime.'],
 ['A Flask API loads models and their features by pair/direction, returns predictions and probabilities and supports exit checks.', 'A Python connector integrates data and execution with MetaTrader5; service endpoints expose health, status, loaded models and uptime.'],
 'Python · Flask · REST APIs · joblib · MetaTrader5'),
 ('Orquestração, retreino e atualização operacional','Orchestration, retraining and operational updates',
 'Coordenação do ciclo de dados, treinamento, avaliação e serviço com modos de execução distintos.',
 'Coordinated data, training, evaluation and serving cycles through distinct execution modes.',
 ['Supervisor organiza extração, dataset, EFS-AHP, treinamento, backtest e serviço; diferencia atualização de dados sem retreino e ciclo completo de retreino.', 'Execuções usam identificação de rodada e logs; rotinas de agendamento e checagem operacional apoiam manutenção do pipeline.'],
 ['The supervisor organizes extraction, datasets, EFS-AHP, training, backtesting and serving; it distinguishes data updates without retraining from full retraining cycles.', 'Runs use identifiers and logs; scheduling and operational checks support pipeline maintenance.'],
 'Python · supervisor · agendamento · logs · automação de pipeline'),
 ('Observabilidade e acompanhamento de modelos','Observability and model follow-up',
 'Conexão entre painel operacional, saúde das fases e revisão de desempenho com dados recentes.',
 'Connected the operational dashboard, pipeline stage health and performance review using recent data.',
 ['Dashboard e registros de saúde acompanham fases, treinamento e operação; APIs permitem inspecionar disponibilidade dos modelos e serviço.', 'Atualização da janela OOS e comparação entre trades registrados e backtest apoiam análise de mudança de regime e decisões de revisão do modelo.'],
 ['Dashboard and health records track stages, training and operation; APIs expose model and service availability.', 'OOS window updates and comparisons between logged trades and backtests support regime-change analysis and model review decisions.'],
 'Python · Flask · dashboard · logs · OOS · monitoramento')
]

def cases(language='pt'):
    out=[]
    for i,(pt_title,en_title,pt_text,en_text,pt_impl,en_impl,stack) in enumerate(MLOPS,1):
        out.append({'id':'case-mlops-'+str(i),'title':pt_title if language=='pt' else en_title,
          'text':pt_text if language=='pt' else en_text,'problem':pt_text if language=='pt' else en_text,
          'implementation':pt_impl if language=='pt' else en_impl,'stack':stack if language=='pt' else stack.replace('validação temporal','temporal validation').replace('agendamento','scheduling').replace('automação de pipeline','pipeline automation').replace('monitoramento','monitoring'),
          'context':'TraderMind · projeto independente de MLOps e pesquisa quantitativa' if language=='pt' else 'TraderMind · independent MLOps and quantitative research project',
          'sources':['mt5/TraderMind/PIPELINE_GUIDE.md','mt5/TraderMind/supervisor.py','mt5/TraderMind/api/app.py'],
          'skills':['MLOps','ML lifecycle','Data pipelines','Model serving','Temporal validation','Observability'],
          'limit':'Escopo de pesquisa e operação demo; sem afirmação de lucratividade ou infraestrutura cloud em produção.',
          'relatedContextAnchors':['projetos'],'depth':'Pipeline local de ML e operação demo'})
    return out

def inject(proposal):
    proposal['topics'].append({'id':'mlops','title':'MLOps — ciclo de vida de modelos no TraderMind',
      'intro':'Engenharia do ciclo de vida de ML: dos dados e experimentos à inferência, supervisão e manutenção operacional.',
      'text':['O TraderMind integra pipeline local de dados, seleção de atributos, treinamento, avaliação temporal, API de inferência, dashboard e conector MetaTrader5. O contexto é de pesquisa e operação de demonstração.'],
      'flow':['Dados e qualidade','Features e treinamento','Validação temporal','Artefatos e inferência','Supervisão e acompanhamento'], 'cases':cases()})

def enhance_editorial(editorial,language='pt'):
    out=copy.deepcopy(editorial)
    out['skillGroups'].append({'title':'MLOps e ciclo de vida de modelos' if language=='pt' else 'MLOps and model lifecycle',
      'description':'Pipelines de dados e features, checkpoints, artefatos de modelos, validação temporal, serving por API, supervisão, retreino e observabilidade.' if language=='pt' else 'Data and feature pipelines, checkpoints, model artifacts, temporal validation, API serving, supervision, retraining and observability.',
      'origin':'TraderMind — pesquisa quantitativa e operação demo integrada ao MetaTrader5.' if language=='pt' else 'TraderMind — quantitative research and demonstration operation integrated with MetaTrader5.'})
    out['skillGroups'].append({'title':'Algoritmos e resolução de problemas' if language=='pt' else 'Algorithms and problem solving',
      'description':'Prática de estruturas de dados, estratégias algorítmicas, análise de complexidade e tratamento de casos de borda.' if language=='pt' else 'Data structure practice, algorithmic strategies, complexity analysis and edge-case handling.',
      'origin':'120 horas de prática no LeetCode.' if language=='pt' else '120 hours of LeetCode practice.'})
    out['skillGroups'][5]['origin']+=(' Formação relacionada: MBA Operational Excellence em andamento na FM2S.' if language=='pt' else 'Related education: ongoing FM2S MBA in Operational Excellence.')
    out['technologyGroups'].append({'title':'MLOps — TraderMind','description':'Python, pandas, NumPy, Parquet, scikit-learn, DEAP/EFS-AHP, joblib, Flask, MetaTrader5; checkpoints, validação temporal, supervisor, logs e dashboard.' if language=='pt' else 'Python, pandas, NumPy, Parquet, scikit-learn, DEAP/EFS-AHP, joblib, Flask, MetaTrader5; checkpoints, temporal validation, supervisor, logs and dashboard.'})
    return out

def practice_markup(language='pt'):
    title='Experiência adicional e prática técnica' if language=='pt' else 'Additional experience and technical practice'
    intro='LeetCode — 120 horas de prática em algoritmos e estruturas de dados' if language=='pt' else 'LeetCode — 120 hours of algorithm and data structure practice'
    text='Prática complementar em resolução de problemas de engenharia de software, análise de complexidade de tempo e espaço, escolha de estruturas de dados e depuração de casos de borda.' if language=='pt' else 'Complementary software engineering problem-solving practice, including time and space complexity, data structure selection and edge-case debugging.'
    topics=[
      ('Arrays, strings e hashing','Arrays, strings and hashing','Two Sum, Group Anagrams, Product of Array Except Self'),
      ('Dois ponteiros, janela deslizante e busca binária','Two pointers, sliding windows and binary search','Longest Substring Without Repeating Characters, Binary Search, Search in Rotated Sorted Array'),
      ('Pilhas, listas encadeadas e intervalos','Stacks, linked lists and intervals','Valid Parentheses, Reverse Linked List, Merge Intervals'),
      ('Árvores, grafos e heaps','Trees, graphs and heaps','Binary Tree Level Order Traversal, Number of Islands, Course Schedule, Top K Frequent Elements'),
      ('Programação dinâmica e backtracking','Dynamic programming and backtracking','Coin Change, House Robber, Longest Increasing Subsequence, Subsets')]
    rows=''.join('<li><strong>'+html.escape(a if language=='pt' else b)+':</strong> '+html.escape(c)+'.</li>' for a,b,c in topics)
    label='Temas e desafios de referência' if language=='pt' else 'Topics and reference challenges'
    return '<section class="page full-page career-project-page"><div class="full-page-inner"><h2 id="cv-pratica-tecnica" class="career-section-title">'+title+'</h2><article class="career-project" id="leetcode-practice"><h3>'+intro+'</h3><p>'+text+'</p><h4>'+label+'</h4><ul class="career-deliverables">'+rows+'</ul></article></div></section>'
