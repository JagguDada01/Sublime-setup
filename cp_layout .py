import sublime
import sublime_plugin
import os


def find_or_create(root, candidates):
    # Open first existing file
    for name in candidates:
        path = os.path.join(root, name)
        if os.path.exists(path):
            return path

    # Otherwise create the first candidate
    path = os.path.join(root, candidates[0])

    try:
        with open(path, "w"):
            pass
    except Exception:
        return None

    return path


def setup_cp_layout(window):
    window.set_layout({
        "cols": [0.0, 0.72, 1.0],
        "rows": [0.0, 0.5, 1.0],
        "cells": [
            [0, 0, 1, 2],  # code
            [1, 0, 2, 1],  # input
            [1, 1, 2, 2]   # output
        ]
    })

    folders = window.folders()
    if not folders:
        return

    root = folders[0]

    code_candidates = [
        "main.cpp",
        "a.cpp",
        "solution.cpp",
        "cf1.cpp"
    ]

    input_candidates = [
    "inputf.in",
    "input.in",
    "input.txt"
    ]

    output_candidates = [
    "outputf.out",
    "output.out",
    "output.txt"
    ]

    code_file = find_or_create(root, code_candidates)
    input_file = find_or_create(root, input_candidates)
    output_file = find_or_create(root, output_candidates)

    if code_file:
        window.focus_group(0)
        window.open_file(code_file)

    if input_file:
        window.focus_group(1)
        window.open_file(input_file)

    if output_file:
        window.focus_group(2)
        window.open_file(output_file)

    window.focus_group(0)


class CpStartupListener(sublime_plugin.EventListener):

    def on_load_project_async(self, window):
        sublime.set_timeout(
            lambda: setup_cp_layout(window),
            200
        )

    def on_new_window(self, window):
        sublime.set_timeout(
            lambda: setup_cp_layout(window),
            200
        )
        
# ------------------------------------------------------------
#  CP Layout Automation for Sublime Text
#  Author : Jaggudada01
#  GitHub : https://github.com/JagguDada01
# ------------------------------------------------------------
# ============================================================
#       _                         ____            _       
#      | | __ _  __ _  __ _ _   _|  _ \  __ _  __| | __ _ 
#   _  | |/ _` |/ _` |/ _` | | | | | | |/ _` |/ _` |/ _` |
#  | |_| | (_| | (_| | (_| | |_| | |_| | (_| | (_| | (_| |
#   \___/ \__,_|\__, |\__, |\__,_|____/ \__,_|\__,_|\__,_|
#               |___/ |___/                               
#
#                     JAGGUDADA01
# ============================================================
