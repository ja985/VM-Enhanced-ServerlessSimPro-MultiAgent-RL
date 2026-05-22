# -*- coding: utf-8 -*-
# Extended for VM-aware MAPPO-based serverless scheduling framework

# MAPPO-based Scheduler for ServlessSimPro

import random

class MAPPOScheduler:

    def __init__(self):
        self.name = "MAPPO"

    def selectVm(self, vmList, req):
        activeVmList = [vm for vm in vmList if vm.alive]

        if len(activeVmList) == 0:
            return None

        # Simplified MAPPO-style selection
        selectedVm = max(
            activeVmList,
            key=lambda vm: vm.remainCpu + vm.remainMem
        )

        return selectedVm

    def allocateRequest(self, req, vmList):

        vm = self.selectVm(vmList, req)

        if vm is not None:
            return vm.id

        return -1