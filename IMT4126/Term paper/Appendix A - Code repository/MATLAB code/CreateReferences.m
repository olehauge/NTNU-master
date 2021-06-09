function [ReferencesMu,ReferencesSigma,Probes]=CreateReferences(AllFeatures,numSamplesForTraining)

% Determine the unique identities of the users
Users=unique(AllFeatures(:,1))';
% Size of all features
% In this code: 27 samples per each of the 12 users, so s(1)=12*27
% In this code: s(2) = 1 (userID) + 1 (sampleNr) + 17 (dur+lat) = 19
s=size(AllFeatures);
% Calculate mean (mu) and standard deviation (sigma) per user
% userID still in references, but sampleNr no longer, so #columns is s(2)-1
ReferencesMu=zeros(length(Users),s(2)-1);
ReferencesSigma=zeros(length(Users),s(2)-1);

for user=Users
    % Select rows for given user and sampleNr from 1 to numSampleForTraining
    p=find(AllFeatures(:,1)==user & AllFeatures(:,2)<=numSamplesForTraining);
    % Calculate mu and sigma over duration and latency features
    % Also include userID in first column
    ReferencesMu(user,:)=[user,mean(AllFeatures(p,3:end))]; 
    ReferencesSigma(user,:)=[user,std(AllFeatures(p,3:end))];
end

% Find all data that will be used as probes for testing
p=find(AllFeatures(:,2)>numSamplesForTraining);
Probes=AllFeatures(p,:);


    