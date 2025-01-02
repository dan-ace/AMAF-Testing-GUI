import CommandExecuter as ex
from influxdb import InfluxDBClient
import time
import os

# Get the home directory
home_directory = os.path.expanduser('~')

client = InfluxDBClient()
measurement_name = 'RD53A-001-RealModule'
database_name = os.getenv('INFLUXDB_DCS')
query = f'SELECT * FROM "{measurement_name}" ORDER BY time DESC LIMIT 1'
dcsPath = '%s/ITk/anl_itk/DCSMonitoring'%(home_directory)
mqdtPath = '%s/ITk/module-qc-database-tools/module_data/'%(home_directory)    

def readLastPoint():
    # Perform the query
    results = client.query(query, database=database_name)
    return list(results.get_points())[-1]

def ANL_Modules_SN(moduleType, index):
    ANL_Modules = {
        # real modules
        'ANL_ITkPix_1': '20UPGM22110049',
        'ANL_ITkPix_2': '20UPGM22110394',
        'ANL_ITkPix_3': '20UPGM22110050',
        'ANL_ITkPix_4': '20UPGM22110573',
        'ANL_ITkPix_5': '20UPGM22110576',
        'ANL_ITkPix_6': '20UPGM22110391',
        'ANL_ITkPix_7': '20UPGM22110401',
        'ANL_ITkPix_8': '20UPGM22110407',
        'ANL_ITkPix_9': '20UPGM22110406',
        'ANL_ITkPix_10': '20UPGM22110405',
        'ANL_ITkPix_11': '20UPGM22110404',
        'ANL_ITkPix_12': '20UPIM12001049',
        'ANL_ITkPix_13': '20UPGM12001050',
        'ANL_ITkPix_14': '20UPIM12101259',
        'ANL_ITkPix_15': '20UPIM12110076',
        'ANL_ITkPix_16': '20UPGM12110001',
        'ANL_ITkPix_17': '20UPGM12110379',
        'ANL_ITkPix_18': '20UPGM12110378',
        'ANL_ITkPix_19': '20UPGM12110248',
        'ANL_ITkPix_20': '20UPGM12110246',
        'ANL_ITkPix_21': '20UPGM12110245',
        'ANL_ITkPix_22': '20UPGM12110004',
        'ANL_ITkPix_23': '20UPIM12602123',
        'ANL_ITkPix_24': '20UPIM12602173',
        'ANL_ITkPix_25': '20UPIM12602229',
        'ANL_ITkPix_26': '20UPIM12602218',
        'ANL_ITkPix_27': '20UPIM12602136',
        'ANL_ITkPix_28': '20UPIM12602013',
        'ANL_ITkPix_29': '20UPIM12602135',
        'ANL_ITkPix_30': '20UPIM12602249',
        'ANL_ITkPix_31': '20UPIM12602242',
        'ANL_ITkPix_32': '20UPIM12602123',
        'ANL_ITkPix_33': '20UPGM23602236',
        'ANL_ITkPix_34': '20UPGM23602126',
        'ANL_ITkPix_35': '20UPGM23602054',
        'ANL_ITkPix_36': '20UPGM23602014',
        'ANL_ITkPix_37': '20UPGM23602155',
        'ANL_ITkPix_38': '20UPGM23602238',
        'ANL_ITkPix_39': '20UPGM23602206',
        'ANL_ITkPix_40': '20UPGM23602031',
        # Japan modules itkpixv2                                                                                                                                                     
        'ANL_ITkPix_41': '20UPGM23603058',
        'ANL_ITkPix_42': '20UPGM23603055',
        'ANL_ITkPix_43': '20UPGM23603042',
        'ANL_ITkPix_44': '20UPGM23603040',
        'ANL_ITkPix_45': '20UPGM23603038',
        # digital modules
        'ANL_DIG_1': '20UPGR92101022',
    }

    moduleName = 'ANL_%s_%s'%(moduleType, index)
    return moduleName, ANL_Modules[moduleName]

