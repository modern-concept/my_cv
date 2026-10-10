"""Public project destinations used by both language renderers."""
import html
import json
import re
from pathlib import Path

REGISTRY=json.loads((Path(__file__).resolve().parents[1]/'cv-project-links.json').read_text(encoding='utf-8'))

def project_links(values, language='pt'):
    destinations={}
    for value in values:
        # The CV data is evidence for a career claim, not an infrastructure project.
        if value == 'my_ cv/cv-data.json':
            continue
        for key,project in REGISTRY['projects'].items():
            if value==key or value.startswith(key+'/'):
                for kind in ['site','repository']:
                    if project.get(kind):
                        label=('Site publicado' if kind=='site' else 'Repositório público') if language=='pt' else ('Live website' if kind=='site' else 'Public repository')
                        destinations[project[kind]]=label+' — '+project['name']
        tool=re.search(r'^utilibox/src/tools/([^/]+)',value)
        if tool and tool[1] in REGISTRY['utiliboxTools']:
            url=REGISTRY['utiliboxTools'][tool[1]]
            destinations[url]=('Abrir ferramenta' if language=='pt' else 'Open tool')+' — '+tool[1]
    # Specific published tools supersede the generic Utilibox landing page.
    if any(url.startswith('https://utiliboxapp.com.br/tools/') for url in destinations):
        destinations.pop('https://utiliboxapp.com.br/',None)
    return ' · '.join('<a class="project-public-link" href="'+html.escape(url,quote=True)+'" target="_blank" rel="noopener noreferrer">'+html.escape(label)+'</a>' for url,label in destinations.items())

def sources(values, language='pt'):
    links=project_links(values,language)
    if links:return '<p class="sources project-links">'+links+'</p>'
    return '<ul class="sources">'+''.join('<li><code>'+html.escape(v)+'</code></li>' for v in values)+'</ul>'

def source_heading(values, language='pt'):
    return ('Links do projeto' if language=='pt' else 'Project links') if project_links(values,language) else ('Fontes do projeto' if language=='pt' else 'Project sources')
