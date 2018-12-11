#!/usr/bin/env python
# _*_coding:utf8_*_

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor

Options = namedtuple(
    'Options', [
        'connection',
        'remoter_user',
        'ask_sudo_pass',
        'verbosity',
        'ask_pass',
        'module_path',
        'forks',
        'become',
        'become_method',
        'become_user',
        'check',
        'listhosts',
        'listtasks',
        'listtags',
        'syntax',
        'sudo_user',
        'sudo',
        'diff'
    ]
)

ops = Options(
    connection='smart',
    remoter_user=None,
    ask_pass=None,
    sudo_user=None,
    forks=5,
    sudo=None,
    ask_sudo_pass=False,
    verbosity=5,
    module_path=None,
    become=None,
    become_method=None,
    become_user=None,
    check=False,
    diff=False,
    listhosts=None,
    listtasks=None,
    listtags=None,
    syntax=None,
)

loader = DataLoader()
passwords = dict()
inventory = InventoryManager(loader=loader,sources=['/root/myansible/hosts'])
variable_manager = VariableManager(loader=loader,inventory=inventory)

def playbook_run(playbook_path):
    playbook = PlaybookExecutor(
        playbooks=playbook_path,
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=ops,
        passwords=passwords
    )

    result = playbook.run()
    return result

if __name__ == '__main__':
    playbook_run(playbook_path=['/root/myansible/check_service.yml'])
