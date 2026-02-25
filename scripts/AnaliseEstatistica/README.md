# Análise Estatística - Ecologia da Paisagem

Projeto simples para visualização e análise estatística dos dados de fragmentos de Mata Nativa da Bacia do Itabapoana (ES).

## Histograma AREA_HA

Script `plotarHistograma_area_ha.py` plota a distribuição da variável AREA_HA (área em hectares dos fragmentos).

- `definir_caracteristicas_histograma()`: define bins, labels, cores e padrões
- `plotar_histograma_normal()`: histograma por frequência
- `plotar_histograma_densidade()`: histograma por densidade (proporção)

### Uso

```bash
pip install -r requirements.txt
python plotarHistograma_area_ha.py
```

Gera `histograma_area_ha.png` (frequência) e `histograma_area_ha_densidade.png` (densidade).
