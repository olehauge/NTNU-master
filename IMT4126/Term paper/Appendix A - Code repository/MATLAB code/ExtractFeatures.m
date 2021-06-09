function features=ExtractFeatures(data)
    
    % All samples are surrounded by -|nr|- markers at the start and end
    p=find(strcmp(data.Action,'-')); 
    start=p(1:2:end);
    stop=p(2:2:end);
    % All users have 27 samples
    numSamples=length(start);
    % All samples have 17 features
    % numFeatures is calculated as the number of timing values in a sample,
    % which will be an even value (1 press + 1 release per key). The number
    % of durations is the number of key presses and the number of latencies
    % is one less, hence the formula below
    numFeatures=(length(data.Time)-length(p))/numSamples-1;
    % Create a structure to hold all duration and latency features for all
    % the samples of a user
    features=zeros(numSamples,numFeatures);
    
    for s=1:numSamples
        % Select data relevant for current sample
        d=data(start(s)+1:stop(s)-1,:);
        % Find only information related to pressing keys
        p=find(strcmp(d.Action,'KEY_DOWN'));
        % c represents the typed text in table format
        c=d(p,3);
        % timeDown in array format
        timeDown=d.Time(p);
        n=length(timeDown);
        % Information related ot key releases
        q=find(strcmp(d.Action,'KEY_UP'));
        dd=d(q,:);
        % Find timeUp values
        timeUp=zeros(n,1);
        for i=1:n
            q=min(find(strcmp(c.Value(i),dd.Value)));
            timeUp(i)=dd.Time(q);
            dd(q,:)=[];
        end
        % Calculate duration and latency values
        dur=timeUp-timeDown;
        lat=timeDown(2:end)-timeUp(1:end-1);
        % Store duration and latency values as a single feature vector
        features(s,:)=[dur;lat]';
    end
            
        
        
        