import wget
import os
import shutil

#Criação de função para download e movimentação de arquivos
def pegaETrataArquivo (lista):  
    for item in lista:
        try:
            wget.download(item)      

        except:
            print('\nDownload falhou '+ item)

def movimentaArquivo(source, destination):
    files = os.listdir(source)
    for file in files:
        try: 
            extensao = file.split('.')[1]
            if extensao != 'git':
                shutil.move(f"{source}/{file}", destination)
            else:
                print('TA TENTANDO MOVER MEU .GIT?')
        except:
            print(file+' é uma pasta')

#Cria a pasta de Download caso não tenha
destination = './download'
if os.path.exists(destination):
    print('\nPasta /Download já existente.')
else:
    os.makedirs(destination)   
    print('\npasta /Download criada.')

#Download de bases de Escolas 2007 - 2019 - Média de Alunos por Turma
pegaETrataArquivo(lista=['http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/media_alunos_turma/2007/media_alunos_turma_escolas_2007.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/media_alunos_turma/2008/media_alunos_turma_escolas_2008.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/media_alunos_turma/2009/media_alunos_turma_escolas_2009.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/media_alunos_turma/2010/media_alunos_turma_escolas_2010_3.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2011/alunos_turma/alunos_turma_escolas_2011.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2012/alunos_turma/media_alunos_turma_escolas_2012.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2013/alunos_turma/media_alunos_turma_escolas_2013.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2014/alunos_turma/media_alunos_turma_escolas_2014.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2015/alunos_turma/media_alunos_turma_escolas_2015.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2016/ATU_2016_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2017/ATU_2017_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2018/ATU_2018_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2019/ATU_2019_ESCOLAS.zip'])

print('10% - Download')
#Download de bases de Escolas 2007 - 2019 - Média de Horas-Aula diária
pegaETrataArquivo(lista=['http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/media_hora_aula_diaria/2010/media_horas_aula_escolas_2010.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2011/horas_aula_diaria/horas_aula_escolas_2011.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2012/horas_aula_diaria/horas_aula_escolas_2012.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2013/horas_aula_diaria/horas_aula_escolas_2013.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2014/horas_aula_diaria/horas_aula_escolas_2014.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2015/horas_aula_diaria/horas_aula_escolas_2015.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2016/HAD_2016_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2017/HAD_2017_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2018/HAD_2018_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2019/HAD_2019_ESCOLAS.zip'])

print('20% - Download')
#Download de bases de Escolas 2007 - 2019 - Taxas de distorção idade-série
pegaETrataArquivo(lista=['http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/taxa_distorcao_idade_serie/2007/tdi_escolas_2007.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/taxa_distorcao_idade_serie/2008/tx_tdi_escolas_2008.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/taxa_distorcao_idade_serie/2009/dados_tdi_escolas_2009.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/taxa_distorcao_idade_serie/2010/tdi_escolas_2010.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2011/distorcao_idade_serie/tdi_escolas_2011.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2012/distorcao_idade_serie/tdi_escolas_2012.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2013/distorcao_idade_serie/tdi_escolas_2013.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2014/distorcao_idade_serie/tdi_escolas_2014.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2015/distorcao_idade_serie/tdi_escolas_2015.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2016/TDI_2016_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2017/TDI_2017_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2018/TDI_2018_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2019/TDI_2019_ESCOLAS.zip'])

print('30% - Download')
#Download de bases de Escolas 2007 - 2019 - Taxas de Rendimento
pegaETrataArquivo(lista=['http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/taxa_rendimento/2007/tx_rendimento_escolas_2007.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/taxa_rendimento/2008/tx_rendimento_escola_2008.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/taxa_rendimento/2009/tx_rendimento_escola_2009.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/taxa_rendimento/2010/tx_rendimento_escolas_2010_19082011.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/taxa_rendimento/2011/tx_rendimento_escolas_2011_2.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2012/taxas_rendimento/tx_rendimento_escolas_2012.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2013/taxa_rendimento/tx_rendimento_escolas_2013.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2014/taxa_rendimento/tx_rendimento_escolas_2014.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2015/taxa_rendimento/tx_rendimento_escolas_2015.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2016/TAXA_REND_2016_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2017/TAXA_REND_2017_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2018/TX_REND_ESCOLAS_2018.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2019/tx_rend_escolas_2019.zip'])

