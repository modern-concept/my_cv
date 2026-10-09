"""Extend the existing complete CV renderer without changing its source file."""
import html
import json
import re


def build_page(base, data, sections, jobs, education, primary_count):
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
    toc = '<nav class="full-card extension-toc" aria-label="Índice das novas seções"><h2>Projetos, especialidades e evidências</h2><p>Extensão em português do CV completo. Os projetos estão relacionados aos seus contextos profissionais, acadêmicos e independentes.</p><ol>' + ''.join('<li><a href="#' + re.search(r'<section id="([^"]+)"', p)[1] + '">' + re.search(r'<h2>(.*?)</h2>', p)[1] + '</a></li>' for p in sections) + '</ol><p><a href="index.html?lang=pt&amp;version=full">CV original</a> · <a href="cv-experimental.md">Versão textual completa</a> · <a href="cv-experimental-data.json">Dados e fontes</a></p></nav>'
    supplemental.insert(0, '<section class="page full-page experimental-page"><div class="full-page-inner">' + toc + '</div></section>')
    marker = '  </div>\n\n  <script>\n    const DATA_URL'
    if marker not in page:
        raise ValueError('Estrutura do motor original mudou; revisar ponto de extensão.')
    page = page.replace(marker, ''.join(supplemental) + '\n' + marker, 1)
    page = page.replace('const DATA_URL = "cv-data.json";', 'const DATA_URL = "cv-experimental-data.json";')
    payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
    page = page.replace('  <script>\n    const DATA_URL', '<script id="experimentalData" type="application/json">' + payload + '</script>\n  <script>\n    const DATA_URL', 1)
    page = page.replace('const res = await fetch(DATA_URL, {cache:"no-store"});\n      const data = await res.json();', 'const data = JSON.parse(document.getElementById("experimentalData").textContent);')
    page = page.replace('requestedLang || localStorage.getItem("cv_lang") || (data.meta && data.meta.defaultLang) || "pt"', 'requestedLang || "pt"')
    page = page.replace('requestedVersion || localStorage.getItem("cv_version") || "compact"', 'requestedVersion || "full"')
    page = page.replace('requestedPrintMode || localStorage.getItem("cv_print_mode") || "cv"', 'requestedPrintMode || "cv"')
    page = page.replace('const L = data.languages[lang];\n      const F = L.fullCv || {};', 'const L = data.languages[lang];\n      document.body.dataset.extensionLanguage = lang;\n      const F = L.fullCv || {};')
    page = page.replace('(F.primaryExperience || []).forEach((job) => primary.appendChild(renderFullJob(job)));', '(F.primaryExperience || []).forEach((job, i) => { const item = renderFullJob(job); item.id = "experiencia-" + (i + 1); primary.appendChild(item); });')
    page = page.replace('(F.additionalExperience || []).forEach((job) => secondary.appendChild(renderFullJob(job, true)));', '(F.additionalExperience || []).forEach((job, i) => { const item = renderFullJob(job, true); item.id = "experiencia-" + ((F.primaryExperience || []).length + i + 1); secondary.appendChild(item); });')
    page = page.replace('(L.education || []).forEach((item) => education.appendChild(renderFullEducationItem(item)));', '(L.education || []).forEach((item, i) => { const entry = renderFullEducationItem(item); entry.id = "formacao-" + (i + 1); education.appendChild(entry); });')
    # Prefill the full CV for static readers. JavaScript subsequently renders the
    # same source data through the original functions when the page is opened.
    pt = data['languages']['pt']
    def fill(id, content):
        nonlocal page
        pattern = r'(<([a-z0-9]+)\b[^>]*\bid="' + id + r'"[^>]*>)(</\2>)'
        page, count = re.subn(pattern, lambda m: m[1] + content + m[3], page, count=1)
        if count != 1:
            raise ValueError('Campo original não encontrado: ' + id)
    fill('fullName', html.escape(pt['profile']['name']))
    fill('fullHeadline', html.escape(pt['profile']['headline']).replace('\n', '<br>'))
    fill('fullContactRow', ''.join('<span class="full-contact-pill">' + html.escape(v['label'] + ': ' + v['value']).replace('\n', ' · ') + '</span>' for v in pt['contact']['items'] if v['label'] not in ['Nascimento', 'Birth', 'CREA-PE']))
    fill('fullBadgeRow', ''.join('<span class="full-badge">' + html.escape(v) + '</span>' for v in pt['fullCv']['headerBadges']))
    fill('fullExperiencePrimary', ''.join(jobs[:primary_count]).replace('class="job"', 'class="full-job"'))
    fill('fullExperienceSecondary', ''.join(jobs[primary_count:]).replace('class="job"', 'class="full-mini-job"'))
    fill('fullEducation', ''.join(education).replace('class="job"', 'class="full-education-entry"'))
    fill('fullSummary', ''.join('<p>' + html.escape(v) + '</p>' for v in pt['profile']['summary']))
    fill('fullResults', ''.join('<li>' + html.escape(v) + '</li>' for v in pt['fullCv']['keyImpacts']))
    for id, values in [('fullStack', pt['fullCv']['coreStack']), ('fullSkills', [v['name'] for v in pt['skills']]), ('fullTools', [v['name'] for v in pt['tools']])]:
        fill(id, ''.join('<span class="full-chip">' + html.escape(v) + '</span>' for v in values))
    for id, label in [('tFullExperience', 'Experiência profissional'), ('tFullSummary', 'Perfil'), ('tFullResults', 'Resultados de impacto'), ('tFullEducation', 'Formação'), ('tFullAdditional', 'Trajetória adicional'), ('tFullStack', 'Stack principal'), ('tFullSkills', 'Habilidades'), ('tFullTools', 'Ferramentas')]:
        fill(id, label)
    page = page.replace('id="fullAvatar"', 'id="fullAvatar" src="avatar.png"', 1)
    return page
