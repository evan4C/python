% fcsdata.m

% *************************
% Fuel Cells(FC) data
% *************************
fc_numberofcells=381; % number of cells
fc_activearea=280; %300; %250; %507;   % Cell Active Area cm^2
% ** Anode *****
fc_anode_volume=0.005; % Anode total volume (whole stack) (m^3)
fc_anode_outlet_flow_constant=3.932009958952965e-9; % kg/s/Pa constant k_out in mdot=k_out*P_anode (old value 5.289e-9)
% ** Cathode ****
fc_volume=0.01; % Stack Air Volume n*Cellvolume
fc_cathode_volume=0.01; % Cathode total volume (whole stack) (m^3)
fc_outlet_flow_constant=0.21776316896166e-5; % constant k_out represents air flow out of stack  mdot=k_out*(P_fc-P_om)
fc_inlet_flow_constant = 0.36293861487e-5; %1.987e-4; % constant k_in represents air flow into stack  mdot=k_in*(P_im-P_fc)
% ** Membrane ****
membranedrydensity = 0.002; % Membrane Dry Density (kg/cm3) (value from Nguyen93)
membranedryeqvweight = 1.1; % % Membrane dry equivalent weight (kg/mol) (value from Nguyen93) 
membranethickness = 1.275e-2; % !!!!!!! chekc !!membrane thickness (cm) (value from Nguyen93)

% *************************
% Air properties
% *************************
Cp = 1004;								% Air Cp = 1004 J/(kg*K)
Cv = 718;								% Air Cv = 718 J/(kg*K)
gamma = 1.4;							% Air
rho = 1.23;								% Air density (kg/m^3)
R = 286.9;								% Air gas constant J/(kg*K)
airgasconstant = 286.9; 			% Air gas constant J/(kg*K)   !!! check if this for dry air ?
oxygenmolarmass = 32e-3; 			% Oxygen Molar Mass (kg/mol)
nitrogenmolarmass = 28e-3; 		% Nitrogen Molar Mass (kg/mol)
oxygengasconstant = 259.8; 		% Oxygen Gas Constant J/(kg*K)
nitrogengasconstant = 296.8; 		% Nitrogen Gas Constant J/(kg*K)

% *************************
% Steam properties
% *************************
vapormolarmass = 18.02e-3; 		% Steam (Vapor) Molar Mass (kg/mol)
vaporgasconstant = 461.5; 			% Steam (Vapor) Gas Constant J/(kg*K)
condenserateconstant = 1000;			% rate constant for condensation and evaporation
waterdensity = 997; 					% water density (kg/m3)

% *************************
% Hydrogen properties
% *************************
hydrogenmolarmass =2.016e-3;		% Hydrogen Molar Mass (kg/mol)
hydrogengasconstant = 4.1243e3;	% Hydrogen gas constant J/(kg*K)


% *************************
% Electrochemistry
% *************************
faradays = 96485; % Faradays number
universalgasconstant = 8.31451;	% Universal Gas Constant J/(mol*K)

% *************************
% Compressor(CP) data
% *************************
dc = 9*0.0254;  			% Compressor diameter (m)
Ta = 30 + 273.15;			% Inlet air temp (K) **i used this value for fitting, this value is used only in compressor map. it is not "actual" inlet temp
cp_inertia = 0.00005;   % Compressor & Motor inertia (kg*m2)

