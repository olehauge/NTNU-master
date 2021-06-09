function [FMR, FNMR] = computeRates_v2(true_scores, false_scores, thershold)
    % Authors comment: 
    % The code below is based on the logic of the following formulas and
    % my understanting of the genuine and impostor values that are present 
    % in the comparison_score_protocol1 matrix:
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
    % , with 0.4 as the thershold. The result was as follows:
    %
    %           FMR:  0.0762
    %           FNMR: 0.9333
    %
    %--------------------------
    % Compute the FMR and FNMR with a given threshold
    norm_set_genuine_scores = normalize(true_scores,'range', [0 1]);
    disp("ch: " + norm_set_genuine_scores);
    
    norm_set_impostor_scores = normalize(false_scores, 'range', [0 1]);
    disp("ch2: " + norm_set_impostor_scores);
    
    norm_set_impostor_scores_thr = norm_set_impostor_scores(norm_set_impostor_scores(1:length(norm_set_impostor_scores)) > thershold);
    norm_set_genuine_scores_thr = norm_set_genuine_scores(norm_set_genuine_scores(1:length(norm_set_genuine_scores)) > thershold);
    FMR = length(norm_set_impostor_scores_thr) / length(norm_set_impostor_scores);
    GMR = length(norm_set_genuine_scores_thr) / length(norm_set_genuine_scores);
    FNMR = 1 -GMR;
    
return