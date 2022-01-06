#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from NaysaEncoderBot.get_cfg import get_config


class Command:
    COMPRESS = get_config(
        "COMMAND_COMPRESS",
        "compress"
    )
    CANCEL = get_config(
        "COMMAND_CANCEL",
        "cancel"
    )
    STATUS = get_config(
        "COMMAND_STATUS",
        "status"
    )
    EXEC = get_config(
        "COMMAND_EXEC",
        "exec"
    )
    HELP = get_config(
        "COMMAND_HELP",
        "help"
    )
    UPLOAD_LOG_FILE = get_config(
        "COMMAND_UPLOAD_LOG_FILE",
        "log"
    )
    TEXT = "Send Resolution Like This /set_res 720p"
