%% Test with ratio

clc;clear all;close all;

% load('ratio.mat')

cubeP_trans = 1;
% halfWave_trans = 0.8;
% laserPower = 0.9e-3;

powerD = 1;
% timeAxis = [0:length(powerD)-1];

% for theta = [0 15 30 45 60 75 90]
%     newRatio = cubeP_trans.*ans(theta+1);
%     powerC = powerD.* newRatio;
%     figure
%     plot(timeAxis,powerC)
% end



%% test with fluctuating power and constant theta

% path C
syms theta Ey Ez;

ratio=[];
test = [0:1:360];

for j =test
theta = j
r = [cosd(theta) -sind(theta);sind(theta) cosd(theta)];
rInv = inv(r);

JonesHalf = [1 0;0 -1];
JonesPol=[1 0 ; 0 0];
JonesHalfRot = r*JonesHalf*rInv;
initial =[Ey; Ez];

TotalTrans = JonesPol*JonesHalfRot  * initial;

time = [0:1:360];
timeEy = 300 + 200.*sind(2.*time);

for i=1:size(timeEy,2)
    if i >10
        break
    end
    solT =  subs (TotalTrans, {Ey,Ez} ,{timeEy(i),0});


outEy(i) = double(solT(1));  
outEz(i) = double(solT(2));  
end

% path D


JonesPolRef=[0 0 ; 0 1];
JonesHalfRot = r*JonesHalf*rInv;
TotalRef = JonesPolRef * JonesHalfRot * initial;

for i=1:size(timeEy,2)
    if i >10
        break
    end
    solT =  subs (TotalRef, {Ey,Ez} ,{timeEy(i),0});

outRefEy(i) = double(solT(1));
outRefEz(i) = double(solT(2));
end

ratio(1+j) = cubeP_trans.* power(mean(outEy./outRefEz),2);
% figure
% subplot(2,1,1)
% plot(time, outEy)
% subplot(2,1,2)
% plot(time,outRefEz)

end 

figure
plot(test,ratio)
