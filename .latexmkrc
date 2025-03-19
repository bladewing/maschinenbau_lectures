$out_dir = '.';
$aux_dir = 'aux/latexmk';
$pdflatex=q/lualatex -synctex=1 -shell-escape %O %S/