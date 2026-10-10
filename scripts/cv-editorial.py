"""Career-first presentation of the saved CV and project evidence."""
import html

def esc(value):
    return html.escape(str(value))

STACKS = {
    'agentes-1': 'TypeScript · Deno · Supabase · contratos tipados · resolução de conflitos',
    'agentes-2': 'Python · pandas · NumPy · simulated annealing · validação temporal',
    'ia-1': 'TypeScript · Deno · APIs de LLM · JSON · telemetria · fallback',
    'ia-2': 'TypeScript · Supabase · contratos de operações · validação referencial',
    'ia-3': 'React · Node.js · Express · SQLite · Gemini · BNCC',
    'ia-4': 'Node.js · Express · SQLite · Gemini · memória conversacional',
    'ml-1': 'Python · scikit-learn · pandas · NumPy · SciPy · DEAP · AHP',
    'ml-2': 'Python · scikit-learn · XGBoost · pandas · Flask · MetaTrader5',
    'visao-1': 'Python · OpenCV · Ultralytics/YOLO · PyTorch · Flask · RTSP',
    'visao-2': 'JavaScript · TensorFlow.js · MoveNet · BlazePose · MediaPipe · WebGL',
    'sia-cases-1': 'React · JavaScript · Node.js · APIs operacionais · regras agronômicas',
    'sia-cases-2': 'JavaScript · Node.js · algoritmos genéticos · rede neural · normalização',
    'sia-cases-3': 'React · dados geoespaciais · trajetória · velocidade · APIs operacionais',
    'sia-cases-4': 'React · JavaScript · curvas e equações · gráficos · dados de campo',
    'sia-cases-5': 'React · Dexie · IndexedDB · Node.js · sincronização',
    'sia-cases-6': 'React · Node.js · modelagem organizacional · avaliações · histórico',
    'sia-cases-7': 'React · Node.js · dados comerciais · pallets · containers',
    'dados-1': 'Node.js · SQL · Oracle · Sequelize · ETL · importação em lotes',
    'mobile-1': 'React Native · Expo · AsyncStorage · React Navigation · APIs',
    'mobile-2': 'Java EE · EJB · JSF · PrimeFaces · JPA/Hibernate · JPQL · Quartz',
    'decisao-1': 'Astro · JavaScript · TypeScript · AHP · TOPSIS · PROMETHEE · simulação',
    'decisao-2': 'Python · pandas · Parquet · OR-Tools/CBC · React · Leaflet',
    'produto-1': 'JavaScript · TypeScript · Astro · entidades e relações · Markdown',
    'produto-2': 'Next.js · Supabase · PostgreSQL · Stripe · Playwright · SQLite',
    'infra-1': 'Windows Server · Linux · Active Directory · Zabbix · GLPI · redes · IoT',
    'infra-2': 'Python · MetaTrader5 · Flask · SQLite · APIs locais',
    'grafica-1': 'TypeScript · React Three Fiber · Three.js · Rapier · Zustand',
    'grafica-2': 'JavaScript · React · Leaflet · Three.js · Canvas · FBX',
}

SKILL_GROUPS = [
    ('IA, agentes e automação', 'Integração de LLMs, saídas estruturadas, contexto, fallback e coordenação por regras; visão computacional e automação de processos.', 'Planejamento Xavier, ClassPlanner, CRM, DVR e trajetória na Bayer.'),
    ('Machine Learning e pesquisa', 'Seleção de atributos, algoritmos evolutivos, experimentos comparativos, ensembles e validação temporal.', 'EFS-AHP no doutorado, TraderMind e modelagem exploratória de irrigação.'),
    ('Engenharia de software', 'Aplicações web e mobile, modelagem de domínio, APIs, persistência, coleta offline, sincronização e integrações desktop.', 'SIA/SIAgro, EBSERH, The Game Project e produtos independentes.'),
    ('Dados e decisão', 'ETL, integração ERP, SQL, indicadores, auditoria operacional, métodos multicritério e otimização com restrições.', 'Agrodan, Labrunier, Utilibox, Cartola Oracle e Logística.'),
    ('Liderança e operações', 'Gestão de tecnologia, interface com o negócio, desenvolvimento de equipes, PMBOK, Scrum, Kanban, governança, infraestrutura e segurança.', 'Technology Enablement Lead, Head de Tecnologia, Gerente de TIC e IT Business Partner.'),
    ('Produtos e métodos aplicados', 'Desenvolvimento de produtos, métodos multicritério, pesquisa operacional, análise financeira, melhoria contínua, aprendizagem e gestão do conhecimento.', 'Utilibox: AHP, TOPSIS, PROMETHEE, filas, VSM/SMED, PDSA, VPL/TIR, Narra e UtiliNotas; SIA: qualidade, packing e gestão operacional.'),
]

