"""Agrodan platform development from the final Agritech.NE project report."""
import copy

ID='agrodan-fruit-vision-platform'
CONTEXT='Agrodan · projeto de P&D da Plataforma Agritech.NE · atuação como desenvolvedor'
STACK=['Visão computacional','Deep Learning','Câmeras','APIs','ERP','Integração com classificadora','Dashboard','Telegram','Servidor dedicado','CRISP-DM']
EN_STACK=['Computer vision','Deep Learning','Cameras','APIs','ERP','Sorting-machine integration','Dashboard','Telegram','Dedicated server','CRISP-DM']
PROJECT={
 'id':ID,'title':'Agrodan / Agritech.NE — plataforma de contagem de frutas e rastreabilidade no packing',
 'area':'Visão computacional, integração industrial e eficiência operacional',
 'status':'Projeto de P&D com implementação e resultados registrados em relatório final de março/2024',
 'priority':'Destaque','association':CONTEXT,'experience':CONTEXT,
 'summary':'Atuação como desenvolvedor na plataforma de identificação e contagem de frutos na esteira de refugo do packing, integrando visão computacional, dados do ERP, classificadora, dashboard e alertas Telegram para apoiar rastreabilidade, acompanhamento dos lotes e redução das paradas de troca.',
 'structure':'Plataforma que relaciona contagem e rastreamento por câmeras, dados do ERP e da classificadora, cálculo do volume processado, acompanhamento e notificações.',
 'stack':STACK,'skills':['Desenvolvimento de plataforma','Visão computacional aplicada','Integração de dados industriais','APIs','Rastreabilidade de lotes','Indicadores operacionais','Automação de notificações','CRISP-DM','P&D aplicado','Eficiência operacional'],
 'evidence':['final-project-report'],'sourceArtifact':'Relatório Final do Trabalho do Bolsista.docx',
 'value':'Integração entre IA, dados e operação industrial para apoiar decisões de troca de lotes e rastreabilidade.',
 'limits':'Participação de Danillo como desenvolvedor confirmada pelo usuário. O relatório identifica outro integrante como bolsista; os resultados são do projeto/equipe. A variação de 30 para 37,5 caixas/h corresponde a 25%, diferente dos 22,5% citados no texto; o CV apresenta os valores absolutos.',
 'breadth':{'applicationAreas':['Agronegócio','Fruticultura','Packing house','Indústria de alimentos','Visão computacional','Rastreabilidade','Automação industrial','Melhoria de processos'],
 'intendedAudience':'Operadores da classificadora, equipes de packing e gestores da Agrodan',
 'problemAndObjective':'Acompanhar o processamento dos lotes e indicar a troca de origem da fruta, reduzindo interrupções e mantendo a rastreabilidade',
 'observableDeliverables':'Desenvolvimento de plataforma, integração por API, aplicação de contagem e sistema de notificações, com dashboard e hospedagem dedicada no escopo; o relatório registra treinamento e acompanhamento em fevereiro/2024',
 'domainMethods':'CRISP-DM; contagem e rastreamento para evitar duplicidades; estimativa de peso por calibre e variedade; reconciliação entre entrada, embalagem e refugo; acompanhamento em tempo real'},
 'reportedProjectResults':{'reportDate':'2024-03','throughputBoxesPerHour':{'before':30,'after':37.5},'dailyChangeoverDowntimeMinutes':{'before':45,'after':5},'operatingCostReductionPercent':17,'reportedFruitCountingPrecisionPercent':98,'attribution':'Resultados do projeto/equipe conforme relatório final; contribuição de Danillo como desenvolvedor.'}
}
EN_PROJECT=('Agrodan / Agritech.NE — fruit counting and packing traceability platform',
 'Worked as a platform developer during the Agrodan employment period, connecting fruit counting and tracking on the reject conveyor with ERP and sorting-machine data, an operational dashboard and Telegram alerts for batch traceability and changeover decisions. The final project report is dated March 2024.')

