# PPGEE0260: Modelagem e Simulação Discreta de Sistemas
# Simulação Epidemiológica Baseada em Agentes

Aluno: Carlos André de Mattos Teixeira

Código baseado em: http://geospatialcss.blogspot.com/2017/06/comparing-four-modeling-approaches.html  

## Descrição do Projeto

**Objetivo:** Simular a evolução de uma epidemia ao longo do tempo com base no modelo SIR. Propor soluções baseadas no comportamento das curvas de infecção.

- Abordagem de simulação baseada em agentes.
- Simulação de diferentes cenários (taxas de infeção)


**Questionamentos:**

- Considerando uma população finita e o Modelo SIR, qual o impacto da taxa de infecção no comportamento da epidemia?
- Quantos % da população é infectada simultaneamente? Como isso impacta o sistema de saúde?
- Como realizar o "achatamento da curva"?


## Requisitos de Execução

- Instalação do software [NetLogo](http://ccl.northwestern.edu/netlogo/).
- **Opcional:** A análise dos resultados é gerada utilizando o software Jupyter Notebook. 


## Instruções de Execução

- Executar o arquivo [`simulation.nlogo`](https://github.com/andrematte/epidemic-simulator/simulation.nlogo).
- Utilizar os sliders para selecionar as configurações de simulação desejadas.
- Pressionar o botão Executar para rodar a simulação.
- **Opcional**: 
  - Salvar os resultados em arquivos csv (clicar com o botão direito nos gráficos de simulação.
  - Executar o arquivo ['results.ipynb'](https://github.com/andrematte/epidemic-simulator/results.ipynb) para gerar os gráficos de resultados.

## Referências

[1] Khalil, K. et. al. (2010, April). An agent-based modelling for pandemic influenza in Egypt. Informatics and Systems.

[2] Stevens, H. (2020, March 14). Why outbreaks like coronavirus spread exponentially, and how to flatten the curve. The Washington Post. Retrieved November 20, 2021, from https://www.washingtonpost.com/graphics/2020/world/corona-simulator/.

[3] Wilensky, U. (2016). NetLogo. NetLogo. Retrieved November 12, 2021, from http://ccl.northwestern.edu/netlogo/.

[4] Wikimedia Foundation. (2020, October 2). Modelo Epidêmico. Wikipedia. Retrieved October 29, 2021, from https://pt.wikipedia.org/wiki/Modelo_epid%C3%AAmico.

[5] Zhou, Y. (2017, June 3). Comparing four modeling approaches: System Dynamics, agent-based modeling, cellular automata, and discrete event simulation using a SIR model as an example. Comparing four modeling approaches: System Dynamics, Agent-based Modeling, Cellular Automata, and Discrete Event Simulation using a SIR model as an example. Retrieved October 29, 2021, from http://geospatialcss.blogspot.com/2017/06/comparing-four-modeling-approaches.html. 