TECH_GROUPS = [
    ('Linguagens', 'Python, SQL, JavaScript, TypeScript e Java.'),
    ('Web, APIs e produtos', 'React, Next.js, Astro, Node.js, Express, Flask, Java EE, JSF, PrimeFaces e Supabase.'),
    ('Mobile e offline', 'React Native, Expo, AsyncStorage, IndexedDB e Dexie; integrações com terminal MetaTrader5.'),
    ('Dados e persistência', 'Oracle, PostgreSQL, SQL Server, SQLite, BigQuery, pandas, NumPy, Parquet e Sequelize.'),
    ('ML e visão computacional', 'scikit-learn, XGBoost, LightGBM, CatBoost, SciPy, DEAP, PyTorch, YOLO, OpenCV, TensorFlow.js e MediaPipe.'),
    ('Decisão e visualização', 'AHP, TOPSIS, PROMETHEE, OR-Tools, GLPK, Power BI, Leaflet, Three.js e React Three Fiber.'),
    ('Automação e integração', 'APIs de LLM, Gemini, Playwright, Puppeteer, Telegram Bot API, Power Platform e RPA.'),
    ('Cloud e operação', 'Azure, GCP, AWS, Docker, Kubernetes, Terraform, Airflow, dbt, MLflow, Windows/Linux, Active Directory e Zabbix/GLPI.'),
]

def core_sections(data, language='pt'):
    import runpy
    from pathlib import Path
    public_links = runpy.run_path(str(Path(__file__).with_name('cv-project-links.py')))['project_links']
    content_data = data['extensions']['locales']['en'] if language == 'en' else data['extensions']
    cases = content_data['cases']
    priorities = content_data['priorityCases']
    groups = [
        ('cv-agrodan', 'Projetos e engenharia aplicada na Agrodan', 'Ecossistema SIA / SIAgro · experiência profissional', [c for c in cases if c['id'].startswith(('case-sia-cases-', 'case-dados-', 'case-mobile-1', 'case-infra-1'))] + [c for c in priorities if c['section'] == 'agrodan']),
        ('cv-utilibox', 'Utilibox — produtos e métodos aplicados', 'Decisão, pesquisa operacional, engenharia de produção, finanças e conhecimento · produto independente', [c for c in priorities if c['section'] == 'utilibox']),
        ('cv-pesquisa', 'Pesquisa aplicada e formação', 'Doutorado, estágio hospitalar e projetos de faculdade', [c for c in cases if c['id'] in ['case-ml-1', 'case-mobile-2']]),
        ('cv-ia', 'Projetos de IA, sistemas multiagentes e Machine Learning', 'Desenvolvimento independente e pesquisa quantitativa', [c for c in cases if c['id'].startswith(('case-agentes-', 'case-ia-', 'case-visao-', 'case-ml-2'))]),
        ('cv-produtos', 'Otimização e integração de sistemas', 'Pesquisa quantitativa e desenvolvimento independente', [c for c in cases if c['id'] in ['case-decisao-2', 'case-infra-2']]),
    ]
    result = []
    for id, title, context, selected in groups:
        content = '<section class="page full-page career-project-page"><div class="full-page-inner"><h2 class="career-section-title" id="' + id + '">' + title + '</h2><p class="career-context">' + context + '</p>'
        for c in selected:
            shortid = c['id'].removeprefix('case-')
            qualifier = ''
            if shortid == 'agentes-1': qualifier = 'Coordenação de agentes por regras; integração de LLMs em camada própria.'
            elif shortid == 'agentes-2': qualifier = 'Pesquisa com agentes de sinais; sem resultado financeiro validado neste levantamento.'
            elif shortid == 'sia-cases-2': qualifier = 'Modelagem exploratória; desempenho fora da amostra ainda não demonstrado.'
            elif shortid in ['visao-2', 'grafica-1', 'grafica-2']: qualifier = 'Protótipos e estudos de interação e visualização.'
            links = ' · '.join('<a href="#' + esc(a) + '">' + ('Doutorado' if a.startswith('formacao') else 'Trajetória Agrodan' if a == 'vinculo-agrodan' else 'Estágio hospitalar' if a == 'experiencia-9' else 'Ferramenta e fontes' if a.startswith('utilibox-tool-') else 'Módulo e fontes' if a.startswith('sia-negocio-') else 'Contexto e projetos') + '</a>' for a in c['relatedContextAnchors'])
            content += '<article class="career-project" id="resumo-' + c['id'] + '"><h3>' + esc(c['title']) + '</h3><p>' + esc(c['text']) + '</p><ul class="career-deliverables">' + ''.join('<li>' + esc(v) + '</li>' for v in c['implementation'][:2]) + '</ul><p class="career-stack"><strong>Engenharia e tecnologias:</strong> ' + esc(c.get('stack', STACKS.get(shortid, ''))) + '.</p>'
            if qualifier: content += '<p class="career-qualifier">' + qualifier + '</p>'
            detail = ' · <a href="#' + c['id'] + '">Detalhes técnicos e fontes</a>' if c['id'].startswith('case-') else ''
            links = links.replace('Ferramenta e fontes', 'Ferramenta').replace('Módulo e fontes', 'Módulo')
            external = public_links(c.get('sources', []), language)
            if external:
                links = ' · '.join(part for part in links.split(' · ') if 'href="#utilibox-tool-' not in part)
                detail = (' · ' if links else '') + external
            else:
                detail = detail.replace('Detalhes técnicos e fontes', 'Detalhes técnicos')
            content += '<p class="career-reference">' + links + detail + '</p></article>'
        result.append(content + '</div></section>')
    result[-1] = result[-1].replace('career-project-page"', 'career-project-page career-last"', 1)
    rendered = ''.join(result)
    if language == 'en':
        import runpy
        from pathlib import Path
        english = runpy.run_path(str(Path(__file__).with_name('cv-english.py')))
        rendered = english['translate_labels'](rendered)
    return rendered

