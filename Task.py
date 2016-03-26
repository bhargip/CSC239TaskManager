from tkinter import *
from tkinter import ttk
import multiprocessing
import os
import time
import subprocess
from collections import defaultdict
from collections import namedtuple
import psutil
from heapq import heapify, heappop
import pwd
import operator

global count
class Task:
	def __init__(self):
		#initialize root and Tk module
		self.root = Tk()
		self.create()
	
	def create(self):
		#create main window
		self.root.wm_title("Task Manager")
		self.root.geometry("800x500")
		global top
		self.top = Frame(self.root)
		self.top.grid(row=0,column=0)
		#create all the options as buttons
		self.cpuStatbutton=Button(self.top,text="CPU and System Statistics",command=self.CPUStat).grid(row=1, column=0, sticky = "w",padx=4,pady=1)
		self.userprocbutton=Button(self.top,text="User and Process Statistics",command=self.ProcStat).grid(row=1, column=2, sticky = "w",padx=4,pady=1)
		self.netbutton=Button(self.top,text="Network Statistics",command=self.NetStat).grid(row=1, column=3, sticky = "w",padx=4,pady=1)
		self.filebutton=Button(self.top,text="File Statistics",command=self.FileStat).grid(row=1, column=4, sticky = "w",padx=4,pady=1)

	def CPUStat(self):
		#create the CPU frame
		self.root.wm_title("CPU Statistics")
		self.root.geometry("800x550")
		self.top.grid_forget()
		global top_1
		self.top_1 = Frame(self.root)
		self.top_1.grid(row=1,column=1)
		#call CPU() to create labels
		self.CPU()
		self.exitcpuStatbtn=Button(self.top_1,text="Back to Main", command=self.back_Main).grid(row=25,column=1,sticky="w",padx=1,pady=1)

	def CPU(self):		
		#create labels and entry fields
		global cputotal
		#CPU stats
		cputotal = multiprocessing.cpu_count()
		self.cpu_0 = Label(self.top_1, text="CPU and System Statistics").grid(row=1,column=1,columnspan=3,sticky="nsew",padx=1,pady=1)
		self.cpu_1 = Label(self.top_1, text="Total no.of CPUs").grid(row=2, column=0,sticky="w",padx=4,pady=1)
		self.cpu_10 = Label(self.top_1, text=cputotal).grid(row=2, column=1,sticky="w",padx=1,pady=1)
		
		self.cpu_2=Label(self.top_1,text="CPU Name").grid(row=3,column=0,sticky="w",padx=1,pady=1)
		cpulbltxt1=StringVar()
		self.cpu_21=Label(self.top_1,textvariable=cpulbltxt1).grid(row=4,column=0,sticky="w",padx=1,pady=1)
		cpulbltxt2=StringVar()
		self.cpu_22=Label(self.top_1,textvariable=cpulbltxt2).grid(row=5,column=0,sticky="w",padx=1,pady=1)
	
		self.usr_1=Label(self.top_1,text="Min").grid(row=3,column=4,sticky="w",padx=1,pady=1)
		self.usr_1=Label(self.top_1,text="Max").grid(row=3,column=5,sticky="w",padx=1,pady=1)	
		self.usr_1=Label(self.top_1,text="Avg").grid(row=3,column=6,sticky="w",padx=1,pady=1)	
		minCputxt=StringVar()
		self.cpu_23=Label(self.top_1,textvariable=minCputxt).grid(row=4,column=4,sticky="w",padx=1,pady=1)
		maxCputxt=StringVar()
		self.cpu_24=Label(self.top_1,textvariable=maxCputxt).grid(row=4,column=5,sticky="w",padx=1,pady=1)
		avgTxt=StringVar()
		self.cpu_25=Label(self.top_1,textvariable=avgTxt).grid(row=4,column=6,sticky="w",padx=1,pady=1)
		
	
		self.usr_1=Label(self.top_1,text="User Mode").grid(row=3,column=1,sticky="w",padx=1,pady=1)
		usrlbltxt1=StringVar()
		self.usr_11=Label(self.top_1,textvariable=usrlbltxt1).grid(row=4,column=1,sticky="w",padx=1,pady=1)
		usrlbltxt2=StringVar()
		self.usr_12=Label(self.top_1,textvariable=usrlbltxt2).grid(row=5,column=1,sticky="w",padx=1,pady=1)

		self.sys_1=Label(self.top_1,text="System Mode").grid(row=3,column=2,sticky="w",padx=1,pady=1)
		syslbltxt1=StringVar()
		self.sys_11=Label(self.top_1,textvariable=syslbltxt1).grid(row=4,column=2,sticky="w",padx=1,pady=1)
		syslbltxt2=StringVar()
		self.sys_12=Label(self.top_1,textvariable=syslbltxt2).grid(row=5,column=2,sticky="w",padx=1,pady=1)

		self.tot_1=Label(self.top_1,text="Total").grid(row=3,column=3,sticky="w",padx=1,pady=1)
		totlbltxt1=StringVar()
		self.tot_11=Label(self.top_1,textvariable=totlbltxt1).grid(row=4,column=3,sticky="w",padx=1,pady=1)
		totlbltxt2=StringVar()
		self.ttl_12=Label(self.top_1,textvariable=totlbltxt2).grid(row=5,column=3,sticky="w",padx=1,pady=1)

		intrlbltxt=StringVar()
		self.intr_1=Label(self.top_1,text="No.of Interrupts").grid(row=6,column=0,sticky="w",padx=4,pady=1)
		self.intr_11=Label(self.top_1,textvariable=intrlbltxt).grid(row=6,column=1,sticky="w",padx=1,pady=1)

		cnswlbltxt=StringVar()
		self.cnsw_1=Label(self.top_1,text="No.of Context Switches").grid(row=7,column=0,sticky="w",padx=4,pady=1)
		self.cnsw_11=Label(self.top_1,textvariable=cnswlbltxt).grid(row=7,column=1,sticky="w",padx=1,pady=1)

		avmemlbltxt=StringVar()
		self.avmem_1=Label(self.top_1,text="Available Memory").grid(row=8,column=0,sticky="w",padx=4,pady=1)
		self.avmem_11=Label(self.top_1,textvariable=avmemlbltxt).grid(row=9,column=0,sticky="w",padx=1,pady=1)

		totmemlbltxt=StringVar()
		self.totmem_1=Label(self.top_1,text="Total Memory").grid(row=8,column=1,sticky="w",padx=4,pady=1)
		self.totmem_11=Label(self.top_1,textvariable=totmemlbltxt).grid(row=9,column=1,sticky="w",padx=1,pady=1)
		
		memutillbltxt=StringVar()
		self.memutil_1=Label(self.top_1,text="Memory Utilization(%)").grid(row=8,column=2,sticky="w",padx=4,pady=1)
		self.memutil_11=Label(self.top_1,textvariable=memutillbltxt).grid(row=9,column=2,sticky="w",padx=1,pady=1)

		prevUsr=[0,0,0,0,0]
		currUsr=[0,0,0,0,0]
		prevSys=[0,0,0,0,0]
		currSys=[0,0,0,0,0]
		prevIntr=[0,0,0,0,0]
		currIntr=[0,0,0,0,0]
		prevCnsw=[0,0,0,0,0]
		currCnsw=[0,0,0,0,0]
		prevAvmem=[0,0,0,0,0]
		currAvmem=[0,0,0,0,0]
		prevTotmem=[0,0,0,0,0]
		currTotmem=[0,0,0,0,0]
		jiffy = os.sysconf(os.sysconf_names['SC_CLK_TCK'])
		minCpu=100
		maxCpu=0
		curravg=0
		prevavg=0
		count=0
		# call get_CPU to fill values
		self.get_CPU(cputotal,prevUsr,prevSys,currUsr,currSys,cpulbltxt1,cpulbltxt2,usrlbltxt1,usrlbltxt2,syslbltxt1,syslbltxt2,totlbltxt1,totlbltxt2,minCputxt,maxCputxt,minCpu,maxCpu,count,prevavg,curravg,avgTxt)
		
		#call get_Intr to get interrupts details
		self.get_Intr(cputotal,prevIntr,currIntr,intrlbltxt)
		#call get_Cnsw to get context switches details
		self.get_Cnsw(cputotal,prevCnsw,currCnsw,cnswlbltxt)
		#call get_Mem to get memory stats
		self.get_Mem(cputotal,prevAvmem,currAvmem,prevTotmem,currTotmem,avmemlbltxt,totmemlbltxt,memutillbltxt)

		#create labels for Disk IO stats
		self.io = Label(self.top_1,text="Min").grid(row=10,column=2,sticky="w", padx=1, pady=1)
		self.io2 = Label(self.top_1,text="Max").grid(row=10,column=3,sticky="w", padx=1, pady=1)
		self.io3 = Label(self.top_1,text="Avg").grid(row=10,column=4,sticky="w", padx=1, pady=1)
		self.reads = Label(self.top_1,text="No of Disk reads").grid(row=11,column=0,sticky="w", padx=4, pady=1)
		readstxt = StringVar()
		self.reads1 = Label(self.top_1, textvariable=readstxt).grid(row=11,column=1,sticky="w", padx=4, pady=1)
		self.blkreads = Label(self.top_1,text="No of blocks read").grid(row=12,column=0,sticky="w", padx=1, pady=1)
		blkreadstxt = StringVar()
		self.blkreads1 = Label(self.top_1,textvariable=blkreadstxt).grid(row=12,column=1,sticky="w", padx=1, pady=1)
		self.writes = Label(self.top_1,text="No of Disk writes").grid(row=13,column=0,sticky="w", padx=0, pady=1)
		writestxt = StringVar()
		self.writes1 = Label(self.top_1, textvariable=writestxt).grid(row=13,column=1,sticky="w", padx=1, pady=1)
		self.blkwrites = Label(self.top_1,text="No of blocks written").grid(row=14,column=0,sticky="w", padx=1, pady=1)
		blkwritestxt = StringVar()
		self.blkwrites1 = Label(self.top_1,textvariable=blkwritestxt).grid(row=14,column=1,sticky="w", padx=1, pady=1)

		
		minRd = StringVar()
		self.minRd = Label(self.top_1,textvariable=minRd).grid(row=11,column=2,sticky="w", padx=1, pady=1)	
		maxRd = StringVar()
		self.maxRd = Label(self.top_1,textvariable=maxRd).grid(row=11,column=3,sticky="w", padx=1, pady=1)
		minBRd = StringVar()
		self.minBRd = Label(self.top_1,textvariable=minBRd).grid(row=12,column=2,sticky="w", padx=1, pady=1)
		maxBRd = StringVar()
		self.maxBRd = Label(self.top_1,textvariable=maxBRd).grid(row=12,column=3,sticky="w", padx=1, pady=1)

		minWr = StringVar()
		self.minWr = Label(self.top_1,textvariable=minWr).grid(row=13,column=2,sticky="w", padx=1, pady=1)	
		maxWr = StringVar()
		self.maxWr = Label(self.top_1,textvariable=maxWr).grid(row=13,column=3,sticky="w", padx=1, pady=1)
		minBWr = StringVar()
		self.minBWr = Label(self.top_1,textvariable=minBWr).grid(row=14,column=2,sticky="w", padx=1, pady=1)
		maxBWr = StringVar()
		self.maxBWr = Label(self.top_1,textvariable=maxBWr).grid(row=14,column=3,sticky="w", padx=1, pady=1)

		avgRd = StringVar()
		self.avgR = Label(self.top_1,textvariable=avgRd).grid(row=11,column=4,sticky="w", padx=1, pady=1)	
		avgBRd = StringVar()
		self.avgBR = Label(self.top_1,textvariable=avgBRd).grid(row=12,column=4,sticky="w", padx=1, pady=1)
		avgWr = StringVar()
		self.avgW = Label(self.top_1,textvariable=avgWr).grid(row=13,column=4,sticky="w", padx=1, pady=1)
		avgBWr = StringVar()
		self.avgBW = Label(self.top_1,textvariable=avgBWr).grid(row=14,column=4,sticky="w", padx=1, pady=1)

		currReads=[0,0,0,0,0]
		currBlocksread=[0,0,0,0,0]
		currWrites=[0,0,0,0,0]
		currBlockswrite=[0,0,0,0,0]
		prevReads=[0,0,0,0,0]
		prevBlocksread=[0,0,0,0,0]
		prevWrites=[0,0,0,0,0]
		prevBlockswrite=[0,0,0,0,0]	
		minReads=100.0
		maxReads=0
		minBlocksread=1000.0
		maxBlocksread=0
		minWrites=100.0
		maxWrites=0
		minBlockswrites=1000.0
		maxBlockswrites=0
		curravgRd=0
		prevavgRd=0
		curravgBRd=0
		prevavgBRd=0
		curravgWr=0
		prevavgWr=0
		curravgBWr=0
		prevavgBWr=0
		count=0
		
		# call get_IO to fill values for Disk IO stats
		self.get_IO(cputotal,readstxt,blkreadstxt,writestxt,blkwritestxt,currReads,currBlocksread,currWrites,currBlockswrite,prevReads,prevBlocksread,prevWrites,prevBlockswrite,minReads,maxReads,minBlocksread,maxBlocksread,minWrites,maxWrites,minBlockswrites,maxBlockswrites,minRd,maxRd,minBRd,maxBRd,minWr,maxWr,minBWr,maxBWr,avgRd,avgBRd,avgWr,avgBWr,curravgRd,prevavgRd,curravgBRd,prevavgBRd,curravgWr,prevavgWr,curravgBWr,prevavgBWr,count)
		
		#create labels for Network Stats
		self.estCon = Label(self.top_1,text="Established TCP Connection").grid(row=15,column=0,sticky="w", padx=4, pady=1)
		estContxt = StringVar()
		self.estCon1 = Label(self.top_1, textvariable=estContxt).grid(row=16,column=0,sticky="w", padx=4, pady=1)

		self.actCon = Label(self.top_1,text="Active TCP Connection").grid(row=15,column=1,sticky="w", padx=1, pady=1)
		actContxt = StringVar()
		self.actCon1 = Label(self.top_1,textvariable=actContxt).grid(row=16,column=1,sticky="w", padx=1, pady=1)
		
		self.Con1 = Label(self.top_1,text="Min").grid(row=17,column=2,sticky="w",padx=1,pady=1)		
		self.Con2 = Label(self.top_1,text="Max").grid(row=17,column=3,sticky="w",padx=1,pady=1)	
		self.Con3 = Label(self.top_1,text="Avg").grid(row=17,column=4,sticky="w",padx=1,pady=1)	

		self.InSeg = Label(self.top_1,text="In Segments").grid(row=18,column=0,sticky="w", padx=1, pady=1)
		InSegtxt = StringVar()
		self.InSeg1 = Label(self.top_1,textvariable=InSegtxt).grid(row=18,column=1,sticky="w", padx=1, pady=1)

		minIns = StringVar()
		self.InSeg2 = Label(self.top_1,textvariable=minIns).grid(row=18,column=2,sticky="w", padx=1, pady=1)	
		maxIns = StringVar()
		self.InSeg3 = Label(self.top_1,textvariable=maxIns).grid(row=18,column=3,sticky="w", padx=1, pady=1)	
		avgIns = StringVar()
		self.InSeg4 = Label(self.top_1,textvariable=avgIns).grid(row=18,column=4,sticky="w", padx=1, pady=1)		
		
		self.OutSeg = Label(self.top_1,text="Out Segments").grid(row=19,column=0,sticky="w", padx=1, pady=1)
		OutSegtxt = StringVar()
		self.OutSeg1 = Label(self.top_1,textvariable=OutSegtxt).grid(row=19,column=1,sticky="w", padx=1, pady=1)

		minOuts = StringVar()
		self.OutSeg2 = Label(self.top_1,textvariable=minOuts).grid(row=19,column=2,sticky="w", padx=1, pady=1)	
		maxOuts = StringVar()
		self.OutSeg3 = Label(self.top_1,textvariable=maxOuts).grid(row=19,column=3,sticky="w", padx=1, pady=1)	
		avgOuts = StringVar()
		self.OutSeg4 = Label(self.top_1,textvariable=avgOuts).grid(row=19,column=4,sticky="w", padx=1, pady=1)	

		self.InData = Label(self.top_1,text="In Datagrams").grid(row=20,column=0,sticky="w", padx=1, pady=1)
		InDatatxt = StringVar()
		self.InData1 = Label(self.top_1,textvariable=InDatatxt).grid(row=20,column=1,sticky="w", padx=1, pady=1)		
		
		minInd = StringVar()
		self.InData2 = Label(self.top_1,textvariable=minInd).grid(row=20,column=2,sticky="w", padx=1, pady=1)	
		maxInd = StringVar()
		self.InData3 = Label(self.top_1,textvariable=maxInd).grid(row=20,column=3,sticky="w", padx=1, pady=1)	
		avgInd = StringVar()
		self.InData4 = Label(self.top_1,textvariable=avgInd).grid(row=20,column=4,sticky="w", padx=1, pady=1)

		self.OutData = Label(self.top_1,text="Out Datagrams").grid(row=21,column=0,sticky="w", padx=1, pady=1)
		OutDatatxt = StringVar()
		self.OutData1 = Label(self.top_1,textvariable=OutDatatxt).grid(row=21,column=1,sticky="w", padx=1, pady=1)

		minOutd = StringVar()
		self.OutData2 = Label(self.top_1,textvariable=minOutd).grid(row=21,column=2,sticky="w", padx=1, pady=1)	
		maxOutd = StringVar()
		self.OutData3 = Label(self.top_1,textvariable=maxOutd).grid(row=21,column=3,sticky="w", padx=1, pady=1)	
		avgOutd = StringVar()
		self.OutData4 = Label(self.top_1,textvariable=avgOutd).grid(row=21,column=4,sticky="w", padx=1, pady=1)

		self.inTraffic = Label(self.top_1,text="InComing Traffic").grid(row=22,column=0,sticky="w", padx=1, pady=1)
		inTraffictxt = StringVar()
		self.inTraffic1 = Label(self.top_1, textvariable=inTraffictxt).grid(row=22,column=1,sticky="w", padx=1, pady=1)

		self.outTraffic = Label(self.top_1,text="Outgoing Traffic").grid(row=23,column=0,sticky="w", padx=1, pady=1)
		outTraffictxt = StringVar()
		self.outTraffic1 = Label(self.top_1,textvariable=outTraffictxt).grid(row=23,column=1,sticky="w", padx=1, pady=1)

		self.totNet = Label(self.top_1,text="Total Network Utilization").grid(row=24,column=0,sticky="w", padx=1, pady=1)
		totNettxt = StringVar()
		self.totNet1 = Label(self.top_1,textvariable=totNettxt).grid(row=24,column=1,sticky="w", padx=1, pady=1)

		currEst=[0,0,0,0,0]
		currAct=[0,0,0,0,0]
		currOverall=[0,0,0,0,0]
		currUpstream=[0,0,0,0,0]
		currDownstream=[0,0,0,0,0]
		currInseg=[0,0,0,0,0]
		currOutseg=[0,0,0,0,0]
		prevInseg=[0,0,0,0,0]
		prevOutseg=[0,0,0,0,0]
		currIndata=[0,0,0,0,0]
		currOutdata=[0,0,0,0,0]
		prevIndata=[0,0,0,0,0]
		prevOutdata=[0,0,0,0,0]
		minInseg=100.0
		maxInseg=0.0
		minOutseg=100.0
		maxOutseg=0.0
		avgInseg=0.0
		avgOutseg=0.0
		prevavgInseg=0.0
		prevavgOutseg=0.0
		minIndata=100.0
		maxIndata=0.0
		minOutdata=100.0
		maxOutdata=0.0
		avgIndata=0.0
		avgOutdata=0.0
		prevavgIndata=0.0
		prevavgOutdata=0.0
		count=0
		
		#call get_Network to get values of Network stats
		self.get_Network(cputotal,estContxt,actContxt,inTraffictxt,outTraffictxt,totNettxt,InSegtxt,OutSegtxt,InDatatxt,OutDatatxt,currEst,currAct,currUpstream,currDownstream,currOverall,currInseg,currOutseg,currIndata,currOutdata,prevInseg,prevOutseg,minInseg,maxInseg,minOutseg,maxOutseg,minIns,maxIns,minOuts,maxOuts,avgIns,avgOuts,avgInseg,avgOutseg,prevavgInseg,prevavgOutseg,count,prevIndata,prevOutdata,minIndata,maxIndata,minOutdata,maxOutdata,minInd,maxInd,minOutd,maxOutd,avgInd,avgOutd,avgIndata,avgOutdata,prevavgIndata,prevavgOutdata)

	def get_CPU(self,cputotal,prevUsr,prevSys,currUsr,currSys,cpulbltxt1,cpulbltxt2,usrlbltxt1,usrlbltxt2,syslbltxt1,syslbltxt2,totlbltxt1,totlbltxt2,minCputxt,maxCputxt,minCpu,maxCpu,count,prevavg,curravg,avgTxt):	
		interval=3000
		cpuUsrmode=0.0
		cpuSysmode=0.0
		cpuUtil=0.0
		totcpuUsrmode=0.0
		totcpuSysmode=0.0
		totcpuUtil=0.0
		prevIdle=0.0
		currIdle=0.0
		previowait=0.0
		curriowait=0.0		
		
		global list1
		list1=defaultdict(list)
		#fetch values from /proc/stat file for each CPU
		for cpunum in range(0,cputotal):		
			p=subprocess.Popen("cat /proc/stat|grep cpu", stdout=subprocess.PIPE,shell=True)
			(cpustat1, err)=p.communicate()
			cpustat=cpustat1.split()
			cpuName,usrmode,sysmode,idletime,iowait,irq,softirq=(cpustat[0],float(cpustat[1]),float(cpustat[3]),float(cpustat[4]),float(cpustat[5]),float(cpustat[6]),float(cpustat[7]))		
			currUsr[cpunum]=usrmode
			currSys[cpunum]=sysmode

			cpuUsrmode=round(((currUsr[cpunum]-prevUsr[cpunum])/interval)*100,2)
			cpuSysmode=round(((currSys[cpunum]-prevSys[cpunum])/interval)*100,2)
			
			cpuUtil=round((cpuUsrmode+cpuSysmode),2)
			totcpuUsrmode+=cpuUsrmode
			totcpuSysmode+=cpuSysmode
			totcpuUtil+=cpuUtil

			cpulbltxt1.set(bytes.decode(cpustat[0]))
			usrlbltxt1.set(cpuUsrmode)
			syslbltxt1.set(cpuSysmode)
			totlbltxt1.set(cpuUtil)
			cpulbltxt2.set(bytes.decode(cpustat[11]))
			usrlbltxt2.set(totcpuUsrmode)
			syslbltxt2.set(totcpuSysmode)
			totlbltxt2.set(round(totcpuUtil,2))
			#calculate min, max, avg
			if(cpuUtil<minCpu):
				minCpu=totcpuUtil
			if(cpuUtil>maxCpu):
				maxCpu=totcpuUtil
			minCputxt.set(round(minCpu,2))
			maxCputxt.set(round(maxCpu,2))
			
			curravg=(((cpuSysmode*count)+(prevavg))/(count+1))
			avgTxt.set(round(curravg,2))
			prevavg=curravg
			
			prevUsr[cpunum]=currUsr[cpunum]
			prevSys[cpunum]=currSys[cpunum]

			count=count+1	
		self.top_1.after(interval,self.get_CPU,cputotal,prevUsr,prevSys,currUsr,currSys,cpulbltxt1,cpulbltxt2,usrlbltxt1,usrlbltxt2,syslbltxt1,syslbltxt2,totlbltxt1,totlbltxt2,minCputxt,maxCputxt,minCpu,maxCpu,count,prevavg,curravg,avgTxt)

	def get_Intr(self,cputotal,prevIntr,currIntr,intrlbltxt):
		interval=3000
		#fetch values for interrupts
		for cpunum in range(0,cputotal):	
			p=subprocess.Popen("cat /proc/stat|grep intr", stdout=subprocess.PIPE, shell=True)
			(intrnum, err)=p.communicate()
			intrnum_split=intrnum.split()	
			currIntr[cpunum]=float(intrnum_split[1])
			counterIntr=round((currIntr[cpunum]-prevIntr[cpunum]),2)	
			intrlbltxt.set(str(counterIntr))
			self.top_1.after(interval,self.get_Intr,cputotal,prevIntr,currIntr,intrlbltxt)

	def get_Cnsw(self,cputotal,prevCnsw,currCnsw,cnswlbltxt):
		interval=3000
		#fetch values for context switches
		for cpunum in range(0,cputotal):
			p=subprocess.Popen("cat /proc/stat|grep ctxt", stdout=subprocess.PIPE, shell=True)
			(cnswnum, err)=p.communicate()
			cnswnum_split=cnswnum.split()
			currCnsw[cpunum]=float(cnswnum_split[1])
			counterCnsw=round((currCnsw[cpunum]-prevCnsw[cpunum]),2)
			cnswlbltxt.set(str(counterCnsw))
			prevCnsw[cpunum]=currCnsw[cpunum]
			self.top_1.after(interval,self.get_Cnsw,cputotal,prevCnsw,currCnsw,cnswlbltxt)
			
	def get_Mem(self,cputotal,prevAvmem,currAvmem,prevTotmem,currTotmem,avmemlbltxt,totmemlbltxt,memutillbltxt):			
		interval=3000
		#fetch values for memory stats from /proc/meminfo
		for cpunum in range(0,cputotal):
			p=subprocess.Popen("cat /proc/meminfo|grep MemFree", stdout=subprocess.PIPE, shell=True)			
			(avmem, err)=p.communicate()
			avmem_split=avmem.split()		
			currAvmem[cpunum]=(int(avmem_split[1]))/1024
			counterAvmem=round((currAvmem[cpunum]-prevAvmem[cpunum]),2)
			avmemlbltxt.set(str(counterAvmem))

			p=subprocess.Popen("cat /proc/meminfo|grep MemTotal", stdout=subprocess.PIPE, shell=True)
			(totmem, err)=p.communicate()
			totmem_split=totmem.split()
			currTotmem[cpunum]=(int(totmem_split[1]))/1024
			counterTotmem=round((currTotmem[cpunum]-prevTotmem[cpunum]),2)
			totmemlbltxt.set(str(counterTotmem))

			diff_mem=currTotmem[cpunum]-currAvmem[cpunum]
			memutil=float(round((diff_mem*100)/currTotmem[cpunum],2))
			memutillbltxt.set(str(memutil))

			self.top_1.after(interval,self.get_Mem,cputotal,prevAvmem,currAvmem,prevTotmem,currTotmem,avmemlbltxt,totmemlbltxt,memutillbltxt)

	def get_IO(self,cputotal,readstxt,blkreadstxt,writestxt,blkwritestxt,currReads,currBlocksread,currWrites,currBlockswrite,prevReads,prevBlocksread,prevWrites,prevBlockswrite,minReads,maxReads,minBlocksread,maxBlocksread,minWrites,maxWrites,minBlockswrites,maxBlockswrites,minRd,maxRd,minBRd,maxBRd,minWr,maxWr,minBWr,maxBWr,avgRd,avgBRd,avgWr,avgBWr,curravgRd,prevavgRd,curravgBRd,prevavgBRd,curravgWr,prevavgWr,curravgBWr,prevavgBWr,count):
		interval=3000
		#fetch values of Disk IO from /proc/diskstats
		for cpunum in range(0,cputotal):
			p= subprocess.Popen("cat /proc/diskstats|grep sda", stdout=subprocess.PIPE,shell=True)
			(io, err) = p.communicate()
			io_1=io.split()
			reads,blocksRead,writes,blocksWrite= (int(io_1[3]),int(io_1[5]),int(io_1[7]),int(io_1[9]))
			
			currReads[0]=round(((reads-prevReads[0])/interval),2)
			currBlocksread[0]=round(((blocksRead-prevBlocksread[0])/interval),2)
			currWrites[0]=round(((writes-prevWrites[0])/interval),2)
			currBlockswrite[0]=round(((blocksWrite-prevBlockswrite[0])/interval),2)
			readstxt.set(str(currReads[0]))
			blkreadstxt.set(str(currBlocksread[0]))
			writestxt.set(str(currWrites[0]))
			blkwritestxt.set(str(currBlockswrite[0]))
			#calculate min,max,avg
			if(currReads[0]<minReads):
				minReads=currReads[0]				
			if(currReads[0]>maxReads):
				maxReads=currReads[0]
			if(currBlocksread[0]<minBlocksread):
				minBlocksread=currBlocksread[0]				
			if(currBlocksread[0]>maxBlocksread):
				maxBlocksread=currBlocksread[0]			
			if(currWrites[0]<minWrites):
				minWrites=currWrites[0]				
			if(currWrites[0]>maxWrites):
				maxWrites=currWrites[0]
			if(currBlockswrite[0]<minBlockswrites):
				minBlockswrites=currBlockswrite[0]				
			if(currBlockswrite[0]>maxBlockswrites):
				maxBlockswrites=currBlockswrite[0]
			
			curravgRd=(((currReads[0]*count)+(prevavgRd))/(count+1))
			avgRd.set(round(curravgRd,2))
			prevavgRd=curravgRd
			
			curravgBRd=(((currBlocksread[0]*count)+(prevavgBRd))/(count+1))
			avgBRd.set(round(curravgBRd,2))
			prevavgBRd=curravgBRd
			
			curravgWr=(((currWrites[0]*count)+(prevavgWr))/(count+1))
			avgWr.set(round(curravgWr,2))
			prevavgWr=curravgWr
			
			curravgBWr=(((currBlockswrite[0]*count)+(prevavgBWr))/(count+1))
			avgBWr.set(round(curravgBWr,2))
			prevavgBWr=curravgBWr
						
			minRd.set(minReads)
			maxRd.set(maxReads)
			minBRd.set(minBlocksread)
			maxBRd.set(maxBlocksread)
			minWr.set(minWrites)
			maxWr.set(maxWrites)
			minBWr.set(minBlockswrites)
			maxBWr.set(maxBlockswrites)
			prevReads[0]=reads
			prevBlocksread[0]=currBlocksread[0]
			prevWrites[0]=currWrites[0]
			prevBlockswrite[0]=currBlockswrite[0]	
			count=count+1		
		self.top_1.after(interval,self.get_IO,cputotal,readstxt,blkreadstxt,writestxt,blkwritestxt,currReads,currBlocksread,currWrites,currBlockswrite,prevReads,prevBlocksread,prevWrites,prevBlockswrite,minReads,maxReads,minBlocksread,maxBlocksread,minWrites,maxWrites,minBlockswrites,maxBlockswrites,minRd,maxRd,minBRd,maxBRd,minWr,maxWr,minBWr,maxBWr,avgRd,avgBRd,avgWr,avgBWr,curravgRd,prevavgRd,curravgBRd,prevavgBRd,curravgWr,prevavgWr,curravgBWr,prevavgBWr,count)

	def get_Network(self,cputotal,estContxt,actContxt,inTraffictxt,outTraffictxt,totNettxt,InSegtxt,OutSegtxt,InDatatxt,OutDatatxt,currEst,currAct,currUpstream,currDownstream,currOverall,currInseg,currOutseg,currIndata,currOutdata,prevInseg,prevOutseg,minInseg,maxInseg,minOutseg,maxOutseg,minIns,maxIns,minOuts,maxOuts,avgIns,avgOuts,avgInseg,avgOutseg,prevavgInseg,prevavgOutseg,count,prevIndata,prevOutdata,minIndata,maxIndata,minOutdata,maxOutdata,minInd,maxInd,minOutd,maxOutd,avgInd,avgOutd,avgIndata,avgOutdata,prevavgIndata,prevavgOutdata):		
		interval=3000
		for cpunum in range(0,cputotal):
			#TCP values
			p= subprocess.Popen("cat /proc/net/snmp|grep Tcp", stdout=subprocess.PIPE,shell=True)
			(nw, err) = p.communicate()
			nw_1=nw.split()
			est,act,insg,outsg= (float(nw_1[25]),float(nw_1[21]),float(nw_1[26]),float(nw_1[27]))
			currEst[cpunum]=float(est)
			currAct[cpunum]=float(act)
			currInseg[cpunum]=round(((insg-prevInseg[cpunum])/interval),2)
			currOutseg[cpunum]=round(((outsg-prevOutseg[cpunum])/interval),2)
			# calculate Min, max, avg
			if(currInseg[cpunum]<minInseg):
				minInseg=currInseg[cpunum]				
			if(currInseg[cpunum]>maxInseg):
				maxInseg=currInseg[cpunum]
			if(currOutseg[cpunum]<minOutseg):
				minOutseg=currOutseg[cpunum]				
			if(currOutseg[cpunum]>maxOutseg):
				maxOutseg=currOutseg[cpunum]
			minIns.set(minInseg)
			maxIns.set(maxInseg)
			minOuts.set(minOutseg)
			maxOuts.set(maxOutseg)
			
			avgInseg=(((currInseg[cpunum]*count)+(prevavgInseg))/(count+1))
			avgIns.set(round(avgInseg,2))
			prevavgInseg=avgInseg
			
			avgOutseg=(((currOutseg[cpunum]*count)+(prevavgOutseg))/(count+1))
			avgOuts.set(round(avgOutseg,2))
			prevavgOutseg=avgOutseg

			prevInseg[cpunum]=currInseg[cpunum]
			prevOutseg[cpunum]=currOutseg[cpunum]	
		
			#UDP values
			p=subprocess.Popen("cat /proc/net/snmp|grep Udp", stdout=subprocess.PIPE,shell=True)
			(nw1, err) = p.communicate()
			nw1_1=nw1.split()
			inData,outData= (float(nw1_1[10]),float(nw1_1[13]))
			currIndata[cpunum]=round(((inData-prevIndata[cpunum])/interval),2)
			currOutdata[cpunum]=round(((inData-prevOutdata[cpunum])/interval),2)
			# calculate Min, max, avg
			if(currIndata[cpunum]<minIndata):
				minIndata=currIndata[cpunum]				
			if(currIndata[cpunum]>maxIndata):
				maxIndata=currIndata[cpunum]
			if(currOutdata[cpunum]<minOutdata):
				minOutdata=currOutdata[cpunum]				
			if(currOutdata[cpunum]>maxOutdata):
				maxOutdata=currOutdata[cpunum]
			minInd.set(minIndata)
			maxInd.set(maxIndata)
			minOutd.set(minOutdata)
			maxOutd.set(maxOutdata)

			avgIndata=(((currIndata[cpunum]*count)+(prevavgIndata))/(count+1))
			avgInd.set(round(avgIndata,2))
			prevavgIndata=avgIndata
			
			avgOutdata=(((currOutdata[cpunum]*count)+(prevavgOutdata))/(count+1))
			avgOutd.set(round(avgOutdata,2))
			prevavgOutdata=avgOutdata

			prevIndata[cpunum]=currIndata[cpunum]
			prevOutdata[cpunum]=currOutdata[cpunum]
			
			#IP values
			p= subprocess.Popen("cat /proc/net/snmp|grep Ip", stdout=subprocess.PIPE,shell=True)
			(nw_2, err) = p.communicate()
			nw_3=nw_2.split()
			inReceives,OutRequests= (float(nw_3[22]),float(nw_3[30]))
			overall=inReceives+OutRequests
			
			p= subprocess.Popen("cat /proc/net/dev|grep eth0", stdout=subprocess.PIPE,shell=True)
			(nw_4, err) = p.communicate()
			nw_5=nw_4.split()
			rxBytes,txBytes=(float(nw_5[1]),float(nw_5[9]))
			totBytes=rxBytes+txBytes
			currDownstream[cpunum]=round((inReceives*100)/rxBytes,2)
			currUpstream[cpunum]=round((OutRequests*100)/txBytes,2)
			currOverall[cpunum]=round((overall*100)/totBytes,2)
	
			estContxt.set(str(currEst[cpunum]))
			actContxt.set(str(currAct[cpunum]))
			InSegtxt.set(str(currInseg[cpunum]))
			OutSegtxt.set(str(currOutseg[cpunum]))
			InDatatxt.set(str(currIndata[cpunum]))
			OutDatatxt.set(str(currOutdata[cpunum]))
			inTraffictxt.set(str(currDownstream[cpunum]))
			outTraffictxt.set(str(currUpstream[cpunum]))
			totNettxt.set(str(currOverall[cpunum]))
			count=count+1	
		self.top_1.after(interval,self.get_Network,cputotal,estContxt,actContxt,inTraffictxt,outTraffictxt,totNettxt,InSegtxt,OutSegtxt,InDatatxt,OutDatatxt,currEst,currAct,currUpstream,currDownstream,currOverall,currInseg,currOutseg,currIndata,currOutdata,prevInseg,prevOutseg,minInseg,maxInseg,minOutseg,maxOutseg,minIns,maxIns,minOuts,maxOuts,avgIns,avgOuts,avgInseg,avgOutseg,prevavgInseg,prevavgOutseg,count,prevIndata,prevOutdata,minIndata,maxIndata,minOutdata,maxOutdata,minInd,maxInd,minOutd,maxOutd,avgInd,avgOutd,avgIndata,avgOutdata,prevavgIndata,prevavgOutdata)

	def ProcStat(self):
		#create frame for process and user tab
		self.root.wm_title("User and Process Statistics")
		self.root.geometry("900x500")
		self.top.grid_forget()
		global top_3
		self.top_3=Frame(self.root)
		self.top_3.grid(row=1,column=1)
		#call Proc() to create treeview and Entrybox
		self.Proc()
		self.exituserStatbtn=Button(self.top_3,text="Back to Main", command=self.back_Main3).grid(row=25,column=0,sticky="w",padx=1,pady=1)
		
	def Proc(self):
		#create the treeview for process tab
		p_id = {}
		p_uname = {}
		p_prior = {}
		p_nice = {}
		p_vir = {}
		p_rss = {}
		p_state = {}
		p_usertime = {}
		p_systime = {}
		prev_usertime = {}
		prev_systime = {}
		p_time = {}
		p_filename = {}
		p_cpuutil = {}
		p_memutil = {}
		interval = 3000
		iteration =0
		
		#get username from the Entrybox
		self.inputtab=Frame(self.top_3)		
		self.uname_input=StringVar()
		self.uname_lbl = Label(self.inputtab,text="Enter User Name").grid(row=1,column=0)
		unametxt=Entry(self.inputtab,textvariable=self.uname_input).grid(row=1,column=1)
		#get process name from the Entrybox
		self.pname_input=StringVar()
		self.pname_lbl = Label(self.inputtab,text="Enter Process Name").grid(row=2,column=0)
		pnametxt=Entry(self.inputtab,textvariable=self.pname_input).grid(row=2,column=1)
		#display treeview
		self.procframe=Frame(self.top_3)
		self.proctree=ttk.Treeview(self.procframe, show="headings",height=20)
		p_vscroll = Scrollbar(self.procframe, orient = VERTICAL, command = self.proctree.yview)
		p_vscroll.pack(fill = Y, side = RIGHT)
		self.proctree['yscrollcommand'] = p_vscroll.set

		self.proctree["columns"]=("pid","uname","priority","nice","virt","rss","state","cpuutil","memutil","time","pname")

		self.proctree.column("pid", anchor=S, width=40)
		self.proctree.column("uname", anchor=S, width=90)
		self.proctree.column("priority", anchor=S, width=70)
		self.proctree.column("nice", anchor=S, width=40)
		self.proctree.column("virt", anchor=S, width=100)
		self.proctree.column("rss", anchor=S, width=50)
		self.proctree.column("state", anchor=S, width=50)
		self.proctree.column("cpuutil", anchor=S, width=100)
		self.proctree.column("memutil", anchor=S, width=120)
		self.proctree.column("time", anchor=S, width=100)
		self.proctree.column("pname", anchor=S, width=100)

		self.proctree.heading("pid", text="PID")
		self.proctree.heading("uname", text="UNAME")
		self.proctree.heading("priority", text="PRIORITY")
		self.proctree.heading("nice", text="NICE")
		self.proctree.heading("virt", text="V. MEMORY")
		self.proctree.heading("rss", text="RSS")
		self.proctree.heading("state", text="STATE")
		self.proctree.heading("cpuutil", text="CPU UTIL.%")
		self.proctree.heading("memutil", text="MEMORY UTIL.%")
		self.proctree.heading("time", text="TIME")

		self.proctree.pack(fill = BOTH)
		self.inputtab.grid(row=1,column=0)
		self.procframe.grid(row=3,column=0)
		#call get_Proc() to fill values in treeview
		self.get_Proc(p_id,p_uname,p_prior,p_nice,p_vir,p_rss,p_state,p_usertime,p_systime,prev_usertime,prev_systime,p_time,p_filename,p_cpuutil,p_memutil,interval,iteration)

	def get_Proc(self,p_id,p_uname,p_prior,p_nice,p_vir,p_rss,p_state,p_usertime,p_systime,prev_usertime,prev_systime,p_time,p_filename,p_cpuutil,p_memutil,interval,iteration):
		#get uname and pname from user input box
		uname_in=self.uname_input.get()
		pname_in=self.pname_input.get()		
		#fetch all values
		fd=open('/proc/meminfo','r')
		for line in fd:
			meminfo = line.split()
			if meminfo[0].find("MemTotal")!=-1:
				tot_mem=int(meminfo[1])
		fd.close()
		#create list of all pids
		pids=[pid for pid in os.listdir('/proc') if pid.isdigit()]
		for pid in pids:
			try:
				f=open(os.path.join('/proc',pid,'stat'),'r')
				file1=os.stat("/proc/%d" %int(pid))
				uid=file1.st_uid
				uname=pwd.getpwuid(uid)[0]
				
				for line in f:
					procstat=line.split()
					p_id[pid] = [procstat[0]]
					p_uname[pid] = [uname]
					p_prior[pid] = [procstat[17]]
					p_nice[pid] = [procstat[18]]
					p_vir[pid] = [int(procstat[22])/1024]
					p_rss[pid] = [(int(procstat[23]))*4096/1024]
					p_state[pid] = [procstat[2]]
					p_usertime[pid] = [float(procstat[13])]
					p_systime[pid] = [float(procstat[14])]
					p_time[pid] = [procstat[21]]
					temp = procstat[1][1:]
					p_filename[pid] = [temp[0:-1]]
					#calculate usertime and systemtime
					if (iteration == 0):
						prev_usertime[pid] = [0]
						prev_systime[pid] = [0]
						p_cpuutil[pid] = [round(((p_systime[pid][0] + p_usertime[pid][0])/interval),3)]
					
					if ((prev_usertime.get(pid) == None) or (prev_systime.get(pid) == None)):
						prev_usertime[pid] = [0]
						prev_systime[pid] = [0]
						p_cpuutil[pid] = [round(((p_systime[pid][0] + p_usertime[pid][0])/interval),3)]
					
					else:
						p_cpuutil[pid] = [round(((p_systime[pid][0] - prev_systime[pid][0] + p_usertime[pid][0] - prev_usertime[pid][0])/interval),3)]
						prev_usertime[pid] = [p_usertime[pid][0]]
						prev_systime[pid] = [p_systime[pid][0]]

					p_memutil[pid] = [round((p_rss[pid][0]*100/tot_mem),4)]
			except IOError:
                		continue
		pids.clear()
		#calculate CPU utilization
		sorted_cpuutil = []
		sorted_cpuutil = sorted(p_cpuutil.items(), key = operator.itemgetter(1), reverse = True)
		i=0
		#clear treeview before repopulating
		self.proctree.delete(*self.proctree.get_children())
		#populate treeview with values
		for onetuple in sorted_cpuutil:
			key, value = onetuple
			#check for user entry and populate specific results
			if (p_uname[key][0].startswith(uname_in) == True) and (p_filename[key][0].startswith(pname_in) == True):
				Found = True
				self.proctree.insert("", i, value=(p_id[key][0],p_uname[key][0],p_prior[key][0],p_nice[key][0],p_vir[key][0],p_rss[key][0],p_state[key][0],p_cpuutil[key][0],p_memutil[key][0],p_time[key][0],p_filename[key][0]))
				i = i + 1
		sorted_cpuutil.clear()
		f.close()
		self.procframe.after(interval,self.get_Proc,p_id,p_uname,p_prior,p_nice,p_vir,p_rss,p_state,p_usertime,p_systime,prev_usertime,prev_systime,p_time,p_filename,p_cpuutil,p_memutil,interval,iteration)

	def NetStat(self):
		#create network tab
		self.root.wm_title("Network Statistics")
		self.root.geometry("800x500")
		self.top.grid_forget()
		global top_4
		self.top_4=Frame(self.root)
		self.top_4.grid(row=1,column=1)
		#call Net to create treeview and entry box
		self.Net()
		self.exituserStatbtn=Button(self.top_4,text="Back to Main", command=self.back_Main4).grid(row=4,column=0,sticky="w",padx=1,pady=1)
		
	def Net(self):		
		#create entry boxes and treeview for Network Stats
		localPortNum = {}
		localIpAdd = {}
		remoteIpAdd = {}
		remotePortNum = {}
		uid = {}
		uname = {}
		interval=3000
		iteration=0
		
		self.inputtab=Frame(self.top_4)				
		self.uname_input=StringVar()
		self.uname_lbl = Label(self.inputtab,text="Enter User Name").grid(row=1,column=0)
		unametxt=Entry(self.inputtab,textvariable=self.uname_input).grid(row=1,column=1)
		
		self.netframe=Frame(self.top_4)
		self.nettree=ttk.Treeview(self.netframe, show="headings",height=20)
		n_vscroll = Scrollbar(self.netframe, orient = VERTICAL, command = self.nettree.yview)
		n_vscroll.pack(fill = Y, side = RIGHT)
		self.nettree['yscrollcommand'] = n_vscroll.set
		
		self.nettree["columns"]=("uname", "localip","localport","remoteip","remoteport")
		self.nettree.column("uname", anchor=S, width=90)
		self.nettree.column("localip", anchor=S, width=150)
		self.nettree.column("localport", anchor=S, width=100)
		self.nettree.column("remoteip", anchor=S, width=150)
		self.nettree.column("remoteport", anchor=S, width=120)

		self.nettree.heading("uname", text = "Username", anchor=S)
		self.nettree.heading("localip", text = "Local IP Address", anchor=S)
		self.nettree.heading("localport", text = "Local Port No.", anchor=S)
		self.nettree.heading("remoteip", text = "Remote IP Address", anchor=S)
		self.nettree.heading("remoteport", text = "Remote Port No.", anchor=S)

		self.nettree.pack(fill = BOTH)
		self.inputtab.grid(row=1,column=0)
		self.netframe.grid(row=3,column=0)
		#call get_Net to fetch and populate treeview
		self.get_Net(localPortNum,localIpAdd,remoteIpAdd,remotePortNum,uid,uname,interval,iteration)

	def get_Net(self,localPortNum,localIpAdd,remoteIpAdd,remotePortNum,uid,uname,interval,iteration):
		#fetch user input
		uname_in = self.uname_input.get()
		#get tcp info
		f = open('/proc/net/tcp','r')
		for line in f:
			net1 = line.split()
			if net1[0][0:1].isdigit():
				key = net1[0][0:1]
				uid[key] = net1[7]
				HexlocalIpAdd = net1[1][:8]
				IntlocalIpAdd = "%i.%i.%i.%i"%(int(HexlocalIpAdd[0:2],16),int(HexlocalIpAdd[2:4],16),int(HexlocalIpAdd[4:6],16),int(HexlocalIpAdd[6:8],16))
				localIpAdd[key] = [IntlocalIpAdd]
				localPortNum[key] = [net1[1][9:]]
				HexForeignIp = net1[2][:8]
				IntForeignIp = "%i.%i.%i.%i"%(int(HexForeignIp[0:2],16),int(HexForeignIp[2:4],16),int(HexForeignIp[4:6],16),int(HexForeignIp[6:8],16))
				remoteIpAdd[key] = [IntForeignIp]
				remotePortNum[key] = [net1[2][9:]]
				#fetch username and uid lists
				uidlist = uid.values()
				for u in uidlist:
					unamelist = (pwd.getpwuid(int(u)))
					uname[key] = [unamelist[0]]
		i = 0
		#clear treeview before repopulating treeview
		self.nettree.delete(*self.nettree.get_children())
		#populate fetched values in treeview
		for akey in uid.keys():
			#check the user input
			if uname[akey][0].startswith(uname_in) == True:
				self.nettree.insert("",i, value=(uname[akey][0],localIpAdd[akey][0],localPortNum[akey][0],remoteIpAdd[akey][0],remotePortNum[akey][0]))
				i = i + 1
		f.close()
		self.netframe.after(interval,self.get_Net,localPortNum,localIpAdd,remoteIpAdd,remotePortNum,uid,uname,interval,iteration)

	def FileStat(self):
		#create File tab
		self.root.wm_title("File Statistics")
		self.root.geometry("800x500")
		self.top.grid_forget()
		global top_5
		self.top_5=Frame(self.root)
		self.top_5.grid(row=1,column=1)
		#call File to create treeview
		self.File()
		self.exituserStatbtn=Button(self.top_5,text="Back to Main", command=self.back_Main5).grid(row=25,column=0,sticky="w",padx=1,pady=1)
		
	def File(self):
		#create treeview for File stats
		interval=3000
		iteration=0
		
		self.inputtab=Frame(self.top_5)		
		self.uname_input=StringVar()
		self.uname_lbl = Label(self.inputtab,text="Enter User Name").grid(row=1,column=0)
		unametxt=Entry(self.inputtab,textvariable=self.uname_input).grid(row=1,column=1)
		
		self.fileframe=Frame(self.top_5)		
		self.filetree = ttk.Treeview(self.fileframe, show = "headings", height = 20)
		f_vscroll = Scrollbar(self.fileframe, orient = VERTICAL, command = self.filetree.yview)
		f_vscroll.pack(fill = Y, side = RIGHT)
		self.filetree['yscrollcommand'] = f_vscroll.set

		self.filetree["columns"]=("pid","uname","filepath","timestamp")
		
		self.filetree.column("pid", anchor=S, width=75)
		self.filetree.column("uname", anchor=S, width=100)
		self.filetree.column("filepath", anchor=S, width=500)
		self.filetree.column("timestamp", anchor=S, width=75)

		self.filetree.heading("pid", text="Process ID",anchor=S)
		self.filetree.heading("uname", text="Username")
		self.filetree.heading("filepath", text="File Path")
		self.filetree.heading("timestamp", text="Time Stamp")

		self.filetree.pack(fill = BOTH)
		self.inputtab.grid(row=1,column=0)
		self.fileframe.grid(row=3,column=0)
		#call get_File to fetch values for treeview
		self.get_File(interval,iteration)
	
	def get_File(self,interval,iteration):
		#get user input
		uname_in = self.uname_input.get()
		i = 0
		#clear treeview before repopulating the treeview
		self.filetree.delete(*self.filetree.get_children())
		#fetch list of all pids
		pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
		for p in pids:
			with os.popen("ls -l /proc/" + p + "/fd") as fd:
				for line in fd.readlines():
					filestat1 = line.split()
					if filestat1[0].startswith("total")== False and (filestat1[10].startswith('socket') == False) and (filestat1[10].startswith('pipe') == False):
						f_time = filestat1[7]
						f_uname = filestat1[2]
						f_fname = filestat1[10]
						f_pid = p
			#check for user input
			if f_uname.startswith(uname_in) == True:
				self.filetree.insert("", i, value = (f_pid, f_uname, f_fname, f_time))
				i = i + 1

		self.fileframe.after(interval,self.get_File,interval,iteration)

	#Return button from CPU stats
	def back_Main(self):
		self.top.grid_forget()
		self.top_1.destroy()
		self.create()

	'''def back_Main2(self):
		self.top.grid_forget()
		self.top_2.destroy()
		self.create()'''
	#Return button from Process Stat
	def back_Main3(self):
		self.top.grid_forget()
		self.top_3.destroy()
		self.create()
		
	#Return button from Network Stat
	def back_Main4(self):
		self.top.grid_forget()
		self.top_4.destroy()
		self.create()

	#Return button from File Stat
	def back_Main5(self):
		self.top.grid_forget()
		self.top_5.destroy()
		self.create()

	def main(self):
		self.root.mainloop()

task = Task()
task.main()
