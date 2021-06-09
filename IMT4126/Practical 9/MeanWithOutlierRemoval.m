function [ReferencesMu,ReferencesSigma,Probes]=MeanWithOutlierRemoval(AllFeatures,numSamplesForTraining)

% Determine the unique identities of the users
Users=unique(AllFeatures(:,1))';
% Size of all features
% In practical: 100 samples per each of the 20 users, so s(1)=20*100
% In practical: s(2) = 1 (userID) + 1 (sampleNr) + 17 (dur+lat) = 19
s=size(AllFeatures);
% Calculate mean (mu) and standard deviation (sigma) per user
% userID still in references, but sampleNr no longer, so #columns is s(2)-1
ReferencesMu=zeros(length(Users),s(2)-1);
ReferencesSigma=zeros(length(Users),s(2)-1);

AllFeatures2 = AllFeatures;

for user=Users
    % Select rows for given user and sampleNr from 1 to numSampleForTraining
    p=find(AllFeatures2(:,1)==user & AllFeatures2(:,2)<=numSamplesForTraining);

    % 1) Delete obvious outlier values, e.g. latencies more than 2 seconds
    % (I also included the durations)
    logMat=AllFeatures2(p,3:end)<=2; % Logical matrix: Check if values are less than or equal to 2; return a matrix of 1's and 0', where 1 = less than 2 and 0 = greater than 2.
    AllFeatures2(p,3:end)=AllFeatures2(p,3:end).*logMat; % Multiply the logical matrix with the original matrix containing the latency values; setting too big values to 0.
    

    % 2) With the remaining values do: (a) Calculate mean and std, and 
    %    (b) Remove values that are more than k times std from mean
    % (a) Calculate mean and std
    ReferencesMu(user,:)=[user,mean(AllFeatures2(p,3:end))];   
    ReferencesSigma(user,:)=[user,std(AllFeatures2(p,3:end))];
    % (b) Remove values that are more than k times std from mean
    k=2;
    actual_std_from_mean=abs(ReferencesSigma(user,:) - ReferencesMu(user,:));
    ktimes_std_from_mean=abs((ReferencesSigma(user,:).*k) - ReferencesMu(user,:));
    logMat2=ktimes_std_from_mean<actual_std_from_mean
    AllFeatures2(p,3:end)=AllFeatures2(p,3:end).*logMat2(:,2:end);
        
        % 3) If values are removed in step 2b, then repeat step 2
        if any(logMat2(:,2:end)==0,2)
            disp('Contains zero')
            disp(any(logMat2(:,2:end)==0,2));
            n = 1;
            while n <= 3
                % 2) With the remaining values do: (a) Calculate mean and std, and (b) Remove values that are more than k times std from mean
                % (a) Calculate mean and std
                ReferencesMu(user,:)=[user,mean(AllFeatures2(p,3:end))];   % Mean scores for user 
                ReferencesSigma(user,:)=[user,std(AllFeatures2(p,3:end))]; % Std scores for user
                % (b) Remove values that are more than k times std from mean
                actual_std_from_mean=abs(ReferencesSigma(user,:) - ReferencesMu(user,:));
                ktimes_std_from_mean=abs((ReferencesSigma(user,:).*k) - ReferencesMu(user,:));
                logMat2=ktimes_std_from_mean<actual_std_from_mean;
                AllFeatures2(p,3:end)=AllFeatures2(p,3:end).*logMat2(:,2:end);
                n = n + 1;
            end
        end
end

       
% Find all data that will be used as probes for testing
p=find(AllFeatures(:,2)>numSamplesForTraining);
Probes=AllFeatures(p,:);


    