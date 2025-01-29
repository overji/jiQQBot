import os
import importlib
from botpy import logging

def parse_command(args):
    _log = logging.get_logger()
    if(len(args) != 0):
        cmd = args[0]
    else:
        cmd = ""
    cmd_list = []
    cmd_target = []
    cmd_introduce = []
    get_all_plugins(cmd_list, cmd_target, cmd_introduce)
    for i in range(0, len(cmd_list)):
        if (cmd_list[i] == cmd):
            _log.info(f"执行{cmd}命令")
            return cmd_target[i](args[1:])
    return "找不到指令，请输入.help获取帮助"

def get_all_plugins(cmd_list, cmd_target, cmd_introduce):
    files = [f for f in os.listdir("./plugins") if os.path.isfile(f)]
    for f in files:
        plugin_name = os.path.splitext(f)[0]
        if(plugin_name != "PLUGIN_LOADER" and plugin_name != "RESTRICTION"):
            module = importlib.import_module(plugin_name)
            interface = getattr(module, f"interface_{plugin_name}")
            intro = getattr(module,f"interface_get_introduction")
            name = getattr(module,f"interface_get_name")
            cmd_list.append(name())
            cmd_target.append(interface)
            cmd_introduce.append(intro())

