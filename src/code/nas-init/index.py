# coding=utf-8
import os


def handler(event, context):
    if not os.path.exists("/mnt/auto/uploads"):
        os.system(
            "mkdir -p /mnt/auto/uploads && cd -")
    if not os.path.exists("/mnt/auto/avatar"):
        os.system(
            "mkdir -p /mnt/auto/avatar && cd -")
    return "nas init"
