# Nomenclatura de Arquivos

Convenção de nomes para arquivos e camadas do projeto.

---

## Estrutura geral

### Dados brutos

Mantêm os nomes originais das fontes (IBGE, ANA, IJSN).

---

## Recortes (padrão)

```
[Dados]_[Recorte/Região]_[Objetivo]_[CRS]
```

| Elemento | Descrição | Exemplos |
|----------|-----------|----------|
| **Dados** | Tipo de dado | `Bacia`, `Municipios`, `UsoSolo`, `MataNativa` |
| **Recorte/Região** | Área de recorte | `BH_Itabapoana`, `BH_Itabapoana_ES`, `ES` |
| **Objetivo** | Uso ou etapa | `AreaEstudo`, `Recorte`, `Extracao`, `Analise` |
| **CRS** | `UTM` ou `4674` | `UTM` (EPSG:31984) ou `4674` (SIRGAS geográfico) |

---

## Arquivos em Recortes_Bacia

| Arquivo | Significado |
|---------|-------------|
| `Bacia_BH_Itabapoana_AreaEstudo_4674` | Bacia do Itabapoana, área de estudo, SIRGAS 2000 geográfico |
| `Bacia_BH_Itabapoana_AreaEstudo_UTM` | Bacia do Itabapoana, área de estudo, UTM 24S |
| `Municipios_ES_Analise_UTM` | Municípios do ES, reprojetados para análise |
| `UsoSolo_BH_Itabapoana_ES_Recorte_UTM` | Uso do solo recortado pela bacia no ES |
| `MataNativa_BH_Itabapoana_ES_Extracao_UTM` | Mata Nativa extraída (códigos 1 e 2) na bacia no ES |

---

## Objetivos (sufixos)

| Objetivo | Uso |
|----------|-----|
| `AreaEstudo` | Limite da área de estudo (ex.: bacia) |
| `Recorte` | Camada recortada pela área de estudo |
| `Extracao` | Seleção de classes (ex.: Mata Nativa) |
| `Analise` | Camada reprojetada para análise |

---

## Abreviações

| Sigla | Significado |
|-------|-------------|
| BH | Bacia Hidrográfica |
| ES | Espírito Santo |

---

## Fragmentos (análise)

A camada principal mantém o nome `Fragmentos_MataNativa_BH_I_ES.gpkg` (legado). Para novas versões, pode-se adotar `Fragmentos_MN_BH_Itabapoana_ES_UTM.gpkg`.
