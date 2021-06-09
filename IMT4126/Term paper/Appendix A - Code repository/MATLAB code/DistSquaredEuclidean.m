function d=DistSquaredEuclidean(mu,sigma,probe)

% Implementation of the squared Euclidean distance metrics
% Only include the latencies
d=sqrt(sum((abs(mu(10:17)-probe(10:17))./sigma(10:17)).^2));

% Remove latencies over 1 second to improve reults
p=probe(10:17)<=1;
d=d.*p;
d=sum(d);