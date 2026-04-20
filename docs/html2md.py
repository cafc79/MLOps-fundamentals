#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML → GitHub Flavored Markdown (GFM)
Optimizado para repositorios GitHub, READMEs y GitHub Pages.
"""

import os
import re
import sys
import logging
from markdownify import markdownify as md

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def _strip_html_attributes(html: str) -> str:
    """Elimina class, id, style y otros atributos que GitHub ignora."""
    return re.sub(r'\s+(?:class|id|style|data-\w+|role|aria-\w+)="[^"]*"', '', html)

def _fix_gfm_tables(md_text: str) -> str:
    """Asegura que las tablas tengan alineación GFM válida."""
    # Si hay tablas mal formateadas, normaliza saltos de línea
    md_text = re.sub(r'\n{2,}(\|)', '\n\n\1', md_text)
    return md_text

def html_to_gfm(html_path: str, output_path: str = None) -> str:
    if not os.path.exists(html_path):
        raise FileNotFoundError(f"No se encontró: {html_path}")

    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # 1️⃣ Limpieza previa de atributos no soportados por GitHub
    clean_html = _strip_html_attributes(html_content)

    # 2️⃣ Conversión a Markdown
    markdown_text = md(
        clean_html,
        heading_style="ATX",
        bullets="-",
        strip=["script", "style", "meta", "link", "noscript", "img", "figure", "figcaption"],
        code_language="",
        strip_document_ending_newline=False
    )

    # 3️⃣ Post-procesamiento GFM
    # Eliminar líneas vacías consecutivas
    markdown_text = re.sub(r'\n{3,}', '\n\n', markdown_text)
    # Quitar espacios trailing
    markdown_text = re.sub(r'[ \t]+\n', '\n', markdown_text)
    # Normalizar listas
    markdown_text = re.sub(r'^\s*[\*\+]\s', '- ', markdown_text, flags=re.MULTILINE)
    # Asegurar tablas GFM
    markdown_text = _fix_gfm_tables(markdown_text)
    # Convertir bloques HTML residuales a blockquotes si son notas/admoniciones
    markdown_text = re.sub(r'<div[^>]*>\s*(.*?)\s*</div>', r'> \1', markdown_text, flags=re.DOTALL)

    # 4️⃣ Guardar
    out_path = output_path or os.path.splitext(html_path)[0] + ".md"
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(markdown_text)

    logging.info(f"✅ GFM generado → {out_path}")
    return markdown_text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python html_to_gfm.py <archivo.html> [salida.md]")
        sys.exit(1)

    try:
        html_to_gfm(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    except Exception as e:
        logging.error(f"❌ Error: {e}")
        sys.exit(1)