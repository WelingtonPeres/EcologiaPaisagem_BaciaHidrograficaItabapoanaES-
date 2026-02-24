# Fontes de Dados

Catálogo das fontes de dados do projeto Ecologia da Paisagem da Bacia do Itabapoana (ES). Para a convenção de nomes dos arquivos, ver `nomenclatura.md`.

---

## 1. Malha Municipal — Municípios do Espírito Santo

| Campo | Informação |
|-------|------------|
| **Arquivo** | `Dados/Dados_Brutos/ES_Municipios_2024_Completo/` |
| **Fonte** | IBGE — Instituto Brasileiro de Geografia e Estatística |
| **Produto** | Malha Municipal Digital (MMD) 2024 |
| **Unidade** | Municípios do Espírito Santo |
| **Formato** | Shapefile (SHP) |
| **Sistema de referência original** | SIRGAS 2000 (geográfico) |
| **Escala** | 1:250.000 |
| **Link** | [IBGE — Malhas Territoriais](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html) |

*Citação em `referencias.md`*

---

## 2. Divisão Hidrográfica Nacional — Bacias Hidrográficas

| Campo | Informação |
|-------|------------|
| **Arquivo** | `Dados/Dados_Brutos/BaciasHidrograficas_Completo/` |
| **Fonte** | ANA — Agência Nacional de Águas e Saneamento Básico / SNIRH |
| **Produto** | Divisão Hidrográfica Nacional (DHN250) |
| **Unidade** | Macrorregiões (macro_RH), Mesorregiões (meso_RH), Microrregiões (micro_RH) |
| **Formato** | Shapefile (SHP) |
| **Sistema de referência original** | SIRGAS 2000 (geográfico, EPSG:4674) |
| **Escala** | 1:250.000 |
| **Link** | [Catálogo SNIRH — Divisão Hidrográfica Nacional](https://metadados.snirh.gov.br/geonetwork/srv/por/catalog.search#/metadata/fb87343a-cc52-4a36-b6c5-1fe05f4fe98c) |

*Citação em `referencias.md`*

---

## 3. Malha Municipal — Unidades da Federação (Brasil)

| Campo | Informação |
|-------|------------|
| **Arquivo** | `Dados/Dados_Brutos/BR_UF_2024_Completo/` |
| **Fonte** | IBGE — Instituto Brasileiro de Geografia e Estatística |
| **Produto** | Malha Municipal Digital (MMD) 2024 |
| **Unidade** | Unidades da Federação (27 estados + DF) |
| **Formato** | Shapefile (SHP) |
| **Sistema de referência original** | SIRGAS 2000 (geográfico) |
| **Escala** | 1:250.000 |
| **Link** | [IBGE — Malhas Territoriais](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html) |

*Citação em `referencias.md`*

**Uso:** Limites estaduais. Reprojetar para UTM 24S antes das análises.

---

## 4. Uso e Cobertura do Solo — Espírito Santo 2019-2020

| Campo | Informação |
|-------|------------|
| **Arquivo** | `Dados/Dados_Brutos/ijsn_mapeamento_uso_solo_2019_2020/` |
| **Fonte** | IJSN — Instituto Jones dos Santos Neves / Geobases ES |
| **Produto** | Mapeamento de Uso e Cobertura do Solo ES 2019-2020 |
| **Unidade** | Estado do Espírito Santo |
| **Formato** | Shapefile (SHP) |
| **Sistema de referência original** | SIRGAS 2000 (geográfico) |
| **Escala** | 1:25.000 (baseado em imagens Kompsat 3/3A) |
| **Link** | [Geobases — IJSN Ortofotomosaico e Uso do Solo](https://geobases.es.gov.br/links-para-img-kpst-19-20) |

*Citação em `referencias.md`*

**Classes do projeto:** Mata Nativa, Mata Nativa em Estágio Inicial de Regeneração (Ortofotomosaico ES 2019-2020).

---

## 5. Sistema de Coordenadas do Projeto

| Parâmetro | Valor |
|-----------|-------|
| **CRS** | SIRGAS 2000 / UTM zone 24S |
| **EPSG** | 31984 |
| **Proj4** | `+proj=utm +zone=24 +south +ellps=GRS80 +units=m +no_defs` |

Todas as camadas devem estar neste CRS para consistência nas análises.
