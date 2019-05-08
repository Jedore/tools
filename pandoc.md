
start using pandoc

- Install [pandoc](https://www.pandoc.org/installing.html)
- install laTex
  - Install [MikTeX](https://miktex.org/download) on Win
  - Install [MacTeX](http://tug.org/mactex/) on Mac

- If markdown file has code block, when convert to pdf
    [Reference1](https://tex.stackexchange.com/questions/323329/pandoc-code-blocks-in-markdown-with-very-long-lines-get-cut-off-when-outputting)  
  write following text into *listings-setup.tex*
  ```tex
  % Contents of listings-setup.tex
  \usepackage{xcolor}
  
  \lstset{
      basicstyle=\ttfamily,
      numberstyle=\footnotesize,
      stepnumber=2,
      numbersep=5pt,
      backgroundcolor=\color{black!10},
      showspaces=false,
      showstringspaces=false,
      showtabs=false,
      tabsize=2,
      captionpos=b,
      breaklines=true,
      breakatwhitespace=true,
      breakautoindent=true,
      linewidth=\textwidth
  }
  ```

  execute command
  ```bash
  pandoc --listings -H listings-setup.tex --toc -V geometry:"left=1cm, top=1cm, right=1cm, bottom=2cm" -V fontsize=12pt test.md -o test.pdf
  ```

- When chinese in markdown, add following text at the top of md file  
    [Reference1](https://pandoc.org/faqs.html)  
    [Reference2](https://github.com/jgm/pandoc/wiki/Pandoc-with-Chinese)
  ```md
  ---
  documentclass: extarticle
  fontsize: 8pt
  CJKmainfont: STSong
  CJKoptions:
    - BoldFont=STHeiti
    - ItalicFont=STKaiti
  ---
  ```
  execute command
  ```bash
  pandoc  test.md -o test.pdf --pdf-engine=xelatex -V mainfont='Microsoft YaHei UI' --listings -H listings-setup.tex --toc
  ```
  
