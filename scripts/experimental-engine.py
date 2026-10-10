"""Extend the existing complete CV renderer without changing its source file."""
import html
import json
import re
import runpy


def build_page(base, data, sections, jobs, education, primary_count, language='pt'):
    page = (base / 'index.html').read_text(encoding='utf-8-sig')
    page = page.replace('<title>CV — Danillo Xavier</title>', '<title>CV completo experimental — Danillo Xavier</title>')
    css = (base / 'scripts/experimental-engine.css').read_text(encoding='utf-8')
    page = page.replace('</head>', '<style>' + css + '</style></head>', 1)
    # Static extensions remain readable in the HTML; the existing renderer fills
    # the original CV, letters, languages and controls from the embedded data.
    supplemental = []
    aliases = {'profissional': 'fullExperiencePrimary', 'trajetoria': 'fullExperienceSecondary'}
    for part in sections:
        for old, new in aliases.items():
            part = part.replace('href="#' + old + '"', 'href="#' + new + '"')
        part = part.replace('class="chapter ', 'class="chapter full-card ')
        supplemental.append('<section class="page full-page experimental-page"><div class="full-page-inner">' + part + '</div></section>')
    toc = '<nav class="full-card extension-toc" aria-label="Índice do acervo técnico"><h2>Acervo técnico e fontes dos projetos</h2><ol>' + ''.join('<li><a href="#' + re.search(r'<section id="([^"]+)"', p)[1] + '">' + re.search(r'<h2>(.*?)</h2>', p)[1] + '</a></li>' for p in sections) + '</ol><p><a href="index.html?lang=pt&amp;version=full">CV original</a> · <a href="cv-experimental.md">Versão textual completa</a> · <a href="cv-experimental-data.json">Dados e fontes</a></p></nav>'
    supplemental.insert(0, '<section class="page full-page experimental-page"><div class="full-page-inner">' + toc + '</div></section>')
    editorial = runpy.run_path(str(base / 'scripts/cv-editorial.py'))
    english = runpy.run_path(str(base / 'scripts/cv-english.py'))
    if language == 'en':
        # Translate navigation separately so repository identifiers and source
        # paths in the already-English archive are never rewritten.
        supplemental[0] = english['translate_labels'](supplemental[0]).replace('cv-experimental.md','cv-experimental-en.md').replace('index.html?lang=pt','index.html?lang=en')
    start = page.index('  <div class="full-cv-view" id="fullCvView">')
    end = page.index('  <script>\n    const DATA_URL', start)
    annex = '<details id="careerAppendices" class="career-appendices"><summary>Acervo técnico completo · cases, catálogos e fontes</summary>' + ''.join(supplemental) + '</details>'
    # Retain the complete CV's actual markup: header, two-column cards,
    # experience grid and original section headings. Add content afterwards.
    original_view = page[start:end]
    closing = original_view.rfind('</div>')
    navigation = '<section class="page full-page career-navigation"><div class="full-page-inner"><div class="full-card career-actions"><a href="#cv-agrodan">SIA / Agrodan</a><a href="#cv-utilibox">Utilibox e métodos aplicados</a><a href="#cv-ia">IA e multiagentes</a><label><input type="checkbox" id="includeAppendices"> Incluir acervo técnico no PDF</label></div></div></section>'
    if language == 'en':
        navigation = english['translate_labels'](navigation)
        annex = annex.replace('<summary>Acervo técnico completo · cases, catálogos e fontes</summary>', '<summary>Complete technical archive · cases, catalogs and sources</summary>', 1)
    career = editorial['core_sections'](data, language)
    page = page[:start] + original_view[:closing] + navigation + career + annex + original_view[closing:] + page[end:]
    page = page.replace('const DATA_URL = "cv-data.json";', 'const DATA_URL = "cv-experimental-data.json";')
    payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
    page = page.replace('  <script>\n    const DATA_URL', '<script id="experimentalData" type="application/json">' + payload + '</script>\n  <script>\n    const DATA_URL', 1)
    page = page.replace('const res = await fetch(DATA_URL, {cache:"no-store"});\n      const data = await res.json();', 'const data = JSON.parse(document.getElementById("experimentalData").textContent);')
    page = page.replace('requestedLang || localStorage.getItem("cv_lang") || (data.meta && data.meta.defaultLang) || "pt"', 'requestedLang || "'+language+'"')
    page = page.replace('if(!data.languages[lang]) lang = "pt";', 'if(!["pt", "en"].includes(lang)) lang = "'+language+'";\n      if(lang !== "'+language+'") { const target = new URL(lang === "en" ? "cv-experimental-en.html" : "cv-experimental.html", location.href); target.search = location.search; location.replace(target); return; }')
    page = page.replace('lang = ({pt: "en", en: "de", de: "pt"})[lang] || "en";', 'lang = lang === "pt" ? "en" : "pt";')
    page = page.replace('lang = ({pt: "en", en: "pt"})[lang] || "en";', 'lang = lang === "pt" ? "en" : "pt";')
    handler = '\n'.join([
        '$("langBtn").addEventListener("click", () => {',
        '        const nextLang = lang === "pt" ? "en" : "pt";',
        '        localStorage.setItem("cv_lang", nextLang);',
        '        const target = new URL(nextLang === "en" ? "cv-experimental-en.html" : "cv-experimental.html", location.href);',
        '        const query = new URLSearchParams({lang: nextLang, version: document.body.dataset.cvVersion || "full", print: document.body.dataset.printMode || "cv"});',
        '        const cover = new URLSearchParams(location.search).get("cover");',
        '        if(cover) query.set("cover", cover);',
        '        target.search = query.toString(); location.assign(target);',
        '      });',
    ])
    page, handler_count = re.subn(r'\$\("langBtn"\)\.addEventListener\("click", \(\) => \{.*?\n      \}\);', lambda match: handler, page, count=1, flags=re.S)
    if handler_count != 1: raise ValueError('Language control changed in the original engine.')

    page = page.replace('requestedVersion || localStorage.getItem("cv_version") || "compact"', 'requestedVersion || "full"')
    page = page.replace('requestedPrintMode || localStorage.getItem("cv_print_mode") || "cv"', 'requestedPrintMode || "cv"')
    page = page.replace('const L = data.languages[lang];\n      const F = L.fullCv || {};', 'const L = data.languages[lang];\n      document.body.dataset.extensionLanguage = lang;\n      const F = L.fullCv || {};')
    page = page.replace('contactRow.appendChild(createChip(`LinkedIn ${item.label}`, "full-contact-pill"));', 'const link = el("a", "full-contact-pill", item.label); link.href = item.url; contactRow.appendChild(link);')
    page = page.replace('(F.primaryExperience || []).forEach((job) => primary.appendChild(renderFullJob(job)));', '(F.primaryExperience || []).forEach((job, i) => { const item = renderFullJob(job); item.id = "experiencia-" + (i + 1); primary.appendChild(item); });')
    page = page.replace('(F.additionalExperience || []).forEach((job) => secondary.appendChild(renderFullJob(job, true)));', '(F.additionalExperience || []).forEach((job, i) => { const item = renderFullJob(job, true); item.id = "experiencia-" + ((F.primaryExperience || []).length + i + 1); secondary.appendChild(item); });')
    page = page.replace('(L.education || []).forEach((item) => education.appendChild(renderFullEducationItem(item)));', '(L.education || []).forEach((item, i) => { const entry = renderFullEducationItem(item); entry.id = "formacao-" + (i + 1); education.appendChild(entry); });')
    relation = '''
      if(/AGRODAN/i.test(job.company)){
        const related = el("p", "career-reference");
        const link = el("a", null, currentLang === "en" ? "Agrodan projects: SIA, data, mobile collection and business workflows" : "Projetos da trajetória na Agrodan: SIA, dados, coleta mobile e processos de negócio");
        link.href = "#cv-agrodan"; related.appendChild(link); wrap.appendChild(related);
      }
      if(/HOSPITAL|HOSPITALAR/i.test(job.company)){
        const related = el("p", "career-reference");
        const link = el("a", null, currentLang === "en" ? "Internship project: hospital indicators and assessments in Java EE" : "Projeto associado ao estágio: indicadores e avaliações hospitalares em Java EE");
        link.href = "#academico"; related.appendChild(link); wrap.appendChild(related);
      }
'''
    page = page.replace('      return wrap;\n    }\n\n    function renderFullEducationItem', relation + '      return wrap;\n    }\n\n    function renderFullEducationItem', 1)
    grouped_renderer = '''
      if(lang === "pt" || lang === "en"){
        const editorial = lang === "en" ? data.extensions.locales.en.editorial : data.extensions.editorial;
        fullSkills.innerHTML = "";
        editorial.skillGroups.forEach(group => {
          const item = el("article", "career-skill");
          item.appendChild(el("h3", null, group.title));
          item.appendChild(el("p", null, group.description));
          item.appendChild(el("p", "career-skill-origin", group.origin));
          fullSkills.appendChild(item);
        });
        fullTools.innerHTML = "";
        editorial.technologyGroups.forEach(group => {
          const row = el("p", "career-tech");
          row.appendChild(el("strong", null, group.title + ": "));
          row.appendChild(document.createTextNode(group.description));
          fullTools.appendChild(row);
        });
      }
'''
    marker = '(L.tools || []).forEach((item) => fullTools.appendChild(createChip(item.name)));'
    page = page.replace(marker, marker + grouped_renderer, 1)
    # Prefill the full CV for static readers. JavaScript subsequently renders the
    # same source data through the original functions when the page is opened.
    pt = data['languages'][language]
    group_data = data['extensions']['locales']['en']['editorial'] if language == 'en' else data['extensions']['editorial']
    def fill(id, content):
        nonlocal page
        pattern = r'(<([a-z0-9]+)\b[^>]*\bid="' + id + r'"[^>]*>).*?(</\2>)'
        page, count = re.subn(pattern, lambda m: m[1] + content + m[3], page, count=1, flags=re.S)
        if count != 1:
            raise ValueError('Campo original não encontrado: ' + id)
    fill('fullName', html.escape(pt['profile']['name']))
    fill('fullHeadline', html.escape(pt['profile']['headline']).replace('\n', '<br>'))
    fill('fullContactRow', ''.join('<span class="full-contact-pill">' + html.escape(v['label'] + ': ' + v['value']).replace('\n', ' · ') + '</span>' for v in pt['contact']['items'] if v['label'] not in ['Nascimento', 'Birth', 'CREA-PE']) + ''.join('<a class="full-contact-pill" href="' + html.escape(v['url'], quote=True) + '">' + html.escape(v['label']) + '</a>' for v in pt['contact']['social']))
    fill('fullBadgeRow', ''.join('<span class="full-badge">' + html.escape(v) + '</span>' for v in pt['fullCv']['headerBadges']))
    fill('fullExperiencePrimary', ''.join(jobs[:primary_count]).replace('class="job"', 'class="full-job"'))
    fill('fullExperienceSecondary', ''.join(jobs[primary_count:]).replace('class="job"', 'class="full-mini-job"'))
    fill('fullEducation', ''.join(education).replace('class="job"', 'class="full-education-entry"'))
    fill('fullSummary', ''.join('<p>' + html.escape(v) + '</p>' for v in pt['profile']['summary']))
    fill('fullResults', ''.join('<li>' + html.escape(v) + '</li>' for v in pt['fullCv']['keyImpacts']))
    for id, values in [('fullStack', pt['fullCv']['coreStack']), ('fullSkills', [v['name'] for v in pt['skills']]), ('fullTools', [v['name'] for v in pt['tools']])]:
        if id == 'fullSkills':
            fill(id, ''.join('<article class="career-skill"><h3>' + html.escape(g['title']) + '</h3><p>' + html.escape(g['description']) + '</p><p class="career-skill-origin">' + html.escape(g['origin']) + '</p></article>' for g in group_data['skillGroups']))
        elif id == 'fullTools':
            fill(id, ''.join('<p class="career-tech"><strong>' + html.escape(g['title']) + ': </strong>' + html.escape(g['description']) + '</p>' for g in group_data['technologyGroups']))
        else:
            fill(id, ''.join('<span class="full-chip">' + html.escape(v) + '</span>' for v in values))
    for id, label in [('tFullExperience', 'Experiência profissional'), ('tFullSummary', 'Perfil'), ('tFullResults', 'Resultados de impacto'), ('tFullEducation', 'Formação'), ('tFullAdditional', 'Trajetória adicional'), ('tFullStack', 'Stack principal'), ('tFullSkills', 'Habilidades'), ('tFullTools', 'Ferramentas')]:
        if language == 'en': label = {'tFullExperience':'Professional experience','tFullSummary':'Profile','tFullResults':'Impact highlights','tFullEducation':'Education','tFullAdditional':'Additional experience','tFullStack':'Core stack','tFullSkills':'Skills','tFullTools':'Tools'}[id]
        fill(id, label)
    if language == 'en':
        page = page.replace('<html lang="pt-BR">','<html lang="en">',1)
        page = page.replace('<title>CV completo experimental — Danillo Xavier</title>','<title>Full CV — Danillo Xavier</title>',1)
    page = page.replace('id="fullAvatar"', 'id="fullAvatar" src="avatar.png"', 1)
    page = page.replace('</body>', '''<script>
    const appendices = document.getElementById("careerAppendices");
    const includeAppendices = document.getElementById("includeAppendices");
    includeAppendices.addEventListener("change", () => {
      document.body.dataset.printAppendices = String(includeAppendices.checked);
    });
    function revealReference(){
      const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      if(target && appendices.contains(target)){
        appendices.open = true;
        requestAnimationFrame(() => target.scrollIntoView({block:"start"}));
      }
    }
    window.addEventListener("hashchange", revealReference);
    revealReference();
    let previousAppendixState = false;
    window.addEventListener("beforeprint", () => {
      previousAppendixState = appendices.open;
      appendices.open = includeAppendices.checked;
    });
    window.addEventListener("afterprint", () => { appendices.open = previousAppendixState; });
    </script></body>''', 1)
    return page
