"""Compress an exported PDF without rasterizing text or changing its layout."""
import argparse
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    source=args.input.resolve()
    destination=(args.output or source.with_name(source.stem+'-compact.pdf')).resolve()
    if not source.is_file():parser.error('PDF de entrada não encontrado.')
    if destination==source:parser.error('Use outro nome para preservar o PDF original.')
    if destination.exists():parser.error('O arquivo de saída já existe. Escolha outro nome.')
    try:
        import pymupdf
    except ImportError:
        parser.error('Instale a dependência: python -m pip install PyMuPDF')
    with pymupdf.open(source) as document:
        document.save(destination,garbage=4,deflate=True,deflate_images=True,deflate_fonts=True,use_objstms=1)
    before=source.stat().st_size/1_000_000
    after=destination.stat().st_size/1_000_000
    print(f'{before:.2f} MB -> {after:.2f} MB: {destination}')
    if after>=2:
        print('Ainda acima de 2 MB. Para o CV de envio, exporte sem incluir o acervo técnico.')

if __name__=='__main__':main()
