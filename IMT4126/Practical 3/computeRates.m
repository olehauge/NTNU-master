function [FMR, FNMR] = computeRates(true_scores, false_scores, thershold)
    % Authors comment: 
    % The code below is copied from "Compute_DET.m" I made some changes to 
    % the variable names and added code to calculate FMR, GMR, and FNMR 
    % given a threshold. I based my logic on the following formulas:
    %
    %           Ωg: set of all genuine scores
    %           Ωi: set of all impostor scores
    %           Ωg(t): set of all genuine scores > t
    %           Ωi(t): set of all impostor scores > t
    %           || Ω ||: number of elements in Ω
    %
    %           FMR(t) = ||Ωi(t)|| / ||Ωi||
    %
    %           GMR(t) = ||Ωg(t)|| / ||Ωg||
    %
    %           FNMR(t) = 1 − GMR(t)
    %
    % I tested the code by adding it in the "To_Plot_DET.m" script, after 
    % Pmiss, Pfa] = Compute_DET(final_genuine_scores,final_imposter_scores);
    % , with 0.6 as the thershold. The result was as follows:
    %
    %           Number of imp gt thr: 84
    %           Number of false: 210
    %           FMR: 0.4
    %
    %           Number of gen gt thr: 6
    %           Number of true: 15
    %           GMR: 0.4
    %           FNMR: 0.6
    
    %--------------------------
    % Compute the FMR and FNMR with a given threshold
    num_true = max(size(true_scores));
    num_false = max(size(false_scores));

    total=num_true+num_false;
    FMR  = zeros(total+1, 1); % Preallocate matrix (1x226) with 0's for speed.
    FNMR = zeros(total+1, 1); % Preallocate matrix (1x226) with 0's for speed.
    
    scores(1:num_false,1) = false_scores;       % First score col is filled with false
    scores(1:num_false,2) = 0;                  % Second score col is filled with 0's for false
    scores(num_false+1:total,1) = true_scores;  % Append true values at the end of col 1
    scores(num_false+1:total,2) = 1;            % Second score col is filled with 1's for true
    
    scores=DETsort(scores);
    sumtrue=cumsum(scores(:,2),1);
    sumfalse=num_false - ([1:total]'-sumtrue);

    FMR(1) = 0;
    FNMR(1) = 1.0;
    FMR(2:total+1) = sumtrue ./ num_true;
    set_of_all_genuine_scores_gt_threshold = FMR(FMR(2:total+1) > thershold);
    FNMR(2:total+1) = sumfalse ./ num_false;
    set_of_all_impostor_scores_gt_threshold = FNMR(FNMR(2:total+1) > thershold);
    
    % Get number of all genuine scores gt threshold
    genGTthr_abs = length(set_of_all_genuine_scores_gt_threshold);
    
    % Get number of all impostor scores gt threshold
    impGTthr_abs = length(set_of_all_impostor_scores_gt_threshold);
    
    % Calculate FMR_threshold = ||set_of_all_impostor_scores_gt_threshold|| / ||set_of_all_impostor_scores||
    FMR = impGTthr_abs / num_false;
    
    % Calculate GMR_threshold = ||set_of_all_genuine_scores_gt_threshold|| / ||set_of_all_genuine_scores||
    GMR_threshold = genGTthr_abs / num_true;

    % Calculate FMNR_threshold = 1 - GMR_threshold;
    FNMR = 1 - GMR_threshold;
return

% Using sort function from "Compute_DET.m" (COPIED)
function [y,ndx] = DETsort(x,col)
% DETsort Sort rows, the first in ascending, the remaining in decending
% thereby postponing the false alarms on like scores.
% based on SORTROWS

if nargin<1, error('Not enough input arguments.'); end
if ndims(x)>2, error('X must be a 2-D matrix.'); end

if nargin<2, col = 1:size(x,2); end
if isempty(x), y = x; ndx = []; return, end

ndx = (1:size(x,1))';

% sort 2nd column ascending
[v,ind] = sort(x(ndx,2));
ndx = ndx(ind);

% reverse to decending order
ndx(1:size(x,1)) = ndx(size(x,1):-1:1);

% now sort first column ascending
[v,ind] = sort(x(ndx,1));
ndx = ndx(ind);
y = x(ndx,:);
