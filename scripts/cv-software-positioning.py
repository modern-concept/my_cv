"""Prioritize software engineering and traceable delivery practices in both locales."""
import copy

def editorial(value, language='pt'):
    out=copy.deepcopy(value)
    pt=language=='pt'
    out['skillGroups'].append({
        'title':'Qualidade, entrega e manutenção de software' if pt else 'Software quality, delivery and maintenance',
        'description':'Smoke tests, validação de contratos e contexto concorrente, verificação de tipos, lint, versionamento e workflow de deploy; supervisão de processos e logs.' if pt else 'Smoke tests, contract and concurrent-context validation, type checking, linting, version control and deployment workflow; process supervision and logs.',
        'origin':'Planejamento Xavier: testes do motor, cenários de contexto obsoleto, TypeScript e workflow GitHub Actions/Supabase. Launch With Me: ESLint. TraderMind: supervisor e logs; pesquisa e operação demo.' if pt else 'Planejamento Xavier: engine tests, stale-context scenarios, TypeScript and GitHub Actions/Supabase workflow. Launch With Me: ESLint. TraderMind: supervisor and logs; research and demo operation.'
    })
    out['technologyGroups'].insert(4,{
        'title':'Qualidade e entrega' if pt else 'Quality and delivery',
        'description':'Git, GitHub Actions, TypeScript, ESLint; smoke tests, validação de contratos e workflow de deploy de Supabase Edge Functions.' if pt else 'Git, GitHub Actions, TypeScript, ESLint; smoke tests, contract validation and Supabase Edge Functions deployment workflow.'
    })
    priorities=['Engenharia de software' if pt else 'Software engineering', 'Dados e decisão' if pt else 'Data and decisions', out['skillGroups'][-1]['title']]
    out['skillGroups'].sort(key=lambda group: priorities.index(group['title']) if group['title'] in priorities else len(priorities))
    out['engineeringEvidence']={
        'planejamentoxavier':['scripts/run-brain-tests.mjs','scripts/brain-strategic-stale-context-test.mjs','scripts/typecheck-app.mjs','.github/workflows/supabase-deploy.yml'],
        'launch_with_me':['package.json: scripts.lint'],
        'mt5':['TraderMind/supervisor.py']
    }
    return out
