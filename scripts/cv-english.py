"""English editorial content; project names and source paths stay unchanged."""
import copy
import html
import runpy
from pathlib import Path

CASES = {
'agentes-1': ('Six-agent planning council — Planejamento Xavier', 'Implemented a council of six specialized agents to support planning and replanning, with evidence for each recommendation, deterministic conflict resolution and traceable actions.', ['Strategy, execution, risk, learning, integrity and mentoring agents analyze the same planning snapshot.', 'Claims carry evidence, confidence, polarity, weight and node references; priorities and deterministic tie-breaking resolve conflicts.'], 'These are rule-based pure functions. LLM integration belongs to a separate layer; the individual agents are not autonomous LLMs.'),
'agentes-2': ('Financial signal ensemble — TraderMind', 'Designed multiagent policy experiments with signal voting, quorum and simulated annealing, separating calibration, temporal validation and out-of-sample evaluation.', ['Twelve signals support ternary voting, minimum active-agent counts and agreement thresholds.', 'Policies choose whether to follow, invert or ignore signals; the selected policy is frozen before final out-of-sample evaluation. Backward as-of joins respect publication delays.'], 'The agents are rule-based signals. Financial returns were not verified in this review.'),
'ia-1': ('Shared AI integration engine — Planejamento Xavier', 'Developed a shared AI integration layer with provider adapters, structured responses, validation, time budgets and task-specific failure handling.', ['Provider capabilities include JSON, text and grounded search; adapters support Gemini, DeepSeek, OpenAI and compatible APIs.', 'Global and per-attempt time budgets, output rejection, fallback and provider health tracking organize execution. Grounded search preserves source references.'], 'Adapters do not establish production usage, SLA or cost savings. Grounded search does not by itself demonstrate vector-based RAG.'),
'ia-2': ('AI-assisted plan review and operation contracts', 'Modeled AI-assisted review proposals with reference validation, alternatives, operations and follow-up, connecting suggested changes to the actual plan.', ['Authorized context contains real IDs, capacity, diagnostics and prior decisions.', 'Normalized operations include dependencies, affected occurrences, expected update timestamps, context fingerprints and validation issues.'], 'Autonomy and behavioral effectiveness were not measured.'),
'ia-3': ('AI-assisted lesson planning — ClassPlanner', 'Integrated Gemini lesson-plan generation into a web application using pedagogical context, Brazilian BNCC curriculum references and structured objectives, methodology and assessment.', ['Prompts combine class, subject, duration, resources, assessment and curriculum skills.', 'Structured JSON responses are parsed into the planning workflow.'], 'JSON parsing does not establish complete schema validation or validated pedagogical quality; the module includes demos and implementation inconsistencies.'),
'ia-4': ('Hybrid conversational CRM — Instagram Conversion CRM', 'Built a hybrid AI-and-rules conversation flow with interaction history, action contracts, failure handling and human handoff.', ['Conversation state and history provide context for the decision engine.', 'Action normalization, retries and handoff connect suggestions to the CRM workflow.'], 'SDK configuration depends on another local project. Conversion uplift and live operation were not verified.'),
'ml-1': ('EFS-AHP — doctoral research framework', 'Developed EFS-AHP as doctoral research combining feature selection, evolutionary algorithms and multicriteria decision analysis, comparing ML alternatives and analyzing performance, dimensionality and computational cost.', ['Experiments compare methods including Random Forest, LASSO and dimensionality-reduction approaches.', 'Python notebooks and evolutionary routines organize datasets, baselines and statistical analysis; AHP supports comparison of alternatives.'], 'Final publications, metrics and statistical significance require confirmation. Dimensionality reduction and feature selection are distinct methods.'),
'ml-2': ('TraderMind — experiments and inference integration', 'Structured quantitative experiments and inference components, connecting data preparation and model/policy evaluation to an API and the MetaTrader5 terminal.', ['Time-series preparation and feature engineering feed model and policy experiments.', 'API and desktop connector components keep research, inference and execution responsibilities separate.'], 'Temporal validation should not be generalized to every notebook. Verified financial returns are not claimed.'),
'visao-1': ('DVR — feedback, datasets and classifier training', 'Implemented a computer-vision workflow with detection, example review and custom classifier training from a pretrained model, integrating epoch monitoring, checkpoints, temporal stabilization and persistent alerts.', ['Reviewed examples form a training dataset; transfer learning and callbacks organize training and checkpoints.', 'Temporal voting and a persistent alert outbox connect detection to operational notifications.'], 'Training code was found but was not executed in this review. Generalization across cameras and similarity between dataset splits need evaluation.'),
'visao-2': ('Mocap — browser inference and visualization', 'Developed browser pose-estimation prototypes integrating inference, keypoint visualization and temporal smoothing to explore motion capture and 3D interaction.', ['Existing pose models process video and webcam input in the browser.', 'Keypoint rendering, smoothing and 3D resources connect inference to interactive visualization.'], 'These applications integrate existing models. Frame rate, latency and retargeting quality were not measured.'),
'sia-cases-1': ('PLANAGRO — inputs, applications and agronomic rules', 'Developed agricultural planning components in PLANAGRO, translating input application, dosage, withholding periods, drift and budgets into rules and interfaces connected to operational data.', ['Domain rules represent dosage, withholding periods, drift and application constraints.', 'Planning interfaces connect operational inputs and budget information to the application workflow.'], 'Code demonstrates rules, but does not establish agronomic validation or deployment across every operation.'),
'sia-cases-2': ('Irrigation — scheduling, genetic algorithms and Kc modeling', 'Explored irrigation scheduling, genetic algorithms and neural modeling of crop coefficient Kc, working with variable encoding, normalization, network parameters and operational backend integration.', ['Categorical encoding and normalization prepare variables such as farm, phase, month and soil.', 'Neural training, serialized model restoration and evolutionary experiments explore irrigation-related decisions.'], 'The reviewed evaluation reuses training data; historical Kc also appears among inputs/targets and output adjustments are heuristic. Out-of-sample accuracy is not established.'),
'sia-cases-3': ('Spraying audit — maps and field execution', 'Built spraying-audit components using spatial and operational data, relating trajectories, speed, field blocks and services to support investigation of field execution.', ['Maps connect movement and speed to field blocks and operational records.', 'Audit interfaces make execution patterns available for operational review.'], 'Previously declared problem-reduction metrics are not attributed to this specific module without confirmation of initiative, period and measurement.'),
'sia-cases-4': ('Dry matter — harvest forecasting and readiness', 'Implemented dry-matter analysis and harvest-forecast components connecting readings, varieties and parameters to charts and monitoring rules.', ['Equations and parameters relate dry-matter observations to harvest readiness.', 'Charts and operational interfaces support monitoring by variety and field context.'], 'The evidence consists of equations and rules; it does not automatically establish a trained ML model or validated forecast accuracy.'),
'sia-cases-5': ('Field notebook and purchasing — local data and synchronization', 'Developed field-data collection and purchase-request workflows with local storage, process components and synchronization routines integrated with domain-specific backend services.', ['Dexie/IndexedDB stores field and purchasing data locally.', 'Synchronization handlers and domain APIs connect local records to the backend.'], 'Complete offline behavior, conflict resolution and synchronization success rates were not measured in this review.'),
'sia-cases-6': ('UGB management, people and improvement suggestions', 'Modeled business-unit and people-management applications and improvement-suggestion workflows combining organizational records, history, assessments, roles and documents.', ['Business units, employees and roles share domain models and reusable components.', 'Assessments, history, 5S and improvement workflows organize management information.'], 'Submodules share architecture and are not independent products. HR outcomes are not claimed without evidence.'),
'sia-cases-7': ('Commercial monitoring, forecasts and pallet movements', 'Developed commercial and logistics components connecting records and forecasts to management interfaces and operational pallet/container data.', ['Commercial entries, forecasts and exchange-rate information support operational views.', 'Pallet and container movements link logistics records to management interfaces.'], 'A forecast screen name does not prove an ML algorithm. Deployment and measured gains require project-specific attribution.'),
'dados-1': ('Modular ETL and operational data quality', 'Structured integration pipelines with reusable importers, batch processing and domain rules for production, packing, quality and people, organizing operational data for analysis and decisions.', ['Node.js and SQL importers separate extraction, transformation and domain-specific processing.', 'Batch persistence, joins and aggregation connect ERP and operational records to indicators.'], 'Historical dependencies and commented routines remain in the archive. Module counts do not establish independent products or deployment of every routine.'),
'mobile-1': ('SIAgro — mobile operational data collection', 'Developed SIAgro mobile modules for work orders, production records and quality using React Native/Expo, business-object modeling, local persistence and operational indicators.', ['Mobile workflows organize work orders, employees, targets and quality records.', 'Reusable local persistence and API integration connect collection and dashboard components.'], 'Complete offline synchronization, operational GPS usage and app publication require confirmation.'),
'mobile-2': ('Hospital indicators and academic gamification', 'During the hospital internship, developed a Java EE web system for indicators and assessments. At university, built a project-management application with gamification and persistence, exploring progression rules and task organization.', ['EBSERH: Java EE, EJB, JSF, PrimeFaces and JPA/Hibernate for hospital indicators and assessments.', 'The Game Project: persistent tasks, progression rules, scheduling and an interactive project timeline.'], 'Hospital internship and university work are separate contexts. Code reuse does not establish another hospital employment experience.'),
'decisao-1': ('Utilibox — multicriteria analysis, queues and applied methods', 'Implemented decision-support and learning tools using multicriteria methods, queueing theory, simulation, financial mathematics and spaced repetition, translating models into explainable interfaces and calculations.', ['AHP, TOPSIS and PROMETHEE connect criteria and alternatives to decision analysis.', 'Queueing, financial and spaced-repetition tools apply domain methods in interactive software.'], 'The catalog contains 136 unique slugs with overlapping categories. Live status is catalog-declared; availability, external validation and actual usage were not verified.'),
'decisao-2': ('Cartola and logistics — decisions under constraints', 'Developed pipelines connecting data and optimization to decisions, exploring team selection under budget/formation constraints and routing with geographical visualization.', ['Cartola combines performance data and probabilistic estimates with constrained team selection.', 'Logistics prototypes combine routes, maps and optimization experiments.'], 'Solution quality and comparison metrics require confirmation. NDVI references alone do not establish an operational remote-sensing pipeline.'),
'produto-1': ('Narra and UtiliNotas — domain and knowledge applications', 'Built narrative and knowledge-organization modules with entity relationships, contextual assistance, response traceability and note interoperability.', ['Related entities and linked notes organize narrative and knowledge contexts.', 'Contextual assistance and interoperability connect editing, information and responses.'], 'Intent dispatch alone does not establish a multiagent architecture or implemented vector RAG/MCP.'),
'produto-2': ('Marketplace, automation and 3D interaction', 'Structured products and prototypes with access rules, integrations and supervised workflows, including a marketplace, commercial collection, personal finance and a narrative 3D experience.', ['Product roles and integrations organize campaigns and commercial workflows.', 'Supervised automation and interactive prototypes explore different product domains.'], 'Revenue, scale and publication are not claimed without data. Payment integrations and planned features have varying maturity.'),
'infra-1': ('IT operations management — Agrodan', 'Managed IT operations, integrating support, servers, networks, continuity, ERP and IoT initiatives with delivery of technology services and solutions.', ['Professional responsibilities cover support, Windows/Linux administration, Active Directory and corporate networks.', 'Backup/recovery, virtualization, monitoring, security and IoT belong to the declared IT management scope.'], 'Source: the existing professional CV, rather than repository code audited in this review.'),
'infra-2': ('MetaTrader5 desktop connector — TraderMind', 'Built a Python connector to the MetaTrader5 desktop terminal, integrating market/account data with the documented research and execution workflow.', ['The connector uses the MetaTrader5 package and requires an authenticated local terminal.', 'Candles and account data connect policy research with separate API, dashboard and execution components.'], 'This is desktop integration, not a custom Qt, Electron, WPF or Swing GUI application.'),
'grafica-1': ('Dente de Leão — interactive narrative world', 'Built a narrative 3D prototype with character controls, camera, interaction, physics and HUD, organizing state and rendering with React Three Fiber, Rapier and Zustand.', ['World, player, camera and interactions are organized into game modules.', 'React Three Fiber, Rapier and Zustand integrate rendering, physics and application state.'], 'A browser prototype; commercial release, a proprietary engine or Unity development are not established.'),
'grafica-2': ('Maps, models and spatial exploration', 'Explored spatial visualization and 3D models with Leaflet and Three.js, building map, drawing, routing and scene-interaction interfaces.', ['Logistics and Leaflet projects combine map interfaces and routing components.', 'Three.js experiments include scenes, interaction and model loading using third-party libraries.'], 'This does not establish comprehensive GIS specialization, operational remote sensing or authorship of rendering libraries.'),
}

