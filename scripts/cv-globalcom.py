"""Globalcom project profile based on the delivered architecture and confirmed implementation status."""
import copy

ID='globalcom-certification-os'
STACK=['TypeScript','React','Node.js','Python','FastAPI','Supabase','PostgreSQL','pgvector','RAG','MCP','Playwright','RLS','RBAC','Filas e workers']
CONTEXT='Modern Concept · Globalcom · arquitetura entregue · implementação em andamento'
PROJECT={
 'id':ID,'title':'Globalcom Certification OS — arquitetura Agentic AI para certificação e compliance',
 'area':'Agentic AI, arquitetura de soluções e compliance educacional','status':'Arquitetura funcional e técnica entregue; implementação em andamento','priority':'Destaque',
 'association':CONTEXT,'experience':CONTEXT,
 'summary':'Desenho e entrega da arquitetura de uma plataforma de certificação e compliance educacional que combina workflow determinístico, orquestração de agentes especialistas, RAG gerenciado, evidências versionadas e integrações para acompanhar escolas nos processos CEA + SEVP.',
 'structure':'Arquitetura entregue em camadas: aplicação web, API, workflow, agentes, documentos, recuperação de conhecimento, integrações, notificações e auditoria.',
 'stack':STACK,'skills':['Arquitetura Agentic AI','Orquestração multiagente','RAG e recuperação híbrida','Inteligência documental','Modelagem de domínio','Workflow e eventos','Integrações API/MCP/RPA','Governança e aprovação humana','Arquitetura multi-tenant','Consultoria e desenho de produto'],
 'evidence':['architecture-proposal'],'value':'Desenho de automação orientada a evidências para uma operação regulada.',
 'sourceArtifact':'globalcom_certification_modern_concept_proposal_v1.html',
 'limits':'Atuação em desenho e entrega da arquitetura funcional e técnica. Implementação em andamento; métricas operacionais e operação em produção ainda não declaradas.',
 'breadth':{'applicationAreas':['Educação','Certificação e acreditação','Compliance','Auditoria','Gestão documental','Operações','Agentic AI'],
 'intendedAudience':'Gestores Globalcom, parceiros, escolas e equipes de certificação',
 'problemAndObjective':'Organizar fases, responsáveis, requisitos e evidências de certificação, com assistência de agentes e controle das decisões críticas',
 'observableDeliverables':'Arquitetura funcional e técnica entregue, apresentação interativa bilíngue, modelo de agentes, arquitetura de dados, política de execução e roadmap de implementação',
 'domainMethods':'Máquina de estados; agentes especializados; RAG contextual; rastreabilidade de evidências; auditoria contínua; human-in-the-loop'}
}
EN_PROJECT=('Globalcom Certification OS — Agentic AI architecture for certification and compliance',
 'Delivered solution architecture, currently being implemented, for educational certification and compliance, combining deterministic workflows, specialist agent orchestration, managed RAG, versioned evidence and integrations for school CEA + SEVP processes.')

