function EER=GetEER(GenScores,ImpScores)

% Create sorted list of all scores
numGen=length(GenScores);
numImp=length(ImpScores);
Scores=sort(unique([GenScores;ImpScores]));
% Score that provides EER is somewhere between start and end of the list
start=1;
stop=length(Scores);

% Continue while we have not reached the EER giving score
while stop-start>1;
    % Consider the for the middle score as threshold the FMR and FNMR
    middle=floor((start+stop)/2);
    value=Scores(middle);
    FMR=sum(ImpScores<=value)/numImp;
    FNMR=sum(GenScores>value)/numGen;
    % Adjust the start or the stop to the middle score
    if FMR <= FNMR
        start=middle;
    else
        stop=middle;
    end
end

% Calculate FMR and FNMR around the threshold giving the EER
m1=Scores(start);
m2=Scores(stop);
FMR1=sum(ImpScores<=m1)/numImp; 
FNMR1=sum(GenScores>m1)/numGen; 
FMR2=sum(ImpScores<=m2)/numImp;
FNMR2=sum(GenScores>m2)/numGen;

% Calculate the EER
if FMR1==FNMR1
    EER=FMR1;
elseif FMR2==FNMR2
    EER=FMR2;
else
    EER=(FMR1+FNMR1+FMR2+FNMR2)/4;
end