PRIORITIES = [
('AHP Online — multicriteria decisions and consistency', 'Developed a multicriteria decision tool organizing criteria, comparisons and alternatives into an analysis and project-export workflow.', ['Saaty-scale comparisons and consistency calculations assess the coherence of judgments.', 'Interactive decision modeling presents results and supports project export.'], 'Astro · JavaScript · AHP · comparison matrices · consistency'),
('TOPSIS and PROMETHEE — rankings and sensitivity', 'Implemented tools for comparing alternatives with configurable criteria, weights and preferences, applying multicriteria methods to management decisions.', ['TOPSIS ranks alternatives by closeness to the ideal solution, with configurable weights and criterion directions.', 'PROMETHEE I and II include preference functions and real-time sensitivity analysis.'], 'Astro · JavaScript · TOPSIS · PROMETHEE · sensitivity analysis'),
('Queueing theory — capacity, waiting and service sizing', 'Developed calculators and visualizations relating demand, service capacity and waiting, supporting study and comparison of service configurations.', ['Calculation routines implement M/M/1, M/M/c, M/D/1, M/M/1/K and Erlang-B/C models.', 'Server-count comparisons and sensitivity curves explore changes in arrival rates.'], 'JavaScript · operations research · queueing models · sensitivity curves'),
('VSM, SMED, PDSA and A3 — production engineering and continuous improvement', 'Translated process-improvement methods into digital tools for mapping flows, analyzing setup, structuring problems and tracking learning cycles.', ['VSM models steps, processing, waiting, uptime, inventory and bottlenecks, with lead-time, takt and PCE metrics.', 'SMED explores internal/external activities, conversion and parallelization; PDSA and A3 structure follow-up and action plans.'], 'Astro · JavaScript · Lean · VSM · SMED · PDSA · A3'),
('Economic analysis — NPV, IRR, payback and scenarios', 'Implemented economic-analysis tools transforming cash flows, costs and financing conditions into comparable indicators.', ['Simple and discounted payback, NPV and IRR calculations support investment analysis.', 'Complementary tools address WACC, break-even and Price, SAC and SAM repayment systems.'], 'JavaScript · financial mathematics · cash flows · investment analysis'),
('Pareto, GUT and SWOT — prioritization and management analysis', 'Developed management tools organizing problems, criteria and scenarios into rankings, charts and decision structures.', ['Pareto includes cumulative curves; GUT ranks severity, urgency and trend; SWOT supports cross-analysis of strategies.', 'Decision trees include chance/outcome nodes, expected monetary value and optimal-path identification.'], 'JavaScript · Pareto · GUT · SWOT · EMV · decision visualization'),
('Narra and UtiliNotas — knowledge, context and persistence', 'Built narrative and knowledge-organization applications with related entities, linked notes and contextual assistance.', ['Markdown editing, internal links and file trees connect note organization to usage context.', 'IndexedDB persistence manages transactions and failures; AI assistance resides in dedicated modules.'], 'Astro · JavaScript · Markdown · IndexedDB · entity modeling · contextual AI'),
('Flashcards — spaced repetition and study tracking', 'Implemented a study application organizing cards and reviews through spaced repetition, retention tracking and export.', ['SM-2, due-card selection, suspension/resumption and review forecasting organize study.', 'Anki Desktop TSV and PDF exports support structured decks and content.'], 'JavaScript · SM-2 · local persistence · TSV · PDF'),
('QMS — audits, records and quality management', 'Developed quality-management modules organizing audits, records and roles with process follow-up and local storage.', ['Audit, configuration and responsibility models support management interfaces.', 'Dexie/IndexedDB local data and synchronization handlers connect workflows.'], 'React · JavaScript · Dexie · IndexedDB · synchronization'),
('Field quality — checklists and operational assessments', 'Developed field-quality assessment workflows with checklists, responses and integration between interfaces and the domain backend.', ['Checklists and responses use Dexie/IndexedDB local persistence.', 'Synchronization routines and corresponding backend routes were located in the archive.'], 'React · JavaScript · Dexie · IndexedDB · Node.js · domain APIs'),
('Packing and box handling — operational interfaces', 'Developed packing and box-handling interfaces organizing access to operations and connecting events to monitoring components.', ['Separate packing and box-handling components structure the corporate frontend.', 'Socket event integration is present in the module code.'], 'React · JavaScript · socket events · operational interfaces'),
]

