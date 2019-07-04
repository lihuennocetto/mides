import os, shutil, sys

### Load data
try:
    os.chdir('C:/Alejandro/Research/MIDES/Empirical_analysis/Analysis/Temp') # Set current directory
    print('Script corrido en computadora de Alejandro')
    directory = 'C:/Alejandro/Research/MIDES/Empirical_analysis/Analysis/Temp'
except: pass
try:
    os.chdir('/Users/lihuennocetto/Dropbox/mides_local_processing/mides/Empirical_analysis/Analysis/Temp') # Set current directory
    print('Script corrido en computadora de Lihuen')
    directory = '/Users/lihuennocetto/Dropbox/mides_local_processing/mides/Empirical_analysis/Analysis/Temp'
except: pass
try:
    os.chdir('/home/andres/gdrive/mides/Empirical_analysis/Analysis/Temp') # Set current directory
    print('Script corrido en computadora de Andres')
    directory = '/home/andres/gdrive/mides/Empirical_analysis/Analysis/Temp'
except: pass

### Variables over which to loop when showing binscatters
initialTUS = ['all', 0, 1, 2]
outcomes = ['zeroEstudiaCEIPCES', 'masEstudiaCEIPCES18','masEstudiaCEIPCES24', 'masEstudiaCEIPCES36', 'masEstudiaCEIPCES48', 'masEnAnosEducCorrectos18', 'masEnAnosEducCorrectos24', 'masEnAnosEducCorrectos36', 'masEnAnosEducCorrectos48']
vOtherConditions = ['menores','menores12','menores1215','menores12zeroEstudiaCEIPCES', 'menores15zeroEstudiaCEIPCES']


### Armo archivo de LaTex que quiero generar
educTex = open('../Output/12_educ_siias.tex', 'w')
educTex.write('\documentclass[12pt]{article} \n')
educTex.write('\\usepackage{float} \n')
educTex.write('\\usepackage{amstext} \n')
educTex.write('\\usepackage{footnote} \n')
educTex.write('\\usepackage[skip=0pt]{caption} \n')
educTex.write('\\usepackage{lscape} \n')
educTex.write('\\usepackage{longtable} \n')
educTex.write('\\usepackage{lscape} \n')
educTex.write('\\usepackage{subfig} \n')
educTex.write('\\usepackage{natbib} \n')
educTex.write('\\usepackage{amsmath} \n')
educTex.write('\\usepackage{amsthm} \n')
educTex.write('\\usepackage{amssymb} \n')
educTex.write('\\usepackage{amsfonts} \n')
educTex.write('\\usepackage[utf8]{inputenc} \n')
educTex.write('\\usepackage{booktabs} \n')
educTex.write('\\usepackage[left=3cm,top=2cm,right=3cm,bottom=2cm]{geometry} \n')
educTex.write('\\usepackage{graphicx} \n')
educTex.write('\\title{MIDES Education-SIIAS: tables and figures} \n')
educTex.write('\\author{Alejandro Lagomarsino \& Lihuen Nocetto} \n')
educTex.write('\linespread{1.3} \n')
educTex.write('\setlength{\parindent}{0pt} \n')
educTex.write('\setlength{\parskip}{1ex plus 0.5ex minus 0.2ex} \n')
educTex.write('\\addtolength{\\textwidth}{4cm} \n')
educTex.write('\\addtolength{\hoffset}{-2cm} \n')
educTex.write('\graphicspath{ {' + directory + '/} } \n')
educTex.write('\\begin{document} \n')
educTex.write('\maketitle \n')
educTex.write('\section{Binscatters} \n')
for initTUS in initialTUS:
    for out in outcomes:
        for region in ['all', 'mdeo', 'int']:
            for iccMenosThres in ['1', '2', 'All']:
                for otherConds in vOtherConditions:
                    educTex.write('\\begin{figure}[H] \n')
                    educTex.write('\caption{' + out + ', TUS inicial= ' + str(initTUS) + ', reg=' + region + ', threshold=' + iccMenosThres + ', ' + otherConds + '} \n')
                    educTex.write('\\includegraphics[scale=0.6]{' + str(initTUS) + out + region + iccMenosThres + otherConds + '.pdf} \n')
                    educTex.write('\centering \n')
                    educTex.write('\label{fig:' + str(initTUS) + out + region + iccMenosThres + otherConds + '} \n')
                    educTex.write('\end{figure} \n')                  
educTex.write('\section{DID} \n')
educTex.write('\end{document} \n')
educTex.close()