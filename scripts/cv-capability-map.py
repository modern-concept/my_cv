"""Bilingual, evidence-based overview rendered as native HTML and SVG."""
import html
import math

DIMENSIONS = [
 ('Software e produtos','Software & products',['Agrodan','ebserh','The game project','ClassPlanner','instagram-conversion-crm','launch_with_me','planejamentoxavier','utilibox','minhas-financas']),
 ('Dados e integração','Data & integration',['Agrodan','agrodan-fruit-vision-platform','[EFS-AHP]','mt5','cartola_oracle','minhas-financas','Scrapers']),
 ('IA e automação','AI & automation',['planejamentoxavier','ClassPlanner','instagram-conversion-crm','DvrPersonAlert','mt5','mocap','instabot','Scrapers']),
 ('ML e visão','ML & vision',['[EFS-AHP]','mt5','DvrPersonAlert','mocap','AlgoritmosGeneticos','agrodan-fruit-vision-platform']),
 ('Mobile e offline','Mobile & offline',['Agrodan','planejamentoxavier']),
 ('MLOps e ciclo de modelos','MLOps & model lifecycle',['mt5','DvrPersonAlert']),
 ('Decisão e otimização','Decision & optimization',['utilibox','[EFS-AHP]','AlgoritmosGeneticos','cartola_oracle','Logistica','Agrodan']),
 ('3D e geoespacial','3D & geospatial',['dente_de_leao','mocap','movimento_3D','Logistica','Agrodan']),
]
SECTORS = [
 ('Agro e indústria','Agriculture & industry',['Agrodan','agrodan-fruit-vision-platform','AlgoritmosGeneticos']),
 ('Educação e pesquisa','Education & research',['[EFS-AHP]','The game project','ClassPlanner']),
 ('Finanças e decisões','Finance & decisions',['mt5','minhas-financas','cartola_oracle','utilibox']),
 ('Operações e logística','Operations & logistics',['Agrodan','Logistica','utilibox']),
 ('Saúde','Healthcare',['ebserh']),
 ('Produtos digitais e CRM','Digital products & CRM',['planejamentoxavier','launch_with_me','instagram-conversion-crm','Scrapers','instabot']),
 ('Interação e visão','Interaction & vision',['DvrPersonAlert','mocap','dente_de_leao','movimento_3D']),
]
STACKS = [
 ('Python / dados / ML','Python / data / ML',{'Python','pandas','scikit-learn','PyTorch','TensorFlow.js','OpenCV','NumPy'}),
 ('Web / APIs','Web / APIs',{'React','Next.js','Astro','Express','Flask','Node.js','Java EE'}),
 ('SQL / persistência','SQL / persistence',{'SQL','SQLite','PostgreSQL','Oracle','MySQL','Supabase','JPA','Hibernate'}),
 ('Mobile / offline','Mobile / offline',{'React Native','Expo','AsyncStorage','Capacitor'}),
 ('3D / mapas','3D / maps',{'Three.js','Leaflet','WebGL','React Three Fiber','Canvas'}),
 ('Automação / integração','Automation / integration',{'Playwright','Puppeteer','Telegram','Telegram Bot API','Quartz','MetaTrader 5'}),
]

