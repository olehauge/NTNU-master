tic
% 12 users, 27 samples per user -> 324 rows in AllFeatures
% PW=welcome42, so 9 durations + 8 latencies = 17 features
% Column 1 = user ID (1..12)
% Column 2 = user sample (1..27)
% Columns 3..11 = durations
% Columns 12..19 = latencies
AllFeatures=zeros(324,19);

for user=1:12
    % Read the data from a file
    data=LoadData(user);
    % Extract duration and latency features from press and release times
    f=ExtractFeatures(data);
    % Add userID as first column and add sampleNr as second column
    f=[user*ones(27,1),[1:27]',f];
    % Store the extracted information in AllFeatures
    AllFeatures((user-1)*27+1:user*27,:)=f;
end

% Select a number of samples for training
numSamplesForTraining=20;

% Create the reference based on the number of samples for training
[Mu,Sigma,Probes]=CreateReferences(AllFeatures,numSamplesForTraining);

% Calculate genuine and impostor scores based on references and probes
[GenScores,ImpScores]=CalculateScores(Mu,Sigma,Probes);

% Calculate the EER based on genuine and impostor scores
Result=GetEER(GenScores,ImpScores)
toc