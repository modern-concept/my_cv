"""Project highlights grounded in the saved SIA and Utilibox inventories."""

UTILIBOX = [
    ('ahp', 'AHP Online — decisão multicritério com consistência', ['ahp-online'],
     'Desenvolvimento de uma ferramenta de decisão multicritério que organiza critérios, comparações e alternativas em um fluxo de análise e exportação de projetos.',
     ['Comparações pela escala de Saaty e cálculo de consistência para avaliar a coerência dos julgamentos.', 'Modelagem da decisão em interface interativa, com apresentação dos resultados e exportação do projeto.'],
     'Astro · JavaScript · AHP · matrizes de comparação · consistência'),
    ('topsis-promethee', 'TOPSIS e PROMETHEE — ranking e sensibilidade de alternativas', ['topsis', 'promethee'],
     'Implementação de ferramentas para comparar alternativas com critérios, pesos e preferências configuráveis, tornando os métodos multicritério utilizáveis em decisões de gestão.',
     ['TOPSIS: classificação pela proximidade à solução ideal, com pesos e direções de critérios configuráveis.', 'PROMETHEE I e II: funções de preferência e análise de sensibilidade em tempo real.'],
     'Astro · JavaScript · TOPSIS · PROMETHEE · análise de sensibilidade'),
    ('filas', 'Teoria das Filas — capacidade, espera e dimensionamento', ['teoria-das-filas', 'queueing-theory'],
     'Desenvolvimento de calculadoras e visualizações para relacionar demanda, capacidade de atendimento e espera, apoiando estudo e comparação de configurações de serviço.',
     ['Modelos M/M/1, M/M/c, M/D/1, M/M/1/K e Erlang-B/C implementados nas rotinas de cálculo.', 'Comparação por número de servidores e curvas de sensibilidade para explorar mudanças na taxa de chegada.'],
     'JavaScript · pesquisa operacional · modelos de filas · curvas de sensibilidade'),
    ('lean', 'VSM, SMED, PDSA e A3 — engenharia de produção e melhoria contínua', ['vsm', 'smed', 'pdsa-manager', 'folha-a3'],
     'Tradução de métodos de melhoria de processos em ferramentas digitais para mapear fluxos, analisar setup, estruturar problemas e acompanhar ciclos de aprendizagem.',
     ['VSM: etapas, processamento, espera, uptime, inventário e gargalos; indicadores de lead time, takt e PCE.', 'SMED: atividades internas/externas e possibilidades de conversão e paralelização; PDSA e A3 estruturam acompanhamento e planos de ação.'],
     'Astro · JavaScript · Lean · VSM · SMED · PDSA · A3'),
    ('financeiro', 'Avaliação econômica — VPL, TIR, payback e cenários', ['calculadora-payback-vpl-tir', 'calculadora-wacc', 'simulador-ponto-de-equilibrio', 'simulador-emprestimo'],
     'Implementação de ferramentas de análise econômica para transformar fluxos de caixa, custos e condições de financiamento em indicadores comparáveis.',
     ['Cálculos de payback simples e descontado, VPL e TIR para avaliação de investimentos.', 'Ferramentas complementares para WACC, ponto de equilíbrio e comparação dos sistemas Price, SAC e SAM.'],
     'JavaScript · matemática financeira · fluxos de caixa · análise de investimentos'),
    ('priorizacao', 'Pareto, GUT e SWOT — priorização e análise gerencial', ['analise-pareto', 'matriz-gut', 'matriz-swot', 'arvore-decisao'],
     'Desenvolvimento de ferramentas de gestão que organizam problemas, critérios e cenários em rankings, gráficos e estruturas de decisão.',
     ['Pareto com curva acumulada; GUT com ranking por gravidade, urgência e tendência; SWOT com estratégias cruzadas.', 'Árvore de decisão com nós de chance e resultado, valor monetário esperado e identificação do caminho ótimo.'],
     'JavaScript · Pareto · GUT · SWOT · EMV · visualização de decisões'),
    ('conhecimento', 'Narra e UtiliNotas — conhecimento, contexto e persistência', ['narra', 'utilinotas'],
     'Construção de aplicações de organização narrativa e conhecimento com entidades relacionadas, notas conectadas e assistência contextual.',
     ['Editor Markdown, links internos e árvore de arquivos; integração entre organização das notas e contexto de uso.', 'Camada de persistência IndexedDB com controle de transações e tratamento de falhas; assistência de IA em módulos próprios.'],
     'Astro · JavaScript · Markdown · IndexedDB · modelagem de entidades · IA contextual'),
    ('aprendizagem', 'Flashcards — repetição espaçada e acompanhamento de estudo', ['anki-flashcards'],
     'Implementação de uma aplicação de estudo que organiza cartões e revisões com repetição espaçada, acompanhamento de retenção e exportação.',
     ['Algoritmo SM-2, seleção de cartões devidos e rotinas de suspensão, retomada e previsão de revisões.', 'Exportação para Anki Desktop em TSV e PDF, com decks e conteúdo estruturado.'],
     'JavaScript · SM-2 · persistência local · TSV · PDF'),
]

SIA = [
    ('sgq', 'SGQ — auditorias, registros e gestão da qualidade', 'Sistema de gestão da qualidade',
     'Desenvolvimento de módulos de qualidade com organização de auditorias, registros e papéis, articulando acompanhamento do processo e armazenamento local.',
     ['Modelagem de auditorias, configurações e responsabilidades em interfaces de gestão.', 'Camada de dados local com Dexie/IndexedDB e handlers de sincronização.']),
    ('qualidade-campo', 'Qualidade de campo — checklists e avaliações operacionais', 'Qualidade de campo e checklists',
     'Desenvolvimento de fluxos de avaliação da qualidade em campo, com checklists, respostas e integração entre a interface e o backend do domínio.',
     ['Organização de checklists e respostas com persistência local via Dexie/IndexedDB.', 'Rotinas de sincronização e rotas de backend correspondentes localizadas no acervo.']),
    ('packing', 'Packing e caixaria — interfaces de acompanhamento da operação', 'Packing e caixaria',
     'Desenvolvimento de interfaces de packing e caixaria para organizar acesso à operação e integrar eventos aos componentes de acompanhamento.',
     ['Separação dos componentes de packing e caixaria no frontend corporativo.', 'Integração de eventos via socket observada no código do módulo.']),
]

def build_records(data):
    ext = data['extensions']
    tools = {t['slug']: t for t in ext['utiliboxCatalog']}
    records = []
    for id, title, slugs, text, implementation, stack in UTILIBOX:
        selected = [tools[s] for s in slugs]
        records.append({'id': 'destaque-utilibox-' + id, 'section': 'utilibox', 'title': title,
                        'context': 'Produto independente — Utilibox', 'text': text,
                        'implementation': implementation, 'stack': stack,
                        'relatedContextAnchors': ['utilibox-tool-' + s for s in slugs],
                        'sources': list(dict.fromkeys('utilibox/' + r for t in selected for r in t['localSourceReferences']))})
    for id, title, module_title, text, implementation in SIA:
        index, module = next((i, m) for i, m in enumerate(ext['agroBusinessModules']) if m['title'] == module_title)
        records.append({'id': 'destaque-sia-' + id, 'section': 'agrodan', 'title': title,
                        'context': 'Experiência profissional — Agrodan', 'text': text,
                        'implementation': implementation, 'stack': ' · '.join(module['stack']),
                        'relatedContextAnchors': ['vinculo-agrodan', 'sia-negocio-' + str(index + 1)],
                        'sources': [s['path'] + ':' + str(s['line']) for s in module['sources']]})
    return records
