% fcsplot.m
% plot simulation results

% output variables are named with out in the beginning
% to list the variables use command 
% >> who out*


figure(11)
subplot(211)
plot(outtime,outSTcurrent)
xlabel('Time (sec)'); ylabel('Stack Current (A)')
subplot(212)
plot(outtime,outCMvoltage)
xlabel('Time (sec)'); ylabel('Compressor Motor Voltage (V)')

figure(12)
subplot(211)
plot(outtime,outSTvoltage)
xlabel('Time (sec)'); ylabel('Stack Voltage (V)')
subplot(212)
plot(outtime,outO2excessratio)
xlabel('Time (sec)'); ylabel('Oxygen Excess Ratio')

figure(13)
subplot(211)
plot(outtime,outSTpower/1000)
xlabel('Time (sec)'); ylabel('Stack Power (kW)')
subplot(212)
plot(outtime,outNETpower/1000)
xlabel('Time (sec)'); ylabel('Net Power (kW)')