EDITORIAL = {
'skillGroups': [
{'title':'AI, agents and automation','description':'LLM integration, structured outputs, context, fallback and rule-based coordination; computer vision and process automation.','origin':'Planejamento Xavier, ClassPlanner, CRM, DVR and professional experience at Bayer.'},
{'title':'Machine Learning and research','description':'Feature selection, evolutionary algorithms, comparative experiments, ensembles and temporal validation.','origin':'EFS-AHP doctoral research, TraderMind and exploratory irrigation modeling.'},
{'title':'Software engineering','description':'Web and mobile applications, domain modeling, APIs, persistence, offline collection, synchronization and desktop integrations.','origin':'SIA/SIAgro, EBSERH, The Game Project and independent products.'},
{'title':'Data and decisions','description':'ETL, ERP integration, SQL, indicators, operational auditing, multicriteria methods and constrained optimization.','origin':'Agrodan, Labrunier, Utilibox, Cartola Oracle and Logística.'},
{'title':'Leadership and operations','description':'Technology management, business alignment, team development, PMBOK, Scrum, Kanban, governance, infrastructure and security.','origin':'Technology Enablement Lead, Head of Technology, IT Manager and IT Business Partner roles.'},
{'title':'Products and applied methods','description':'Product development, multicriteria methods, operations research, financial analysis, continuous improvement, learning and knowledge management.','origin':'Utilibox: AHP, TOPSIS, PROMETHEE, queues, VSM/SMED, PDSA, NPV/IRR, Narra and UtiliNotas; SIA: quality, packing and operations.'}],
'technologyGroups': [
{'title':'Languages','description':'Python, SQL, JavaScript, TypeScript and Java.'},
{'title':'Web, APIs and products','description':'React, Next.js, Astro, Node.js, Express, Flask, Java EE, JSF, PrimeFaces and Supabase.'},
{'title':'Mobile and offline','description':'React Native, Expo, AsyncStorage, IndexedDB and Dexie; integrations with the MetaTrader5 terminal.'},
{'title':'Data and persistence','description':'Oracle, PostgreSQL, SQL Server, SQLite, BigQuery, pandas, NumPy, Parquet and Sequelize.'},
{'title':'ML and computer vision','description':'scikit-learn, XGBoost, LightGBM, CatBoost, SciPy, DEAP, PyTorch, YOLO, OpenCV, TensorFlow.js and MediaPipe.'},
{'title':'Decision and visualization','description':'AHP, TOPSIS, PROMETHEE, OR-Tools, GLPK, Power BI, Leaflet, Three.js and React Three Fiber.'},
{'title':'Automation and integration','description':'LLM APIs, Gemini, Playwright, Puppeteer, Telegram Bot API, Power Platform and RPA.'},
{'title':'Cloud and operations','description':'Azure, GCP, AWS, Docker, Kubernetes, Terraform, Airflow, dbt, MLflow, Windows/Linux, Active Directory and Zabbix/GLPI.'}],
}

