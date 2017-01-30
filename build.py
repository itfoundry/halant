#! /usr/bin/env AFDKOPython
# encoding: UTF-8
from __future__ import division, absolute_import, print_function, unicode_literals
import hindkit as kit

family = kit.Family(
    trademark = "Halant",
    script_name = "Devanagari",
    client_name = "Google Fonts",
    initial_release_year = 2014,
)
family.set_masters()
family.set_styles([
    ("Light",     0, 300),
    ("Regular",  21, 400),
    ("Medium",   44, 500),
    ("SemiBold", 70, 600),
    ("Bold",    100, 700),
])

i = family.info
i.openTypeNameDesigner = "Vivek Sadamate and Ninad Kale (Devanagari), Jonny Pinhorn (Latin)"
i.openTypeHheaAscender, i.openTypeHheaDescender, i.openTypeHheaLineGap = 1050, -350, 100
i.openTypeOS2TypoAscender, i.openTypeOS2TypoDescender, i.openTypeOS2TypoLineGap = 1050, -350, 100
i.openTypeOS2WinAscent, i.openTypeOS2WinDescent = 1100, 400

project = kit.Project(
    family,
    fontrevision = "2.100",
    options = {

        "prepare_kerning": True,
        "prepare_mark_positioning": True,

        "match_mI_variants": "single",
        "position_marks_for_mI_variants": True,

        "build_ttf": True,
        "do_style_linking": True,

        # "use_os_2_version_4": True,
        #     "prefer_typo_metrics": True,
        #     "is_width_weight_slope_only": True,

        "additional_unicode_range_bits": [0, 1, 2],

    },
)

# (light_min, light_max), (bold_min, bold_max)
# project.adjustment_for_matching_mI_variants = (0, 0), (0, 0)

project.build()
