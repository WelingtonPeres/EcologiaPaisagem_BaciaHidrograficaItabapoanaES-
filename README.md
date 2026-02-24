# Ecologia da Paisagem - Bacia do Itabapoana (ES)

Análise de fragmentos de Mata Nativa e Mata Nativa em Estágio Inicial de Regeneração na Bacia do Itabapoana, Espírito Santo.

## Introdução

A Bacia do Itabapoana divide território entre Espírito Santo e Rio de Janeiro, no domínio da Mata Atlântica. O bioma perdeu a maior parte da cobertura original. Ribeiro et al. (2009) estimam que restam menos de 8% do que existia. Com a fragmentação, o que importa não é só quanto resta de floresta, mas como os remanescentes se distribuem no espaço. O tamanho de cada fragmento, sua forma e a distância entre eles passam a definir o que ainda pode persistir. Forman e Godron (1986) já destacavam esse papel da estrutura da paisagem.

A maior parte dos fragmentos da Mata Atlântica tem menos de 50 ha. Ribeiro et al. (2009) chegaram a esse resultado em escala nacional. Em bacias do Espírito Santo, estudos como o de Pirovani et al. (2014) na Bacia do Itapemirim e o de Santos et al. (2015) apontam na mesma direção. A maior parte dos remanescentes é pequena. Fragmentos nessa faixa costumam abrigar menos espécies do que um trecho florestal contínuo de área equivalente, já que a proporção de borda em relação ao núcleo tende a ser maior.

A distância entre fragmentos também conta. Quanto mais isolado um remanescente, menor a chance de troca de indivíduos e genes com outros fragmentos. Martensen et al. (2012) mostraram que a conectividade está ligada à riqueza de aves de sotobosque. Mello et al. (2016) e Souza et al. (2014) usam métricas de conectividade para indicar onde vale a pena priorizar ações de conservação.

A forma do fragmento entra na conta. Fragmentos alongados têm mais perímetro em relação à área. Patton (1975) propôs um índice que junta perímetro e área para quantificar isso. Quando o fragmento é alongado, a borda ganha peso e o núcleo diminui, o que reduz a qualidade do habitat. Forman e Godron (1986) discutem esse efeito em detalhe.

Este projeto trabalha com os fragmentos de **Mata Nativa** e **Mata Nativa em Estágio Inicial de Regeneração** na parte capixaba da bacia. Os dados vêm do mapeamento de uso do solo do IJSN (2019-2020). As métricas seguem a literatura citada em [docs/referencias.md](docs/referencias.md).

## Objetivo

- Calcular métricas de fragmentação florestal (área, perímetro, forma, conectividade, isolamento)
- Classificar fragmentos por tamanho, forma e conectividade estrutural
- CRS: SIRGAS 2000 / UTM 24S (EPSG:31984)

## Metodologia

### Fluxo de processamento

O trabalho foi organizado em 22 etapas, das quais 17 estão concluídas. O fluxo segue três blocos principais:

1. **Aquisição e preparação** (Etapas 1-7): Estruturação do repositório, download das bases (IBGE, ANA, IJSN), extração da bacia, recorte do uso do solo e seleção das classes Mata Nativa e Mata em Estágio Inicial.
2. **Processamento vetorial** (Etapas 8-9): Unificação das classes (dissolve + explode), correção topológica (fechamento morfológico com buffer ±0,5 m para eliminar frestas artificiais).
3. **Métricas e classificações** (Etapas 10-17): Cálculo de área, perímetro, índice de forma, área nuclear, isolamento (distância ao vizinho mais próximo), classificações por tamanho, forma e conectividade, e atribuição de município a cada fragmento.

As etapas 18-22 (contagem, estilização, mapas, análises por município e sub-bacias) estão planejadas e documentadas em [docs/Procedimentos/procedimentos.md](docs/Procedimentos/procedimentos.md).

### Tecnologias e fontes de dados

| Item | Especificação |
|------|---------------|
| **SIG** | QGIS (versão 3.16 ou superior recomendada) |
| **CRS** | SIRGAS 2000 / UTM zone 24S (EPSG:31984) |
| **Formato de saída** | GeoPackage (.gpkg) |
| **Fontes** | IBGE (malhas municipais e UFs), ANA/SNIRH (bacias hidrográficas), IJSN/Geobases (uso e cobertura do solo ES 2019-2020) |

As camadas foram reprojetadas para UTM 24S antes das análises. As métricas foram calculadas na Calculadora de campos do QGIS, com funções como `overlay_nearest` para o isolamento e `overlay_intersects` para a atribuição de município. Detalhes das fontes em [docs/fontes-dados.md](docs/fontes-dados.md).

### Critérios metodológicos

**Área Mínima Mapeável (AMM):** 0,5 ha. Fragmentos menores foram excluídos após a correção topológica, com base em Rutchey et al. (2008), Wickham et al. (2004) e Mello et al. (2016).

