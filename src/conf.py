# -*- coding: utf-8 -*-
import spyce 

# -- Project information -----------------------------------------------------

name = spyce.PYPROJECT_TOML['tool']['poetry']['name']
project = spyce.PYPROJECT_TOML['tool']['poetry']['description']
author = spyce.PYPROJECT_TOML['tool']['poetry']['authors'][0]
release = spyce.PYPROJECT_TOML['tool']['spyce']['document_id']
copyright = spyce.PYPROJECT_TOML['tool']['spyce']['copyright_year'] \
    + ', ' \
    + spyce.PYPROJECT_TOML['tool']['spyce']['organization']

# -- General configuration ---------------------------------------------------

extensions = [
'sphinxcontrib.bibtex',
'sphinx.ext.autodoc',
'sphinx.ext.todo',
'sphinxcontrib.plantuml',
'sphinx.ext.intersphinx',
"sphinx_revealjs",
'sphinxcontrib.programoutput',
]

# templates_path = ['_static']
intersphinx_mapping = {'rgvflood': ('https://glossary.rgvflood.com/en/latest', None)}
source_suffix = ".rst"
master_doc = "index"
language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = 'sphinx'
numfig = True
numfig_format = {'figure': 'Figure: %s', 'table': 'Table: %s', 'code-block': 'Listing: %s', 'section': 'Section: %s'}

# -- Options for bibtex output ---------------------------------------------------

bibtex_bibfiles = ['_static/references.bib']

# -- Options for plantuml output ---------------------------------------------------

plantuml = "plantuml"

# -- Options for todo output ---------------------------------------------------

todo_include_todos = False

# -- Options for HTML output ---------------------------------------------------

on_rtd = True

if on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = 'alabaster'
html_title = project
html_short_title = name
html_logo = "_static/RGVFloodLogo.png"
html_baseurl = "https://docs.rgvflood.com"
html_static_path = ['_static']
htmlhelp_basename = project

# -- Options for Revealjs Slide output ---------------------------------------------------
revealjs_script_conf = """
    { 
        hash: true,
        width: 1600,
        height: 900,
    }
"""
revealjs_script_plugins = [
    {
        "src": "revealjs4/plugin/highlight/highlight.js",
        "name": "RevealHighlight",
    },
    {
        "src": "revealjs4/plugin/notes/notes.js",
        "name": "RevealNotes",
    },    
]
revealjs_static_path = ['_static']
revealjs_style_theme = 'bluetunnel.css'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
'pointsize': '12pt',
'preamble': '\\usepackage{svg}',
'releasename': html_title+'\par Project Deliverable ID',
'extraclassoptions': 'openany,oneside',
'babel': '\\usepackage[american]{babel}',
'maketitle': r''' 
\sphinxmaketitle

    %\renewcommand{\familydefault}{\sfdefault}
    \newcommand\signature[3]{% Role; Name; Department
    %\begin{center}
    {\sffamily
    \vspace{1cm}\par
    \textbf{#1}:\par
        \begin{minipage}{10cm}
        \centering
        \vspace{3cm}\par
        \rule{10cm}{1pt}\par
        \textbf{#2}\par
        #3%
        \end{minipage}
    }
    %\end{center}
    }
    \newcommand\insertdate[1][\today]{\vfill\begin{flushright}#1\end{flushright}}

    {\LARGE\sffamily \textbf{Approval Page}}
    
    \signature{Technical Review By}{William Kirkey, Ph.D.}{Chief of Research and Technology Development}
    
    \signature{Final Approval For Submission}{Andrew N.S. Ernest, Ph.D., P.E., BCEE, D.WRE}{Chief Executive Officer}
        
    \insertdate

''',
}
authors = author
latex_documents = [
  ('index', name+'.tex', 'Lower Rio Grande Valley Development Council Flood Infrastructure Fund',
   authors, 
   'manual'),
]
latex_logo = '_static/RATESLogo.png'
latex_appendices = ['glossary']
