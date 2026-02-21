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

### Tecnologias utilizadas

O processamento foi feito no **QGIS** (Sistema de Informações Geográficas). Os dados de entrada vêm do IBGE (malhas municipais e UFs), da ANA/SNIRH (bacias hidrográficas) e do IJSN/Geobases (uso e cobertura do solo do ES, 2019–2020). As camadas foram reprojetadas para SIRGAS 2000 / UTM 24S (EPSG:31984). O resultado final está em GeoPackage (`.gpkg`). As métricas foram calculadas na Calculadora de campos do QGIS, com uso de funções como `overlay_nearest` para o isolamento.

### Classificações adotadas

**Tamanho** (Fernandes & Fernandes, 2017; Santos et al., 2015):

| Classe        | Área (ha) |
|---------------|-----------|
| Muito pequeno | &lt; 5    |
| Pequeno       | 5–10      |
| Médio         | 10–100    |
| Grande        | 100–250   |
| Muito grande  | &gt; 250  |

**Forma** (Patton, 1975). Índice DI = P / (2√πA). Classes:

| Classe         | Faixa do índice |
|----------------|-----------------|
| Compacto       | DI &lt; 1,5     |
| Alongado       | 1,5–2,0         |
| Muito alongado | ≥ 2,0           |

**Conectividade** (Ribeiro et al., 2009; Martensen et al., 2012; Mello et al., 2016). Baseada na distância ao vizinho mais próximo:

| Classe              | Distância (m) |
|---------------------|---------------|
| Alta conectividade  | &lt; 100      |
| Média conectividade | 100–500       |
| Baixa conectividade | ≥ 500         |

Outras métricas: área nuclear (buffer negativo de 50 m) e isolamento (distância borda a borda ao fragmento mais próximo). O roteiro completo das 14 etapas está em [docs/Procedimentos/procedimentos.md](docs/Procedimentos/procedimentos.md).

## Estrutura

```
Ecologia_Paisagem/
├── docs/
│   ├── Procedimentos/       Roteiro e procedimentos (QGIS), imagens
│   ├── fontes-dados.md     Catálogo de fontes
│   └── referencias.md      Citações bibliográficas
└── Dados/                  Dados geográficos (não versionados, ver fontes-dados.md)
    ├── Bacia_Itabapoana/
    ├── Shapes_Completos/   IBGE, ANA, IJSN (dados originais)
    │   ├── BaciasHidrograficas_Completo/
    │   ├── BR_UF_2024_Completo/
    │   ├── ES_Municipios_2024_Completo/
    │   └── ijsn_mapeamento_uso_solo_2019_2020/
    └── Shapes_Recortes/    Recortes pela bacia
        ├── BaciaHidrografica_Itabapoana/
        ├── BaciaHidrografica_Itabapoana_ES/
        └── UsoDeSolo_BH_Itabapoana_ES/
```

## Documentação

| Documento | Descrição |
|-----------|-----------|
| [docs/Procedimentos/procedimentos.md](docs/Procedimentos/procedimentos.md) | Roteiro completo, etapas 1–14, expressões QGIS |
| [docs/fontes-dados.md](docs/fontes-dados.md) | Fontes de dados (IBGE, ANA, IJSN) e links |
| [docs/referencias.md](docs/referencias.md) | Referências bibliográficas |

## Dados

Os dados geográficos não estão no repositório (tamanho). Obtenha conforme [docs/fontes-dados.md](docs/fontes-dados.md) e organize em `Dados/`.

## Licença

[Definir conforme uso do projeto]
