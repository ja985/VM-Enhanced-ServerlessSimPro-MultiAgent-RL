# -*- coding: utf-8 -*-
# VM-aware Physical Machine Layer
import random

tempId = 0
MEM = 192
CPU = 64


class PM:
    def __init__(self, startTime):
        global tempId
        self.id = tempId
        self.mem = MEM
        self.remainMem = self.mem
        self.cpu = CPU
        self.remainCpu = self.cpu

        # Added VM-aware hierarchy
        self.vmList = []

        self.containerIdList = []
        self.start_end_time = [startTime, -1]
        self.alive = True
        tempId += 1

    def createVm(self, vm):
        self.vmList.append(vm)

    def getActiveVms(self):
        return [vm for vm in self.vmList if vm.alive]

    @staticmethod
    def resetId():
        global tempId
        tempId = 0
