import matplotlib.patches as patches

# Цвета типов атак

ATTACK_COLORS = {
    "Взрыв": "#db2e2e",
    "Вооруженное нападение": "#538dbd",
    "Покушение": "#5f9e6e",
    "Захват заложников": "#f7ac4b",
    "Атака на инфраструктуру": "#a7a7a7",
    "Угон транспорта": "#a7a7a7"
}

def attack_palette(columns):
    return [ATTACK_COLORS.get(c, "#cccccc") for c in columns]


def style_title(ax, title, subtitle=None, title_height=0.12):

    fig = ax.figure

    top = 0.92   # высота заголовка
    left = 0.06  # левый отступ

    fig.patches.append(
        patches.Rectangle(
            (0, top),
            1,
            title_height,
            transform=fig.transFigure,
            color="#e7e7e7"
        )
    )

    fig.text(
        left,
        top + title_height * 0.60,
        title,
        ha="left",
        va="center",
        fontfamily="Bebas Neue",
        fontweight="bold",
        fontsize=30,
        color="#434343"
    )

    if subtitle:
        fig.text(
            left,
            top + title_height * 0.18,
            subtitle,
            ha="left",
            va="center",
            fontfamily="Helvetica",
            fontsize=11,
            color="#565656"
        )



def style_legend(ax, title=None, loc="bc", alpha=0.85, ncol=1,
                 shift_x=0.0, shift_y=0.0, handles=None):

    loc_map = {
        "tr": ("upper right", (1 + shift_x, 1 + shift_y)),
        "tl": ("upper left", (0 + shift_x, 1 + shift_y)),
        "br": ("lower right", (1 + shift_x, 0 + shift_y)),
        "bl": ("lower left", (0 + shift_x, 0 + shift_y)),
        "bc": ("lower center", (0.5 + shift_x, 0 + shift_y)),
        "cl": ("center left", (0 + shift_x, 0.5 + shift_y)),
        "cr": ("center right", (1 + shift_x, 0.5 + shift_y))
    }

    loc_name, anchor = loc_map.get(loc, ("upper right", (1 + shift_x, 1 + shift_y)))

    legend = ax.legend(
        title=title,
        handles=handles,
        loc=loc_name,
        bbox_to_anchor=anchor,
        ncol=ncol,
        frameon=True,
        facecolor="#f9f9f9",
        framealpha=alpha
    )

    # стиль заголовка
    title_obj = legend.get_title()
    title_obj.set_fontweight("bold")
    title_obj.set_ha("left")

    # выравнивание блока
    legend._legend_box.align = "left"

    # убрать рамку
    legend.get_frame().set_edgecolor("none")

    return legend


def style_footer(ax, height=0.04):

    fig = ax.figure

    fig.patches.append(
        patches.Rectangle(
            (0, 0),              # нижний левый угол figure
            1,                   # ширина всей figure
            height,              # высота футера
            transform=fig.transFigure,
            color="#f5f5f5",     # тот же фон что у figure
            zorder=0
        )
    )