def overview(data, language='pt'):
    en=language=='en'
    tr=lambda pt,eng:eng if en else pt
    esc=lambda s:html.escape(str(s),quote=True)
    projects=data['extensions']['projects']
    lookup={p['id']:p for p in projects}
    included=set(p for row in DIMENSIONS+SECTORS for p in row[2])
    if not included <= lookup.keys(): raise ValueError('Capability map references an unknown project')
    indexes={p['id']:i+1 for i,p in enumerate(projects)}
    names={'Agrodan':'SIA / SIAgro','[EFS-AHP]':'EFS-AHP','mt5':'TraderMind','agrodan-fruit-vision-platform':'Agritech.NE','ebserh':'EBSERH','The game project':'The Game Project','planejamentoxavier':'Planejamento Xavier','instagram-conversion-crm':'Conversion CRM','utilibox':'Utilibox','ClassPlanner':'ClassPlanner','AlgoritmosGeneticos':tr('Algoritmos genéticos','Genetic algorithms'),'minhas-financas':tr('Minhas Finanças','Personal finance'),'Logistica':tr('Logística','Logistics'),'dente_de_leao':'Dente de Leão','movimento_3D':'Movimento 3D','cartola_oracle':'Cartola Oracle','DvrPersonAlert':'DVR Person Alert','launch_with_me':'Launch With Me'}
    def links(ids):
        return ' · '.join('<a href="#projeto-'+str(indexes[p])+'">'+esc(names.get(p,p))+'</a>' for p in ids)
    labels=[row[1 if en else 0] for row in DIMENSIONS]
    maximum=max(len(row[2]) for row in DIMENSIONS)
    minimum=min(len(row[2]) for row in DIMENSIONS)
    # Relative portfolio index: remap the observed breadth to a 6–10 scale.
    scores=[6+4*(len(row[2])-minimum)/(maximum-minimum) for row in DIMENSIONS]
    cx,cy,radius=230,170,112
    def point(i,r):
        a=-math.pi/2+i*math.pi/4
        return (cx+math.cos(a)*r,cy+math.sin(a)*r)
    def polygon(r):return ' '.join(f'{x:.1f},{y:.1f}' for x,y in (point(i,r) for i in range(8)))
    svg='<svg class="strength-radar" viewBox="0 0 460 340" role="img" aria-labelledby="strength-chart-title"><title id="strength-chart-title">'+esc(tr('Índice relativo de abrangência por competência: escala de 6 a 10','Relative breadth index by capability: scale from 6 to 10'))+'</title>'
    for n in [2,4,6,8,10]:svg+='<polygon class="radar-grid" points="'+polygon(radius*n/10)+'"/>'
    for i in range(8):
        x,y=point(i,radius)
        svg+=f'<line class="radar-grid" x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}"/>'
    svg+='<polygon class="radar-area" points="'+' '.join(f'{x:.1f},{y:.1f}' for i,score in enumerate(scores) for x,y in [point(i,radius*score/10)])+'"/>'
    for i,row in enumerate(DIMENSIONS):
        x,y=point(i,radius*scores[i]/10)
        tx,ty=point(i,radius+28)
        anchor='middle' if i in [0,4] else 'start' if i<4 else 'end'
        score_label=f'{scores[i]:.1f}'.rstrip('0').rstrip('.').replace('.',',' if not en else '.')
        svg+=f'<circle class="radar-dot" cx="{x:.1f}" cy="{y:.1f}" r="4"/><text x="{tx:.1f}" y="{ty:.1f}" text-anchor="{anchor}">'+esc(labels[i])+f'<tspan x="{tx:.1f}" dy="14">{score_label} / 10</tspan></text>'
    svg+='</svg>'
    def bars(rows):
        high=max(n for title,n in rows)
        return '<div class="map-bars">'+''.join('<div class="map-bar"><span>'+esc(title)+'</span><div class="map-track"><i style="width:'+str(round(n/high*100))+'%"></i></div><b>'+str(n)+'</b></div>' for title,n in rows)+'</div>'
    stack_rows=[(eng if en else pt,sum(bool(set(lookup[p]['stack']) & tokens) for p in included)) for pt,eng,tokens in STACKS]
    sector_rows=[(row[1 if en else 0],len(row[2])) for row in SECTORS]
    title=tr('Habilidades, stacks e áreas de atuação','Capabilities, stacks and application domains')
    content='<section class="page full-page capability-overview"><div class="full-page-inner"><div class="map-heading"><span class="map-eyebrow">'+tr('03 / PANORAMA PROFISSIONAL','03 / PROFESSIONAL OVERVIEW')+'</span><h2 class="career-section-title" id="cv-capability-map">'+title+'</h2><p>'+tr('Engenharia de software, IA, dados e decisões conectadas à operação e ao desenvolvimento de produtos.','Software engineering, AI, data and decisions connected to operations and product development.')+'</p></div>'
    content+='<div class="map-metrics"><div><b>'+str(len(included))+'</b><span>'+tr('projetos no panorama','projects in this overview')+'</span></div><div><b>8</b><span>'+tr('frentes técnicas','technical capabilities')+'</span></div><div><b>7</b><span>'+tr('áreas de aplicação','application domains')+'</span></div></div>'
    content+='<div class="map-chart-grid"><article class="map-panel"><h3>'+tr('Força do portfólio · abrangência','Portfolio strength · breadth')+'</h3>'+svg+'</article><article class="map-panel"><h3>'+tr('Stack · presença nos projetos','Stack · presence across projects')+'</h3>'+bars(stack_rows)+'<p class="map-note">'+tr('Número de projetos que usam ao menos uma tecnologia de cada família.','Projects using at least one technology in each family.')+'</p><p class="map-stack-text">Python · SQL · JavaScript · TypeScript · Java<br>React · Node.js · Java EE · React Native<br>Oracle · PostgreSQL · SQLite · Supabase<br>scikit-learn · PyTorch · OpenCV · TensorFlow.js</p></article></div>'
    content+='<div class="map-lower-grid"><article class="map-panel"><h3>'+tr('Onde apliquei essas competências','Where I applied these capabilities')+'</h3>'+bars(sector_rows)+'</article><article class="map-panel map-highlights"><h3>'+tr('Diferenciais conectados à trajetória','Strengths connected to career experience')+'</h3><p><strong>'+tr('Liderança e operação','Leadership & operations')+'</strong><br>'+tr('Bayer, Agrodan e Labrunier: tecnologia, transformação, indicadores e integração com o negócio.','Bayer, Agrodan and Labrunier: technology, transformation, indicators and business integration.')+'</p><p><strong>Agentic AI / MLOps</strong><br>'+tr('Planejamento Xavier: coordenação multiagente. TraderMind: ciclo de modelos. Globalcom: proposta de arquitetura com RAG, MCP e auditoria.','Planejamento Xavier: multiagent coordination. TraderMind: model lifecycle. Globalcom: architecture proposal with RAG, MCP and audit.')+'</p><p><strong>'+tr('Pesquisa e melhoria contínua','Research & continuous improvement')+'</strong><br>'+tr('EFS-AHP no doutorado; Utilibox em decisão, Lean e finanças; visão industrial na Agritech.NE.','Doctoral EFS-AHP; Utilibox for decisions, Lean and finance; industrial vision at Agritech.NE.')+'</p></article></div>'
    content+='<p class="map-note">'+tr('Radar: índice relativo de abrangência do portfólio, de 6 a 10. Barras: quantidade de projetos relacionados. Um projeto pode apoiar várias frentes. Backups, referências de terceiros e a proposta Globalcom não entram na contagem.','Radar: relative portfolio breadth index, from 6 to 10. Bars: related project counts. A project may support several capabilities. Backups, third-party references and the Globalcom proposal are excluded from the counts.')+'</p></div></section>'
    provenance='<section class="page full-page capability-evidence"><div class="full-page-inner"><h2 class="career-section-title">'+tr('Projetos que sustentam o panorama','Projects supporting the overview')+'</h2><div class="map-evidence-grid">'+''.join('<article><h3>'+esc(row[1 if en else 0])+'</h3><p>'+links(row[2])+'</p></article>' for row in DIMENSIONS)+'</div></div></section>'
    evidence='<div class="map-overview-evidence"><h3>'+tr('Projetos de referência por competência','Reference projects by capability')+'</h3><div class="map-evidence-grid">'+''.join('<article><h3>'+esc(row[1 if en else 0])+'</h3><p>'+links(row[2])+'</p></article>' for row in DIMENSIONS)+'</div></div>'
    content=content.removesuffix('</div></section>')+evidence+'</div></section>'
    return content,''
