clc
clear all
close all

%% Ez and Ey

theta =[0:1:360];     % adjust division accodring to servo motor

% initial laser values
Ez=0;
Ey=132.742;

outC = Ey.*(cosd(theta).^2 - sind(theta).^2) +2.*Ez.*cosd(theta).*sind(theta);
outD = 2.*Ey.*cosd(theta).*sind(theta) - Ez.*(cosd(theta).^2 - sind(theta).^2);

figure
plot(theta, outC, theta, outD)
legend('outEc','outEd')

%% Intensity of both Ey and Ez

cubeP_trans = 0.9554;
halfWave_trans = 0.9804996;
impedance = 376.7303;

intensityC = cubeP_trans .* halfWave_trans .* outC.^2 ./ (2.*impedance);
intensityD =  halfWave_trans .* outD.^2 ./ (2.*impedance); %ignore s-trans too small

figure
plot(theta, intensityC, theta, intensityD,theta, intensityC+intensityD)
legend('intensityC','intensityD','Total Intensity') % FIND THIS FORMULA

%% Power of both Ey and Ez

area = pi*(3.5e-3)^2;

powerC = intensityC.*area;
powerD = intensityD.*area;

figure
plot(theta, powerC*1000, theta, powerD*1000, theta, (powerC+powerD)*1000)
legend('powerC','powerD','totalPower')
hold on
plot(theta, ((powerC/cubeP_trans)+powerD)*1000)

%% theory powr eqn testing

% theta=45;
PowerNew= area.*halfWave_trans ./(2.*impedance) .* (cubeP_trans.*Ey.^2.*(cosd(theta).^2 -sind(theta).^2).^2 + (2.*Ey.*cosd(theta).*sind(theta)).^2);
% PowerNew = area .*halfWave_trans./(2.*impedance) .*(cubeP_trans.*outC.^2 + outD.^2);


% keep Pc as 10

Pd=0.5e-3;
Pc = PowerNew-Pd

figure
plot(theta, Pd)