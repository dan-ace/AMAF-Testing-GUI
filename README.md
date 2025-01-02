# AMAF-Testing-GUI

To make electrical testing easier hopefully

# Requirements before starting

This GUI needs a python version with tkinter installed with it, as well as the customtkinter
package installed through pip. Python3.11 with the most recent version of customtkinter is 
recommended. Some testsetups don't have tkinter installed with python, so I'll have to 
figure out how to install tkinter safely and document it here.

# How to download this GUI
```
git clone https://github.com/dan-ace/AMAF-Testing-GUI.git
```

Just download the folder called 'forGUI' into the ITk folder of the desired testsetup,
and it should have everything you need I guess.                                        
example:
```
/home/itktestsetupN/ITk/forGUI/
```
I hope to integrate this into the AMAF_ITkTesting repository in the future, but with
the way the GUI is right now, it doesn't really matter where you put the forGUI folder.
The gui uses absolute paths right now, so for now the user will have to replace 
'itktestsetupN' with the right name after downloading the folder

# How to start the GUI
```
cd /home/itktestsetupN/ITk/forGUI/             
python3.11 main.py 
```
# How to use the GUI

At the top of the window, there are several tabs you can choose from (YARR, MQT, DCS, etc.) 
that can be clicked to display different testing options

On the darker left-side area of the window, there are controls for hardware and interlocks. 
On the lighter area of the window, there are options to run YARR and MQT tests, as well as MQAT and
MQDT interactibility

# Interlocks

Clicking this tab will show interlock controls once they are functional (this is tricky so it may take
a while for me to figure out)

# DCS

Clicking this tab shows on/off switches for DCS hardware. Ideally on startup, the GUI will be able to 
tell what is on and what is off, and will be able to reflect that with the switches (say LV is already on once
the GUI is started up, then the switch will display as 'on' or in this case green). The tab will also show 
input boxes for you to type in desired voltage values, in case you need to change LV, HV, Peltier, Chiller values

# Source Control

Clicking this tab will show buttons for moving the source to any of the FE chips, or to the center of the module. 
There is also a button to put away the source

# YARR

In this tab, you have to select which module you are testing from a dropdown menu (ANL_ITkPix_N).
Then, you can check the boxes of whichever tests you want to run in one go. However, the tests are 
still divided up into MHT, TUN, and PFA for now, so you can't mix and match tests (like if you wanted 
run an MHT digital scan and a PFA noise scan in one go, for example.) Anyway, you should only use the checkboxes
you absolutely know what you're doing (since some tests require others done before it, some need HV on and some
don't, etc.)

There are green buttons that allow you to run a certain set of tests. For example, you can run all MHT tests with
the green "Run All MHT Tests" button. The inexperienced tester can use these buttons consecutively (MHT -> TUN -> PFA)
to complete all YARR tests without having to interact with the command line. However, the PFA options will be split into
two buttons (one for 'with source scan' and one for 'without source scan'. There is also a button to run ALL Yarr tests
(MHT, TUN, and PFA with source scan) in one go. 

If you choose to use the checkboxes to run tests, the order of the tests will go from first column (from top to bottom),
to second column (from top to bottom), then to third column (from top to bottom). I will try to make it so that you
can change the order of the tests you select (like the first one you click would have a '1' next to it, and the second
one will have a '2' next to it, and so on) but it will have to be added in the future.

# MQT

This tab will be similar to the YARR tab; MQT tests are shown in check boxes with the order running from top to bottom,
You can either only the test(s) you selected, or run all MQT tests in one go. However, running certain MQT tests requires 
changing Peltier voltage in order to keep the module in the target range (20 C for warm, -15 C for cold), so the "Run All 
Tests" button can only be run once a temperature regulation script is ready.

# MQAT

This tab will display options to interact with the Module QC Analysis Tools without having to work with the command line.
However, this tab won't be needed since, ideally, Local DB will do analysis on all data anyway. This tab is mainly for debugging 
purposes.

There will be options to do analysis on a certain set of MHT test runs, or a set of TUN test runs, or an MQT test, etc., in case 
the run that was performed wasn't uploaded to localdb
This won't really be needed for MQT tests though, since the MQT Test Running script that the GUI will use already has the
analysis being done after the run is finished.

# MQDT

This tab will display options to interact with the Module QC Database Tools without having to work with the command line.
There will be options to enabled/disable chips without having to open the connectivity file, download new configs (safely,
without overwriting previous configs for a module)

# Full QC

in the future, if there's time, there will be options in this tab to run stuff like thermal cycling, or different
sub-tabs for whichever stage the module is in. Then, you could just press a button and all tests for that stage will be done
automatically. 

# Disclaimer
Some of these functions may be too ambitious to be honest, but I'll do my best


