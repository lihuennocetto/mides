''' 
Script that explains flow of programs to perform empirical analysis over MIDES dataset

********************************** BUILD **************************************

1)  Objective: Limpiar bases de visitas y tener un archivo con todas las variables
               de visitas a nivel de hogar y otro de personas
    Code:      Code\1_cleaning_visitas.do
    Input:     Input\Visitas_Hogares_Muestra_enmascarado.csv
               Input\Visitas_Personas_Muestra_enmascarado.csv
    Output:    Output\visitas_hogares_vars.csv
               Output\visitas_hogares_vars.dta
               Output\visitas_personas_vars.csv
               Output\visitas_personas_vars.dta

2)  Objective: Generar dos archivos (hogares y personas) con datos mínimos de las
               visitas y datos completos de TUS
    Code:      Code\2_visitas_TUS.do
    Input:     Output\visitas_hogares_vars.csv
               Output\visitas_personas_vars.csv
               Input\TUS_Muestra_enmascarado.csv
    Output:    Output\visitas_hogares_TUS.csv
               Output\visitas_hogares_TUS.dta
               Output\visitas_personas_TUS.csv
               Output\visitas_personas_TUS.dta

3)  Objective: Generar dos archivos (hogares y personas) con datos mínimos de las
               visitas y datos completos de AFAM
    Code:      Code\3_visitas_AFAM
    Input:     Output\visitas_hogares_vars.csv
               Output\visitas_personas_vars.csv
               Input\AFAM_enmascarado (todas las 13 carpetas)
    Output:    Output\visitas_hogares_AFAM.csv
               Output\visitas_hogares_AFAM.dta
               Output\visitas_personas_AFAM.csv
               Output\visitas_personas_AFAM.dta

4)  Objective: Generar dos archivos (hogares y personas) con datos mínimos de las
               visitas y datos PP y suspendidos educativos
    Code:      Code\4_visitas_PPySusp.do
    Input:     Output\visitas_hogares_vars.csv
               Output\visitas_personas_vars.csv
               Input\PP_Muestra_enmascarado.csv
               Input\Suspendidos_Muestra_enmascarado.csv
    Output:    Output\visitas_hogares_PPySusp.csv
               Output\visitas_hogares_PPySusp.dta
               Output\visitas_personas_PPySusp.csv
               Output\visitas_personas_PPySusp.dta

5)  Objective: Generar variables de umbrales de AFAM y TUS según individuos 
               están en programas especiales (ej. Jóvenes en RED) y reemplazar 
               archivos con estas nuevas variables
    Code:      Code\5_umbrales_especiales
    Input:     Output\visitas_hogares_TUS.csv
               Output\visitas_personas_TUS.csv
               Input\AFAM_enmascarado (todas las 13 carpetas)
               Archivos que vengan de SIIAS
    Output:    Output\visitas_hogares_vars.csv
               Output\visitas_personas_vars.csv

6)  Objective: Mover bases generadas de Output del Build al Input de Analysis
    Code:      Code\6_move_build_analysis.py
    Input:     Output\visitas_hogares_vars.csv
               Output\visitas_hogares_vars.dta
               Output\visitas_personas_vars.csv
               Output\visitas_personas_vars.dta
               Output\visitas_hogares_PPySusp.csv
               Output\visitas_hogares_PPySusp.dta
               Output\visitas_personas_PPySusp.csv
               Output\visitas_personas_PPySusp.dta
               Output\visitas_hogares_TUS.csv
               Output\visitas_hogares_TUS.dta
               Output\visitas_personas_TUS.csv
               Output\visitas_personas_TUS.dta
               Output\visitas_hogares_AFAM.csv
               Output\visitas_hogares_AFAM.dta
               Output\visitas_personas_AFAM.csv
               Output\visitas_personas_AFAM.dta
    Output:    ..Analysis\Input\MIDES\visitas_hogares_vars.csv
               ..Analysis\Input\MIDES\visitas_hogares_vars.dta
               ..Analysis\Input\MIDES\visitas_personas_vars.csv
               ..Analysis\Input\MIDES\visitas_personas_vars.dta
               ..Analysis\Input\MIDES\visitas_hogares_PPySusp.csv
               ..Analysis\Input\MIDES\visitas_hogares_PPySusp.dta
               ..Analysis\Input\MIDES\visitas_personas_PPySusp.csv             
               ..Analysis\Input\MIDES\visitas_personas_PPySusp.dta
               ..Analysis\Input\MIDES\visitas_hogares_TUS.csv
               ..Analysis\Input\MIDES\visitas_hogares_TUS.dta
               ..Analysis\Input\MIDES\visitas_personas_TUS.csv               
               ..Analysis\Input\MIDES\visitas_personas_TUS.dta
               ..Analysis\Input\MIDES\visitas_hogares_AFAM.csv
               ..Analysis\Input\MIDES\visitas_hogares_AFAM.dta
               ..Analysis\Input\MIDES\visitas_personas_AFAM.csv              
               ..Analysis\Input\MIDES\visitas_personas_AFAM.dta


****************************** ANALYSIS ***************************************

1)  Objective: Mirar first stage en TUS tanto para perder, ganar y 
               duplicar beneficio.
    Code:      Code\1_tus_first_stage.py
    Input:     Input\MIDES\visitas_hogares_TUS.csv
               Input\MIDES\visitas_hogares_vars.csv
    Output:    
               
2)  Objective: Mirar second stage de impacto TUS en PP.
    Code:      Code\2_tus_PP.py
               Code\2_tus_PP.do
    Input:     Input\MIDES\visitas_personas_TUS.csv
               Input\MIDES\visitas_personas_PPySusp.csv
    Output:    

3)  Objective: Mirar second stage de impacto TUS en suspendidos educativos.
    Code:      Code\3_tus_suspendidos.py
    Input:     Input\MIDES\visitas_personas_TUS.csv
               Input\MIDES\visitas_personas_PPySusp.csv
    Output:              

4)  Objective: Mirar second stage de impacto TUS en variables de base visitas 
               y balance re-visitas y no re-visitados (para hogares revistados).
    Code:      Code\4_tus_vars_revistadas.do
               Code\4_tus_vars_revistadas.py
    Input:     Input\MIDES\visitas_hogares_TUS.csv
               Input\MIDES\visitas_personas_TUS.csv
               Input\MIDES\visitas_hogares_vars.csv
               Input\MIDES\visitas_personas_vars.csv
    Output:  
            
5)  Objective: Armar basic summary statstics.
    Code:      Code\5_summary_stats.py
    Input:     Input\MIDES\visitas_hogares_TUS.csv
               Input\MIDES\visitas_personas_TUS.csv
               Input\MIDES\visitas_hogares_vars.csv
               Input\MIDES\visitas_personas_vars.csv
               Input\MIDES\visitas_personas_PPySusp.csv
               Input\IPC_TC.xlsx
    Output: 

            
7)  Objective: Poner visitas en un mapa y poner colores con si luego de visita
               se perdió, ganó, duplicó, mantuvo 1 o mantuvo 2, etc transferencias
               y si son censales o recorrido tipo
    Code:      Code\6_mapa_visitas.py
    Input:     Input\MIDES\visitas_hogares_TUS.csv
               Input\MIDES\visitas_personas_TUS.csv
               Input\MIDES\visitas_hogares_vars.csv
               Input\MIDES\visitas_personas_vars.csv
               
    Output: 
        
8)  Objective: Generar variables de lo que "sucedió" en tu barrio.
    Code:      Code\7_gen_variables_nbd.do
    Input:     Input\MIDES\visitas_hogares_TUS.csv
               Input\MIDES\visitas_personas_TUS.csv
               Input\MIDES\visitas_hogares_vars.csv
               Input\MIDES\visitas_personas_vars.csv
               
    Output: 
        
9)  Objective: Mirar impactos por meses antes y después de visita con variables AFAM.
    Code:      Code\9_tus_envars_afam.py
    Input:     Input\MIDES\visitas_hogares_TUS.csv
               Input\MIDES\visitas_personas_TUS.csv
               Input\MIDES\visitas_hogares_AFAM.csv
               Input\MIDES\visitas_personas_AFAM.csv
               
    Output:

10) Objective: Mirar impactos ganar/perder en revisitas para grupos 
               con mismos inobservables
    Code:      Code\10_revisitados_inobservables.py
               Code\10_revisitados_inobservables.do
    Input:     Temp\vars_personas_revisitadas.csv

               
    Output:
'''