ROWS=[
 ('Desenvolvimento da plataforma de visão computacional no packing','Computer vision platform development for packing operations',
 'Atuei como desenvolvedor no projeto da plataforma, durante meu vínculo na Agrodan, conectando a solução de contagem e rastreamento de frutos ao acompanhamento operacional do packing.',
 'Worked as a developer on the platform project during my Agrodan employment period, connecting fruit counting and tracking to operational packing monitoring.',
 ['Plataforma para identificar e registrar mangas na esteira de refugo, com contagem e rastreamento para evitar duplicidades.', 'Integração entre aplicação de contagem, API de dados industriais, dashboard e notificações; o relatório descreve duas câmeras em funcionamento.', 'Projeto de P&D em parceria com a Agrodan no contexto da Plataforma Agritech.NE, com metodologia CRISP-DM e acompanhamento dos resultados.'],
 ['Platform for identifying and recording mangoes on the reject conveyor, with counting and tracking to avoid duplicates.', 'Connected the counting application, industrial data API, dashboard and notifications; the report describes two operating cameras.', 'Applied R&D project with Agrodan in the Agritech.NE context, using CRISP-DM and project result follow-up.']),
 ('Integração ERP, classificadora e rastreabilidade de lotes','ERP, sorting-machine integration and batch traceability',
 'A plataforma relaciona o lote recebido, a quantidade embalada e o refugo para acompanhar a origem da fruta e apoiar a transição entre lotes.',
 'The platform connects incoming batches, packed volume and rejected fruit to track fruit origin and support batch transitions.',
 ['API para acessar dados da classificadora e de embalagem, combinados com registros de lote do ERP e informações de variedade, colheita e manejo.', 'A contagem de frutos é combinada com a distribuição de calibres da classificadora e faixas de peso por variedade para estimar o peso do refugo.', 'Reconciliação entre volume de entrada, volume embalado e peso estimado do refugo; verificação de proximidade de 98% do volume de entrada para apoiar a troca de lote.'],
 ['API access to sorting-machine and packing data, combined with ERP batch records and variety, harvest and handling information.', 'Fruit counts are combined with the sorting-machine size distribution and variety-specific weight ranges to estimate reject weight.', 'Reconciled incoming volume, packed volume and estimated reject weight; a 98% incoming-volume proximity threshold supports batch-change decisions.']),
 ('Dashboard, alertas e apoio à decisão operacional','Dashboard, alerts and operational decision support',
 'Desenvolvimento da plataforma de acompanhamento e notificações para dar aos operadores informação sobre o processamento e o momento de troca de lote.',
 'Developed the monitoring and notification platform to provide operators with processing information and batch-change timing.',
 ['Acompanhamento dos dados integrados de produção e preparação de avisos via Telegram quando o volume processado se aproxima do volume de entrada.', 'O escopo prevê aplicações de contagem e acompanhamento em servidor dedicado; o relatório registra treinamento e acompanhamento em fevereiro/2024.', 'A contagem, os calibres e o volume de processamento apoiam a decisão operacional sem depender apenas da retirada manual da fruta do tanque.'],
 ['Monitored integrated production data and prepared Telegram alerts when processed volume approaches incoming volume.', 'The scope includes dedicated-server counting and monitoring applications; the report records training and follow-up in February 2024.', 'Counts, size distributions and processing volume support operational decisions beyond manual fruit removal from the tank.']),
 ('Resultados do projeto e melhoria do processo industrial','Project outcomes and industrial process improvement',
 'A integração da plataforma ao processo de packing apresentou ganhos registrados no relatório final do projeto, relacionados à produtividade, paradas e custos operacionais.',
 'Platform integration into the packing workflow produced project-level outcomes recorded in the final report, covering throughput, downtime and operating costs.',
 ['Produção registrada no relatório: de 30 para 37,5 caixas por hora; paradas por troca de controle: de 45 para 5 minutos por dia.', 'O relatório registra redução de 17% dos custos operacionais relacionados à mão de obra e ao tempo de processamento.', 'Precisão de contagem reportada de 98%; a calibração por variedade continuava necessária, com ajuste específico para manga Kent indicado no relatório.'],
 ['Reported throughput increased from 30 to 37.5 boxes per hour; daily control-change downtime decreased from 45 to 5 minutes.', 'The report records a 17% reduction in operating costs associated with labor and processing time.', 'Reported counting precision was 98%; variety-specific calibration remained necessary, with a Kent mango adjustment identified in the report.'])
]