def getDCS(scanType):
    # Continuous monitoring temperature
    while True:
        temp = readLastPoint()['temperature_moduleN']
        modulePower = readLastPoint()['LV_voltage']
        moduleCurrent = readLastPoint()['LV_current']
        hvPower = readLastPoint()['HV_voltage']
        hvCurrent = readLastPoint()['HV_current']
        isModulePowered = False
        if modulePower!=None and moduleCurrent!=None:
            if (float(modulePower)>0.0 and float(moduleCurrent)>0.0) or scanType=='IV-MEASURE':
                isModulePowered = True
                #print('Module power is on')
            else:
                print('Module power is off.', flush=True)
                isTurnOnLV = input('Do you want to turn on the module power?: [Y/N]\n')
                if isTurnOnLV=='Y':                    
                    ex.runCmdP('python3.6 %s/LVControl.py --poweron'%(dcsPath), False, 0)
                    #ex.runCmdP('python3.6 %s/LVControl.py --setcurrent \"2.1,6.60\"'%(dcsPath), False, 0)
                    #ex.runCmdP('python3.6 %s/LVControl.py --setcurrent \"2.1,4.41\"'%(dcsPath), False, 0)
                    ex.runCmdP('python3.6 %s/LVControl.py --setcurrent \"2.3,5.88\"'%(dcsPath), False, 0)
                    print('Checking if the module is powred on...')
                    time.sleep(5)
                    getDCS(scanType)
            if temp!=None and isModulePowered is True: break
    print('current temperature =   %s C'%temp)
    print("module voltage reading: %-5s [V] \t current reading: %-5s [A]"%(modulePower, moduleCurrent))
    print("HV voltage reading:     %-5s [V] \t current reading: %-5s [A]"%(hvPower, hvCurrent))
    if float(temp)<0.0:     tempStr = 'cold'
    else: tempStr = 'warm'
    if 'LP' in scanType or 'PROTECTION' in scanType: tempStr = 'LP'
    returnDic = {
        'tempStr': tempStr,
        'hvPower': hvPower,
        'hvCurrent': hvCurrent,        
    }
    return returnDic

def getConnectivity(mqdtPath, moduleSN, scanType):
    connectivity = '%s/%s/%s_L2_%s.json '%(mqdtPath, moduleSN, moduleSN, getDCS(scanType)['tempStr'])
    if ex.isFileExist(connectivity[:-1]) is False:
        print(connectivity+' does not exist. This module type is maybe L1 quad. Checking...')
        #print(ex.isFileExist(connectivity))
        connectivity = connectivity.replace('L2', 'L1')
    elif ex.isFileExist(connectivity[:-1]) is False:
        print(connectivity[:-1]+' does not exist neither. Check if the module config file exist.')
        ex.cdDir('%s/ITk/module-qc-database-tools'%(home_directory))
        ex.runCmd('source venv/bin/activate')
        ex.runCmd('generateYARRConfig -sn %s -o module_data'%(moduleSN))
        #ex.cdDir('%s/ITk/module-qc-database-tools'%(home_directory))
        #exit()                    
    return connectivity
        
def YARR_commandBuilder(moduleSN, scanType, addOption, moduleName):
    scanDic = {
        'digital': 'std_digitalscan.json',
        'analog': 'std_analogscan.json',
        'threshold': 'std_thresholdscan_hr.json',

        'tune_globalthreshold' : 'std_tune_globalthreshold.json',
        'thresholdscan_hr' : 'std_thresholdscan_hr.json',
        'totscan' : 'std_totscan.json',

        'tune_pixelthreshold' : 'std_tune_pixelthreshold.json',
        'retune_globalthreshold' : 'std_retune_globalthreshold.json',
        'retune_pixelthreshold' : 'std_retune_pixelthreshold.json',
        'thresholdscan_hd' : 'std_thresholdscan_hd.json',
        'thresholdscan_zerobias' : 'std_thresholdscan_zerobias.json',
        'noisescan' : 'std_noisescan.json',
        'discbumpscan': 'std_discbumpscan.json',
        'mergedbumpscan': 'std_mergedbumpscan.json',
        'selftrigger_source': 'selftrigger_source.json',
    }

    cmd = './bin/scanConsole ' if 'eye' not in scanType else './bin/eyeDiagram '
    cmd += '-r configs/controller/specCfg-rd53b-16x1.json '
    if 'eye' not in scanType:
        cmd += '-o data/%s '%(moduleName)

    connectivity = getConnectivity(mqdtPath, moduleSN, scanType)
        
    cmd += '-c %s'%(connectivity)
    if 'eye' not in scanType:
        cmd += '-s configs/scans/itkpixv2/%s '%(scanDic[scanType])
    if 'NONE' not in addOption: cmd += addOption
        
    return cmd

