#!/usr/bin/env python
# coding: utf8

import json
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import ansible.constants as C

'''class ResultCallback(CallbackBase):
    """A sample callback plugin used for performing an action as results come in

    If you want to collect all results into a single object for processing at
    the end of the execution, look into utilizing the ``json`` callback plugin
    or writing your own custom callback plugin
    """
    def v2_runner_on_ok(self, result, **kwargs):
        """Print a json representation of the result

        This method could store the result in an instance attribute for retrieval later
        """
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))
不想使用自定义输出 屏蔽回调函数'''

# since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
#become=tom,become_method=sudo #tom 用sudo方式提权执行命令
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
## 链接可以设置为local/ssh/smart 本地链接，ssh链接，智能选择本地ssh

# initialize needed objects
loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
#分析yml json 文件 把内容转成python数据
passwords = dict() #vault_pass='secret'需要加密登陆加上

# Instantiate our ResultCallback for handling results as they come in. Ansible expects this to be one of its main display outlets
'''results_callback = ResultCallback()'''

# create inventory, use path to host config file as source or hosts in a comma separated string
#主机清单,使用字符串主机名,逗号分隔,也可以使用列表
#inventory = InventoryManager(loader=loader, sources='localhost,web1.tedu.cn')
inventory = InventoryManager(loader=loader, sources=['/root/myansible/hosts'])

# variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
#变量管理器,没有不用改
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
play_source =  dict(
        name = "Ansible Play",   # 脚本功能解释
        hosts = 'webservers',    # 需要执行命令的主机组, 在inventory定义的主机清单里面找
        gather_facts = 'no',    #要不要获得主机的基本信息
        tasks = [
            # dict(action=dict(module='shell', args='ls'), register='shell_out'),
            # dict(action=dict(module='shell', args='useradd kellon'), register='shell_out'),
            # dict(action=dict(module='shell', args='id kellon'), register='shell_out'),
            dict(action=dict(module='yum', args='name=vsftpd state=installed'), register='shell_out'),
            # dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
            # shell回显输出,显示执行shell命令是的标准输出,不用可注 释掉
         ]
    )

# Create play object, playbook objects use .load instead of init or new methods,
# this will also automatically create the task objects from the info provided in play_source
# 生成一个play对象
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
tqm = None   # 任务管理队列 TaskQueueManager 缩写
try:
    tqm = TaskQueueManager(
              inventory=inventory,
              variable_manager=variable_manager,
              loader=loader,
              options=options,
              passwords=passwords,
              #'''stdout_callback=results_callback, ''' # Use our custom callback instead of the ``default`` callback plugin, which prints to stdout
          )
    # 生成实例,然后运行
    result = tqm.run(play) # most interesting data for a play is actually sent to the callback's methods
finally:
    # we always need to cleanup child procs and the structres we use to communicate with them
    if tqm is not None:
        tqm.cleanup()   #执行tqm清理工作

    # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
    # 最后删除临时目录