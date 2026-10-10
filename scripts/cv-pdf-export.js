/* Native text PDF export, using the current CV DOM and local pdfmake assets. */
(() => {
  const button = document.getElementById('downloadPdfBtn');
  const status = document.getElementById('pdfExportStatus');
  let loading;
  let busy = false;
  const labels = lang => lang === 'en' ? {
    button: 'Download compact PDF', busy: 'Generating PDF…',
    ready: 'PDF downloaded', error: 'Could not generate the PDF. Please try again.',
    large: 'All selected content was retained; the file exceeds 2 MB.'
  } : {
    button: 'Baixar PDF leve', busy: 'Gerando PDF…',
    ready: 'PDF baixado', error: 'Não foi possível gerar o PDF. Tente novamente.',
    large: 'Todo o conteúdo selecionado foi mantido; o arquivo ultrapassou 2 MB.'
  };
  const activeLanguage = () => document.body.dataset.extensionLanguage === 'en' ? 'en' : 'pt';
  function updateLabels(lang = activeLanguage()) {
    button.textContent = labels(lang)[busy ? 'busy' : 'button'];
    if (!busy) status.textContent = '';
  }
  function script(src) {
    return new Promise((resolve, reject) => {
      const element = document.createElement('script');
      element.src = new URL(src, document.baseURI).href;
      element.onload = resolve;
      element.onerror = () => { element.remove(); reject(new Error('PDF asset could not be loaded: ' + src)); };
      document.head.appendChild(element);
    });
  }
  async function library() {
    if (!loading) loading = (async () => {
      await script('vendor/pdfmake/pdfmake.min.js');
      await script('vendor/pdfmake/vfs_fonts.js');
      if (!window.pdfMake) throw new Error('PDF engine unavailable');
      return window.pdfMake;
    })().catch(error => { loading = null; throw error; });
    return loading;
  }
  function configuration() {
    const language = activeLanguage();
    return {
      language,
      version: document.body.dataset.cvVersion === 'full' ? 'full' : 'compact',
      mode: document.body.dataset.printMode || 'cv',
      appendices: Boolean(document.getElementById('includeAppendices' + (language === 'en' ? '-en' : '')).checked)
    };
  }
  function documentDefinition(config) {
    const references = [];
    const destinations = new Set();
    const en = config.language === 'en';
    const normalize = text => text.replace(/\s+/g, ' ');
    const selected = element => {
      if (!element || element.nodeType !== Node.ELEMENT_NODE) return true;
      const language = element.closest('[data-content-language]');
      if (language && language.dataset.contentLanguage !== config.language) return false;
      if (element.closest('.career-appendices') && !config.appendices) return false;
      return !element.matches('script,style,input,button,label,img,.career-navigation,.tool-context-anchor + input');
    };
    function destination(element, block) {
      if (element.id && !destinations.has(element.id)) {
        block.id = element.id;
        destinations.add(element.id);
      }
      return block;
    }
    function inline(node, inherited = {}) {
      if (node.nodeType === Node.TEXT_NODE) return [{text: normalize(node.textContent), ...inherited}];
      if (node.nodeType !== Node.ELEMENT_NODE || !selected(node)) return [];
      if (node.tagName === 'BR') return [{text: '\n', ...inherited}];
      const format = {...inherited};
      if (node.matches('b,strong')) format.bold = true;
      if (node.matches('em,i')) format.italics = true;
      if (node.tagName === 'A') {
        const href = node.getAttribute('href') || '';
        if (/^https?:\/\//i.test(href) || /^(mailto|tel):/i.test(href)) {
          format.link = href; format.color = '#205575'; format.decoration = 'underline';
        }
        if (href.startsWith('#')) format._destination = decodeURIComponent(href.slice(1));
      }
      const items = [...node.childNodes].flatMap(child => inline(child, format));
      items.forEach(item => {
        if (item._destination) { references.push([item, item._destination]); delete item._destination; }
      });
      return items;
    }
    function paragraph(element, style) {
      const runs = inline(element);
      if (!runs.some(item => item.text.trim())) return [];
      const job = element.closest('.full-job');
      const column = element.closest('.full-column');
      const dense = job || column;
      return [destination(element, {text: runs, style: style || (dense ? 'jobParagraph' : 'paragraph'), fontSize: column ? (style === 'company' ? 7.8 : 7) : undefined, margin: [0, 0, 0, dense ? 2 : 4]})];
    }
    function table(element) {
      const rows = [...element.querySelectorAll(':scope > thead > tr,:scope > tbody > tr,:scope > tr')];
      if (!rows.length) return [];
      const width = Math.max(...rows.map(row => row.children.length));
      const body = rows.map(row => {
        const cells = [...row.children].map(cell => ({stack: blocks(cell), bold: cell.tagName === 'TH', fillColor: cell.tagName === 'TH' ? '#edf3f6' : undefined, margin: [3, 3, 3, 3]}));
        while (cells.length < width) cells.push({text: ''});
        if (row.id) destination(row, cells[0]);
        return cells;
      });
      return [destination(element, {table: {headerRows: element.querySelector('thead') ? 1 : 0, widths: Array(width).fill('*'), body}, layout: 'lightHorizontalLines', fontSize: 7.5, margin: [0, 3, 0, 8]})];
    }
    function svg(element) {
      const clone = element.cloneNode(true);
      clone.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
      clone.querySelectorAll('title').forEach(item => item.remove());
      clone.querySelectorAll('.radar-grid').forEach(item => { item.setAttribute('fill', 'none'); item.setAttribute('stroke', '#ccd6df'); });
      clone.querySelectorAll('.radar-area').forEach(item => { item.setAttribute('fill', '#d9edf2'); item.setAttribute('stroke', '#2b768c'); item.setAttribute('stroke-width', '2'); });
      clone.querySelectorAll('.radar-dot').forEach(item => item.setAttribute('fill', '#2b768c'));
      clone.querySelectorAll('text,tspan').forEach(item => { item.setAttribute('fill', '#172636'); item.setAttribute('font-family', 'Roboto'); item.setAttribute('font-size', '10'); });
      return [{svg: new XMLSerializer().serializeToString(clone), width: 250, margin: [0, 2, 0, 5]}];
    }
    function columns(element) {
      const children = [...element.children].filter(selected);
      if (!children.length) return [];
      const result = [];
      for (let i = 0; i < children.length; i += 2) {
        result.push({columns: children.slice(i, i + 2).map(child => ({width: '*', stack: blocks(child)})), columnGap: 14, margin: [0, 0, 0, 6]});
      }
      return result;
    }
    function blocks(element) {
      if (!selected(element)) return [];
      const tag = element.tagName.toUpperCase();
      if (tag === 'SVG') return svg(element);
      if (tag === 'TABLE') return table(element);
      if (/^H[1-6]$/.test(tag)) {
        const level = Number(tag[1]);
        const column = element.closest('.full-column');
        return [destination(element, {text: inline(element), style: 'heading' + Math.min(level, 4), fontSize: column ? 10 : undefined, headlineLevel: level, margin: [0, level > 1 ? (column ? 5 : 7) : 0, 0, column ? 3 : 5], keepWithNext: true})];
      }
      if (tag === 'P' || tag === 'SUMMARY') return paragraph(element, element.classList.contains('career-reference') ? 'reference' : undefined);
      if (tag === 'UL' || tag === 'OL') {
        const job = element.closest('.full-job,.full-column');
        const items = [...element.children].filter(item => item.tagName === 'LI').map(item => ({stack: blocks(item), margin: [0, 0, 0, job ? 1 : 3]}));
        if (!items.length) return [];
        return [destination(element, {[tag === 'UL' ? 'ul' : 'ol']: items, fontSize: job ? 7.1 : 8, margin: [0, 1, 0, job ? 3 : 6]})];
      }
      if (element.classList.contains('full-header')) {
        const title = element.querySelector('.full-title');
        return title ? blocks(title) : [];
      }
      if (element.matches('.full-page-grid,.full-split,.full-experience-grid,.map-chart-grid,.map-lower-grid,.map-evidence-grid')) return [destination(element, {stack: columns(element)})];
      if (element.classList.contains('map-metrics')) {
        return [{columns: [...element.children].map(child => ({text: [...child.children].map(item => normalize(item.textContent).trim()).join(' '), bold: true, fontSize: 10})), columnGap: 12, margin: [0, 5, 0, 8]}];
      }
      if (element.classList.contains('map-bar')) {
        const fraction = Math.max(0,Math.min(1,parseFloat(element.querySelector('i').style.width)/100));
        return [{columns: [{text: element.querySelector('span').textContent, width: 90}, {width:110,canvas:[{type:'rect',x:0,y:3,w:110,h:5,color:'#e4edf2'},{type:'rect',x:0,y:3,w:110*fraction,h:5,color:'#397e99'}]}, {text: element.querySelector('b').textContent, width: 18, bold: true, alignment:'right'}],columnGap:4, margin: [0, 0, 0, 5], fontSize: 7.5}];
      }
      if (element.matches('.full-chip-list,.full-contact-row,.full-badge-row,.skill-cluster-nav')) {
        const children = [...element.children].filter(selected);
        if (children.every(child => !child.querySelector('p,h3,div'))) {
          const runs = children.flatMap((child, i) => [...(i ? [{text: ' · '}] : []), ...inline(child)]);
          return [destination(element, {text: runs, fontSize: 7.5, margin: [0, 0, 0, 6]})];
        }
      }
      if (element.matches('.name,.headline,.full-job-company,.full-job-role,.company,.role,.date,.full-job-meta,.full-tech-line,.full-title>div,.skill-case-context')) {
        const style = element.matches('.full-job-company,.company') ? 'company' : element.matches('.full-job-role,.role') ? 'role' : element.matches('.name') ? 'heading1' : element.matches('.headline') ? 'heading3' : 'reference';
        return paragraph(element, style);
      }
      if (element.matches('.tool-context-anchor')) return [destination(element, {text: '\u200b', fontSize: 0.1, lineHeight: 0.1})];
      const childElements = [...element.children].filter(selected);
      if (!childElements.length) return paragraph(element);
      const result = [];
      let pending = [];
      const flush = () => {
        if (pending.some(item => item.text.trim())) result.push({text: pending, margin: [0, 0, 0, 4]});
        pending = [];
      };
      for (const child of element.childNodes) {
        if (child.nodeType === Node.TEXT_NODE) pending.push(...inline(child));
        else if (child.nodeType === Node.ELEMENT_NODE && selected(child)) {
          if (child.matches('a,b,strong,em,i,br') || (child.tagName === 'SPAN' && !child.classList.contains('impact-project-links') && !child.classList.contains('skill-case-context') && !child.id)) pending.push(...inline(child));
          else { flush(); result.push(...blocks(child)); }
        }
      }
      flush();
      if (element.id && result.length) return [destination(element, {stack: result, margin: element.matches('article,.full-card') ? [0, 0, 0, 5] : undefined})];
      return result;
    }
    const content = [];
    if (config.mode !== 'cover') {
      if (config.version === 'full') {
        const root = document.getElementById('fullCvView').cloneNode(true);
        for (const child of root.children) {
          if (!selected(child)) continue;
          if (child.matches('.full-page')) {
            const entry = {stack: blocks(child)};
            if (content.length) entry.pageBreak = 'before';
            content.push(entry);
          } else if (child.matches('[data-content-language]')) {
            for (const section of child.children) {
              if (!selected(section)) continue;
              const entry = {stack: blocks(section)};
              if (section.classList.contains('capability-overview')) entry.pageBreak = content.length ? 'before' : undefined;
              content.push(entry);
            }
          }
        }
      } else {
        const cv = document.getElementById('cvPage').cloneNode(true);
        for (const selector of ['#name','#headline','#summary','#contact','#social','#secExp','#secEdu','#secSkills','#secTools']) {
          const section = cv.querySelector(selector);
          if(section) content.push(...blocks(section));
        }
      }
    }
    if (config.mode !== 'cv') {
      const letter = document.querySelector('.cover-letter-page').cloneNode(true);
      content.push({stack: blocks(letter), pageBreak: content.length ? 'before' : undefined});
    }
    for (const [item, id] of references) {
      if (destinations.has(id)) { item.linkToDestination = id; item.color = '#205575'; item.decoration = 'underline'; }
      else if (/^https?:$/.test(location.protocol)) { item.link = location.href.split('#')[0] + '#' + encodeURIComponent(id); item.color = '#205575'; }
    }
    return {
      pageSize: 'A4', pageMargins: [30, 28, 30, 30], compress: true,
      info: {title: 'Danillo Xavier — ' + (en ? 'CV' : 'Currículo'), author: 'Danillo Xavier', subject: config.mode + ' / ' + config.version + ' / ' + config.language},
      defaultStyle: {font: 'Roboto', fontSize: 8, color: '#172636', lineHeight: 1.12},
      styles: {
        paragraph: {fontSize: 8}, jobParagraph: {fontSize: 7.1, lineHeight: 1.04}, reference: {fontSize: 7, color: '#4c5b68'},
        company: {fontSize: 9, bold: true, color: '#205575'}, role: {fontSize: 8.3, bold: true},
        heading1: {fontSize: 19, bold: true}, heading2: {fontSize: 12, bold: true, color: '#205575'},
        heading3: {fontSize: 9.5, bold: true}, heading4: {fontSize: 8.5, bold: true}
      },
      footer: (page, count) => ({text: 'Danillo Xavier  ·  ' + page + ' / ' + count, alignment: 'right', fontSize: 7, color: '#647380', margin: [30, 0, 30, 0]}),
      content
    };
  }
  button.addEventListener('click', async () => {
    if (busy) return;
    const config = configuration();
    busy = true; button.disabled = true; updateLabels(config.language);
    status.textContent = labels(config.language).busy;
    try {
      // Snapshot the selected content before loading assets or yielding to the UI.
      const definition = documentDefinition(config);
      const pdf = await library();
      const blob = await new Promise(resolve => pdf.createPdf(definition).getBlob(resolve));
      const link = document.createElement('a');
      const url = URL.createObjectURL(blob);
      link.href = url;
      link.download = 'CV_Danillo_Xavier_' + config.language.toUpperCase() + '_' + config.version + '_' + config.mode + (config.version === 'full' && config.mode !== 'cover' && config.appendices ? '_integral' : '') + '.pdf';
      document.body.appendChild(link); link.click(); link.remove();
      setTimeout(() => URL.revokeObjectURL(url), 60000);
      status.textContent = labels(config.language).ready + ' — ' + (blob.size / 1000000).toFixed(2) + ' MB' + (blob.size >= 2000000 ? '. ' + labels(config.language).large : '');
    } catch (error) {
      console.error('CV PDF export:', error);
      status.textContent = labels(config.language).error;
    } finally {
      busy = false; button.disabled = false; button.textContent = labels(activeLanguage()).button;
    }
  });
  window.CvPdfExport = {updateLabels};
  updateLabels();
})();