LABELS = {
'Projetos e engenharia aplicada na Agrodan':'Projects and applied engineering at Agrodan',
'Ecossistema SIA / SIAgro · experiência profissional':'SIA / SIAgro ecosystem · professional experience',
'Utilibox — produtos e métodos aplicados':'Utilibox — products and applied methods',
'Decisão, pesquisa operacional, engenharia de produção, finanças e conhecimento · produto independente':'Decisions, operations research, production engineering, finance and knowledge · independent product',
'Pesquisa aplicada e formação':'Applied research and education',
'Doutorado, estágio hospitalar e projetos de faculdade':'Doctoral research, hospital internship and university projects',
'Projetos de IA, sistemas multiagentes e Machine Learning':'AI, multiagent systems and Machine Learning projects',
'Desenvolvimento independente e pesquisa quantitativa':'Independent development and quantitative research',
'Otimização e integração de sistemas':'Optimization and systems integration',
'Pesquisa quantitativa e desenvolvimento independente':'Quantitative research and independent development',
'Coordenação de agentes por regras; integração de LLMs em camada própria.':'Rule-based agent coordination; LLM integration in a separate layer.',
'Pesquisa com agentes de sinais; sem resultado financeiro validado neste levantamento.':'Signal-agent research; financial returns were not validated in this review.',
'Modelagem exploratória; desempenho fora da amostra ainda não demonstrado.':'Exploratory modeling; out-of-sample performance is not established.',
'Protótipos e estudos de interação e visualização.':'Interaction and visualization prototypes and studies.',
'Engenharia e tecnologias:':'Engineering and technologies:', 'Trajetória Agrodan':'Agrodan career context',
'Estágio hospitalar':'Hospital internship', 'Ferramenta e fontes':'Tool and sources', 'Módulo e fontes':'Module and sources',
'Ferramenta':'Tool', 'Módulo':'Module', 'Detalhes técnicos':'Technical details', 'Contexto e projetos':'Context and projects', 'Detalhes técnicos e fontes':'Technical details and sources', 'Doutorado':'Doctoral research',
'Índice do acervo técnico':'Technical archive contents', 'Acervo técnico e fontes dos projetos':'Technical archive and project sources',
'CV original':'Original CV', 'Versão textual completa':'Complete text version', 'Dados e fontes':'Data and sources',
'Acervo técnico completo · cases, catálogos e fontes':'Complete technical archive · cases, catalogs and sources',
'SIA / Agrodan':'SIA / Agrodan', 'Utilibox e métodos aplicados':'Utilibox and applied methods', 'IA e multiagentes':'AI and multiagent systems',
'Incluir acervo técnico no PDF':'Include the technical archive in the PDF',
}

