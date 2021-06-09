function d=Dist_Metric_3(mu,sigma,probe)

% Implementation of the Scaled Manhattan Distance metrics; how often a user
% does something wrong
p=probe(1:17)<=3; % Thershold
probe=probe.*p;
d=sum(abs(mu-probe)./sigma);

