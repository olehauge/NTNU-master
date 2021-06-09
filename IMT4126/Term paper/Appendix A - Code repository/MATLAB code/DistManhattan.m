function d=DistManhattan(mu,sigma,probe)

% Implementation of the Manhattan distance metrics
% Only include the latencies
d=abs(mu(10:17)-probe(10:17));

% Remove latencies over 1 second to improve reults
p=probe(10:17)<=1;
d=d.*p;
d=sum(d);