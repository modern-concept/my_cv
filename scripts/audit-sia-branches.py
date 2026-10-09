"""Read local Git references without checkout/fetch and catalog SIA business modules."""
import io
import json
import re
import subprocess
import tarfile
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parent/'Agrodan'
def git(repo,*args): return subprocess.check_output(['git',*args],cwd=repo)
def archive(repo,ref,prefix):
    raw=git(repo,'archive',ref,prefix)
    with tarfile.open(fileobj=io.BytesIO(raw)) as tar:
        return {m.name:tar.extractfile(m).read().decode('utf-8',errors='replace') for m in tar if m.isfile() and m.name.endswith(('.js','.jsx','.ts','.tsx')) and m.size<2_000_000}

# Domains and objectives are interpretations of module names, UI and code,
# with wrappers explicitly identified below to avoid inflating implementation.
DOMAINS={
'AbastecimentoFrota':('Abastecimento da frota','Frota e custos','Acompanhar abastecimentos e sua leitura gerencial'),
'Absenteismo':('Absenteísmo','Pessoas e operação','Disponibilizar acompanhamento de absenteísmo'),
'Acompanhamentos':('Acompanhamentos operacionais','Gestão','Compor cartões, filtros, gráficos e tabelas de acompanhamento'),
'Areas':('Áreas de campo e packing','Navegação operacional','Organizar acesso a informações de campo, packing e qualidade'),
'AtelEscola':('Monitoramento Atel Escola','Monitoramento ambiental','Representar dados e leituras de monitoramento de umidade no contexto do módulo'),
'AuditoriaPulverizacao':('Auditoria de pulverização','Operações agrícolas e geoinformação','Relacionar trajeto, velocidade, talhões e serviços para avaliar a execução da pulverização'),
'AuditoriaSGA':('Auditoria SGA','Auditoria operacional','Disponibilizar a visão de auditoria relacionada ao SGA'),
'AuditoriaSIA':('Auditoria SIA','Governança de dados','Disponibilizar a visão de auditoria no SIA'),
'AvaliacaoEquipe':('Avaliação de equipes','RH e desempenho','Organizar respostas, avaliação, qualidade e resumo de equipes'),
'AvaliacaoEquipeADM_OFC':('Avaliação de equipes administrativas','RH e desempenho','Representar o processo de avaliação de equipes administrativas'),
'AvaliacaoEscolaAlunoProfessor':('Avaliação aluno–professor','Educação e avaliação','Modelar a avaliação entre alunos e professores'),
'AvaliacaoEscolaGestorGestor':('Avaliação gestor–gestor','Educação e avaliação','Modelar avaliação entre gestores no contexto escolar'),
'AvaliacaoEscolaProfessorGestor':('Avaliação professor–gestor','Educação e avaliação','Modelar o processo de avaliação de gestores por professores'),
'AvaliacaoEscolaProfessorProfessor':('Avaliação professor–professor','Educação e avaliação','Modelar avaliação entre professores'),
'AvaliacaoInvertida':('Avaliação invertida','RH e avaliação','Representar uma perspectiva invertida no processo de avaliação'),
'AvaliacaoPares':('Avaliação por pares','RH e avaliação','Modelar avaliações entre pares e seus resumos'),
'BatidaPonto':('Batidas de ponto','RH e jornadas','Disponibilizar leitura de registros de ponto'),
'CFO':('Visão CFO','Gestão financeira','Disponibilizar a visão gerencial identificada como CFO'),
'COMERCIAL':('Resultados comerciais','Comercial','Organizar lançamentos, resultados, auditorias e visão gerencial comercial'),
'CONTAS_PAGAR':('Contas a pagar','Finanças','Disponibilizar acompanhamento de contas a pagar'),
'CadastroTalhoes':('Cadastro de talhões','Gestão agrícola','Disponibilizar consulta/gestão do cadastro de talhões'),
'CadernoCampo':('Caderno de campo','Coleta agrícola','Organizar apontamentos, seleção de equipe, atividade e qualidade, com armazenamento local e sincronização no código'),
'CaixasEmbaladas':('Caixas embaladas','Packing','Disponibilizar acompanhamento de caixas embaladas'),
'CaixasEmbaladasUgb':('Caixas embaladas por UGB','Packing e unidades de gestão','Relacionar a leitura de embalagem às unidades de gestão'),
'ConferenciaInsumos':('Conferência de insumos','Suprimentos e operação','Disponibilizar informações para conferência de insumos'),
'ControlePallets':('Controle de pallets','Packing e rastreabilidade','Disponibilizar leitura de controle dos pallets'),
'ControleQualidade':('Controle de qualidade','Qualidade','Disponibilizar acompanhamento de controle de qualidade'),
'ControleRecebimento':('Controle de recebimento','Packing e suprimentos','Disponibilizar a leitura do recebimento operacional'),
'CronogramaSafra':('Cronograma de safra','Planejamento agrícola','Organizar cronograma, colheita e edição da programação'),
'CronogramaSafraForm':('Formulário do cronograma de safra','Coleta e planejamento','Representar a entrada/edição de cronograma e talhões'),
'CronogramaSafraSIA':('Cronograma de safra integrado ao SIA','Planejamento e sincronização','Relacionar edição, visualização e sincronização da programação de safra'),
'Croquis':('Croquis','Informação espacial','Disponibilizar representação de croquis'),
'Custos':('Custos','Controladoria','Disponibilizar acompanhamento dos custos operacionais'),
'DashSatisfacao':('Dashboard de satisfação','Qualidade de serviço','Disponibilizar visão consolidada de satisfação'),
'Embalagem':('Embalagem','Packing','Disponibilizar indicadores da operação de embalagem'),
'EstoqueVirtual':('Estoque virtual','Estoques','Integrar a consulta ao dashboard de estoque virtual'),
'Faturamento':('Faturamento','Comercial e finanças','Disponibilizar acompanhamento de faturamento'),
'FechamentoTalhoes':('Fechamento de talhões','Planejamento agrícola','Disponibilizar acompanhamento de fechamento dos talhões'),
'FlutuacaoPreco':('Flutuação de preços','Comercial','Disponibilizar leitura da variação de preços'),
'FolhaPagamento':('Folha de pagamento','RH e finanças','Disponibilizar acompanhamento da folha de pagamento'),
'GestaoEstoque':('Gestão de estoque','Supply chain','Disponibilizar a visão de gestão de estoque'),
'GestaoUGBs':('Gestão de unidades de negócio','Gestão organizacional','Articular UGBs, colaboradores, avaliações, planos e melhorias em uma estrutura modular'),
'Horimetro':('Horímetro','Frota e equipamentos','Disponibilizar acompanhamento de horas dos equipamentos'),
'IndicadorBPM':('Indicadores e satisfação BPM','Gestão de processos','Organizar indicadores e registros de satisfação do serviço'),
'IndicadorLogistica':('Satisfação da logística','Logística e qualidade de serviço','Representar satisfação relacionada à logística'),
'IndicadorTI':('Indicadores de TI e fila de chamados','Gestão de TIC','Relacionar indicadores, satisfação e fila de chamados'),
'Irrigacao':('Monitoramento de irrigação','Irrigação agrícola','Organizar monitoramento e entrada de dados relacionados à irrigação'),
'Irrigas':('Visão Irrigas','Irrigação','Disponibilizar a visão identificada como Irrigas'),
'LeanPackingGame':('Lean Packing Game','Produção e aprendizagem','Integrar acesso ao simulador de operações Lean Packing Game'),
'Log Horas':('Registro de horas','Operação e jornadas','Organizar o registro e a leitura de horas'),
'MAD':('Monitoramento MAD','Monitoramento agrícola','Representar dados de umidade/monitoramento presentes neste módulo'),
'MAF':('Monitoramento MAF e manga','Qualidade do fruto','Representar manga, posições de linhas e dados do monitoramento MAF'),
'MIP':('Monitoramento integrado de pragas','Agricultura e geoinformação','Representar dados de pragas no módulo MIP'),
'MateriaSeca':('Matéria seca e previsão de colheita','Qualidade e maturação','Relacionar leituras, variedades e equações para explorar previsão e ponto de colheita'),
'Materiais':('Materiais','Suprimentos','Disponibilizar informações de materiais'),
'MovimentacaoMateriais':('Movimentação de materiais','Suprimentos e rastreabilidade','Disponibilizar informações de movimentação de materiais'),
'MovimentacaoPallet':('Movimentação de pallets e containers','Packing e logística','Organizar movimentações, dados de container e conferências'),
'Orcamento':('Orçamento','Controladoria','Disponibilizar acompanhamento do orçamento'),
'Organograma':('Organograma e áreas','RH e estrutura organizacional','Representar áreas, indicadores e organização das fazendas'),
'PDCA':('PDCA de mão de obra','Gestão e melhoria contínua','Organizar planos, auditorias e acompanhamento gerencial de mão de obra'),
'Packing':('Packing e caixaria','Produção e embalagem','Organizar acesso à operação de packing e caixaria'),
'PlanejamentoAgro':('PLANAGRO — planejamento e regras agrícolas','Planejamento agronômico e governança','Relacionar atividades, insumos, orçamento e verificações de aplicação, carência, dosagem e deriva'),
'PrevisaoResultados':('Previsão de resultados e câmbio','Planejamento comercial','Organizar previsões, acompanhamento de resultados e contexto de câmbio'),
'ProgramacaoProcessamento':('Programação de processamento','Packing e capacidade','Disponibilizar a programação de processamento'),
'Projetos':('Projetos','Gestão de projetos','Disponibilizar informações de projetos'),
'QtdFuncionarios':('Quantidade de funcionários','RH e operação','Disponibilizar indicadores de quantidade de colaboradores'),
'QualidadeCampo':('Qualidade de campo e checklists','Qualidade agrícola','Organizar checklists, respostas e avaliação de qualidade de campo'),
'RH':('Visão de RH','Gestão de pessoas','Disponibilizar acesso às informações de recursos humanos'),
'RISCO_SST':('Riscos de segurança do trabalho','SST e geoinformação','Representar riscos de segurança do trabalho no contexto agrícola'),
'Ramais':('Ramais','Serviços corporativos','Disponibilizar consulta aos ramais corporativos'),
'Refugo':('Refugo','Packing e qualidade','Disponibilizar leitura de refugo na operação'),
'RelatoriosBI':('Relatórios BI','Analytics','Integrar o acesso a relatórios de BI'),
'ResumoMO':('Resumo de mão de obra','RH e operação','Disponibilizar leitura consolidada de mão de obra'),
'RitualGerencial':('Ritual gerencial','Gestão','Disponibilizar informações para acompanhamento gerencial'),
'SGQ':('Sistema de gestão da qualidade','Auditoria e qualidade','Organizar auditorias, registros, papéis e acompanhamento da qualidade'),
'SgqRelatorios':('Relatórios de qualidade','Qualidade e analytics','Organizar relatórios vinculados ao SGQ'),
'SaldoBH':('Saldo de banco de horas','RH e jornadas','Disponibilizar o acompanhamento do saldo de horas'),
'Satisfacao':('Satisfação','Qualidade de serviço','Disponibilizar informações de satisfação'),
'Seguranca':('Segurança','Segurança e gestão','Disponibilizar informações do módulo identificado como Segurança'),
'SolicitacaoCompras':('Solicitações de compras','Compras e orçamento','Organizar itens, centros e solicitações, com contexto local e sincronização no código'),
'SugestaoMelhorias':('Sugestões de melhoria','Inovação e melhoria contínua','Organizar submissão, avaliação e tratamento de sugestões e registros associados'),
'UgbOficina':('UGB Oficina','Manutenção e gestão','Disponibilizar a visão da unidade de oficina'),
'ValidacaoColheita':('Validação de colheita','Operação agrícola','Disponibilizar a leitura de validação da colheita'),
'ValidacaoMDO':('Validação MDO','Pessoas e operação','Disponibilizar validação de mão de obra no módulo MDO'),
'ValidacaoMO':('Validação de mão de obra','Pessoas e operação','Disponibilizar a visão de validação de mão de obra'),
'Vigias':('Monitoramento de vigias','Operação e vigilância','Representar acompanhamento de vigias e informação espacial'),
}
BACKEND={
'CadernoCampo':'rotas-caderno-campo.js','CronogramaSafraSIA':'rotas-cronograma-safra.js','QualidadeCampo':'rotas-qualidade-campo.js','PlanejamentoAgro':'rotas-planagro.js','PrevisaoResultados':'rotas-previsao-resultados.js','SolicitacaoCompras':'rotas-solicitacao-compras.js','SugestaoMelhorias':'rotas-sugestao-melhorias.js','COMERCIAL':'comercial/rotas-comercial.js','MateriaSeca':'rotas-materia-seca.js','MovimentacaoPallet':'rotas-containers.js','GestaoUGBs':'rotas-gestaoUGB.js','AvaliacaoEquipe':'rotas-avaliacao-equipe.js','AvaliacaoInvertida':'rotas-avaliacao-invertida.js','AvaliacaoPares':'rotas-avaliacao-pares.js','Irrigacao':'rotas-irrigacao.js','MAD':'rotas-mad.js','MAF':'maf/rotas-maf.js','IndicadorTI':'rotas-ti.js','IndicadorBPM':'rotas-satisfacao-bpm.js','Log Horas':'rotas-log-horas.js','MovimentacaoMateriais':'rotas-movimentacao-materiais.js','Materiais':'rotas-materiais.js','Orcamento':'rotas-orcamento.js','ValidacaoMDO':'rotas-validacao-mdo.js','AuditoriaPulverizacao':'rotas-miam.js'}

