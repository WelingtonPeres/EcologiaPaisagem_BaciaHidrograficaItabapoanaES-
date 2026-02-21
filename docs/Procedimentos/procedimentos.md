# Roteiro — Ecologia da Paisagem da Bacia do Itabapoana

Guia do que foi feito no projeto e onde encontrar cada resultado.

---

## Visão geral

| Item | Descrição |
|------|-----------|
| **Objetivo** | Analisar a Ecologia da Paisagem da Bacia do Itabapoana (ES) |
| **Foco** | Fragmentos de Mata Nativa e Mata Nativa em Estágio Inicial de Regeneração |
| **CRS** | SIRGAS 2000 / UTM 24S (EPSG:31984) |
| **Documentação** | `fontes-dados.md` · `referencias.md` |

---

## Roteiro — O que foi feito

### Etapa 1. Estruturação do repositório ✅

**O que foi feito:** Criação da estrutura de pastas do projeto.

**Onde está:**
```
Ecologia_Paisagem/
├── docs/          → Documentação
├── Dados/         → Dados geográficos
├── scripts/       → Código de análise
├── resultados/    → Outputs
└── figuras/       → Figuras para publicação
```

**Configuração do Git LFS (arquivos GIS grandes):**

Para versionar arquivos geográficos sem exceder o limite do GitHub (100 MB por arquivo), o projeto usa Git LFS (Large File Storage).

**Requisitos:** Git LFS instalado (`winget install GitHub.GitLFS` no Windows).

**Passos:**
1. Na raiz do repositório: `git lfs install`
2. Definir os tipos de arquivo trackeados:
   ```bash
   git lfs track "*.gpkg"
   git lfs track "*.shp"
   git lfs track "*.shx"
   git lfs track "*.dbf"
   git lfs track "*.prj"
   git lfs track "*.tif"
   ```
3. Commitar o arquivo `.gitattributes` gerado automaticamente: `git add .gitattributes` e `git commit -m "Configurar Git LFS para arquivos GIS"`

**Tipos configurados:** .gpkg, .shp, .shx, .dbf, .prj, .tif

---

### Etapa 2. Aquisição de dados ✅

**O que foi feito:** Download das bases necessárias.

