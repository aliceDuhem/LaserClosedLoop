# LaserClosedLoop


### Essential Libraries Needed:

> Ni-Visa <br />
> Visa <br />
> Guizero <br />
> ThorlabsPM100 <br />
> Pyusb <br />


### Codes needed to run (yet to interlink):

LaserControl<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  |-- ratioCodes (Mathematical algorithm returning angle closest to desired intensity) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  |-- GetPower (Initialise and read power meter values) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  |-- Motor_calibration (Motor calibration during power on) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  |-- characteristics (Class to hold specs of the system) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  |-- ControlCode (PID control)  <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  |-- App2 (UI for users to input desired intensity and optical properties of system) <br />

### Testing Functions:

LaserControl<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |<br />
&nbsp;&nbsp;&nbsp; Tests <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   | <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  |-- SaveDataCsv (Function to write output array into csv for analysis) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  |-- testDictCode (Tests dictionary to verify its theoretical functionality) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  |-- TestDictionaryWithPowerMeter (Tests interlinkage between dictionary and power meter) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  |-- findDifference (Tests mathematical rigour of dictionary codes) <br />

### Matlab commands to test theory:


MatlabStuff<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  | <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  |-- Jone1 (Made jones matrices in matlab and derived initial ratios) <br />
