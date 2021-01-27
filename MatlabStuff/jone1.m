
clc 
clear all
close all


% polarizing beam cube errors and specs (reflects s-pol)
% p-pol transmittance 95.54% @ 532nm
% s-pol transmittance 0.04348% @ 532nm
% total R_s > 99.50% 
cubeP_trans = 1; % 0.9554
cubeS_trans = 0.0004348; %this not needed as the max difference in power is 3.83e-4 mW

% half wave plate errors and specs
% reflectance 0.25% @ 532nm
% transmittamnce 98.04996% @ 532nm

halfWave_trans = 1; %0.8804996, incldue as mean sqr err between original and transmitted Ey = 0.8482 

% laser spec and error
% 0.8mW < power < 1mW, typical @ 0.9mW
% frequency changes with temprature


%% Find transmitted output Ey

% use jones matrix to find 'transfer function' of whole system

syms theta Ey Ez;

r = [cosd(theta) -sind(theta);sind(theta) cosd(theta)];
rInv = inv(r);

JonesHalf = [1 0;0 -1];
JonesPol=[1 0 ; 0 0];
JonesHalfRot = r*JonesHalf*rInv;
initial =[Ey; Ez];  % only adjust Ey becsaue laser linearly pol.
                    % keep Ez as 0, laser pol in Y direc only.
                    % adjust in bottom {} brackets
                    
TotalTrans = JonesPol*JonesHalfRot  * initial;

thetaAxis =[0:1:360];     % adjust division accodring to servo motor

for i=1:size(thetaAxis,2)
    
solT =  subs (TotalTrans, {theta, Ey,Ez} ,{thetaAxis(i),1500,0});

outEy(i) = double(solT(1));  
outEz(i) = double(solT(2));  
end

% plot theta against Ey proportion
% Ez remains 0 as 2nd polariser cuts it off
figure(1)
subplot(2,1,2)

yyaxis left
plot(thetaAxis,outEy)
xlabel('theta')
ylabel('Ey amplitude out')
title('Transmitted Output Ey of laser')

hold on
intensity = cubeP_trans .* halfWave_trans .* outEy.^2 ./ (2.*376.7303);   
%include transmittance above
power = intensity .* (pi.*(3.5e-3.^2));

yyaxis right
plot(thetaAxis,power.*1000)
xlabel('theta deg')
ylabel('Output power [mW]')


%% test with malus law instead of jones

intensity1 = 0.9e-3 / (pi*(3.5e-3^2));
intensity1Out = cubeP_trans .* halfWave_trans .* intensity1 .* cosd(thetaAxis).^2;


figure
plot(thetaAxis,intensity1Out.*1000.* (pi.*(3.5e-3.^2)),thetaAxis, power.*1000)
legend('Malus','Jones')
ylabel('Ey power [mW]')
xlabel('theta')
title('Malus Law vs Jones')

% intensity - intensity1Out gave a mean squared error of 1.5903e-10, which
% is neglegable. So i suggest we ignore it.
% this shows that my equations are very close to malus law


%% reflected output Ez to detector

JonesPolRef=[0 0 ; 0 1];
JonesHalfRot = r*JonesHalf*rInv;
TotalRef = JonesPolRef * JonesHalfRot * initial;

for i=1:size(thetaAxis,2)
    
solT =  subs (TotalRef, {theta, Ey,Ez} ,{thetaAxis(i),1500,0});

outRefEy(i) = double(solT(1));
outRefEz(i) = double(solT(2));
end

figure(1)
subplot(2,1,1)
yyaxis left
plot(thetaAxis,outRefEz)
xlabel('theta')
ylabel('Ez amplitude out')
title('Reflected Output Ez of laser')
hold on

intensityRef = halfWave_trans.* outRefEz.^2 ./ (2.*376.7303);
powerRef = intensityRef .* (pi.*(3.5e-3.^2));

% figure
yyaxis right
plot(thetaAxis,powerRef.*1000)
xlabel('theta deg')
ylabel('Output power [mW]')
% title('Power vs theta')

%% Ez and Ey between half wave and cube

between = JonesHalfRot * initial;

for i=1:size(thetaAxis,2)
    
solBet =  subs (between, {theta, Ey,Ez} ,{thetaAxis(i),1500,0});

BetEy(i) = double(solBet(1));
BetEz(i) = double(solBet(2));
end

figure
hold on
plot(thetaAxis, sqrt(halfWave_trans).* BetEy, thetaAxis, sqrt(halfWave_trans).*BetEz)
plot(thetaAxis, BetEy, thetaAxis, BetEz)
% legend('Ey','Ez')

%% plot path C including s-pol 
% cannot use equaton outEY as that contains final transform
% can ignore as difference too small 1e-4 mW in power

FinalEz = BetEz.*sqrt(halfWave_trans).*sqrt(cubeS_trans);
FinalEy = BetEy.*sqrt(halfWave_trans).*sqrt(cubeP_trans);
% outEy = outEy .* sqrt(halfWave_trans);

Etot = sqrt(FinalEz.^2 + FinalEy.^2);


intensityNew = Etot.^2 ./ (2.*376.7303); 
powerNew = intensityNew .*(pi.*(3.5e-3.^2));
figure
plot(thetaAxis, powerNew*1000)