# Title, purpose, engineering details; both languages explicitly describe design work.
CASES=[
 ('Arquitetura Agentic AI e orquestração de especialistas','Coordenar tarefas especializadas com evidências e supervisão humana',[
 'Desenho de 10 agentes especialistas: compliance, evidências, documentos, pesquisa, redação, comunicação, prazos, risco, auditoria de sistemas e integração/RPA.',
 'Orquestrador dedicado verifica pré-condições, distribui tarefas e consolida resultados; um auditor independente revisa agentes, ferramentas, fontes e decisões.',
 'Contratos de execução associam escola, processo, requisito e tarefa a ferramentas autorizadas, evidências, confiança e escalonamento humano.'],
 'Agentic AI architecture and specialist orchestration','Coordinate specialized tasks with evidence and human oversight',[
 'Designed 10 specialist roles: compliance, evidence, documents, research, writing, communication, deadlines, risk, systems audit and integration/RPA.',
 'A dedicated orchestrator checks preconditions, distributes tasks and consolidates results; an independent auditor reviews agents, tools, sources and decisions.',
 'Execution contracts connect school, process, requirement and task context to approved tools, evidence, confidence and human escalation.']),
 ('RAG gerenciado e inteligência documental','Recuperar conhecimento adequado à escola, requisito e versão documental',[
 'Desenho de seis coleções: normativas oficiais, conhecimento operacional, contexto gerencial, precedentes de e-mails, documentos por escola e templates aprovados.',
 'Arquitetura de recuperação híbrida com embeddings e pgvector, filtros por tenant, escola, framework, requisito, versão, validade e aprovação.',
 'Previsão de ingestão, classificação, extração, versionamento, reprocessamento de embeddings, linhagem de chunks e persistência de citações.'],
 'Managed RAG and document intelligence','Retrieve knowledge matching school, requirement and document version',[
 'Designed six collections: official regulations, operational knowledge, management context, email precedents, school-specific documents and approved templates.',
 'Hybrid retrieval architecture with embeddings and pgvector; tenant, school, framework, requirement, version, validity and approval filters.',
 'Specified ingestion, classification, extraction, versioning, embedding reprocessing, chunk lineage and citation persistence.']),
 ('Workflow, eventos e execução persistente','Manter processos e tarefas em execução mesmo sem usuário conectado',[
 'Máquina de estados especificada controla dependências, responsáveis, prazos, pré-condições e critérios de conclusão das nove fases do processo.',
 'Desenho de filas, eventos, webhooks e jobs agendados, com workers especializados para workflow, agentes, documentos, RAG, notificações, RPA e auditoria.',
 'Stack sugerida: Node.js/TypeScript, NestJS ou Fastify, Zod e BullMQ ou alternativa; Temporal aparece como opção para workflows duráveis.'],
 'Workflow, events and persistent execution','Keep processes and tasks running without an active user session',[
 'The specified state machine controls dependencies, owners, deadlines, preconditions and completion criteria across nine process phases.',
 'Designed queues, events, webhooks and scheduled jobs, with specialist workflow, agent, document, RAG, notification, RPA and audit workers.',
 'Suggested Node.js/TypeScript, NestJS or Fastify, Zod and BullMQ or an alternative queue; Temporal is an optional durable workflow engine.']),
 ('Governança de IA, segurança e auditoria contínua','Controlar autonomia, acesso aos dados e qualidade das decisões',[
 'Política de execução especificada distingue execução automática, ações que exigem aprovação humana e decisões críticas reservadas a pessoas.',
 'Desenho de isolamento por parceiro/escola com RLS e RBAC, menor privilégio, cofre de segredos, logs, retenção, backup e recuperação.',
 'Auditor independente verifica correspondência entre citação e evidência, versão normativa, integridade de dados e respeito às etapas; planejamento de auditoria trimestral e reuniões a cada quatro meses.'],
 'AI governance, security and continuous audit','Control autonomy, data access and decision quality',[
 'The specified execution policy separates automatic execution, human approval actions and critical decisions reserved for people.',
 'Designed partner/school isolation with RLS and RBAC, least privilege, secret management, logs, retention, backup and recovery.',
 'An independent auditor checks citation/evidence alignment, regulation versions, data integrity and workflow compliance; quarterly audits and four-month review meetings are planned.']),
 ('Integrações API, MCP e RPA para operações externas','Conectar a plataforma a fontes e portais com execução controlada',[
 'Estratégia de integração prioriza APIs, usa MCP para acesso padronizado a ferramentas e prevê RPA quando não há integração formal.',
 'Especificação de workers de navegador isolados com Playwright, políticas de retry, idempotência, detecção de mudança de layout e fallback manual.',
 'Escopo arquitetural inclui migração/sincronização do Notion, e-mails, portais e conectores futuros para sistemas escolares e financeiros; QuickSchools, QuickBooks e Wave são referências iniciais.'],
 'API, MCP and RPA integrations for external operations','Connect sources and portals with controlled execution',[
 'Integration strategy prioritizes APIs, uses MCP for standardized tool access and proposes RPA when formal integration is unavailable.',
 'Specified isolated Playwright browser workers, retry policies, idempotency, layout change detection and manual fallback.',
 'Architectural scope includes Notion migration/synchronization, email, portals and future school/financial system connectors; QuickSchools, QuickBooks and Wave are initial references.']),
 ('Modelagem de domínio e produto para certificação','Traduzir uma operação de certificação em entidades e fluxos de produto',[
 'Modelagem de domínio entregue relaciona parceiros, escolas, frameworks, fases, requisitos, tarefas, documentos, evidências, riscos, decisões e histórico.',
 'Supabase/PostgreSQL é a fonte canônica projetada, com Storage para documentos, Auth, Realtime e vetores pgvector; frontend React/TypeScript com visualização de fluxos.',
 'Arquitetura contempla readiness, gaps, planos corretivos, self-study e reutilização de artefatos; resultados esperados são objetivos do produto, sem métricas de impacto realizadas.'],
 'Certification domain and product modeling','Translate certification operations into product entities and workflows',[
 'Delivered domain design connects partners, schools, frameworks, phases, requirements, tasks, documents, evidence, risks, decisions and history.',
 'Supabase/PostgreSQL is the designed canonical store, with document Storage, Auth, Realtime and pgvector; a React/TypeScript frontend includes workflow visualization.',
 'Architecture covers readiness, gaps, corrective plans, self-study and artifact reuse; expected outcomes are product goals rather than achieved impact metrics.']),
 ('Consultoria, arquitetura de soluções e roadmap','Entregar a arquitetura e o roadmap de implantação incremental',[
 'Entrega documental combina visão executiva, arquitetura detalhada, apresentação navegável PT/EN e planejamento de implantação.',
 'Roadmap parte da descoberta e domínio operacional, evolui para RAG/documentos, agentes, compliance contínuo, integrações e inteligência de certificação.',
 'Definição de indicadores a acompanhar: tempo por fase, completude de evidências, reutilização, aprovação de drafts, erros de agentes, saúde das integrações e cobertura de auditoria.'],
 'Consulting, solution architecture and roadmap','Deliver the architecture and roadmap for incremental implementation',[
 'Documented deliverables combine an executive view, detailed architecture, navigable PT/EN presentation and implementation planning.',
 'Roadmap starts with discovery and operational domain, then adds RAG/documents, agents, continuous compliance, integrations and certification intelligence.',
 'Defined target measures: phase duration, evidence completeness, reuse, draft approval, agent errors, integration health and audit coverage.']),
]

