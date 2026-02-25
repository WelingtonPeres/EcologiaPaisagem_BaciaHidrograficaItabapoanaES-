"""
Histograma de AREA_HA com intervalos da classificação TAMANHO.
Dados: MataNativa_Mesclagem_Fragmentos.csv - Bacia do Itabapoana (ES).
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

PASTA_DADOS = Path(__file__).resolve().parent.parent / "EcologiaPaisagem_BaciaHidrograficaItabapoanaES-" / "data"
ARQUIVO_CSV = PASTA_DADOS / "MataNativa_Mesclagem_Fragmentos.csv"


def definir_caracteristicas_histograma(**kwargs) -> dict:
    """
    Retorna dicionário com características do histograma.
    Aceita kwargs para customizar valores padrão.
    """
    padrao = {
        "bins": [0, 5, 10, 100, 250, float("inf")],
        "labels": ["[0-5]", "[5-10]", "[10-100]", "[100-250]", "[>=250]"],
        "cor_barras": "grey",
        "cor_borda": "black",
        "alpha": 1.0,
        "figsize": (10, 6),
        "titulo": "Distribuição da área dos fragmentos de Mata Nativa\nBacia do Itabapoana (ES)",
        "label_x": "Área (ha)",
        "label_y_freq": "Frequência",
        "label_y_dens": "Densidade",
        "dpi": 150,
    }
    padrao.update(kwargs)
    return padrao


def plotar_histograma_normal(
    serie: pd.Series,
    ax: plt.Axes | None = None,
    config: dict | None = None,
) -> plt.Axes:
    """Histograma com frequência (contagem)."""
    if config is None:
        config = definir_caracteristicas_histograma()
    if ax is None:
        _, ax = plt.subplots(figsize=config["figsize"])

    area_class = pd.cut(serie, bins=config["bins"], labels=config["labels"], right=False)
    counts = area_class.value_counts().sort_index()

    x_pos = range(len(counts))
    bars = ax.bar(
        x_pos,
        counts.values,
        edgecolor=config["cor_borda"],
        color=config["cor_barras"],
        alpha=config["alpha"],
    )
    ax.bar_label(bars, labels=counts.values)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(counts.index)
    ax.set_xlabel(config["label_x"])
    ax.set_ylabel(config["label_y_freq"])
    ax.set_title(config["titulo"])

    return ax


def plotar_histograma_densidade(
    serie: pd.Series,
    ax: plt.Axes | None = None,
    config: dict | None = None,
) -> plt.Axes:
    """Histograma com densidade (proporção)."""
    if config is None:
        config = definir_caracteristicas_histograma()
    if ax is None:
        _, ax = plt.subplots(figsize=config["figsize"])

    area_class = pd.cut(serie, bins=config["bins"], labels=config["labels"], right=False)
    counts = area_class.value_counts().sort_index()
    densidades = counts.values / len(serie)

    x_pos = range(len(counts))
    bars = ax.bar(
        x_pos,
        densidades,
        edgecolor=config["cor_borda"],
        color=config["cor_barras"],
        alpha=config["alpha"],
    )
    ax.bar_label(bars, labels=[f"{d:.2%}" for d in densidades])
    ax.set_xticks(x_pos)
    ax.set_xticklabels(counts.index)
    ax.set_xlabel(config["label_x"])
    ax.set_ylabel(config["label_y_dens"])
    ax.set_title(config["titulo"])

    return ax


def main() -> None:
    df = pd.read_csv(ARQUIVO_CSV)
    pasta_saida = Path(__file__).resolve().parent
    area_ha = df["AREA_HA"].dropna()
    config = definir_caracteristicas_histograma()

    fig, ax = plt.subplots(figsize=config["figsize"])
    plotar_histograma_normal(area_ha, ax=ax, config=config)
    plt.tight_layout()
    plt.savefig(pasta_saida / "histograma_area_ha.png", dpi=config["dpi"], bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=config["figsize"])
    plotar_histograma_densidade(area_ha, ax=ax, config=config)
    plt.tight_layout()
    plt.savefig(pasta_saida / "histograma_area_ha_densidade.png", dpi=config["dpi"], bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