def translate_labels(text):
    for source, target in sorted(LABELS.items(), key=lambda pair: -len(pair[0])):
        text = text.replace(source, target)
    return text

def build_locale(data):
    ext = data['extensions']
    cases = []
    for c in ext['cases']:
        key = c['id'].removeprefix('case-')
        if key.startswith('globalcom-'):
            globalcom=runpy.run_path(str(Path(__file__).with_name('cv-globalcom.py')))
            cases.append(next(record for record in globalcom['records']('en') if record['id']==c['id']))
            continue
        title, text, implementation, limit = CASES[key]
        record = copy.deepcopy(c)
        record.update(title=title, text=text, implementation=implementation, limit=limit,
                      problem=text, skills=translate_stack(ext['editorial']['caseStacks'][key]).split(' · '), depth='Depth is described by the implementation and source evidence.',
                      context='Professional experience — Agrodan' if 'vinculo-agrodan' in c['relatedContextAnchors'] else 'Doctoral research' if key=='ml-1' else 'Hospital internship and university project' if key=='mobile-2' else 'Independent projects, prototypes and research',
                      stack=translate_stack(ext['editorial']['caseStacks'][key]))
        cases.append(record)
    if len(ext['priorityCases']) != len(PRIORITIES):
        raise ValueError('English priority translations must match the selected projects.')
    priorities = []
    for c, (title, text, implementation, stack) in zip(ext['priorityCases'], PRIORITIES):
        record = copy.deepcopy(c)
        record.update(title=title, text=text, implementation=implementation, stack=stack,
                      context='Professional experience — Agrodan' if c['section']=='agrodan' else 'Independent product — Utilibox')
        priorities.append(record)
    globalcom=runpy.run_path(str(Path(__file__).with_name('cv-globalcom.py')))
    return {'cases':cases, 'priorityCases':priorities, 'editorial':globalcom['enhance_editorial'](EDITORIAL,'en')}