print('40% - Download')
#Download de bases de Escolas 2007 - 2019 - Taxa de Não Resposta (TNR)
pegaETrataArquivo(lista=['http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/taxa_nao_resposta/2010/tx_nao_resposta_escolas_2010.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/taxa_nao_resposta/2011/tx_nao_resposta_escolas_2011.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2012/taxa_nao_resposta/tx_nao_resposta_escolas_2012.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2013/taxa_nao_resposta/tx_nao_resposta_escolas_2013.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2014/taxa_nao_resposta/tx_nao_resposta_escolas_2014.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2015/taxa_nao_resposta/tx_nao_resposta_escolas_2015.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2016/TNR_2016_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2017/TNR_2017_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2018/TNR_ESCOLAS_2018.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2019/tnr_escolas_2019.zip'])

print('50% - Download')
#Download de bases de Escolas 2007 - 2019 - Percentual de Docentes com Curso Superior
pegaETrataArquivo(lista=['http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2011/proporcao_docentes_formacao_superior/dsu_escolas_2011.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2012/proporcao_docentes_formacao_superior/dsu_escolas_2012.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2013/proporcao_docentes_formacao_superior/dsu_escolas_2013.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2014/proporcao_docentes_formacao_superior/dsu_escolas_2014.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2015/proporcao_docentes_formacao_superior/dsu_escolas_2015.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2016/DSU_2016_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2017/DSU_2017_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2018/DSU_2018_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2019/DSU_2019_ESCOLAS.zip'])

print('60% - Download')
#Download de bases de Escolas 2007 - 2019 - Adequação da Formação Docente
pegaETrataArquivo(lista=['http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2013/adequacao_formacao_docente/adequacao_formacao_docente_escolas_2013.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2014/adequacao_formacao_docente/adequacao_formacao_docente_escolas_2014.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2015/adequacao_formacao_docente/adequacao_formacao_docente_escolas_2015.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2016/AFD_2016_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2017/AFD_2017_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2018/AFD_2018_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2019/AFD_2019_ESCOLAS.zip'])

print('70% - Download')
#Download de bases de Escolas 2007 - 2019 - Regularidade do Corpo Docente
pegaETrataArquivo(lista=['http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2013/regularidade_corpo_docente/regularidade_corpo_docente_escolas_2013.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2014/regularidade_corpo_docente/regularidade_corpo_docente_escolas_2014.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2015/regularidade_corpo_docente/regularidade_corpo_docente_escolas_2015.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2016/IRD_2016_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2017/IRD_2017_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2018/IRD_2018_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2019/IRD_2019_ESCOLAS.zip'])

print('80% - Download')
#Download de bases de Escolas 2007 - 2019 - Esforço Docente
pegaETrataArquivo(lista=['http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2019/IED_2019_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2018/IED_2018_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2017/IED_2017_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2016/IED_2016_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2015/esforco_docente/esforco_docente_escolas_2015.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2014/esforco_docente/esforco_docente_escolas_2014.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2013/esforco_docente/esforco_docente_escolas_2013.zip'])

print('90% - Download')
#Download de bases de Escolas 2007 - 2019 - Complexidade de Gestão da Escola
pegaETrataArquivo(lista=['http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2019/ICG_2019_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2018/ICG_2018_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2017/ICG_2017_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2016/ICG_2016_ESCOLAS.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2015/complexidade_gestao_escola/complexidade_gestao_escola_escolas_2015.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2014/complexidade_gestao_escola/complexidade_gestao_escola_escolas_2014.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2013/complexidade_gestao_escola/complexidade_gestao_escola_escolas_2013.zip'])


#Download de bases de Escolas 2007 - 2019 - Nível Socioeconômico
pegaETrataArquivo(lista=['http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2011_2013/nivel_socioeconomico/Indicador_INSE_por_Escola.zip',
                            'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2015/nivel_socioeconomico/Indicador_Inse_2015.zip'])
print('100% - Download')

#Move arquivos para a pasta de Download
movimentaArquivo(source='./', destination='./download')


#Download de bases de Escolas 2007 - 2019 - Taxas de Transição
#Download de bases de Escolas 2007 - 2019 - Remuneração Média dos Docentes
#Download de bases de Escolas 2007 - 2019 - Indicador de Fluxo da Educação Superior


# import extrai_limpa_zip
# import retira_pasta