def audit():
    refs=[r for r in git(ROOT,'for-each-ref','--format=%(refname:short)','refs/remotes/origin').decode().splitlines() if r!='origin']
    trees={r:git(ROOT,'ls-tree','-r','--name-only',r).decode('utf-8').splitlines() for r in refs}
    cached={}
    backend=archive(ROOT/'etl','origin/development','servers/server-backend')
    modules=[]
    for key,(title,domain,goal) in DOMAINS.items():
        prefix='src/pages/'+key+'/'
        containing=[r for r in refs if any(p.startswith(prefix) and p.endswith(('.js','.jsx')) for p in trees[r])]
        if not containing: continue
        ref='origin/development' if 'origin/development' in containing else max(containing,key=lambda r:sum(p.startswith(prefix) for p in trees[r]))
        if ref not in cached: cached[ref]=archive(ROOT,ref,'src/pages')
        files={p:s for p,s in cached[ref].items() if p.startswith(prefix)}
        names=sorted(files,key=lambda p:(p.count('/'),not p.endswith('/'+key+'.js'),p))
        imports=set()
        for s in files.values():
            imports.update(m for m in re.findall(r"(?:from\s*|require\()[\"']([^\"']+)[\"']",s) if not m.startswith(('.','/')))
        joined='\n'.join(files.values())
        iframe=any('<iframe' in s for s in files.values())
        wrappers=len(files)<=2 and iframe
        features=[]
        for marker,label in [('Dexie','Persistência IndexedDB via Dexie'),('localDb','Camada de dados local'),('handleSinc','Handlers de sincronização'),('sync','Referências a sincronização'),('useState','Estado por hooks'),('useEffect','Efeitos e carregamento por hooks'),('Leaflet','Mapas e informação espacial'),('react-leaflet','Mapas Leaflet'),('xlsx','Planilhas'),('react-to-print','Impressão'),('socket.io','Eventos via socket'),('axios','Integração HTTP'),('avisoCarencia','Regra de carência'),('avisoDosagem','Regra de dosagem'),('avisoDeriva','Regra de deriva'),('calcular_previsao','Função de previsão'),('isPontoColheita','Regra de ponto de colheita')]:
            if marker in joined: features.append(label)
        symbols=[]
        for path in names:
            for match in re.finditer(r'(?m)(?:function\s+(\w+)\s*\(|(?:const|let)\s+(\w+)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>)',files[path]):
                symbol=match.group(1) or match.group(2)
                if symbol not in ['styles','TabPanel','TabContainer','withStyles','getTabContent','pagina']: symbols.append({'name':symbol,'path':path,'line':files[path][:match.start()].count('\n')+1})
        sources=[{'path':'Agrodan@'+ref+':'+p,'line':1} for p in names[:3]]
        endpoint=[]
        mapped=BACKEND.get(key)
        bp='servers/server-backend/rotas/'+mapped if mapped else None
        if bp in backend:
            sources.append({'path':'Agrodan/etl@origin/development:'+bp,'line':1})
            endpoint=re.findall(r"\.\s*(?:get|post|put|delete)\s*\(\s*['\"]([^'\"]+)['\"]",backend[bp])
            features.append('Rotas backend correspondentes localizadas')
        skills=['Integração de informações','Interface React'] if wrappers else ['Modelagem de processo','Engenharia frontend','Estado e interação','Integração de dados']
        skills.extend(features[:5])
        status='Página de integração/embedding de dashboard ou simulador; não comprova autoria do recurso incorporado' if wrappers else 'Código de módulo em referência Git local; uso e implantação a contextualizar'
        packages=sorted({'/'.join(m.split('/')[:2]) if m.startswith('@') else m.split('/')[0] for m in imports})
        modules.append({'title':title,'domain':domain,'objective':goal,'sources':sources,'skills':skills,'stack':packages,'importsObserved':sorted(imports), 'status':status,'implementationSignals':features,'sourceFiles':len(files),'branches':containing,'representativeRef':ref,'embeddedContent':iframe,'wrapperOnlyEvidence':wrappers,'symbols':symbols[:14],'backendRoutes':list(dict.fromkeys(endpoint))[:14],
          'result':'Código e integração identificados nesta revisão; não inferir resultado de negócio ou produção a partir da branch.'})
    # Add submodules as parts of the UGB application, explicitly linked to parent.
    dev=cached.get('origin/development') or archive(ROOT,'origin/development','src/pages')
    subprefix='src/pages/GestaoUGBs/Modulos/'
    for key,title in [('Funcionarios','Gestão UGB — colaboradores e histórico'),('UGBs','Gestão UGB — unidades e papéis'),('5S','Gestão UGB — 5S'),('Avaliacao_humana','Gestão UGB — avaliação humana'),('PlanoAcao','Gestão UGB — plano de ação'),('QualificacaoTecnica','Gestão UGB — qualificação técnica'),('RequalificacaoTecnica','Gestão UGB — requalificação técnica'),('SugestaoMelhorias','Gestão UGB — sugestões de melhoria')]:
        files={p:s for p,s in dev.items() if p.startswith(subprefix+key+'/')}
        if not files: continue
        primary=subprefix+key+'/index.js'
        joined='\n'.join(files.values())
        modules.append({'title':title,'domain':'Submódulo de Gestão UGB; relacionado ao case principal','objective':'Representar '+title.split(' — ')[-1]+' no fluxo de gestão das unidades','sources':[{'path':'Agrodan@origin/development:'+primary,'line':1}], 'skills':['Modelagem organizacional','Interfaces de gestão','Reuso de componentes'],'stack':['React','JavaScript'],'status':'Submódulo; não contar como produto independente','implementationSignals':['Código do fluxo de gestão UGB'],'sourceFiles':len(files),'branches':['origin/development'],'representativeRef':'origin/development','symbols':[],'backendRoutes':[],'wrapperOnlyEvidence':False,'embeddedContent':'<iframe' in joined})
    manifest=json.loads(git(ROOT,'show','origin/development:package.json').decode('utf-8'))
    payload={'method':'Revisão estática de referências Git já disponíveis localmente, sem checkout, fetch, execução ou alteração do SIA. Módulos são agrupados pelo caminho de negócio; variações entre branches não são novos projetos. Bibliotecas declaradas, wrappers e submódulos são identificados.', 'refs':refs,'branchesInspected':len(refs),'frontendFilesInDevelopment':sum(p.startswith('src/') and p.endswith(('.js','.jsx','.ts','.tsx')) for p in trees['origin/development']),'modules':modules,'frontendManifest':manifest.get('dependencies',{})}
    (BASE/'sia-branch-cases.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'SIA: {len(refs)} refs locais, {len(modules)} módulos/submódulos de negócio; {sum(m["wrapperOnlyEvidence"] for m in modules)} com evidência principal de embedding.')

if __name__=='__main__': audit()