def cases(language='pt'):
    result=[]
    for i,(pt_title,en_title,pt_text,en_text,pt_impl,en_impl) in enumerate(ROWS,1):
        result.append({'id':'case-agritech-'+str(i),'title':pt_title if language=='pt' else en_title,
          'text':pt_text if language=='pt' else en_text,'problem':'Apoiar rastreabilidade, acompanhamento de lotes e redução de interrupções no packing' if language=='pt' else 'Support traceability, batch monitoring and fewer packing interruptions',
          'implementation':pt_impl if language=='pt' else en_impl,'skills':PROJECT['skills'] if language=='pt' else ['Platform development','Computer vision integration','Industrial data integration','APIs','Batch traceability','Operational dashboards','R&D','CRISP-DM'],
          'stack':' · '.join(STACK if language=='pt' else EN_STACK),
          'context':CONTEXT if language=='pt' else 'Agrodan · Agritech.NE applied R&D project · platform developer',
          'sources':[ID+'/final-project-report'],'limit':PROJECT['limits'],
          'relatedContextAnchors':['vinculo-agrodan'],'depth':'Desenvolvimento de plataforma e integração industrial' if language=='pt' else 'Platform development and industrial integration'})
    return result

def inject(proposal):
    proposal['projects'].append(copy.deepcopy(PROJECT))
    proposal['topics'].append({'id':'agritech','title':'Agrodan / Agritech.NE — desenvolvimento de plataforma e visão computacional industrial',
      'intro':'Experiência como desenvolvedor durante o vínculo na Agrodan. Projeto de contagem automatizada de frutas, integração industrial e rastreabilidade no packing; relatório final de março/2024.',
      'text':['O projeto integra fruticultura, indústria de alimentos, visão computacional, Deep Learning, dados de produção, APIs, dashboards, notificações e melhoria de processos. Os resultados apresentados são os registrados para o projeto/equipe.'],
      'flow':['Contagem e rastreamento','Integração ERP e classificadora','Estimativa de peso e reconciliação de volumes','Acompanhamento e notificações','Avaliação operacional'], 'cases':cases()})

def enhance_editorial(editorial,language='pt'):
    out=copy.deepcopy(editorial)
    origin=' Plataforma de contagem e rastreabilidade de frutas Agrodan/Agritech.NE: atuação como desenvolvedor.' if language=='pt' else ' Agrodan/Agritech.NE fruit counting and traceability platform: developer contribution.'
    for i in [0,2,3,5]:out['skillGroups'][i]['origin']+=origin
    out['skillGroups'].append({'title':'Visão computacional e integração industrial' if language=='pt' else 'Computer vision and industrial integration',
      'description':'Desenvolvimento de plataforma com contagem/rastreamento de frutos, integração ERP/classificadora, estimativa de peso, dashboard e alertas operacionais.' if language=='pt' else 'Platform development with fruit counting/tracking, ERP/sorting-machine integration, weight estimation, dashboard and operational alerts.',
      'origin':'Agrodan / Plataforma Agritech.NE — projeto de P&D, relatório final de março/2024.' if language=='pt' else 'Agrodan / Agritech.NE — applied R&D project, March 2024 final report.'})
    out['technologyGroups'].append({'title':'Integração de IA no packing' if language=='pt' else 'Packing AI integration',
      'description':'Visão computacional, Deep Learning, câmeras, APIs, ERP, classificadora, dashboard, Telegram e servidor dedicado; CRISP-DM como metodologia do projeto.' if language=='pt' else 'Computer vision, Deep Learning, cameras, APIs, ERP, sorting machine, dashboard, Telegram and a dedicated server; CRISP-DM project methodology.'})
    return out

def experience_markup(language='pt'):
    title='Experiência em P&D industrial — Agrodan / Agritech.NE' if language=='pt' else 'Industrial R&D experience — Agrodan / Agritech.NE'
    role='Desenvolvedor da plataforma de contagem e rastreabilidade de frutas' if language=='pt' else 'Fruit counting and traceability platform developer'
    period='Durante o vínculo na Agrodan · relatório final: março/2024' if language=='pt' else 'During the Agrodan employment period · final report: March 2024'
    body=PROJECT['summary'] if language=='pt' else EN_PROJECT[1]
    label='Projeto e participação técnica' if language=='pt' else 'Project and technical contribution'
    return '<section class="page full-page career-project-page"><div class="full-page-inner"><h2 class="career-section-title" id="cv-pd-industrial">'+title+'</h2><article class="career-project"><h3>'+role+'</h3><p class="career-context">'+period+'</p><p>'+body+'</p><p class="career-reference"><a href="#resumo-case-agritech-1">'+label+'</a></p></article></div></section>'