def RecoverConfig_commandBuilder(moduleSN, scanType, addOption, moduleName):
    connectivity = getConnectivity(mqdtPath, moduleSN, scanType)
    zeroBiaseOutputDir, creation_time = ex.get_last_created_subdirectory_info('data/%s'%moduleName)
    iszeroBiase = False
    for file in os.listdir(zeroBiaseOutputDir):
        # Check if 'zerobias' is in the file name
        if 'zerobias' in file.lower():
            iszeroBiase = True
            cmd = './bin/revert-chip-configs -c %s -d %s'%(connectivity, zeroBiaseOutputDir)
    if iszeroBiase is False:
        print ('\033[91mLast data was not zerobias scan.\033[0m')
        print ('Last folder: '%zeroBiaseOutputDir)
        exit()            
    return cmd

def MQT_commandBuilder(moduleSN, scanType, moduleName):
    config = 'src/module_qc_tools/data/configs/example_merged_vmux.json'
    tempstr = getDCS(scanType)['tempStr']
    connectivity = getConnectivity(mqdtPath, moduleSN, scanType)
    cmd = 'venv/bin/measurement-%s -c %s -m %s -o output/%s'%(scanType, config, connectivity, moduleName)
    
    return cmd, tempstr
    
def MQT_outputTaker(moduleName, runtype):
    outputPath = '%s/ITk/module-qc-tools/output/%s/Measurements/%s'%(home_directory, moduleName, runtype.replace('-','_'))
    #print (outputPath)
    outputDir, creation_time = ex.get_last_created_subdirectory_info(outputPath)
    print(f"Output directory is: {outputDir}")
    print(f"Creation time: {creation_time}")
    #outputDir = 'output/ANL_ITkPix_4/Measurements/ANALOG_READBACK/2024-01-19_090511'
    #module-qc-tools-upload --path output/Measurements/ADC_CALIBRATION/2024-01-18_152409/ --host 192.168.0.235 --port 80 --out output_an

    cmd_upload = 'venv/bin/module-qc-tools-upload --path %s --host 192.168.0.121 --port 80 --out output_an'%(outputDir)
    cmd_analysis = 'venv/bin/analysis-%s -i %s -o outputs/%s'%(runtype, outputDir, moduleName)

    return cmd_upload, cmd_analysis

def MQAT_outputTaker(moduleName, runtype, cmd):
    outputPath = '%s/ITk/module-qc-analysis-tools/outputs/%s/%s'%(home_directory, moduleName, runtype.replace('-','_'))
    #print (outputPath)
    outputDir, creation_time = ex.get_last_created_subdirectory_info(outputPath)
    print(f"Output directory is: {outputDir}")
    print(f"Creation time: {creation_time}")
    #outputDir = 'output/ANL_ITkPix_4/Measurements/ANALOG_READBACK/2024-01-19_090511'
    #module-qc-tools-upload --path output/Measurements/ADC_CALIBRATION/2024-01-18_152409/ --host 192.168.0.235 --port 80 --out output_an
    connectivity = cmd[cmd.find('-m')+len('-m '):cmd.rfind('json')+len('json')]
    connectivityPath = connectivity[:connectivity.rfind('/')]
    if 'L1' in connectivity:
        testType = connectivity[connectivity.rfind('L1'):-len('.json')]
    else:
        testType = connectivity[connectivity.rfind('L2'):-len('.json')]
    
    cmd_update = 'venv/bin/analysis-update-chip-config -i %s -c %s -t %s --override'%(outputDir, connectivityPath, testType)

    return cmd_update

