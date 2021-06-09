clear;
clc;
load('Averages.mat')

% Sort and split references and probes
ind = AverageMean(:,2) == 1;
disp('Finding reference values...');
references = AverageMean(ind,:);
ind2 = AverageMean(:,2)==2;
disp('Finding probe values...');
probes = AverageMean(ind2,:);
fprintf('\n');

% Genuine Scores
GenuineScores = [];
for i = 1:size(references,1)
   mhd = sum(abs(references(i,3:end)-probes(i,3:end))); % Manhattan Distance
   disp('Calculating genuine scores');
   GenuineScore = mhd/length(references(i,3:end)); % Calculate Genuine Score
   GenuineScores=[GenuineScores,GenuineScore]; % Add Distance Score to Genuie Score matrix
end
disp('Genuine Scores');
disp(GenuineScores);
fprintf('Genuine score length: %d\n', length(GenuineScores));

% Impostor Scores
ImpostorScores = [];
fprintf('\n');
disp('Calculating impostor scores');
for i = 1:size(references,1)
    fprintf('Reference for user %d\n', i);
    for n = 1:size(probes,1)
        if probes(n,1) ~= references(i,1)
            reference = references(i,3:end);
            probe = probes(n,3:end);
            mhd = sum(abs(probe-reference)); % Manhattan Distance
            disp('Calculating Impostor Scores for all probe values...')
            ImpostorScore = mhd/length(probes(n,3:end)); % Calculate Impostor Score:
            ImpostorScores=[ImpostorScores,ImpostorScore]; % Add Distance Score to Impostor Score matrix
        end
    end
end
fprintf('Total number of Impostor Scores: %d\n', length(ImpostorScores));


% Results
fprintf('\nResults\n');
% The minumum and maximum matrix value
fprintf('Lowest genuine score: %f\nHighest genuine score: %f\n',min(GenuineScores),max(GenuineScores));
fprintf('Lowest impostor score: %f\nHighest impostor score: %f\n',min(ImpostorScores),max(ImpostorScores));
sum(GenuineScores>0.89)