def translate_stack(text):
    phrases = {'contratos tipados':'typed contracts','resolução de conflitos':'conflict resolution','validação temporal':'temporal validation','APIs de LLM':'LLM APIs','telemetria':'telemetry','contratos de operações':'operation contracts','validação referencial':'reference validation','memória conversacional':'conversation history','APIs operacionais':'operational APIs','regras agronômicas':'agronomic rules','algoritmos genéticos':'genetic algorithms','rede neural':'neural network','normalização':'normalization','dados geoespaciais':'geospatial data','trajetória':'trajectory','velocidade':'speed','curvas e equações':'curves and equations','gráficos':'charts','dados de campo':'field data','sincronização':'synchronization','modelagem organizacional':'organizational modeling','avaliações':'assessments','histórico':'history','dados comerciais':'commercial data','importação em lotes':'batch import','simulação':'simulation','entidades e relações':'entities and relationships','redes':'networks','APIs locais':'local APIs'}
    for source, target in phrases.items(): text=text.replace(source,target)
    return text

def archive_section(id, title, body):
    return '<section id="'+id+'" class="chapter"><h2>'+html.escape(title)+'</h2>'+body+'</section>'

def paragraphs(values): return ''.join('<p>'+html.escape(v)+'</p>' for v in values)
def bullets(values): return '<ul>'+''.join('<li>'+html.escape(v)+'</li>' for v in values)+'</ul>'
PUBLIC_LINKS=runpy.run_path(str(Path(__file__).with_name('cv-project-links.py')))
def sources(values): return PUBLIC_LINKS['sources'](values,'en')
def source_heading(values): return PUBLIC_LINKS['source_heading'](values,'en')
def source_block(values): return PUBLIC_LINKS['source_block'](values,'en')
PROJECT_DETAILS=runpy.run_path(str(Path(__file__).with_name('cv-project-details.py')))