def MQT_chipConfigUpdater():
    outputPath = '%s/ITk/module-qc-analysis-tools/outputs/%s/%s'%(home_directory, moduleName, runtype.replace('-','_'))
    #print (outputPath)
    outputDir, creation_time = ex.get_last_created_subdirectory_info(outputPath)
    print(f"Output directory is: {outputDir}")
    print(f"Creation time: {creation_time}")

    # analysis-update-chip-config -i outputs/ADC_CALIBRATION/2023-06-29_160842/ -c /home/itkpixsetup2/ITk/module-qc-database-tools/module_data/20UPGR92101022/ -t L2_warm
    cmd_chip_config_update = 'venv/bin/analysis-update-chip-config' # -i %s -o -c -t L1_%s'%()
    
    return cmd_chip_config_update

def HVcontrol(onoff, scanType):

    # check if HV power supply's I&V
    currentDCS = getDCS(scanType) 
    hvPower, hvCurrent = currentDCS['hvPower'], currentDCS['hvCurrent']
    hvPowerOnNorm, hvPowerOffNorm = 70, 0.8
    # HV voltage reading:     70.0  [V] 	 current reading: 0.676 [A]
    # HV voltage reading:     0.04 [V] 	 current reading: 0.003 [A]

    if onoff is 'ON':
        if (abs(hvPower)<hvPowerOnNorm):
            initialhv = max(abs(hvPower), 5)
            ex.runCmdP("python3.6 %s/HVControl.py --rampvoltage \" -5,0\""%(dcsPath), False, 0)
            ex.runCmdP('python3.6 %s/HVControl.py --setcurrent \" %f,0.000003\"'%(dcsPath, initialhv), False, 0)
            ex.runCmdP('python3.6 %s/HVControl.py --poweron'%(dcsPath), False, 0)
            time.sleep(10)
            print ('HV will be ramped up from %f to %f with step of 5V.'%(int(initialhv)+5, hvPowerOnNorm))
            for set_hv in range(int(initialhv)+5, hvPowerOnNorm+5, 5):
                ex.runCmdP('python3.6 %s/HVControl.py --setcurrent \" %f,0.000003\"'%(dcsPath, set_hv), False, 0)
                time.sleep(6)
        ex.runCmdP('python3.6 %s/HVControl.py --setcurrent \" %f,0.000003\"'%(dcsPath, hvPowerOnNorm), False, 0)
        currentDCS = getDCS(scanType)
        hvPower, hvCurrent = currentDCS['hvPower'], currentDCS['hvCurrent']
        if hvPower > (hvPowerOnNorm-3):
            print ('current HV = %.2f'%(hvPower))
            print ('\033[32mHV is fully ramped up\033[0m')            
        else:
            ex.runCmdP('python3.6 %s/HVControl.py --clearEvent'%(dcsPath), False, 0)
            print ('\033[91mHV was not ramped up. If you do not know how to resolve this, please, contact to experts.\033[0m')
            exit()
    if onoff is 'OFF':
        if (abs(hvPower)>hvPowerOffNorm):
            ex.runCmdP('python3.6 %s/HVControl.py --rampvoltage \" -1,0\"'%(dcsPath), False, 0)
            ex.runCmdP('python3.6 %s/HVControl.py --poweroff'%(dcsPath), False, 0)
            if (abs(hvPower)<5):
                ex.runCmdP('python3.6 %s/HVControl.py --rampvoltage \" -0.1,0\"'%(dcsPath), False, 0)
        while (abs(hvPower)>hvPowerOffNorm):
            time.sleep(30)
            currentDCS = getDCS(scanType)
            hvPower, hvCurrent = currentDCS['hvPower'], currentDCS['hvCurrent']
        print ('\033[32mHV is fully ramped down\033[0m')
