#!/usr/bin/env python3
################################################################################
# Abstract:
# A wrapper for oauth2_proxy
#
# Description:
#
#
# Copyright (c) 2015 Dragon Law
# Project: Dragon Law Data Manager
# Creation: Lingxiao Xia
# Creation Date: 18/05/2015
################################################################################
import os, subprocess, time, argparse, string, random, fileinput, sys, signal
from datetime import datetime

def cookie_id_generator(size=32, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

class oauth2_proxy_handler():
    def __init__(self,proxy,configFile,logFile):
        self.proxy = proxy
        self.configFile = configFile
        self.logFile = logFile
        
    def cookie_setter(self):
        session_id = ''
        with fileinput.input(self.configFile,inplace=1) as f:
            for line in f:
                if 'cookie_secret = ' in line:
                    session_id = cookie_id_generator()
                    line = 'cookie_secret = "'+session_id+'"\n'
                sys.stdout.write(line)
        return session_id
                
    def run(self):
        session_id = self.cookie_setter()
        with open(self.logFile, 'a+') as log:
            rightNow = datetime.now()
            timestamp = str(rightNow.year).zfill(4)+'/'+str(rightNow.month).zfill(2)+'/'+str(rightNow.day).zfill(2)+' '+str(rightNow.hour).zfill(2)+':'+str(rightNow.minute).zfill(2)+':'+str(rightNow.second).zfill(2)
            log.write(timestamp+' Logging session with id: '+session_id+'\n')
            log.flush()
            self.proc = subprocess.Popen(self.proxy+' -config="'+self.configFile+'"',shell=True, stdout=log, stderr=log, preexec_fn=os.setsid)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('proxy', metavar="PROXY", nargs = '?', default ='', help = "Location of oauth2_proxy binary.")
    parser.add_argument('configFile', metavar="CFG_FILE", nargs = '?', default ='', help = "Configuration file for oauth2_proxy")
    parser.add_argument('logFile', metavar="LOG_FILE", nargs = '?', default ='', help = "Log file to write to for oauth2_proxy")
    args = parser.parse_args()
    oauth2_proxy_handler(args.proxy,args.configFile,args.logFile).run()
        
        
        
        
        
        
        
        
        
        
        
        
        
