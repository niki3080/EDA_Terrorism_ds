import matplotlib.patches as patches

# Цвета типов атак

ATTACK_COLORS = {
    "Взрыв": "#db2e2e",
    "Вооруженное нападение": "#538dbd",
    "Покушение": "#5f9e6e",
    "Захват заложников": "#f7ac4b",
    "Атака на инфраструктуру": "#a7a7a7"
}

def attack_palette(columns):
    return [ATTACK_COLORS.get(c, "#cccccc") for c in columns]


def style_title(ax, title, subtitle=None, title_height=0.12, gap=0.02):

    fig = ax.figure
    pos = ax.get_position()

    # серая зона
    fig.patches.append(
        patches.Rectangle(
            (0, pos.y1 + gap),   # ← добавили gap
            1,
            title_height,
            transform=fig.transFigure,
            color="#e7e7e7"
        )
    )

    left = pos.x0

    fig.text(
        left,
        pos.y1 + gap + title_height * 0.60,
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
            pos.y1 + gap + title_height * 0.18,
            subtitle,
            ha="left",
            va="center",
            fontfamily="Helvetica",
            fontsize=11,
            color="#565656"
        )


def style_legend(ax, title=None, loc="bc", alpha=0.85, ncol=1, shift_x=0.0, handles=None):
    loc_map = {
        "tr": ("upper right", (1 + shift_x, 1)),
        "tl": ("upper left", (0 + shift_x, 1)),
        "br": ("lower right", (1 + shift_x, 0)),
        "bl": ("lower left", (0 + shift_x, 0)),
        "bc": ("lower center", (0.5 + shift_x, 0))
    }

    loc_name, anchor = loc_map.get(loc, ("upper right", (1, 1)))

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