% Parameters for flow map
phimax4 = -0.00003699056149;
phimax3 = 0.00027039932787;
phimax2 = -0.00053623540171;
phimax1 = -0.00004636845793;
phimax0 = 0.00221194680963;
beta2 = 1.76566519765589;
beta1 = -1.34836801554691;
beta0 = 2.44418790092002;
psimax5 = -0.00978754892186;
psimax4 = 0.10580782154809;
psimax3 = -0.42936513568305;
psimax2 = 0.80120999043258;
psimax1 = -0.68344136821569;
psimax0 = 0.43331043048640;
% Parameters for efficiency map version 1 (paraboloid) 
PRmax_CP=4;			% Maximum of PR axis
Flowlbmax_CP=14;	% Max. of Flow axis (14 lb/min) 
p_CP=0.01;			% y-axis crossing of center line (asymptote)
q_CP=0.65;			% distance of top point from y axis
r_CP=80;				% max efficiency
th_CP=50*pi/180;	% angle of center line
a_CP=0.26;
b_CP=0.06;
c_CP=1.5;
% Parameter for compressor efficiency lookup table
alliedsignaleff=[200	200	200	200	200	200	200	200	200	200	200	200	200	200	200	200	200	200	200	200	200	200	200	200	200	200
60	60	50	50	50	40	30	30	20	20	10	10	10	10	10	10	10	10	10	10	10	10	10	10	10	20
70	70	60	60	50	50	40	30	20	20	10	10	10	10	10	10	10	10	10	10	10	10	10	10	10	20
76	76	70	70	60	50	50	40	30	20	20	10	10	10	10	10	10	10	10	10	10	10	10	10	10	20
76	76	76	76	70	60	50	50	40	30	20	20	10	10	10	10	10	10	10	10	10	10	10	10	10	20
78	78	76	76	76	70	60	50	50	40	30	20	20	20	10	10	10	10	10	10	10	10	10	10	10	20
76	76	78	76	76	70	70	60	50	50	40	30	30	20	20	10	10	10	10	10	10	10	10	10	10	20
70	70	77	77	76	76	70	70	60	50	50	40	40	30	20	20	10	10	10	10	10	10	10	10	10	20
65	65	75.5	78	77	77	77	70	70	60	50	50	50	40	30	20	20	10	10	10	10	10	10	10	10	20
57	57	72	77	79	78	77.5	77	77	70	60	60	50	50	40	30	20	20	20	10	10	10	10	10	10	10
54	54	68.3	75	78.7	79	79	78.3	77	76.5	70	70	60	50	50	40	30	20	20	20	10	10	10	10	10	10
50	50	63	72.5	76.7	79	79	79	78.9	78.4	77.6	77	70	60	50	50	40	30	30	20	20	20	20	10	10	10
45	50	60	70	74.7	78	79	79	79	79	78.5	78	77	70	60	50	50	40	40	30	20	20	20	20	20	20
45	50	56	65	72	75.5	78.2	79	79	79	79	76	77.7	70	70	60	50	50	50	40	30	30	30	20	20	20
40	45	50	60.5	69.5	74	74.8	78.2	79	79	79	79	78	77	77	70	60	60	60	50	40	40	30	30	30	30
40	45	50	56.5	65	71	74.4	75.4	78.1	78.8	79	79	78.8	78.3	77.5	77.5	70	70	60	60	50	50	40	40	30	30
35	40	45	50	61.3	68	71	74.7	76.4	78.1	78.7	78.8	78.9	78.8	78.32	78	76.7	76.7	70	70	60	60	50	50	40	40
30	35	40	50	57	64.3	69.7	72.8	74.7	76	78	78.4	78.6	78.7	78.6	78.3	78	77	76	76	70	60	60	60	50	50
25	30	35	45	50	60	66	70	72.5	74.6	75	77.4	78.2	78.5	78.6	78.4	78.3	78.1	77	76	75	70	70	60	60	60
25	30	35	40	50	56	62	67.2	70.2	72.8	74.6	75.5	77	78.2	78.4	78.3	78.3	78.2	77.9	76.7	75.9	75.3	74	70	70	70
20	25	30	35	45	50	58	64	67.8	70.2	72.2	74.3	75.2	76.4	78	78.1	78.2	78.2	78.1	77.4	76.6	75.8	75.2	74	73	73
20	20	25	30	40	50	55	60	65	68	70	71.8	74.2	75	75.9	77.3	78	78.1	78	77.6	76.9	76.3	75.6	74.4	73	73
15	20	20	30	35	45	50	56	61.5	60.8	63	69.5	70.8	73.5	74.6	75.3	76.3	77.1	77.5	77.4	77	76.5	76	74.7	73.3	73
10	15	20	25	30	40	45	50	56	62.5	66	68	69	70.5	72.2	74	74.8	75.6	76.3	76.8	76.7	76.4	76.1	75.1	73.7	73
5	10	15	25	30	35	40	45	50	57	63.5	66.3	68	69.2	70	70.8	72.2	73.4	74.3	75	75.4	75.5	75.3	74.8	74	73
20	10	15	20	25	30	35	40	45	50	60	65	66.4	67.7	69	69.5	70.2	70.8	71.75	72.8	73.4	74	74.2	74.2	73	73
20	5	10	20	25	30	35	40	45	45	50	50	65	66.5	67.5	68.2	69	69.5	69.7	69.8	70	70.5	70.7	73	73	73];
alliedsignalflow=[-0.5 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 5.5 6 6.5 7 7.5 8 8.5 9 9.5 10 10.5 11 11.5 12 12.5];
alliedsignalpr=[1 1.1 1.2 1.3 1.4 1.5 1.6	1.7 1.8 1.9	2 2.1	2.2 2.3 2.4	2.5 2.6 2.7	2.8 2.9 3 3.1 3.2	3.3 3.4 3.5];

% **************************
% Compressor Motor (CM) 
% **************************
cm_kv = 0.0153; % V/(rad/sec)
cm_kt = 0.0225; % N-m/Amp
cm_R = 1.2; % Ohm
cm_maxtorque = 1.5; % N-m

% **************************
% Inlet Manifold(IM) Data 
% **************************
im_volume = 0.02; % square meter -- 10 cm diameter pipe 2.5 m long 


% **************************
% Outlet Manifold(OM) Data 
% **************************
om_volume = 0.005; % square meter
% the following four parameters are used when we do not have turbine connected (atmospheric = 1 atm)
om_outlet_flow_constant_low_slope = 2.814706706635605e-007; % k1 in flow=k1(Pom-1atm) for (Pom-1atm)< Pswitch (the fourth parameter)
om_outlet_flow_constant_high_slope = 3.364352011898919e-006; % k2 in flow=k2(Pom-1atm)+k3 for (Pom-1atm) > Pswitch
om_outlet_flow_constant_high_ycross = -0.43514459803041; % k3 above
om_outlet_flow_constant_switch = 1.411486690097637e+005; % Pswitch (Pascal)
om_outlet_choke_pr = (2/(gamma+1))^(gamma/(gamma-1));
om_Cd = 0.0124; %0.011; % See Heywood appendix C
om_At = 0.002; %0.0023; % 
om_d = 0.06; % exit pipe diameter

       
       
load ('setpoints/setpoint23') % load initial condition at 40kW
       