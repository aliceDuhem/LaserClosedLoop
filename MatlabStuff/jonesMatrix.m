

clear all
close all
clc

theta = [0:1:180];
initial = [1;0]; % initial only verticaly pol



for i=1:size(theta,2)
    
M = [cosd(theta(i)).^2 sind(theta(i)).*cosd(theta(i));sind(theta(i)).*cosd(theta(i)) sind(theta(i)).^2];

out = M*initial;

% figure(1)
% hold on
% plot(theta(i), out(1),'x')
% plot(theta(i),out(2),'o')
% plot(theta(i), sqrt(out(1)^2 + out(2)^2),'s')
% ylabel('Output Amplitude ')
% xlabel('theta, deg')
% title('vertical amplitude X, horizontal amplitude o, Total .')
ini(i) = 
out1(i)=out(1);
out2(i)=out(2);
intensity(i) = sqrt(out(1)^2 + out(2)^2);
% figure(2)
% hold on
% plot(theta(i), sqrt(out(1)^2 + out(2)^2),'.','k')
% title('intensity')
% xlabel('Intensity
end



figure(1)
hold on
plot(theta, out1, 'b--')
% plot(theta,out2,'r')
% plot(theta, intensity)
legend('vertical','horizontal','E^2')
ylabel('Proportion of original')
xlabel('theta (deg) relative to vertical') 