| Dado | Localização | Fonte |
|------|-------------|-------|
| Municípios do ES | `Dados/Shapes_Completos/ES_Municipios_2024_Completo/` | [IBGE](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html) |
| Unidades da Federação | `Dados/Shapes_Completos/BR_UF_2024_Completo/` | [IBGE](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html) |
| Bacias hidrográficas (todas) | `Dados/Shapes_Completos/BaciasHidrograficas_Completo/` | [ANA/SNIRH](https://metadados.snirh.gov.br/geonetwork/srv/por/catalog.search#/metadata/fb87343a-cc52-4a36-b6c5-1fe05f4fe98c) |
| Uso e cobertura do solo (ES 2019-2020) | `Dados/Shapes_Completos/ijsn_mapeamento_uso_solo_2019_2020/` | [Geobases/IJSN](https://geobases.es.gov.br/links-para-img-kpst-19-20) |

**Convenção de nomenclatura:** Arquivos reprojetados para UTM 24S recebem o sufixo `_UTM` (ex.: `nome_original_UTM.gpkg`).

---

### Etapa 3. Extração e reprojeção da Bacia do Itabapoana ✅

**O que foi feito:** Extração da Bacia do Itabapoana do shapefile de microrregiões hidrográficas (micro_RH) e reprojeção para UTM 24S (EPSG:31984).

| Etapa | Origem | Destino |
|-------|--------|---------|
| Extração | `BaciasHidrograficas_Completo/micro_RH/micro_RH.shp` | `Dados/Shapes_Recortes/BaciaHidrografica_Itabapoana/BaciaHidrografia_Itabapoana.shp` |
| Reprojeção | Shape em SIRGAS 2000 (EPSG:4674) | `BaciaHidrografia_Itabapoana_UTM.gpkg` (UTM 24S) |

**1. Extração:** Seleção da microrregião correspondente à Bacia do Itabapoana no QGIS e exportação em nova camada.

**2. Reprojeção (QGIS):** Seguindo os passos abaixo:

1. Abra a Caixa de Ferramentas (engrenagem no menu superior ou `Ctrl + Alt + T`)
2. Digite na busca: **Reprojetar** (ou Reproject)
3. Dê um duplo clique em **Vetor geral > Reprojetar camada** (Reproject layer)
4. Na janela que abrir:
   - **Camada de entrada:** O shapefile da Bacia (em EPSG:4674)
   - **SRC Alvo:** Clique no globinho à direita e escolha **EPSG:31984 — SIRGAS 2000 / UTM zone 24S**
   - **Reprojetado:** Salve em arquivo novo (`...` > Salvar no arquivo). **Nomenclatura:** arquivos reprojetados terminam com `_UTM` (ex.: `BaciaHidrografia_Itabapoana_UTM.gpkg` em `Dados/Shapes_Recortes/BaciaHidrografica_Itabapoana/`)

---

### Etapa 4. Municípios do ES e interseção com a Bacia ✅

**O que foi feito:** Adição dos Municípios do Espírito Santo e interseção com o shape da Bacia do Itabapoana.

**Procedimento:**
1. Municípios do ES adicionados ao projeto (versão reprojetada: `ES_Municipios_2024_UTM.gpkg`)
2. Interseção entre o shape dos Municípios e o shape da Bacia do Itabapoana (ambos em UTM 24S)
3. Resultado: região da Bacia no ES e municípios com território na bacia.

![Interseção Municípios x Bacia do Itabapoana - QGIS](interseccao_municipios_bacia_itabapoana_qgis.png)

- **Roxo:** Municípios do ES · **Laranja:** Municípios com área na bacia · **Azul:** Limite da bacia

**Como foi feito:** Ferramenta *Interseção* no QGIS, usando Municípios do ES como camada de entrada e Bacia do Itabapoana como camada de recorte.

---

### Etapa 5. Uso e cobertura do solo (IJSN) ✅

**O que foi feito:** Download do mapeamento de uso e cobertura do solo do Espírito Santo (2019-2020).

| Dado | Localização | Fonte |
|------|-------------|-------|
| Uso e cobertura do solo ES 2019-2020 | `Dados/Shapes_Completos/ijsn_mapeamento_uso_solo_2019_2020/` | [Geobases — IJSN](https://geobases.es.gov.br/links-para-img-kpst-19-20) |

**O que contém:** Shapefile com classes de uso do solo baseado na interpretação do Ortofotomosaico ES 2019-2020 (imagens Kompsat 3/3A). Inclui as classes **Mata Nativa** e **Mata Nativa em Estágio Inicial de Regeneração**, que são o foco das análises do projeto.

---

### Etapa 6. Recorte do uso do solo pela Bacia do Itabapoana (ES) ✅

**O que foi feito:** Recorte do mapeamento de uso e cobertura do solo pela área da Bacia do Itabapoana no Espírito Santo.

| Camada de entrada | Camada de recorte | Resultado |
|-------------------|-------------------|-----------|
| `ijsn_mapeamento_uso_solo_2019_2020` (uso do solo ES) | Bacia do Itabapoana no ES (`BaciaHidrografia_Itabapoana_UTM` ou interseção Municípios ∩ Bacia) | `UsoDeSolo_BH_Itabapoana_ES` |

**Onde está:** `Dados/Shapes_Recortes/UsoDeSolo_BH_Itabapoana_ES/`

![Uso do solo recortado pela Bacia do Itabapoana - QGIS](uso_solo_recortado_bacia_itabapoana_es.png)

**Como foi feito:** Ferramenta *Recortar* (Clip) no QGIS — camada de entrada: uso do solo; camada de recorte: Bacia do Itabapoana no ES (ambas em UTM 24S).

---

### Etapa 7. Extração dos fragmentos de Mata Nativa e Mata Nativa em Estágio Inicial ✅

**O que foi feito:** Extração das classes **Mata Nativa** (código 1) e **Mata Nativa em Estágio Inicial de Regeneração** (código 2) do recorte de uso do solo (`UsoDeSolo_BH_Itabapoana_ES`). As duas classes ficam no **mesmo shape**.

**Onde está:** `Dados/Shapes_Recortes/UsoDeSolo_BH_Itabapoana_ES/MataNativa_BH_Itabapoana_ES/`

![Extração Mata Nativa — Bacia do Itabapoana ES](extracao_mata_nativa_bacia_itabapoana_es.png)

**Como foi feito (QGIS):**
1. Abra a camada `UsoDeSolo_BH_Itabapoana_ES` (ou `UsoDeSolo_BH_I_ES`)
2. **Selecionar por atributo:** Clique com o botão direito na camada → *Selecionar* → *Selecionar feições por expressão*
3. Use a expressão: `"Código" IN (1, 2)` — em que **1** = Mata Nativa e **2** = Mata Nativa em Estágio Inicial de Regeneração
4. Com as feições selecionadas: Clique direito na camada → *Exportar* → *Salvar feições selecionadas como...* → salvar em `UsoDeSolo_BH_Itabapoana_ES/MataNativa_BH_Itabapoana_ES/`

**Alternativa:** Ferramenta *Extrair por atributo* na Caixa de Ferramentas (Vetor geral > Extrair por atributo) — campo `Código`, valores 1 e 2.

---

### Etapa 8. Unificação das classes e criação dos fragmentos ✅

**O que foi feito:** Unificação das classes Mata Nativa (código 1) e Mata em Estágio Inicial (código 2) em um único shape de fragmentos. Polígonos que se tocam foram mesclados; cada área desconectada virou um fragmento individual.

**Onde está:** `Dados/Shapes_Recortes/UsoDeSolo_BH_Itabapoana_ES/MataNativa_BH_Itabapoana_ES/MataNativa_Mesclagem_Fragmentos/Fragmentos_MataNativa_BH_I_ES.gpkg`

**Passo 1: Mesclar (Dissolve sem filtros)**

Objetivo: unir polígonos que se tocam, independente do código (1 ou 2).

1. Menu: **Vetor** → **Ferramentas de Geoprocessamento** → **Mesclar (Dissolve)**
2. **Camada de entrada:** `MataNativa_BH_Itabapoana_ES`
3. **Campos para mesclar:** deixe em **branco** (não selecione nada). Assim o QGIS une tudo que está se tocando.
4. **Mesclado:** Salvar em arquivo temporário (ex.: `Mata_Mesclada_Temp.shp`)
5. Clique em **Executar**

**Passo 2: Explodir (De múltiplas partes para partes simples)**

Objetivo: separar geograficamente — cada área desconectada vira uma linha na tabela (um fragmento).

1. Menu: **Vetor** → **Ferramentas de Geometria** → **De múltiplas partes para partes simples** (Multipart to singlepart)
2. **Camada de entrada:** `Mata_Mesclada_Temp.shp` (resultado do Passo 1)
3. **Partes simples:** Salvar em arquivo → `Fragmentos_MataNativa_BH_I_ES.gpkg` em `MataNativa_Mesclagem_Fragmentos/`
4. Clique em **Executar**

---

### Etapa 9. Cálculo de área e perímetro ✅

**O que foi feito:** Cálculo da área (em hectares) e do perímetro (em metros) de cada fragmento na camada `Fragmentos_MataNativa_BH_I_ES.gpkg`.

**Como foi feito (QGIS):**
1. Abra a tabela de atributos da camada `Fragmentos_MataNativa_BH_I_ES` (clique direito → *Abrir tabela de atributos*)
2. Ative o modo de edição (ícone de lápis)
3. **Calculadora de campos:** ícone de abacus ou *Campos* → *Calculadora de campos*

**Área em hectares:**
- Novo campo (ex.: `area_ha`), tipo **Decimal**
- Expressão: `$area / 10000` — `$area` retorna área em m²; divisão por 10.000 converte para hectares (1 ha = 10.000 m²)

**Perímetro em metros:**
- Novo campo (ex.: `perimetro_m`), tipo **Decimal**
- Expressão: `$perimeter` — retorna o perímetro em metros (CRS UTM)

4. Marque *Atualizar feições existentes* e selecione todas as feições
5. Clique em **OK** e salve as edições

**Observação:** `$area` e `$perimeter` exigem CRS projetado (UTM 24S) para resultados corretos em m² e m.

---

### Etapa 10. Classificação dos fragmentos por tamanho ✅

**O que foi feito:** Classificação de cada fragmento em classes de tamanho na camada `Fragmentos_MataNativa_BH_I_ES.gpkg`, com base em Fernandes e Fernandes (2017) e Santos et al. (2015), metodologia amplamente utilizada em estudos de fragmentação na Mata Atlântica.

**Classes adotadas:**

| Classe        | Área (ha) |
|---------------|-----------|
| Muito pequeno | < 5       |
| Pequeno       | 5–10      |
| Médio         | 10–100    |
| Grande        | 100–250   |
| Muito grande  | > 250     |

**Interpretação ecológica:** O limiar de 50 ha é relevante — Ribeiro et al. (2009) indicam que mais de 80% dos fragmentos da Mata Atlântica são menores que 50 ha e que fragmentos nessa faixa são insuficientes para manter a maioria das espécies florestais.

**Como foi feito (QGIS):**
1. Abra a tabela de atributos da camada `Fragmentos_MataNativa_BH_I_ES`
2. Ative o modo de edição
3. **Calculadora de campos** → Novo campo (ex.: `classe_tamanho`), tipo **Texto (string)**
4. Expressão:

```
CASE
  WHEN "Area_Ha" < 5 THEN 'Muito pequeno'
  WHEN "Area_Ha" >= 5 AND "Area_Ha" < 10 THEN 'Pequeno'
  WHEN "Area_Ha" >= 10 AND "Area_Ha" < 100 THEN 'Médio'
  WHEN "Area_Ha" >= 100 AND "Area_Ha" < 250 THEN 'Grande'
  ELSE 'Muito grande'
END
```

5. Marque *Atualizar feições existentes* e selecione todas as feições
6. Clique em **OK** e salve as edições

**Observação:** O nome do campo de área pode variar (ex.: `area_ha`). Ajuste na expressão se necessário.

**Referências:** Ribeiro et al. (2009); Fernandes & Fernandes (2017); Santos et al. (2015). Ver `docs/referencias.md`.

---

### Etapa 11. Cálculo do Índice de Forma e Classificação por Forma ✅

**O que foi feito:** Cálculo do índice de forma e classificação em classes de forma de cada fragmento na camada `Fragmentos_MataNativa_BH_I_ES.gpkg`, com base em Patton (1975) e no princípio isoperimétrico (círculo como forma de referência).

**Fórmula utilizada:**

$$DI = \frac{P}{2\sqrt{\pi A}}$$

Onde:
- **DI** = Índice de Diversidade / Índice de Forma (circularidade)
- **P** = Perímetro do fragmento (m)
- **A** = Área do fragmento (m²)
- **π** = Constante Pi (3,14159...)

**Interpretação:** DI = 1 quando o fragmento é perfeitamente circular; valores > 1 indicam formas mais alongadas ou irregulares (maior relação perímetro/área, maior exposição a efeitos de borda).

**Passo 1 — Cálculo do índice (QGIS):**
1. Abra a tabela de atributos da camada `Fragmentos_MataNativa_BH_I_ES`
2. Ative o modo de edição
3. **Calculadora de campos** → Novo campo (ex.: `indice_forma` ou `IndiceForma`), tipo **Decimal**
4. Expressão: `$perimeter / (2 * sqrt(pi() * $area))`
5. Marque *Atualizar feições existentes* e selecione todas as feições
6. Clique em **OK** e salve as edições

**Passo 2 — Classificação por forma (3 classes):**

| Classe         | Faixa do índice | Interpretação ecológica |
|----------------|-----------------|-------------------------|
| Compacto       | DI < 1,5        | Forma próxima do círculo; menor relação perímetro/área; menor efeito de borda |
| Alongado       | 1,5 ≤ DI < 2,0  | Forma alongada; maior relação perímetro/área; maior efeito de borda |
| Muito alongado | DI ≥ 2,0        | Forma muito alongada ou irregular; alta exposição a efeitos de borda |

1. **Calculadora de campos** → Novo campo (ex.: `classe_forma`), tipo **Texto (string)**
2. Expressão:

```
CASE
  WHEN "IndiceForma" < 1.5 THEN 'Compacto'
  WHEN "IndiceForma" >= 1.5 AND "IndiceForma" < 2.0 THEN 'Alongado'
  ELSE 'Muito alongado'
END
```

3. Marque *Atualizar feições existentes* e selecione todas as feições
4. Clique em **OK** e salve as edições

**Observação:** O nome do campo do índice pode variar (ex.: `indice_forma`, `IndiceForma`). Ajuste na expressão se necessário.

**Referências:** Patton (1975); Forman & Godron (1986). Limiares baseados em estudos de fragmentação florestal (Cerne, Revista Árvore). Ver `docs/referencias.md`.

---

### Etapa 12. Cálculo da Área Nuclear (Core Area) ✅

**O que foi feito:** Cálculo da área nuclear (área central) de cada fragmento na camada `Fragmentos_MataNativa_BH_I_ES.gpkg`, considerando o efeito de borda de 50 m.

**Conceito:** A área nuclear é a porção do fragmento que permanece livre da influência direta das bordas. Um buffer negativo de 50 m a partir do perímetro remove a zona de borda, onde ocorrem alterações microclimáticas e maior exposição a distúrbios. A largura de 50 m é comumente utilizada em estudos de ecologia da paisagem para representar a penetração do efeito de borda.

**Expressão utilizada (QGIS):**

```
COALESCE(area(buffer($geometry, -50)) / 10000, 0)
```

Onde:
- **buffer($geometry, -50)** = buffer negativo de 50 m para dentro do polígono (remove a zona de borda)
- **area(...)** = área em m² (CRS UTM)
- **/ 10000** = conversão para hectares
- **COALESCE(..., 0)** = retorna 0 quando o buffer resulta em geometria nula (fragmentos muito pequenos em que a área central desaparece)

**Como foi feito (QGIS):**
1. Abra a tabela de atributos da camada `Fragmentos_MataNativa_BH_I_ES`
2. Ative o modo de edição
3. **Calculadora de campos** → Novo campo (ex.: `coreArea` ou `area_nuclear_ha`), tipo **Decimal**
4. Expressão: `COALESCE(area(buffer($geometry, -50)) / 10000, 0)`
5. Marque *Atualizar feições existentes* e selecione todas as feições
6. Clique em **OK** e salve as edições

**Observação:** O resultado é em hectares. Fragmentos com dimensão menor que 100 m (diâmetro ou largura) podem ter área nuclear zero, pois o buffer de 50 m de cada lado elimina toda a área interna.

---

### Etapa 13. Cálculo do Isolamento (Distância ao Vizinho Mais Próximo) ✅

**O que foi feito:** Cálculo da distância de cada fragmento ao fragmento mais próximo (vizinho mais próximo) na camada `Fragmentos_MataNativa_BH_I_ES.gpkg`.

**Conceito:** O isolamento (ou *Mean Nearest Neighbor Distance — MNN*) mede a distância borda-a-borda entre cada fragmento e seu vizinho mais próximo. Valores altos indicam fragmentos mais isolados na paisagem; valores baixos indicam maior proximidade entre remanescentes. É uma métrica fundamental para avaliar conectividade estrutural e potencial de fluxo de espécies entre fragmentos.

**Expressão utilizada (QGIS):**

```
distance(
  $geometry,
  geometry(
    get_feature_by_id(
      @layer,
      array_first(overlay_nearest(@layer, $id))
    )
  )
)
```

Onde:
- **overlay_nearest(@layer, $id)** = retorna o ID do(s) fragmento(s) mais próximo(s) na mesma camada (exclui o próprio)
- **array_first(...)** = pega o primeiro da lista (vizinho mais próximo)
- **get_feature_by_id(@layer, ...)** = obtém a feição com esse ID
- **geometry(...)** = extrai a geometria da feição vizinha
- **distance($geometry, geometry(...))** = calcula a distância borda-a-borda em metros (CRS UTM)

**Como foi feito (QGIS):**
1. Abra a tabela de atributos da camada `Fragmentos_MataNativa_BH_I_ES`
2. Ative o modo de edição
3. **Calculadora de campos** → Novo campo (ex.: `isolamento_m` ou `dist_vizinho_m`), tipo **Decimal**
4. Cole a expressão acima
5. Marque *Atualizar feições existentes* e selecione todas as feições
6. Clique em **OK** e salve as edições

**Observação:** O resultado é em metros. A função `overlay_nearest` está disponível no QGIS 3.16+. Em versões anteriores, pode-se usar a ferramenta *Join attributes by nearest* ou *Distance to nearest hub*.

---

### Etapa 14. Classificação da Conectividade (3 classes) ✅

**O que foi feito:** Classificação da conectividade estrutural de cada fragmento na camada `Fragmentos_MataNativa_BH_I_ES.gpkg`, com base na distância ao vizinho mais próximo (isolamento) calculada na Etapa 13.

**Conceito:** A conectividade é inversa ao isolamento — quanto menor a distância ao vizinho mais próximo, maior a conectividade estrutural. Os limiares adotados seguem Ribeiro et al. (2009), Martensen et al. (2012) e Mello et al. (2016).

**Classes adotadas (3 classes):**

| Classe              | Faixa (m) | Interpretação ecológica |
|---------------------|-----------|-------------------------|
| Alta conectividade  | < 100     | Travessias curtas pela matriz muito eficazes; aves e pequenos mamíferos podem cruzar |
| Média conectividade | 100–500   | Conectividade moderada; algumas espécies podem cruzar |
| Baixa conectividade | ≥ 500     | Fragmentos isolados; fluxo entre fragmentos limitado para a maioria das espécies |

**Como foi feito (QGIS):**
1. Abra a tabela de atributos da camada `Fragmentos_MataNativa_BH_I_ES`
2. Ative o modo de edição
3. **Calculadora de campos** → Novo campo (ex.: `classe_conectividade`), tipo **Texto (string)**
4. Expressão:

```
CASE
  WHEN "Isolamento_m" < 100 THEN 'Alta conectividade'
  WHEN "Isolamento_m" >= 100 AND "Isolamento_m" < 500 THEN 'Média conectividade'
  ELSE 'Baixa conectividade'
END
```

5. Marque *Atualizar feições existentes* e selecione todas as feições
6. Clique em **OK** e salve as edições

**Observação:** O nome do campo de isolamento pode variar (ex.: `isolamento_m`, `dist_vizinho_m`). Ajuste na expressão se necessário.

**Referências:** Ribeiro et al. (2009); Martensen et al. (2012); Mello et al. (2016). Ver `docs/referencias.md`.

**Resultado — Tabela de atributos (MataNativa_Mesclada):** Campos `Area_Ha`, `Tamanho`, `Perimetro_m`, `Forma`, `IndiceForma`, `CoreArea_He`, `Conectividade`, `Isolamento_m`.

![Tabela de atributos — MataNativa_Mesclada (5383 feições)](tabela_atributos_fragmentos_mata_nativa.png)

---

## 📋 Próximos passos

### Etapa 15. 📋 Contagem de fragmentos por tamanho

**Objetivo:** Quantificar o número de fragmentos em cada classe de tamanho (Muito pequeno, Pequeno, Médio, Grande, Muito grande) para caracterizar a estrutura da paisagem.

**Como fazer (QGIS):**
1. Abra a camada `Fragmentos_MataNativa_BH_I_ES`
2. Use a ferramenta **Resumir por categoria** (Vetor > Ferramentas de análise > Resumir por categoria) ou a **Tabela de atributos** com o campo `classe_tamanho` (ou `Tamanho`)
3. Conte as feições por valor do campo de classificação de tamanho
4. Registre os resultados em tabela (ex.: em `resultados/` ou na documentação)

**Alternativa:** Na tabela de atributos, use *Selecionar feições por expressão* para cada classe e anote a contagem, ou exporte para planilha e use tabela dinâmica.

---

### Etapa 16. 📋 Aplicar classificações para visualização por cor em shapes diferentes

**Objetivo:** Criar camadas separadas (ou estilos distintos) para visualizar fragmentos por tamanho, forma e conectividade, cada um com esquema de cores adequado.

**Procedimento:**
1. **Por tamanho:** Estilizar a camada `Fragmentos_MataNativa_BH_I_ES` pelo campo `classe_tamanho` (ou `Tamanho`) com cores distintas (ex.: gradiente do menor ao maior fragmento)
2. **Por forma:** Estilizar pelo campo `classe_forma` (ou `Forma`) com paleta adequada (Compacto, Alongado, Muito alongado)
3. **Por conectividade:** Estilizar pelo campo `classe_conectividade` (ou `Conectividade`) com cores que indiquem alta, média e baixa conectividade

**Opcional:** Exportar cópias da camada para shapes/GeoPackages distintos (ex.: `Fragmentos_por_Tamanho.gpkg`, `Fragmentos_por_Forma.gpkg`, `Fragmentos_por_Conectividade.gpkg`) com estilos salvos (.qml) para uso em mapas temáticos.

**Como fazer (QGIS):** Painel de Camadas → clique direito na camada → *Propriedades* → *Simbologia* → *Categorizado* → campo desejado → *Classificar* → ajustar cores e rótulos.

---

### Etapa 17. 📋 Construir os mapas com legendas adequadas

**Objetivo:** Produzir mapas finais para relatório ou publicação, com layout, escala, norte, legenda e demais elementos cartográficos.

**Procedimento:**
1. Abra o **Compositor de impressão** (Projeto > Novo layout de impressão)
2. Adicione o mapa da área de estudo com as camadas estilizadas (Etapa 16)
3. Inclua **legenda** com as classes de tamanho, forma e conectividade (conforme o mapa temático)
4. Adicione **escala gráfica**, **rosa dos ventos** e **título**
5. Salve o layout e exporte em PNG ou PDF para `figuras/` ou `resultados/`

**Sugestão de mapas:**
- Mapa 1: Fragmentos por tamanho (legenda: Muito pequeno, Pequeno, Médio, Grande, Muito grande)
- Mapa 2: Fragmentos por forma (legenda: Compacto, Alongado, Muito alongado)
- Mapa 3: Fragmentos por conectividade (legenda: Alta, Média, Baixa conectividade)

**Onde salvar:** `figuras/` ou `resultados/` conforme a estrutura do projeto.

---

## 🔮 Análises futuras

### Etapa 18. 🔮 Análise de fragmentos por município

**Objetivo:** Quantificar e caracterizar os fragmentos de Mata Nativa em cada município da Bacia do Itabapoana (ES), permitindo comparações entre municípios e identificação de prioridades locais.

**Dados necessários:**
- `Fragmentos_MataNativa_BH_I_ES.gpkg` (fragmentos com métricas calculadas)
- Municípios com área na bacia (interseção Municípios ∩ Bacia, Etapa 4)

**Procedimento (QGIS):**
1. **Interseção espacial:** Vetor > Ferramentas de geoprocessamento > Interseção. Camada de entrada: fragmentos; camada de recorte: municípios da bacia. Resultado: cada fragmento ganha atributo do município (ou municípios, se houver polígonos em mais de um).
2. **Resumir por categoria:** Contar fragmentos e somar área por município. Campos úteis: `classe_tamanho`, `classe_forma`, `classe_conectividade`.
3. **Tabela de resultados:** Número de fragmentos, área total (ha), área média por fragmento, distribuição por classe de tamanho/forma/conectividade por município.

**Saídas esperadas:** Tabela e mapas temáticos por município; identificação de municípios com maior fragmentação ou maior concentração de fragmentos grandes.

---

### Etapa 19. 🔮 Análise de fragmentos por sub-bacias

**Objetivo:** Analisar a distribuição dos fragmentos nas sub-bacias (micro, meso ou macro) da Bacia do Itabapoana, permitindo identificar sub-bacias mais preservadas ou mais fragmentadas.

**Dados necessários:**
- `Fragmentos_MataNativa_BH_I_ES.gpkg`
- Sub-bacias da Bacia do Itabapoana (ex.: micro_RH recortado pela bacia, ou divisão hidrológica mais detalhada se disponível)

**Procedimento (QGIS):**
1. **Preparar sub-bacias:** Se a Bacia do Itabapoana for uma microrregião única, considerar subdivisão por mesorregiões ou por microbacias (ANA/SNIRH ou dados locais). Alternativa: dividir a bacia por municípios como proxy de sub-unidades.
2. **Interseção espacial:** Fragmentos ∩ sub-bacias. Cada fragmento recebe o atributo da sub-bacia onde está.
3. **Resumir por categoria:** Contagem e área por sub-bacia; distribuição por classes de tamanho, forma e conectividade.
4. **Métricas por sub-bacia:** Número de fragmentos, área total de Mata Nativa, percentual da sub-bacia, fragmentação média.

**Saídas esperadas:** Tabela comparativa entre sub-bacias; mapas temáticos por sub-bacia; identificação de sub-bacias prioritárias para conservação ou restauração.

**Observação:** A disponibilidade de sub-bacias dentro da Bacia do Itabapoana depende das bases (ANA, órgãos estaduais). Se não houver divisão oficial, a análise por município (Etapa 18) pode servir como aproximação.

---

## Onde encontrar cada coisa

| Procurando por... | Arquivo ou pasta |
|-------------------|------------------|
| Fontes de dados e metadados | `docs/fontes-dados.md` |
| Citações para relatórios | `docs/referencias.md` |
| Bacia do Itabapoana (área de estudo) | `Dados/Shapes_Recortes/BaciaHidrografica_Itabapoana/` — UTM: `BaciaHidrografia_Itabapoana_UTM.gpkg` |
| Municípios do ES (completo) | `Dados/Shapes_Completos/ES_Municipios_2024_Completo/` — versão UTM: `ES_Municipios_2024_UTM.gpkg` |
| Limites estaduais | `Dados/Shapes_Completos/BR_UF_2024_Completo/` |
| Todas as bacias (origem) | `Dados/Shapes_Completos/BaciasHidrograficas_Completo/` |
| Uso e cobertura do solo ES 2019-2020 | `Dados/Shapes_Completos/ijsn_mapeamento_uso_solo_2019_2020/` |
| Uso do solo recortado (Bacia Itabapoana ES) | `Dados/Shapes_Recortes/UsoDeSolo_BH_Itabapoana_ES/` |
| Mata Nativa + Mata em Estágio Inicial (códigos 1 e 2, mesmo shape) | `Dados/Shapes_Recortes/UsoDeSolo_BH_Itabapoana_ES/MataNativa_BH_Itabapoana_ES/` |
| Fragmentos de Mata Nativa (unificados, um polígono por fragmento) | `Dados/Shapes_Recortes/UsoDeSolo_BH_Itabapoana_ES/MataNativa_BH_Itabapoana_ES/MataNativa_Mesclagem_Fragmentos/Fragmentos_MataNativa_BH_I_ES.gpkg` |

---