def records(language='pt'):
    out=[]
    for i,row in enumerate(CASES,1):
        title,problem,implementation=row[:3] if language=='pt' else row[3:]
        out.append({'id':'case-globalcom-'+str(i),'title':title,'problem':problem,'implementation':implementation,
          'text':('Arquitetura entregue, em implementação: ' if language=='pt' else 'Delivered architecture, implementation in progress: ')+problem[0].lower()+problem[1:]+'.',
          'context':CONTEXT if language=='pt' else 'Modern Concept · Globalcom · delivered architecture · implementation in progress',
          'skills':PROJECT['skills'] if language=='pt' else ['Agentic AI architecture','Multiagent orchestration','RAG','Workflow design','Human-in-the-loop','Solution architecture'],
          'stack':' · '.join(STACK).replace('Filas e workers','Queues and workers') if language=='en' else ' · '.join(STACK),
          'sources':[ID+'/architecture-proposal'],
          'limit':PROJECT['limits'] if language=='pt' else 'Contribution: functional and technical architecture design and delivery. Implementation is in progress; production operation and operational metrics have not yet been declared.',
          'relatedContextAnchors':['projetos'],'depth':'Arquitetura entregue · em implementação' if language=='pt' else 'Delivered architecture · implementation in progress'})
    return out

def inject(proposal):
    proposal['projects'].append(copy.deepcopy(PROJECT))
    proposal['topics'].append({'id':'globalcom','title':'Globalcom — arquitetura Agentic AI, compliance e automação',
      'intro':'Arquitetura funcional e técnica entregue pela Modern Concept; implementação em andamento.',
      'text':['A arquitetura entregue relaciona educação, acreditação, compliance, gestão documental, operações, governança e automação. O material entregue descreve a arquitetura e o roadmap da implementação em andamento.'],
      'flow':['Domínio e workflow','Conhecimento e evidências','Agentes especialistas','Validação e aprovação humana','Integrações e auditoria contínua'],
      'cases':records()})

def enhance_editorial(editorial,language='pt'):
    out=copy.deepcopy(editorial)
    out['skillGroups'].append({'title':'Arquitetura Agentic AI e governança' if language=='pt' else 'Agentic AI architecture and governance',
      'description':'Desenho de orquestradores, agentes especialistas, ferramentas autorizadas, RAG contextual, auditoria independente e aprovação humana.' if language=='pt' else 'Design of orchestrators, specialist agents, approved tools, contextual RAG, independent auditing and human approval.',
      'origin':'Globalcom Certification OS — arquitetura entregue pela Modern Concept; implementação em andamento.' if language=='pt' else 'Globalcom Certification OS — Modern Concept delivered architecture; implementation in progress.'})
    out['technologyGroups'].append({'title':'Stack especificada na arquitetura — Globalcom Agentic AI' if language=='pt' else 'Architecture-specified stack — Globalcom Agentic AI',
      'description':'React/TypeScript, Node.js, Python/FastAPI, Supabase/PostgreSQL, pgvector, RAG, MCP e Playwright; NestJS/Fastify e BullMQ como alternativas sugeridas, Temporal opcional.' if language=='pt' else 'React/TypeScript, Node.js, Python/FastAPI, Supabase/PostgreSQL, pgvector, RAG, MCP and Playwright; NestJS/Fastify and BullMQ as suggested alternatives, optional Temporal.'})
    return out
