# VM abstraction layer for VM-aware ServlessSimPro

tempVmId = 0

class VM:
    def __init__(self, startTime, hostPm, mem=64, cpu=16):
        global tempVmId
        self.id = tempVmId
        self.hostPm = hostPm
        self.mem = mem
        self.cpu = cpu
        self.remainMem = mem
        self.remainCpu = cpu
        self.containerIdList = []
        self.start_end_time = [startTime, -1]
        self.alive = True
        tempVmId += 1

    def canAllocate(self, cpuReq, memReq):
        return self.remainCpu >= cpuReq and self.remainMem >= memReq

    @staticmethod
    def resetId():
        global tempVmId
        tempVmId = 0
