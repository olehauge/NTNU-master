function [GenScores,ImpScores]=CalculateScores(Mu,Sigma,Probes)

% Find unique userIDs
Users=unique(Mu(:,1))';
GenScores=[];
ImpScores=[];

for user=Users
    % Find probes for the current user
    p=find(Probes(:,1)==user);
    % Reserve room for the genuine scores for this user
    Scores=zeros(length(p),1);
    % Calculate genuine scores
    for i=1:length(p)
        % remove userID and sampleNr from the probe
        probe=Probes(p(i),3:end); 
        % Calculate distance score
        % Scores(i)=DistScaledManhattan(Mu(user,2:end),Sigma(user,2:end),probe);
        % Scores(i)=DistSquaredEuclidean(Mu(user,2:end),Sigma(user,2:end),probe);
        Scores(i)=DistManhattan(Mu(user,2:end),Sigma(user,2:end),probe);
    end
    % Add the genuine scores of this user to the GenScores list
    GenScores=[GenScores;Scores];
    
    % Find probes for impostor users
    q=find(Probes(:,1)~=user);
    % Reserve room for the impostor scores against this user
    Scores=zeros(length(q),1);
    % Calculate impostor scores
    for i=1:length(q)
        % Remove userID and sampleNr from the probe
        probe=Probes(q(i),3:end); 
        % calculate the distance score
        % Scores(i)=DistScaledManhattan(Mu(user,2:end),Sigma(user,2:end),probe); 
        % Scores(i)=DistSquaredEuclidean(Mu(user,2:end),Sigma(user,2:end),probe);
        Scores(i)=DistManhattan(Mu(user,2:end),Sigma(user,2:end),probe);
    end
    % Add the impostor scores for this user to the ImpScores list
    ImpScores=[ImpScores;Scores];
end
