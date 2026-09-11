from pathlib import Path

REPO_URL = "https://github.com/shaikhamalkawi-ux/When-AI-Exposure-Rankings-Disagree-Robust-Top-k-Occupational-Selection-under-Uncertainty"

p = Path("source/main.tex")
s = p.read_text(encoding="utf-8")

if "\\usepackage[hidelinks]{hyperref}" not in s:
    marker = "\\usepackage{microtype}\n"
    if marker not in s:
        raise SystemExit("microtype package marker not found")
    s = s.replace(marker, marker + "\\usepackage[hidelinks]{hyperref}\n", 1)

availability = (
    "\\medskip\n"
    "\\noindent\\textbf{Data and Code Availability---} "
    "The data, code, scenario matrices, selected lists, and reproducibility materials supporting this study are publicly available in the project "
    f"\\href{{{REPO_URL}}}{{\\textbf{{GitHub}}~\\raisebox{{0.15ex}}{{\\scriptsize$\\nearrow$}}}}.\n\n"
)

if "Data and Code Availability---" not in s:
    marker = "\\begin{thebibliography}{30}\\footnotesize"
    if marker not in s:
        raise SystemExit("bibliography marker not found")
    s = s.replace(marker, availability + marker, 1)

p.write_text(s, encoding="utf-8")