def build_archive(base, data, locale):
    catalog = runpy.run_path(str(base/'scripts/cv-english-catalogs.py'))
    globalcom=runpy.run_path(str(base/'scripts/cv-globalcom.py'))
    catalog['PROJECTS'][globalcom['ID']]=globalcom['EN_PROJECT']
    ext = data['extensions']
    sections = [archive_section('vinculos','Projects and career context',
      '<article id="vinculo-agrodan"><h3>Agrodan — professional SIA / SIAgro ecosystem</h3><p>Field operations, packing, people, planning, purchasing, quality and commercial modules belong to the professional Agrodan trajectory. Individual modules are not assigned to specific roles or dates from commit timestamps.</p>' + bullets(['IT Business Partner','IT Manager','Head of Technology','Administrative management — supply chain, controlling and HR operations']) + '<a href="#fullExperiencePrimary">Professional experience</a></article><h3>EFS-AHP — doctoral research</h3><p>Feature selection, evolutionary algorithms and multicriteria analysis are associated with doctoral research at CÉSAR School.</p><a href="#formacao-1">Education</a><h3>EBSERH and The Game Project</h3><p>EBSERH belongs to the hospital internship. The Game Project was university work. Other projects include independent products, research, studies and entrepreneurial initiatives; individual company/date attribution is not inferred.</p>')]
    sections.append(archive_section('extensao','Scope of professional and technical experience', paragraphs([
      'The trajectory combines software, data and automation engineering with technology leadership and applications in agriculture, operations, education, finance, production, planning and digital products.',
      'Depth is described by implemented domain models, persistence, integrations, data pipelines, research methods, interfaces and prototypes. The number of modules does not establish independent products or a seniority rating.'])))
    for prefix in dict.fromkeys(c['id'].split('-')[1] for c in locale['cases']):
        selected=[c for c in locale['cases'] if c['id'].startswith('case-'+prefix+'-')]
        body=''
        for c in selected:
            body+='<article id="'+c['id']+'" class="case"><h3>'+html.escape(c['title'])+'</h3>'+paragraphs([c['context'],c['text']])+PROJECT_DETAILS['case_markup'](c,ext['projects'],'en')+'<h4>Engineering and implementation</h4>'+bullets(c['implementation'])+'<p><strong>Technologies and methods:</strong> '+html.escape(c['stack'])+'</p>'+source_block(c['sources'])+'<p class="scope"><strong>Evidence scope:</strong> '+html.escape(c['limit'])+'</p></article>'
        sections.append(archive_section('especialidade-'+prefix,'Technical cases — '+{'agentes':'multiagent coordination','ia':'AI integration','ml':'Machine Learning and research','visao':'computer vision','sia':'agricultural and business applications','dados':'data engineering','mobile':'mobile and enterprise web','decisao':'decision support','produto':'products and knowledge','infra':'infrastructure and desktop integration','grafica':'3D and spatial visualization','globalcom':'Globalcom Agentic AI solution architecture'}[prefix],body))
    academic=''
    for p in ext['projects']:
        if p['id'] in ['ebserh','The game project','[EFS-AHP]']:
            title,description=catalog['PROJECTS'][p['id']]
            academic+='<article class="case"><h3>'+html.escape(title)+'</h3>'+paragraphs([description,', '.join(p['stack'])])+sources([p['id']+'/'+e for e in p['evidence']])+'</article>'
    sections.append(archive_section('academico','Doctoral, hospital internship and university projects',academic))
    for key,names,id,prefix,title in [('agroBusinessModules','MODULE_TITLES','sia-negocio','sia-negocio-','SIA — business modules'),('agroTechnicalFlows','FLOW_TITLES','sia-fluxos','sia-fluxo-','SIA / SIAgro — data and mobile workflows')]:
        items=ext[key]; titles=catalog[names]
        if len(items)!=len(titles): raise ValueError('English module titles need updating: '+key)
        cards=[]
        for i,(m,name) in enumerate(zip(items,titles)):
            embedded='embedding' in m['status']
            scope='Dashboard/report integration page; source code does not establish authorship of the embedded resource.' if embedded else 'Module code in the local Git archive; deployment and individual contribution must be interpreted in the professional context.'
            signals=[catalog['SIGNALS'][s] for s in m['implementationSignals']]
            cards.append('<article id="'+prefix+str(i+1)+'" class="module"><h3>'+html.escape(name)+'</h3><p><strong>Application:</strong> '+('Integration of information for ' if embedded else 'Operational workflow for ')+html.escape(name.lower())+'.</p><p><a href="#vinculo-agrodan">Professional context — Agrodan</a></p><p><strong>Observed stack:</strong> '+html.escape(', '.join(m['stack']))+'</p>'+bullets(signals)+sources([s['path']+':'+str(s['line']) for s in m['sources']])+'</article>')
        intro='94 business modules and submodules across 23 local Git references.' if key=='agroBusinessModules' else '48 technical workflows and modules across the checkout, ETL and mobile layers.'
        sections.append(archive_section(id,title,paragraphs([intro,'These entries belong to a shared ecosystem and may overlap across interfaces, APIs, data processing and integrations. They are not a count of independent products.'])+'<div class="module-grid">'+''.join(cards)+'</div>'))
    projects=''
    for i,p in enumerate(ext['projects']):
        title,description=catalog['PROJECTS'][p['id']]
        projects+='<article class="case" id="projeto-'+str(i+1)+'"><h3>'+html.escape(title)+'</h3>'+paragraphs([description])+PROJECT_DETAILS['markup'](p,'en')+'<p><strong>Architecture:</strong> '+html.escape(PROJECT_DETAILS['architecture'](p,'en'))+'</p><p><strong>Stack:</strong> '+html.escape(', '.join(p['stack']))+'</p>'+sources([p['id']+'/'+e for e in p['evidence']])+'</article>'
    sections.append(archive_section('projetos','Complete project and reference catalog',paragraphs(['37 projects and references include professional applications, doctoral research, independent products, prototypes, studies, backups and third-party references. Source availability alone does not prove exclusive authorship, deployment or measured impact.'])+projects))
    tools=ext['utiliboxCatalog']; names=catalog['TOOL_TITLES']
    if len(tools)!=len(names): raise ValueError('English tool titles need updating.')
    rows=''
    for t,name in zip(tools,names):
        rows+='<tr id="utilibox-tool-'+t['slug']+'"><th scope="row">'+html.escape(name)+'</th><td>'+html.escape('Interactive tool or reference for '+name.lower()+'.')+'</td><td>'+sources(['utilibox/'+r for r in t['localSourceReferences']] or ['utilibox/src/data/tools.js'])+'</td></tr>'
    sections.append(archive_section('utilibox-catalogo','Utilibox — complete application and tool catalog',paragraphs(['136 unique tool entries cover 17 overlapping commercial categories. Methods and maturity vary across the catalog; live status is declared by the catalog rather than independently checked in this review. The main CV highlights the decision, operations, finance, knowledge and learning applications.'])+'<table><thead><tr><th>Tool</th><th>Application</th><th>Links / references</th></tr></thead><tbody>'+rows+'</tbody></table>'))
    matrix=''
    for c in locale['cases']+locale['priorityCases']:
        matrix+='<tr><th scope="row">'+html.escape(c['title'])+'</th><td>'+html.escape(c['stack'])+bullets(c['implementation'])+'</td></tr>'
    sections.append(archive_section('origem-habilidades','Capabilities and their project origins','<table><thead><tr><th>Project</th><th>Engineering and demonstrated capabilities</th></tr></thead><tbody>'+matrix+'</tbody></table>'))
    sections.append(archive_section('fontes-interpretacao','Project and career context',paragraphs(['The projects cover professional applications at Agrodan, doctoral EFS-AHP research, hospital management during the internship and university project gamification. Independent initiatives include digital products, decision tools, education, finance, automation and interactive experiences.'])))
    return [PROJECT_DETAILS['reader_content'](part,'en') for part in sections]