def career_markup(data):
    def card(titleid, bodyid, title, cls='', tag='div'):
        return '<section class="full-card"><h2 class="career-section-title" id="' + titleid + '">' + title + '</h2><' + tag + ' id="' + bodyid + '" class="' + cls + '"></' + tag + '></section>'
    page1 = '<section class="page full-page career-opening"><div class="full-page-inner"><header class="full-header"><div class="full-avatar"><img id="fullAvatar" alt="Danillo Xavier"></div><div class="full-title"><h1 class="name" id="fullName"></h1><div class="headline" id="fullHeadline"></div><div class="full-contact-row" id="fullContactRow"></div></div></header>'
    page1 += card('tFullSummary', 'fullSummary', 'Perfil profissional', 'full-summary')
    page1 += '<section class="full-card career-areas"><h2 class="career-section-title">Áreas de atuação</h2><p>Engenharia de IA e automação · Sistemas multiagentes · Machine Learning e pesquisa aplicada · Engenharia de software web e mobile · Dados e apoio à decisão · Liderança de tecnologia e operações</p></section>'
    page1 += '<section class="full-card career-recognition"><h2 class="career-section-title" id="tCareerRecognition">Reconhecimentos e responsabilidades</h2><div class="full-badge-row" id="fullBadgeRow"></div></section>'
    page1 += card('tFullResults', 'fullResults', 'Resultados de impacto', 'full-results', 'ul')
    page1 += '</div></section>'
    career = '<section class="page full-page career-history"><div class="full-page-inner">' + card('tFullExperience', 'fullExperiencePrimary', 'Experiência profissional', 'full-experience-grid') + card('tFullAdditional', 'fullExperienceSecondary', 'Trajetória adicional') + '</div></section>'
    formation = '<section class="page full-page career-formation"><div class="full-page-inner">' + card('tFullEducation', 'fullEducation', 'Formação')
    formation += '<section class="full-card"><h2 class="career-section-title" id="tFullSkills">Competências e aplicações</h2><div id="fullSkills" class="career-skill-groups"></div></section>'
    formation += '<section class="full-card"><h2 class="career-section-title" id="tFullTools">Tecnologias e ferramentas</h2><div id="fullTools" class="career-tech-groups"></div></section>'
    formation += '<section class="full-card"><h2 class="career-section-title" id="tFullStack">Stack principal</h2><div id="fullStack" class="full-chip-list"></div></section></div></section>'
    return page1 + career + formation + core_sections(data)

def editor_data():
    return {'skillGroups': [{'title': t, 'description': d, 'origin': o} for t, d, o in SKILL_GROUPS], 'technologyGroups': [{'title': t, 'description': d} for t, d in TECH_GROUPS], 'caseStacks': STACKS, 'layout': 'original-complete-cv-with-projects', 'appendicesDefault': 'collapsed'}
