"""Compress the PDF structure and portrait while retaining all pages and text."""
import argparse
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--photo-quality',type=int,default=85,help='JPEG quality for the portrait (1–100; default 85).')
    args=parser.parse_args()
    source=args.input.resolve()
    destination=(args.output or source.with_name(source.stem+'-compact.pdf')).resolve()
    if not source.is_file():parser.error('PDF de entrada não encontrado.')
    if destination==source:parser.error('Use outro nome para preservar o PDF original.')
    if destination.exists():parser.error('O arquivo de saída já existe. Escolha outro nome.')
    if not 1<=args.photo_quality<=100:parser.error('A qualidade da foto deve estar entre 1 e 100.')
    try:
        import pymupdf
    except ImportError:
        parser.error('Instale a dependência: python -m pip install PyMuPDF')
    with pymupdf.open(source) as document:
        seen=set()
        for image in document[0].get_images():
            xref=image[0]
            if xref in seen:continue
            seen.add(xref)
            mask=document.xref_get_key(xref,'SMask')
            pixels=pymupdf.Pixmap(document,xref)
            if pixels.colorspace and pixels.colorspace.n==3 and not pixels.alpha:
                jpeg=pixels.tobytes('jpeg',jpg_quality=args.photo_quality)
                if len(jpeg)<len(document.xref_stream_raw(xref) or b''):
                    document[0].replace_image(xref,stream=jpeg)
                    if mask[0]=='xref':document.xref_set_key(xref,'SMask',mask[1])
        pages=len(document)
        document.save(destination,garbage=4,clean=True,deflate=True,deflate_images=True,deflate_fonts=True,use_objstms=1,compression_effort=100)
    before=source.stat().st_size/1_000_000
    after=destination.stat().st_size/1_000_000
    print(f'{before:.2f} MB -> {after:.2f} MB: {destination}')
    print(f'{pages} paginas preservadas. Texto e graficos vetoriais nao foram convertidos em imagens.')
    if after>=2:
        print('Ainda acima de 2 MB. Nenhuma pagina foi removida.')

if __name__=='__main__':main()
