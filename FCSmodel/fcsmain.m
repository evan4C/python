% fcsmain.m
% Main file for U of M Fuel Cell Stack Simulation package.
% The FCS simulink model is created in Matlab 6.5

% add paths
addpath('setpoints')
addpath('data')

% Load parameters
fcsdata

% Open Simulink model
fcsystem

% output variables are named with out in the beginning
% to list the variables use command 
% >> who out*

% plant state vector is output in variable 'plantstates'
% to find steady-state value use command
% >> ssstates = outstates(end,:)