**Correção topológica:** Fechamento morfológico (buffer +0,5 m, dissolve, buffer −0,5 m) para eliminar frestas artificiais da vetorização, sem unir fragmentos separados por estradas reais (Mader, 1984; Forman, 1997).

**Precisão numérica:** Quatro casas decimais no banco espacial; duas casas na apresentação dos resultados.

### Classificações adotadas

**Tamanho** (Fernandes & Fernandes, 2017; Santos et al., 2015):

| Classe        | Área (ha) |
|---------------|-----------|
| Muito pequeno | &lt; 5    |
| Pequeno       | 5–10      |
| Médio         | 10–100    |
| Grande        | 100–250   |
| Muito grande  | ≥ 250     |

**Forma** (Patton, 1975). Índice DI = P / (2√πA):

| Classe         | Faixa do índice |
|----------------|-----------------|
| Compacto       | DI &lt; 1,5     |
| Alongado       | 1,5 ≤ DI &lt; 2,0 |
| Muito alongado | DI ≥ 2,0        |

**Conectividade** (Ribeiro et al., 2009; Martensen et al., 2012; Mello et al., 2016). Baseada na distância ao vizinho mais próximo:

| Classe              | Distância (m) |
|---------------------|---------------|
| Alta conectividade  | &lt; 100      |
| Média conectividade | 100–500       |
| Baixa conectividade | ≥ 500         |

**Outras métricas:** Área nuclear (buffer negativo de 50 m a partir do perímetro) e isolamento (distância borda a borda ao fragmento mais próximo).

## Reproducibilidade

O roteiro completo está documentado em [docs/Procedimentos/procedimentos.md](docs/Procedimentos/procedimentos.md), com ferramentas, parâmetros e expressões do QGIS. Cada etapa indica origem, destino e critérios adotados. A convenção de nomenclatura dos arquivos está em [docs/nomenclatura.md](docs/nomenclatura.md).

## Como usar

1. **Obter os dados:** Baixe as bases conforme [docs/fontes-dados.md](docs/fontes-dados.md) e organize em `Projeto/Dados/`.
2. **Configurar Git LFS:** Se for versionar dados GIS, execute `git lfs install` e tracke os tipos `.gpkg`, `.shp`, `.shx`, `.dbf`, `.prj`, `.tif`.
3. **Seguir o roteiro:** Abra o QGIS e execute as etapas em [docs/Procedimentos/procedimentos.md](docs/Procedimentos/procedimentos.md).

## Estrutura do repositório

```
Ecologia_Paisagem/
├── docs/
│   ├── Procedimentos/       Roteiro e procedimentos (QGIS), imagens
│   ├── fontes-dados.md     Catálogo de fontes
│   ├── nomenclatura.md     Convenção de nomes
│   └── referencias.md      Citações bibliográficas
└── Projeto/
    └── Dados/              Dados geográficos
        ├── Dados_Brutos/       Camadas baixadas (IBGE, ANA, IJSN)
        │   ├── BaciasHidrograficas_Completo/
        │   ├── BR_UF_2024_Completo/
        │   ├── ES_Municipios_2024_Completo/
        │   └── ijsn_mapeamento_uso_solo_2019_2020/
        ├── Recortes_Bacia/     Recortes na área da bacia do Itabapoana
        │   ├── Bacia_BH_Itabapoana_AreaEstudo/
        │   ├── MataNativa_BH_Itabapoana_ES_Extracao/
        │   └── UsoSolo_BH_Itabapoana_ES_Recorte/
        └── Fragmentos_Analise/ Camada principal com métricas
            └── Fragmentos_MataNativa_BH_I_ES.gpkg
```

## Documentação

| Documento | Descrição |
|-----------|-----------|
| [docs/Procedimentos/procedimentos.md](docs/Procedimentos/procedimentos.md) | Roteiro completo, etapas 1–22, expressões QGIS |
| [docs/fontes-dados.md](docs/fontes-dados.md) | Fontes de dados (IBGE, ANA, IJSN) e links |
| [docs/nomenclatura.md](docs/nomenclatura.md) | Convenção de nomes para arquivos e camadas |
| [docs/referencias.md](docs/referencias.md) | Referências bibliográficas |

## Dados

Os dados geográficos ficam em `Projeto/Dados/`. Se não estiverem no repositório (por tamanho ou por não terem sido commitados), obtenha conforme [docs/fontes-dados.md](docs/fontes-dados.md) e organize nessa pasta.

## Citação

Se usar este projeto em pesquisa ou relatórios, cite-o. O repositório inclui um arquivo `CITATION.cff` para importação em gestores de referência. Citação sugerida:

> Ecologia da Paisagem - Bacia do Itabapoana (ES). Análise de fragmentos de Mata Nativa na Bacia do Itabapoana, Espírito Santo. Disponível em: [URL do repositório]. Acesso em: [data].

## Licença

[Definir conforme uso do projeto. Sugestão: MIT ou CC-BY 4.0 para dados e documentação.]
