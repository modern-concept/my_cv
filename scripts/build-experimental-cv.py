"""Create an additive, statically rendered CV experiment from saved evidence."""
import copy
import html
import json
import re
from collections import defaultdict
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
DATE='2026-10-09'
def read(name): return json.loads((BASE/name).read_text(encoding='utf-8-sig'))
def esc(value): return html.escape(str(value),quote=True)
def slug(value): return re.sub(r'[^a-z0-9]+','-',value.lower()).strip('-')
def paras(values): return ''.join('<p>'+esc(v).replace('\n','<br>')+'</p>' for v in values)
def bullets(values): return '<ul>'+''.join('<li>'+esc(v)+'</li>' for v in values)+'</ul>'
def chips(values): return '<ul class="chips">'+''.join('<li>'+esc(v)+'</li>' for v in values)+'</ul>'
def sources(values): return '<ul class="sources">'+''.join('<li><code>'+esc(v)+'</code></li>' for v in values)+'</ul>'
def section(id,title,body,cls=''):
    return '<section id="'+id+'" class="chapter '+cls+'"><h2>'+esc(title)+'</h2>'+body+'</section>'

def build():
    original=read('cv-data.json')
    proposal=read('cv-proposta-detalhada.json')
    experimental=copy.deepcopy(original)
    pt=experimental['languages']['pt']
    current=original['languages']['pt']
    pt['skills']=[{'name':v} for v in proposal['skills']]+[
      {'name':'Gestão e liderança profissional: PMBOK, Scrum, Kanban, arquitetura, mentoria, comunicação e segurança.'},
      {'name':'Experiência profissional já declarada: MLOps, RAG, MCP, Agentic AI e RPA; contextos e tecnologias mantidos a partir do CV atual.'},
      {'name':'Infraestrutura e operação: servidores Windows/Linux, redes, Active Directory, monitoramento, help desk, backup/recovery, virtualização e IoT — trajetória de TIC na Agrodan.'}
    ]
    pt['tools']=[{'name':v} for v in proposal['tools']]+[
      {'name':'Cloud e dados profissionais (CV atual): Azure, GCP, AWS, BigQuery, PySpark, Airflow, dbt e MLflow.'},
      {'name':'Plataforma e automação profissionais (CV atual): Docker, Kubernetes, Terraform, Power BI, Power Platform, RPA e BPMN.'},
      {'name':'Infraestrutura e IoT profissionais (CV atual): Windows Server, Linux, firewall, Active Directory, Zabbix, GLPI, Mikrotik, Unifi, Arduino e Raspberry Pi.'}
    ]
    additional=['JavaScript','TypeScript','Java','React Native','Expo','Next.js','Astro','Express','Flask','JSF','PrimeFaces','EJB','JPA/Hibernate','PostgreSQL','Supabase','SQLite','SQL Server','Sequelize','pandas','NumPy','scikit-learn','XGBoost','LightGBM','CatBoost','SciPy','DEAP','Jupyter','Ultralytics/YOLO','OpenCV','TensorFlow.js','MediaPipe','Three.js','React Three Fiber','Rapier','Leaflet','OR-Tools','GLPK','Dexie','AHP','TOPSIS','PROMETHEE']
    pt['fullCv']['coreStack']=list(dict.fromkeys(pt['fullCv']['coreStack']+additional))
    # Keep all existing sections verbatim. Only skills/tools/coreStack may differ.
    allowed={'skills','tools','fullCv'}
    for key,value in current.items():
        if key not in allowed and pt[key]!=value: raise ValueError('Conteúdo original alterado: '+key)
    for key,value in current['fullCv'].items():
        if key!='coreStack' and pt['fullCv'][key]!=value: raise ValueError('Bloco profissional alterado: '+key)
    for language in ['en','de']:
        if experimental['languages'][language]!=original['languages'][language]: raise ValueError('Idioma original alterado')

    full=current['fullCv']
    anchors={}
    jobs=full['primaryExperience']+full['additionalExperience']
    for i,job in enumerate(jobs):
        anchors[i]='experiencia-'+str(i+1)
    agro_ids=[anchors[i] for i,j in enumerate(jobs) if 'AGRODAN' in j['company'].upper()]
    hospital_ids=[anchors[i] for i,j in enumerate(jobs) if 'HOSPITAL' in j['company'].upper()]
    bayer_ids=[anchors[i] for i,j in enumerate(jobs) if 'BAYER' in j['company'].upper()]
    founder_ids=[anchors[i] for i,j in enumerate(jobs) if 'FUNDADOR' in j['role'].upper()]
    def context_links(context):
        links=[]
        if 'Agrodan' in context or 'agrodan' in context: links.append(('vinculo-agrodan','Experiência profissional · Agrodan — trajetória de cargos'))
        if 'EBSERH' in context or 'hospital' in context.lower(): links.extend((a,'Estágio · Hospital Universitário de Petrolina') for a in hospital_ids)
        if 'doutorado' in context.lower() or 'EFS-AHP' in context: links.append(('formacao-1','Doutorado · CÉSAR School'))
        if 'faculdade' in context.lower(): links.append(('academico','Projeto acadêmico · The Game Project'))
        if not links: links.append(('projetos','Projetos independentes, pesquisa e produtos'))
        return links
    def linked(context):
        links=context_links(context)
        # A corporate project is linked to the trajectory, without assigning it
        # to a specific role/date before that attribution has been established.
        seen=set(); unique=[]
        for a,label in links:
            if label not in seen: unique.append((a,label));seen.add(label)
        return '<p class="association"><strong>Vínculo:</strong> '+ ' · '.join('<a href="#'+a+'">'+esc(label)+'</a>' for a,label in unique)+'</p>'
    job_html=[]
    for i,j in enumerate(jobs):
        job_html.append('<article id="'+anchors[i]+'" class="job"><h3>'+esc(j['role'])+'</h3><p class="company">'+esc(j['company'])+'</p><p class="meta">'+esc(j['period'])+' · '+esc(j.get('employment',''))+' · '+esc(j.get('location',''))+'</p>'+chips(j.get('highlights',[]))+bullets(j.get('bullets',[]))+('<p><strong>Tecnologias relacionadas no histórico:</strong> '+esc(', '.join(j['technologies']))+'</p>' if j.get('technologies') else '')+'</article>')
    primary_count=len(full['primaryExperience'])
    base_parts=[section('perfil','Perfil profissional',paras(current['profile']['summary'])),section('reconhecimento','Reconhecimentos e responsabilidades',bullets(full['headerBadges'])),section('profissional','Experiência profissional',''.join(job_html[:primary_count])),section('trajetoria','Trajetória adicional',''.join(job_html[primary_count:])),section('resultados','Resultados de impacto',bullets(full['keyImpacts']))]
    edu=[]
    for i,e in enumerate(current['education']):
        edu.append('<article id="formacao-'+str(i+1)+'" class="job"><h3>'+esc(e['degree']).replace('\n','<br>')+'</h3><p class="company">'+esc(e['school'])+'</p><p class="meta">'+esc(e['from'])+' — '+esc(e['to'])+'</p>'+bullets(e.get('details',[]))+'</article>')
    base_parts.append(section('formacao','Formação',''.join(edu)))
    base_parts.append(section('competencias','Habilidades e competências',bullets([v['name'] for v in pt['skills']])+'<h3>Origem das competências</h3><p>Os cases e módulos abaixo relacionam as competências ao problema, à implementação e à experiência correspondente. Tecnologias informadas na trajetória profissional são diferenciadas dos artefatos localizados nos projetos.</p>'))
    base_parts.append(section('tecnologias','Tecnologias e ferramentas',bullets([v['name'] for v in pt['tools']])+'<h3>Stack principal ampliada</h3>'+chips(pt['fullCv']['coreStack'])))

    new_sections=[]
    new_sections.append(section('extensao','Extensão da experiência e contextos de atuação',
      '<p>A trajetória combina engenharia de software, dados e automação com liderança de tecnologia e aplicações em agronegócio, operações, educação, finanças, produção, planejamento e produtos digitais.</p>'+
      '<div class="context-grid">'+
      '<article><h3>Trabalho e operações</h3><p>Na Agrodan, o ecossistema SIA reúne módulos de campo, planejamento, qualidade, packing, pessoas, comercial, compras e gestão, com aplicações web/mobile, APIs e dados. A Bayer, Labrunier e a gestão de TIC mantêm os relatos profissionais já apresentados neste currículo.</p><a href="#profissional">Ver experiência profissional</a></article>'+
      '<article><h3>Pesquisa do doutorado</h3><p>EFS-AHP é a pesquisa vinculada ao doutorado profissional em Engenharia de Software. Relaciona seleção de atributos, algoritmos evolutivos, AHP e avaliação experimental.</p><a href="#formacao-1">Ver doutorado</a></article>'+
      '<article><h3>Estágio e faculdade</h3><p>EBSERH está ligado ao estágio no Hospital Universitário de Petrolina. The Game Project foi desenvolvido na faculdade como aplicação de gestão de projetos com gamificação.</p><a href="#academico">Ver projetos acadêmicos e de estágio</a></article>'+
      '<article><h3>Produtos e iniciativas próprias</h3><p>O acervo também inclui produtos, pesquisa, estudos e experimentação empreendedora. Cada projeto independente mantém seu contexto; sua existência não estabelece vínculo com Bayer, Labrunier ou outra empresa.</p><a href="#projetos">Ver catálogo de projetos</a></article></div>'+
      '<h3>Como ler a profundidade dos projetos</h3><p>A profundidade é descrita pela engenharia observada: aplicações com domínio e persistência, pipelines de dados, pesquisa com experimentos, integração de modelos, interfaces de visualização e protótipos. Os termos não representam uma classificação de senioridade por contagem de projetos.</p>'))
    cases=[]
    for topic in proposal['topics']:
        content='<p class="intro">'+esc(topic['intro'])+'</p>'+paras(topic['text'])
        content+='<ol class="flow">'+''.join('<li>'+esc(v)+'</li>' for v in topic['flow'])+'</ol>'
        for i,c in enumerate(topic['cases']):
            cid='case-'+topic['id']+'-'+str(i+1)
            record={**c,'id':cid,'relatedContextAnchors':[a for a,_ in context_links(c['context'])],'depth':'Arquitetura e métodos descritos pelos artefatos abaixo; implantação e impacto conforme o contexto.'}
            cases.append(record)
            content+='<article class="case" id="'+cid+'"><p class="kicker">Case · '+esc(c['context'])+'</p><h3>'+esc(c['title'])+'</h3>'+linked(c['context'])+'<p><strong>Problema:</strong> '+esc(c['problem'])+'</p><p class="delivery"><strong>Contribuição e entrega:</strong> '+esc(c['text'])+'</p><h4>Engenharia, métodos e profundidade</h4>'+bullets(c['implementation'])+'<h4>Competências evidenciadas</h4>'+chips(c['skills'])+'<h4>Fontes do projeto</h4>'+sources(c['sources'])+'<p class="scope"><strong>Alcance da evidência:</strong> '+esc(c['limit'])+'</p></article>'
        new_sections.append(section('especialidade-'+topic['id'],topic['title'],content,'specialty'))
    academic=[]
    for p in proposal['projects']:
        if p['id'] in ['[EFS-AHP]','ebserh','The game project']:
            academic.append('<article class="case"><h3>'+esc(p['title'])+'</h3><p>'+esc(p['association'])+'</p>'+linked(p['association'])+paras([p['summary'],p['structure']])+chips(p['stack'])+sources([p['id']+'/'+e for e in p['evidence']])+'</article>')
    new_sections.append(section('academico','Projetos vinculados a formação, estágio e faculdade',''.join(academic)))
    def module_cards(items,branch=False):
        output=[]
        for i,m in enumerate(items):
            mid=('sia-negocio-' if branch else 'sia-fluxo-')+str(i+1)
            body='<article class="module" id="'+mid+'"><p class="kicker">'+esc(m['domain'])+'</p><h3>'+esc(m['title'])+'</h3>'+linked('Agrodan')+'<p><strong>Finalidade:</strong> '+esc(m['objective'])+'.</p><p><strong>Competências:</strong> '+esc('; '.join(m['skills']))+'.</p><p><strong>Stack observada:</strong> '+esc(', '.join(m['stack']) or 'Ver fontes do módulo')+'.</p>'
            if m['implementationSignals']: body+='<p><strong>Mecanismos:</strong> '+esc('; '.join(m['implementationSignals']))+'.</p>'
            if branch and m['symbols']: body+='<p><strong>Funções de implementação:</strong> '+esc(', '.join(s['name'] for s in m['symbols'][:8]))+'.</p>'
            body+=sources([s['path']+':'+str(s['line']) for s in m['sources']])+'<p class="scope">'+esc(m['status'])+'.</p></article>'
            output.append(body)
        return '<div class="module-grid">'+''.join(output)+'</div>'
    new_sections.append(section('sia-negocio','SIA — catálogo de módulos e projetos de negócio',
      '<p>Experiência profissional na Agrodan. O acervo de 23 referências Git locais inclui 94 módulos e submódulos de negócio. São partes do mesmo ecossistema; versões, integrações e componentes compartilhados não são produtos independentes.</p>'+linked('Agrodan')+
      '<p>O catálogo inclui implementação de regras e processos e páginas de integração de relatórios/dashboards. Em cada entrada, o alcance é descrito conforme o material encontrado.</p>'+module_cards(proposal['agroBusinessModules'],True)))
    new_sections.append(section('sia-fluxos','SIA / SIAgro — fluxos de dados, indicadores e desenvolvimento mobile',
      '<p>Detalhamento de 48 fluxos e módulos técnicos do checkout, ETL e aplicativo mobile. Há sobreposição com o catálogo de negócio: um processo pode ter tela, API, importação e visualização, apresentados em suas respectivas camadas.</p>'+module_cards(proposal['agroModules'])))
    project_html=[]
    project_records=[]
    for i,p in enumerate(proposal['projects']):
        pid='projeto-'+str(i+1)
        b=p.get('breadth',{})
        if p['priority']=='Arquivo': depth='Estudo, referência, configuração ou versão histórica; alcance detalhado abaixo.'
        elif any(word in p['status'].lower() for word in ['protótipo','experimenta']): depth='Protótipo/experimentação: implementação exploratória sem escala comprovada.'
        elif p['id']=='[EFS-AHP]': depth='Pesquisa aplicada do doutorado: métodos, baselines e avaliação experimental.'
        elif p['id']=='Agrodan': depth='Sistema corporativo modular: processos de negócio, dados e interfaces web/mobile.'
        else: depth=p['status']+': profundidade expressa pela arquitetura, métodos e artefatos.'
        project_records.append({**p,'anchor':pid,'relatedContextAnchors':[a for a,_ in context_links(p['association'])],'demonstratedDepth':depth})
        project_html.append('<article id="'+pid+'" class="case"><p class="kicker">'+esc(p['area'])+' · '+esc(p['status'])+'</p><h3>'+esc(p['title'])+'</h3><p><strong>Contexto:</strong> '+esc(p['association'])+'</p>'+linked(p['association'])+'<p>'+esc(p['summary'])+'</p><p><strong>Problema e público:</strong> '+esc(b.get('problemAndObjective',p['value']))+' — '+esc(b.get('intendedAudience','Contexto a detalhar'))+'.</p><p><strong>Entrega:</strong> '+esc(b.get('observableDeliverables',p['structure']))+'.</p><p><strong>Profundidade demonstrada:</strong> '+esc(depth)+'</p><p><strong>Estrutura:</strong> '+esc(p['structure'])+'</p><p><strong>Métodos:</strong> '+esc(b.get('domainMethods','; '.join(p['skills'])))+'.</p><p><strong>Áreas de aplicação:</strong> '+esc('; '.join(b.get('applicationAreas',[p['area']])))+'.</p><h4>Stack</h4>'+chips(p['stack'])+'<h4>Habilidades</h4>'+bullets(p['skills'])+'<h4>Evidências de implementação</h4>'+sources([p['id']+'/'+e for e in p['evidence']])+'<p class="scope">'+esc(p['limits'])+'</p></article>')
    new_sections.append(section('projetos','Catálogo completo de projetos e repertório',
      '<p>36 pastas locais, incluindo produtos, pesquisa, protótipos, estudos, versões anteriores e referências. O contexto e o alcance de cada entrada determinam como ela contribui para a trajetória.</p>'+''.join(project_html)))
    # Tool topics are kept as a separate appendix: they expand domain breadth,
    # without turning 136 catalog entries into 136 independent work experiences.
    tool_rows=[]
    for tool in proposal['utiliboxTools']:
        refs=tool.get('localSourceReferences',[])
        tool_rows.append('<tr><th scope="row">'+esc(tool['name'])+'</th><td>'+esc(tool['desc'])+'</td><td>'+esc('; '.join(c['title'] for c in tool['categories']))+'</td><td>'+sources(['utilibox/'+r for r in refs] or ['utilibox/src/data/tools.js — verificar alias/rota'])+'</td></tr>')
    new_sections.append(section('utilibox-catalogo','Utilibox — aplicações e ferramentas do catálogo',
      '<p>O catálogo contém 136 ferramentas únicas em 17 categorias comerciais, com sobreposição entre categorias. Ele demonstra temas e métodos traduzidos em software, com graus distintos de maturidade. O status live é uma declaração do catálogo, sem validação de disponibilidade nesta revisão.</p><div class="table-scroll"><table><thead><tr><th>Ferramenta</th><th>Objetivo</th><th>Área</th><th>Fonte</th></tr></thead><tbody>'+''.join(tool_rows)+'</tbody></table></div>'))
    provenance=defaultdict(list)
    for record in proposal['skillProvenance']:
        entry=record['case']+' — '+record['context']
        if entry not in provenance[record['skill']]: provenance[record['skill']].append(entry)
    skill_rows=[]
    for skill,origins in sorted(provenance.items(),key=lambda x:x[0].lower()):
        skill_rows.append('<tr><th scope="row">'+esc(skill)+'</th><td>'+bullets(origins)+'</td></tr>')
    new_sections.append(section('origem-habilidades','Matriz de habilidades e cases de origem',
      '<p>Competências relacionadas aos cases apresentados. A correspondência completa com os arquivos de origem está disponível em <a href="cv-experimental-data.json">cv-experimental-data.json</a>; os cases acima incluem as evidências específicas.</p><div class="table-scroll"><table><thead><tr><th>Habilidade</th><th>Projetos, módulos e contexto</th></tr></thead><tbody>'+''.join(skill_rows)+'</tbody></table></div>'))

    old_summary=''.join('<article class="job"><h3>'+esc(e['company']).replace('\n','<br>')+'</h3><p>'+esc(e['role']).replace('\n','<br>')+'</p><p class="meta">'+esc(e['from'])+' — '+esc(e['to'])+'</p>'+paras(e.get('paragraphs',[]))+'</article>' for e in current['experience'])
    preserved=[section('sintese-original','Síntese de experiência da versão original',old_summary)]
    for key,title in [('coverLetter','Carta de apresentação'),('coverLetterSwiss','Carta de apresentação — Suíça')]:
        c=current[key]
        preserved.append(section(slug(key),title,paras([c['greeting'],*c['paragraphs'],c['closing'],c['signature']]),'letter'))
    agro_roles='<ul>'+''.join('<li><a href="#'+anchors[i]+'">'+esc(j['role'])+'</a> — '+esc(j['period'])+'</li>' for i,j in enumerate(jobs) if i in [k for k in anchors if anchors[k] in agro_ids])+'</ul>'
    association_map=section('vinculos','Vínculos entre projetos e trajetória',
      '<article id="vinculo-agrodan"><h3>Agrodan — ecossistema SIA / SIAgro</h3><p>Vínculo profissional confirmado. Os projetos de campo, packing, pessoas, planejamento, compras, qualidade e comercial estão ligados à trajetória na empresa. A distribuição de cada entrega pelos cargos e períodos específicos não é inferida pelas datas dos commits.</p>'+agro_roles+'<p><a href="#especialidade-sia-cases">Cases de negócio e métodos</a> · <a href="#sia-negocio">Módulos de negócio</a> · <a href="#sia-fluxos">ETL e mobile</a></p></article>'+
      '<article><h3>EFS-AHP — doutorado</h3><p>A pesquisa de seleção de atributos e decisão multicritério está vinculada ao doutorado profissional em Engenharia de Software.</p><p><a href="#formacao-1">Formação</a> · <a href="#case-ml-1">Case de pesquisa EFS-AHP</a></p></article>'+
      '<article><h3>EBSERH — estágio hospitalar</h3><p>O sistema de indicadores e avaliações está associado ao estágio no Hospital Universitário de Petrolina.</p><p><a href="#'+(hospital_ids[0] if hospital_ids else 'trajetoria')+'">Experiência de estágio</a> · <a href="#academico">Implementação e stack</a></p></article>'+
      '<article><h3>The Game Project — faculdade</h3><p>Projeto acadêmico de gestão de projetos com gamificação. O vínculo com a faculdade foi confirmado; não é atribuído a uma empresa nem constitui outra experiência hospitalar.</p><a href="#academico">Case acadêmico</a></article>'+
      '<article><h3>Demais projetos — pesquisa, produtos e empreendedorismo</h3><p>Parte do acervo está ligada a iniciativas empreendedoras ao longo dos anos. A associação individual de cada produto às empresas fundadas, datas e participação precisa de contexto específico; o catálogo mantém os projetos com sua finalidade e evidências próprias.</p><a href="#projetos">Catálogo completo</a></article>')
    all_sections=base_parts+[association_map]+new_sections+preserved
    toc='<nav class="toc" aria-label="Índice do currículo"><h2>Índice</h2><ol>'+''.join('<li><a href="#'+re.search(r'<section id="([^"]+)"',part)[1]+'">'+re.search(r'<h2>(.*?)</h2>',part)[1]+'</a></li>' for part in all_sections)+'</ol></nav>'
    links=' · '.join('<a href="'+esc(s['url'])+'">'+esc(s['label'])+'</a>' for s in current['contact']['social'])
    contact=' · '.join(esc(item['label'])+': '+esc(item['value']) for item in current['contact']['items'])
    linked_data={'@context':'https://schema.org','@type':'Person','name':current['profile']['name'],'description':' '.join(current['profile']['summary']),'sameAs':[s['url'] for s in current['contact']['social']],'knowsAbout':[s['name'] for s in pt['skills']]}
    experimental['extensions']={'version':'experimental-additive','generatedAt':DATE,'language':'pt','sourceCommit':'648d76f','method':'CV original preservado. Habilidades, ferramentas e stack ajustadas; especialidades, cases, módulos e evidências acrescentados. Artefatos Git não equivalem automaticamente a autoria exclusiva, implantação ou resultado.', 'cases':cases,'projects':project_records,'topics':proposal['topics'],'agroBusinessModules':proposal['agroBusinessModules'],'agroTechnicalFlows':proposal['agroModules'],'skillProvenance':proposal['skillProvenance'],'utiliboxCatalog':proposal['utiliboxTools']}
    (BASE/'cv-experimental-data.json').write_text(json.dumps(experimental,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    css='''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f1f4f2;color:#1f332e;font:16px/1.65 system-ui,-apple-system,Segoe UI,sans-serif}a{color:#166655}a:focus-visible,button:focus-visible{outline:3px solid #d99b54;outline-offset:3px}.toolbar{max-width:1180px;margin:auto;padding:18px 24px;display:flex;justify-content:space-between;gap:18px;flex-wrap:wrap}.toolbar button{padding:8px 14px;border:1px solid #ccd8cf;background:white;color:#1f332e;border-radius:8px;cursor:pointer;font:inherit}main{max-width:1180px;margin:auto;padding:20px 28px 70px;background:white}.cv-header{display:grid;grid-template-columns:120px 1fr;gap:28px;padding:30px 0;border-bottom:3px solid #176453}.cv-header img{width:120px;height:120px;object-fit:cover;border-radius:50%}h1{font-size:clamp(30px,4vw,46px);line-height:1.12;margin:0 0 15px}h2{font-size:28px;line-height:1.25;color:#174e40;border-bottom:1px solid #dbe4dd;padding-bottom:14px}h3{font-size:21px;line-height:1.4;margin:10px 0}h4{font-size:15px;margin-bottom:7px}p{margin:10px 0 15px}.headline{font-size:24px;line-height:1.35}.meta,.scope,.sources{color:#53685f;font-size:13px}.kicker{font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:#176453;font-weight:700}.experiment{font-size:13px;background:#e9f1ea;padding:13px 16px;border-radius:8px;margin:22px 0}.toc ol{columns:2;column-gap:35px;padding-left:23px}.toc li{padding:3px;break-inside:avoid}.chapter{margin:45px 0;scroll-margin-top:20px}.company{font-weight:650}.job{padding:18px 0;border-bottom:1px solid #e3e9e4;scroll-margin-top:20px}.chips{display:flex;flex-wrap:wrap;gap:7px;list-style:none;padding:0}.chips li{font-size:13px;background:#edf3ee;padding:4px 9px;border-radius:6px}.case{padding:24px;border:1px solid #dae3dc;border-radius:12px;margin:24px 0;scroll-margin-top:20px}.delivery{background:#eff6f0;border-left:4px solid #176453;padding:14px 18px}.association{font-size:14px}.scope{border-top:1px solid #e2e9e4;padding-top:12px}.sources{padding-left:20px;overflow-wrap:anywhere}.sources code{font:12px/1.5 ui-monospace,Consolas,monospace}.flow{display:flex;gap:10px;flex-wrap:wrap;padding-left:22px}.flow li{padding:5px 11px;background:#f2f5f1;border-radius:6px;font-size:13px}.context-grid,.module-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}.context-grid article,.module{border:1px solid #dbe5dd;padding:20px;border-radius:10px}.module{font-size:14px}.module h3{font-size:18px}.module .sources code{font-size:11px}table{border-collapse:collapse;width:100%;font-size:13px}td,th{text-align:left;vertical-align:top;padding:13px;border-bottom:1px solid #dfe7e0}thead{background:#edf4ee}th{font-weight:650}.table-scroll{overflow:auto}td ul{padding-left:18px}.footnote{font-size:13px;color:#53685f;border-top:1px solid #dbe5dd;padding-top:20px}ul{padding-left:23px}.intro{font-size:18px}.letter{max-width:850px}footer{padding:20px 28px;text-align:center;font-size:13px;color:#53685f}@media(max-width:740px){main{padding:15px 18px 50px}.cv-header{grid-template-columns:1fr;gap:15px}.cv-header img{width:90px;height:90px}.context-grid,.module-grid{grid-template-columns:1fr}.toc ol{columns:1}.case{padding:18px}.headline{font-size:21px}h2{font-size:24px}table{min-width:640px}}@page{size:A4;margin:13mm}@media print{body{background:white;font-size:10pt;line-height:1.45}.toolbar,.experiment,.no-print,footer{display:none!important}main{padding:0;max-width:none}.cv-header{padding:0 0 20px;grid-template-columns:75px 1fr;gap:18px}.cv-header img{width:75px;height:75px}h1{font-size:26pt}.headline{font-size:15pt}h2{font-size:17pt;break-after:avoid}h3{font-size:13pt;break-after:avoid}h4{font-size:10pt;break-after:avoid}.chapter{break-before:page;margin:0 0 15px}.job{break-inside:avoid;padding:10px 0}.case{border-radius:0;padding:12px;margin:14px 0;break-inside:auto}.delivery{break-inside:avoid}.module-grid{gap:10px}.module{break-inside:avoid;padding:10px;font-size:9pt;border-radius:0}.module h3{font-size:11pt}.chips li{font-size:8pt}.meta,.scope,.sources{font-size:8pt}.sources code,.module .sources code{font-size:7pt}table{min-width:0;font-size:8pt}td,th{padding:7px;overflow-wrap:anywhere}thead{display:table-header-group}tr{break-inside:avoid}.toc{break-after:page}.toc ol{columns:2;font-size:9pt}.context-grid article{break-inside:avoid}.flow li{font-size:8pt}.intro{font-size:11pt}a{color:inherit;text-decoration:none}}'''
    page='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Danillo Xavier — CV completo experimental</title><meta name="description" content="Currículo completo de Danillo Xavier, com experiência profissional, pesquisa, projetos, competências e evidências de implementação."><style>'+css+'</style><script type="application/ld+json">'+json.dumps(linked_data,ensure_ascii=False).replace('<','\\u003c')+'</script></head><body><div class="toolbar"><a href="index.html">CV original</a><div><a href="cv-experimental-data.json">Dados estruturados</a> · <a href="cv-experimental.md">Versão em texto</a> · <button id="print" type="button">Imprimir / PDF</button></div></div><main><header class="cv-header"><img src="avatar.png" alt="Danillo Xavier"><div><h1>'+esc(current['profile']['name'])+'</h1><p class="headline">'+esc(current['profile']['headline']).replace('\n','<br>')+'</p><p>'+contact+'</p><p>'+links+'</p></div></header><p class="experiment">Versão experimental ampliada · 09/10/2026 · Conteúdo original preservado; competências e tecnologias reorganizadas; novas seções de projetos e evidências acrescentadas. Extensão inicialmente em português. Versões originais: <a href="index.html?lang=en&amp;version=full">EN</a> · <a href="index.html?lang=de&amp;version=full">DE</a>.</p>'+toc+''.join(all_sections)+'<aside class="footnote"><h2>Fontes e interpretação</h2><p>Os relatos profissionais, cargos, períodos, reconhecimentos e impactos foram mantidos a partir do currículo existente. Os novos cases usam revisão estática de código, estrutura e documentos disponíveis localmente. As fontes indicam de onde vêm os métodos e competências; a existência de código não comprova autoria exclusiva, implantação ou impacto medido.</p><p>A notação <code>Agrodan@origin/development:caminho</code> identifica um arquivo em uma referência Git local. Pode ser consultado com <code>git show origin/development:caminho</code> no repositório indicado. São registros locais, sem afirmação de disponibilidade pública ou atualização remota.</p><p>Vínculos confirmados: Agrodan — experiência profissional; EBSERH — estágio no Hospital Universitário de Petrolina; The Game Project — faculdade; EFS-AHP — pesquisa do doutorado. Parte dos demais projetos vem de iniciativas empreendedoras; sua associação individual e datas não são inferidas automaticamente.</p></aside></main><footer>Danillo Xavier · CV experimental · 09/10/2026</footer><script>document.getElementById("print").addEventListener("click",()=>window.print());</script></body></html>'
    ids=set(re.findall(r'\bid="([^"]+)"',page))
    internal_links=set(re.findall(r'href="#([^"]+)"',page))
    if internal_links-ids: raise ValueError('Vínculos sem destino: '+str(internal_links-ids))
    (BASE/'cv-experimental.html').write_text(page,encoding='utf-8')
    # Text counterpart includes the same visible content for plain-text readers.
    text=re.sub(r'<(h[1-4])[^>]*>(.*?)</\1>',lambda m:'\n\n'+'#'*int(m[1][1])+' '+re.sub('<[^>]+>','',m[2])+'\n', ''.join(all_sections),flags=re.S)
    text=re.sub(r'<li[^>]*>','\n- ',text)
    text=re.sub(r'<(?:br|/p|/article|/tr)[^>]*>','\n',text)
    text=re.sub(r'<[^>]+>',' ',text)
    text=html.unescape(text)
    text=re.sub(r'[ \t]+',' ',text)
    text=re.sub(r'\n\s*\n\s*\n','\n\n',text)
    (BASE/'cv-experimental.md').write_text('# '+current['profile']['name']+'\n\n'+current['profile']['headline']+'\n\n'+html.unescape(contact)+'\n\nVersão experimental ampliada — 09/10/2026.\n'+text+'\n',encoding='utf-8')
    print(f'CV experimental gerado: {len(cases)} cases aprofundados, {len(project_records)} pastas, 94 módulos de negócio e 48 fluxos técnicos. Blocos originais preservados.')

if __name__=='__main__': build()
